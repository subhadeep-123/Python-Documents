from ftplib import FTP
with FTP("ftp1.at.proftpd.org") as ftp:
    ftp.login()
    ftp.dir()
    print("---------")
    ftp.retrlines('LIST')
