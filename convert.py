#!/usr/local/bin/python
# -*- coding: utf-8 -*-
# Coded by James Greig
# Requires dnspython

import dns.query
import dns.zone
import dns.exception
import io
import sys
from dns.rdataclass import *
from dns.rdatatype import *

def _parse_zone(domain,siteid):
    try:
        _zonedata = dns.zone.from_file(domain,domain + '.')
        names = _zonedata.nodes.keys()
        names.sort()
        f = io.StringIO()
        for name, node in _zonedata.nodes.items():
                rdatasets = node.rdatasets
                for rdataset in rdatasets:
                        for rdata in rdataset:
                                _namestr = "%s" % (name)
                                if _namestr == '@':
                                        host = ''
                                else:
                                        host = "%s" % (name)
                                if rdataset.rdtype == NS:
                                        _record_out('NS',host,rdata.target,'',siteid)
                                if rdataset.rdtype == MX:
                                        _record_out('MX',host,rdata.exchange,rdata.preference,siteid)
                                if rdataset.rdtype == A:
                                        _record_out('A',host,rdata.address,'',siteid)
                                if rdataset.rdtype == AAAA:
                                        _record_out('AAAA',host,rdata.address,'',siteid)
                                if rdataset.rdtype == TXT:
                                         _record_out('TXT',host,rdata.strings,'',siteid)
                                if rdataset.rdtype == CNAME:
                                        target = "%s" % (rdata.target)
                                        if target == '@':
                                                _fulltarget = domain
                                        else:
                                                _fulltarget = rdata.target
                                        _record_out('CNAME',host,_fulltarget,'',siteid)
                                if rdataset.rdtype == SRV:
                                        target = "%s" % (rdata.target)
                                        if target == '@':
                                                _fulltarget = domain
                                        else:
                                                _fulltarget = rdata.target
                                        srv = "<Srv Protocol=\"tcp\" Port=\"%d\" Priority=\"%d\" Weight=\"%d\"/>" % (rdata.port,rdata.priority,rdata.weight)
                                        _record_out('SRV',host,_fulltarget,srv,siteid)

    except IOError as err:
        print "fail %s" % (err)
        exit

def _record_out(type,host,value,opt,siteid):
        print "\t<add_rec>"
        print "\t<site-id>%s</site-id>" % (siteid)
        print "\t\t<type>%s</type>" % (type)
        print "\t\t<host>%s</host>" % (host)
        print "\t\t<value>%s</value>" % (value)
        print "\t\t<opt>%s</opt>" % (opt)
        print "\t</add_rec>"

if __name__ == "__main__":
    if len(sys.argv) > 2:
        print "<dns>"
        _parse_zone( sys.argv[1], sys.argv[2])
        print "</dns>"
    else:
        print sys.argv[0] + " <domain.tld> <plesk site id>"
        print "* filename must match the origin"
        print "* obtain the site id from plesk"
        print "Use the XML-RPC API Explorer extension to paste import"
        exit()
