# concrete-cms
Concrete5-CMS RCE (CVE-2021-22968)

Affected versions 8.5.6 and 9.0.0

Full write-up at: https://www.fortbridge.co.uk/research/multiple-vulnerabilities-in-concrete-cms-part1-rce/

Steps to reproduce
* upload test.php somewhere accessible for the vulnerable server
* you need a valid upload request in request.txt
* you need to start script.py as a Turbo Intruder script - this will find the volatile dir and write the second request in request2.txt. It will also start a secondary Turbo Intruder which will run script2.py in order to find and trigger test.php on the victim server
