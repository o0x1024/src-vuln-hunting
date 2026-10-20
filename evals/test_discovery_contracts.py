"""Owned offline format/URL/description experiments, no target requests."""
import csv
import io
import ipaddress
import json
import re
from urllib.parse import urljoin,urlsplit
from xml.etree import ElementTree as ET


def main():
    # Same reference text does not identify an endpoint without its base.
    ref='./item'
    bases=['https://app.invalid/a/page','https://app.invalid/a/page/',
           'https://cdn.invalid/css/theme.css','https://cdn.invalid/modules/main.js']
    resolved=[urljoin(base,ref) for base in bases]
    assert resolved==['https://app.invalid/a/item','https://app.invalid/a/page/item',
                     'https://cdn.invalid/css/item','https://cdn.invalid/modules/item']
    assert urlsplit(urljoin(bases[0],'//other.invalid/item')).hostname=='other.invalid'
    callback=urlsplit('https://client.invalid/cb?code=OWNED#access_token=FIXTURE')
    assert callback.path+'?'+callback.query=='/cb?code=OWNED'
    assert callback.fragment=='access_token=FIXTURE'
    # CSV quoting changes which value occupies the second/third column.
    line='192.0.2.7,"Example, Inc.",api.fixture.invalid'
    fields=next(csv.reader([line]))
    assert fields==['192.0.2.7','Example, Inc.','api.fixture.invalid']
    assert line.split(',')[1]=='"Example' and fields[1] != fields[2]
    # A loose IPv4 extractor throws away the exact route prefix and context.
    whois='route: 192.0.2.0/24\norigin: AS64500\ncontact: 198.51.100.7\nroute6: 2001:db8::/32\nremark: 999.999.999.999\n'
    loose=re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b',whois)
    assert loose==['192.0.2.0','198.51.100.7','999.999.999.999']
    routes=[]
    for row in whois.splitlines():
        key,_,value=row.partition(':')
        if key in ('route','route6'):routes.append(str(ipaddress.ip_network(value.strip())))
    assert routes==['192.0.2.0/24','2001:db8::/32']
    try:ipaddress.ip_address(loose[-1]);raise AssertionError('invalid octets accepted')
    except ValueError:pass
    # A self-owned WSDL separates declared binding/operation/address from any
    # actual successful SOAP call. No external entities or fetches are used.
    xml='''<wsdl:definitions xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/"
      xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/" targetNamespace="urn:owned">
      <wsdl:binding name="OwnedBinding" type="OwnedPortType">
        <wsdl:operation name="ReadOwn"><soap:operation soapAction="urn:owned:read"/></wsdl:operation>
      </wsdl:binding><wsdl:service name="Owned"><wsdl:port name="OwnedPort" binding="OwnedBinding">
        <soap:address location="https://service.invalid/soap"/>
      </wsdl:port></wsdl:service></wsdl:definitions>'''
    root=ET.fromstring(xml)
    ns={'w':'http://schemas.xmlsoap.org/wsdl/','s':'http://schemas.xmlsoap.org/wsdl/soap/'}
    operation=root.find('w:binding/w:operation',ns)
    action=operation.find('s:operation',ns).get('soapAction')
    endpoint=root.find('w:service/w:port/s:address',ns).get('location')
    assert (operation.get('name'),action,endpoint)==('ReadOwn','urn:owned:read','https://service.invalid/soap')
    assert root.find('.//operation') is None  # unqualified name is different
    report={'result':'pass','scope':'Python URL resolution, CSV/WHOIS field parsing and owned XML namespace/description fields only; not DNS, browser base selection, GraphQL execution, SOAP authorization or target coverage.',
            'url_resolution':dict(zip(bases,resolved)),'network_path_reference_host':'other.invalid',
            'csv_fields':fields,'loose_ipv4':loose,'strict_routes':routes,
            'wsdl':{'operation':operation.get('name'),'action':action,'endpoint':endpoint,'business_request_sent':False},
            'network_requests':0}
    print(json.dumps(report,ensure_ascii=False,indent=2))

import contextlib
import unittest


class DiscoveryContractTest(unittest.TestCase):
    def test_contract(self):
        """URL 解析、CSV/WHOIS 字段与自有 WSDL 的确定性契约（零网络请求）。"""
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            main()
        report = json.loads(buf.getvalue())
        self.assertEqual(report.get('network_requests'), 0)


if __name__ == '__main__':
    unittest.main()
