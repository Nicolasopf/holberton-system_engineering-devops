# Postmortem

## Issue Summary
### Resume of problem
Not enough disk usage caused by an unexpected error log of Lets encrypt, this error did appear only in one host (We did have a lot of hosts in that moment, every host affected).

### Duration
From 15/01/2021 3:00 a.m to 17/01/2021 2 a.m (GMT-5)

### Impact

All the server was affected. Websites, webmail, everything stopped working.
Every user couldn't access to the services.

### Root cause
Server didn't have enough storage

## Timeline
The issue was detected at 15/01/2021 11 a.m by a customer complained.

### Action taken
We reviewed the status of the system, CPU, RAM, and other problems not related to disk usage.
When we noticed the problem was the disk usage, we searched for the files and folders with the higher size to take actions as delete some of them, create a compressed file, etc.

### Misleading investigation
We were searching for problems related to plugins installed in some of the CMS, we wasted many time there.

This incident did not scale to other team or persons.

### How the incident was resolved
The incident was resolved at 2 a.m 17/01/2021 Deleting files with high size, also, searching for some error logs that were generating very high Gigabytes of error log.
We changed the file permissions of that file to be written so the error wouldn't appear in the error log. (Because the file could get a size of 50 gb in 5 minutes.)

The main error was not detected, it was something related to Let's encrypt error log but we haven't idea what was the error.

## Corrective and preventative measures

* Give a max size of files.
* Have a cronjob to delete error logs to not have so many errors in a file.
* Implement a monitoring server stats of CPU, Disk Usage, RAM, and if possible to email or send message to the respective person which can solve the problem.


## Authors
Nicolás Urrea - nico15935746@gmail.com