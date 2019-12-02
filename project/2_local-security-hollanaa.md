==================================================================================
test session starts
==================================================================================
platform linux -- Python 3.7.4, pytest-5.3.1, py-1.8.0, pluggy-0.13.1 --
/home/main-user/.pyenv/versions/3.7.4/envs/ENV3/bin/python3.7
cachedir: .pytest\\_cache
rootdir:
/home/main-user/Documents/courses/2019-03-Fall/cloud-649/cm/cloudmesh-configuration,
inifile: pytest.ini
collected 7 items                                                                                                                                                                       

tests/test\\_encryption.py::TestEncrypt::test\_sec\_section\_exists PASSED
tests/test\_encryption.py::TestEncrypt::test\_kh\_load\_public PASSED
tests/test\_encryption.py::TestEncrypt::test\_kh\_load\_private PASSED
tests/test\_encryption.py::TestEncrypt::test\_RSA\_encryption PASSED
tests/test\_encryption.py::TestEncrypt::test\_AESGCM\_nonces PASSED
tests/test\_encryption.py::TestEncrypt::test\_AESGCM\_encryption PASSED
tests/test\_encryption.py::TestEncrypt::test\_benchmark 
+-------------------+---------------------------------------------+
| Machine Attribute | Value                                       |
+-------------------+---------------------------------------------+
| BUG\_REPORT\_URL    | "https://bugs.debian.org/"                  |
| HOME\_URL          | "https://www.debian.org/"                   |
| ID                | debian                                      |
| NAME              | "Debian GNU/Linux"                          |
| PRETTY\_NAME       | "Debian GNU/Linux 9 (stretch)"              |
| SUPPORT\_URL       | "https://www.debian.org/support"            |
| VERSION           | "9 (stretch)"                               |
| VERSION\_CODENAME  | stretch                                     |
| VERSION\_ID        | "9"                                         |
| cpu\_count         | 4                                           |
| mac\_version       |                                             |
| machine           | ('x86\_64',)                                 |
| mem\_active        | 1.9 GiB                                     |
| mem\_available     | 1.4 GiB                                     |
| mem\_free          | 738.4 MiB                                   |
| mem\_inactive      | 785.3 MiB                                   |
| mem\_percent       | 60.0%                                       |
| mem\_total         | 3.6 GiB                                     |
| mem\_used          | 1.7 GiB                                     |
| node              | ('stretch',)                                |
| platform          | Linux-4.9.0-9-amd64-x86\_64-with-debian-9.11 |
| processor         | ('',)                                       |
| processors        | Linux                                       |
| python            | 3.7.4 (default, Aug 22 2019, 13:52:30)      |
|                   | [GCC 6.3.0 20170516]                        |
| release           | ('4.9.0-9-amd64',)                          |
| sys               | linux                                       |
| system            | Linux                                       |
| user              | main-user                                   |
| version           | #1 SMP Debian 4.9.168-1+deb9u5 (2019-08-11) |
| win\_version       |                                             |
+-------------------+---------------------------------------------+
+-------------+-------+---------------------+-----+--------------+-----------+--------+-------------+-------------+
| timer       | time  | start               | tag | node         | user      |
system | mac\_version | win\_version |
+-------------+-------+---------------------+-----+--------------+-----------+--------+-------------+-------------+
| sec\_section | 0.136 | 2019-12-02 02:58:03 |     | ('stretch',) | main-user |
Linux  |             |             |
| load\_pub    | 0.053 | 2019-12-02 02:58:03 |     | ('stretch',) | main-user |
Linux  |             |             |
| load\_prv    | 0.092 | 2019-12-02 02:58:03 |     | ('stretch',) | main-user |
Linux  |             |             |
| RSA\_enc     | 0.085 | 2019-12-02 02:58:03 |     | ('stretch',) | main-user |
Linux  |             |             |
| AES-nonce   | 0.0   | 2019-12-02 02:58:04 |     | ('stretch',) | main-user |
Linux  |             |             |
| AES-enc     | 0.0   | 2019-12-02 02:58:04 |     | ('stretch',) | main-user |
Linux  |             |             |
+-------------+-------+---------------------+-----+--------------+-----------+--------+-------------+-------------+

csv,timer,time,starttag,node,user,system,mac\_version,win\_version
#csv,sec\_section,0.136,None,('stretch',),main-user,Linux,,
#csv,load\_pub,0.053,None,('stretch',),main-user,Linux,,
#csv,load\_prv,0.092,None,('stretch',),main-user,Linux,,
#csv,RSA\_enc,0.085,None,('stretch',),main-user,Linux,,
#csv,AES-nonce,0.0,None,('stretch',),main-user,Linux,,
#csv,AES-enc,0.0,None,('stretch',),main-user,Linux,,

