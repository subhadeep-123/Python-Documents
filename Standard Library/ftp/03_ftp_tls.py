import ftplib
from typing import Any
from ftplib import FTP_TLS, FTP


def connect(host: str) -> Any:
    try:
        with FTP_TLS(host) as ftp:
            ftp.login()
            ftp.dir()
            resp = ftp.quit()
    except ftplib.all_errors() as err:
        print(err)
    return resp


if __name__ == '__main__':
    resp = connect('ftp.pureftpd.org')
    print(resp)
