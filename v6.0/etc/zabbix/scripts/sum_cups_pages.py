#!/usr/bin/env python

import re

pagelog = open('/var/log/cups/page_log', 'r')
pages = 0
for line in pagelog.readlines():
    for value in re.findall('(?<=total\s)[0-9]+', line):
        pages += int(value)
pagelog.close()
pagesfile = open('/tmp/pagelog_pagecount', 'w')
pagesfile.write(str(pages))
pagesfile.close
