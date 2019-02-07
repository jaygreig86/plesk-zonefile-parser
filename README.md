
# Intro

There's currently nothing around that allows you to import a bind file into Plesk so here's a quick python script that will at the very least give you an xml output you can use to import them into plesk which can be especially useful if you have a large zone or a large number of zones to import.

This makes use of the dnspython lib and outputs xml to be copy/pasted into the plesk XML-RPC API extension.  I'll produce something that will import direct in the near future perhaps based on this but using an xml lib.

# Requirements

Built for Python version 2
dnspython library needed

## On Freebsd

pkg install py27-dnspython-1.15.0

## On Debian or similar

apt install python-dnspython

# Usage
$ python convert.py <domain.tld> <site id>
    
The below shows how to retrieve the site ID as you'll need this to produce the correct xml output.  Head to the XML-RPC API Explorer extension (install it if you don't have it already) under plesk extensions, copy and paste in the below and it should give you the site ID you're going to need.

```
<site>
    <get>
      <filter>
      <name>domain.tld</name>
       </filter>
       <dataset>
            <gen_info/>
       </dataset>
    </get>
</site>
```
