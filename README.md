
# Intro

Just a simple python script that parses a standard bind file using the dnspython lib and outputs xml
to be copy/pasted into the plesk XML-RPC API extension.  I'll produce something that will import direct
also.

The below shows how to retrieve the site ID as you'll need this to produce the correct xml output
```
<packet>
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
# Requirements

Built for Python version 2
dnspython library needed

## On Freebsd

pkg install py27-dnspython-1.15.0

## On Debian or similar

apt install python-dnspython
