from ftplib import FTP

HOST = 'ftp1.at.proftpd.org'
with FTP(HOST) as ftp:
    ftp.login()
    ftp.set_debuglevel(2)
    ftp.set_pasv(False)
    print(ftp.dir())
    print(ftp.getwelcome())
    print(ftp.sendcmd('PWD'))
    print(ftp.sendcmd('SYST'))
    print(ftp.voidcmd('PWD'))
    print(ftp.dir())
    # with open('text.txt', 'wb') as file:
    #     ftp.retrbinary('RETR README.MIRRORS', file.write)
    ftp.retrlines('NLST')
