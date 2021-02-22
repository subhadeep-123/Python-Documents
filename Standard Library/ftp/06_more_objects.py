import ftplib


def connect():
    try:
        ftp = ftplib.FTP('ftp1.at.proftpd.org')
        ftp.login()
        print(ftp.getwelcome())
        print(f"Current Directory", ftp.pwd())
        print(f"All Files in the Directory-\n{ftp.dir()}")
        print('Valid commands are cd/get/ls/exit - ex: get readme.txt')
        ftp_command(ftp)
    except ftplib.all_errors() as err:
        print(f"The Error is - {err}")


def ftp_command(ftp):
    while True:
        command = input('Enter a Command')
        commands = command.split()
        if commands[0] == 'cd':
            try:
                ftp.cwd(command[1])
                print(f"Directory of {ftp.pwd()}")
                ftp.dir()
                print(f"Directory of {ftp.pwd()}")
            except ftplib.error_perm as e:
                error_code = str(e).split(None, 1)
                if error_code[0] == '550':
                    print(error_code[1])
                elif commands[0] == 'get':
                    try:
                        ftp.retrbinary(
                            'RETR ' + commands[1], open(commands[1], 'wb').write)
                        print('File Successfully downloaded.')
                    except ftplib.error_perm as e:
                        error_code = str(e).split(None, 1)
                        if error_code[0] == '550':
                            print(
                                error_code[1], 'File may not exists or you may not have prermission')
                elif commands[0] == 'ls':
                    print('Directory of'. ftp.pwd())
                    ftp.dir()
                elif commands[0] == 'exit':
                    print(ftp.quit())
                    break
                else:
                    print('Invalid command, try again (valid options:cd/get/ls/exit).')


if __name__ == '__main__':
    connect()
