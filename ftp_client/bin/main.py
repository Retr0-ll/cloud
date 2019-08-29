from ftp_client.core.client import FtpClient


if __name__ == '__main__':
    mainpage = '''
    主页
        1、注册
        2、登录
        退出请按q
    '''

    ftp = FtpClient()
    ftp.connect('localhost', 9999)
    while True:
        print('\033[1;35m{}\033[0m'.format(mainpage))
        choice = input('>>>:')
        if choice == 'q':
            exit()
        elif choice == '1':
            ftp.register()
        elif choice == '2':
            auth_tag = False
            count = 0
            while auth_tag is not True:  ####功能：3次验证不通过即退出
                count += 1
                if count <= 3:
                    auth_tag = ftp.auth()
                else:
                    exit()
            ftp.interactive()
            ftp.close()
