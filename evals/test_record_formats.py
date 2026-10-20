"""Owned offline record/format experiments; no network, capture or spreadsheet."""
import base64
import csv
import hashlib
import io
import json
import os
import struct
import subprocess


def main():
    body = b'OWNED_FRAME'
    header = struct.pack('!IHHIIII', 0xa1b2c3d4, 2, 4, 0, 0, 65535, 1)
    record = struct.pack('!IIII', 100, 123456, len(body), len(body)+7) + body
    raw = header+record
    assert len(header) == 24 and len(record) == 16+len(body)
    # Independently choose byte order from the magic and parse actual bytes.
    order = {b'\xa1\xb2\xc3\xd4':'>', b'\xd4\xc3\xb2\xa1':'<'}[raw[:4]]
    major, minor, zone, sig, snap, link = struct.unpack(order+'HHIIII', raw[4:24])
    sec, usec, captured, original = struct.unpack(order+'IIII', raw[24:40])
    assert (major,minor,snap,link) == (2,4,65535,1)
    assert (sec,usec,captured,original) == (100,123456,len(body),len(body)+7)
    assert raw[40:40+captured] == body and original != captured
    try:
        io.StringIO().write(header)
        raise AssertionError('bytes unexpectedly accepted by text output')
    except TypeError:
        pass
    out = io.BytesIO(); out.write(raw); assert out.getvalue() == raw
    # Encoders use the same base64 alphabet but produce different input bytes
    # for any downstream fingerprint algorithm. Do not require a mmh3 package.
    sample = bytes(range(90))
    flat = base64.b64encode(sample); wrapped = base64.encodebytes(sample)
    assert flat != wrapped and wrapped.endswith(b'\n')
    assert base64.b64decode(flat) == base64.b64decode(wrapped) == sample
    assert hashlib.sha256(b'100').digest() != hashlib.sha256(b'100\n').digest()
    # CSV quoting roundtrips text without disabling a later spreadsheet
    # interpreter. This does NOT start that interpreter or prove computation.
    buf = io.StringIO(newline='')
    csv.writer(buf,quoting=csv.QUOTE_ALL).writerow(['=1+1','a,b','line\nbreak'])
    serialized = buf.getvalue()
    assert list(csv.reader(io.StringIO(serialized,newline=''))) == [['=1+1','a,b','line\nbreak']]
    # An inert shell fragment demonstrates the variable-name and default
    # contracts. It does not invoke ffuf, DNS, external programs or writes.
    shell = 'name=fixture; name_=WRONG; x=42; printf "%s\\n" "$name_$x.json" "${name}_${x}.json" "${1:-/dev/stdin}"'
    env = {'PATH':os.defpath,'LC_ALL':'C'}
    a = subprocess.run(['/bin/bash','--noprofile','--norc','-c',shell,'fixture'],capture_output=True,text=True,timeout=5,env=env)
    b = subprocess.run(['/bin/bash','--noprofile','--norc','-c',shell,'fixture',''],capture_output=True,text=True,timeout=5,env=env)
    assert a.returncode == b.returncode == 0
    assert a.stdout.splitlines() == b.stdout.splitlines() == ['WRONG42.json','fixture_42.json','/dev/stdin']
    print(json.dumps({'pcap':{'header':24,'record_header':16,'captured':captured,'original':original,'binary_roundtrip':'pass'},'base64':{'flat_bytes':len(flat),'wrapped_bytes':len(wrapped),'decoded_equal':True},'csv':{'quoted_formula_retained':True,'spreadsheet_executed':False},'shell':a.stdout.splitlines(),'network_requests':0},ensure_ascii=False))


import contextlib
import unittest


class RecordFormatTest(unittest.TestCase):
    def test_formats(self):
        """pcap 字节序/base64 编码器/CSV 引号/shell 变量展开的确定性契约（零网络请求）。"""
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            main()
        report = json.loads(buf.getvalue())
        self.assertEqual(report.get('network_requests'), 0)


if __name__ == '__main__':
    unittest.main()
