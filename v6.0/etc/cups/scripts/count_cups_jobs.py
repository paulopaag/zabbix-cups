#!/usr/bin/env python
pagelog = open('/var/log/cups/page_log', 'r')
Jobs = pagelog.readlines()
count = 0
for job in Jobs:
        count+=1
jobsfile = open('/tmp/pagelog_jobcount', 'w')
jobsfile.write(str(count))
jobsfile.close
