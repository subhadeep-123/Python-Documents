from ftplib import FTP
ftp = FTP('ftp.us.debian.org')
resp = ftp.login()
print(f"The return resp from server - {resp}")
print(ftp.retrlines('LIST'))
print(ftp.cwd('debian'))
print(ftp.retrlines('LIST'))
with open('README', 'wb') as fp:
    ftp.retrbinary('RETR README', fp.write)
# for i in ftp.mlsd():
#     print(i)
# print(ftp.nlst())
# print(ftp.delete('README'))
# ftp.nlst()
ftp.mkd('Test')
ftp.cwd('Test')
qresp = ftp.quit()
print(f"The return resp from server - {qresp}")
