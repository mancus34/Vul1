#!/usr/bin/python3

from nist_scrape import set_data, get_cvss

CVE1 = 'CVE-2013-3661'
CVE2 = 'CVE-2009-2030'
CVE3 = 'CVE-1999-0607'
CVE4 = 'CVE-2000-0762'
CVE5 = 'CVE-3000-0000'
CVE6 = 'CVE-1234-123+'

print('testing valid cvss rating...')
set_data(CVE1)
print(CVE1 + '\tExpected=4.9' + '\tActual=' + get_cvss())

set_data(CVE2)
print(CVE2 + '\tExpected=10.0' + '\tActual=' + get_cvss())

set_data(CVE3)
print(CVE3 + '\tExpected=5.0' + '\tActual=' + get_cvss())

set_data(CVE4)
print(CVE4 + '\tExpected=10.0' + '\tActual=' + get_cvss())

print('\ntesting exceptions...')
set_data(CVE5)
print(CVE5 + '\tExpected=cvss not found' + '\tActual=' + get_cvss())

set_data(CVE6)
print(CVE6 + '\tExpected=invalid CVE' + '\tActual=' + get_cvss())

print('testing done')
