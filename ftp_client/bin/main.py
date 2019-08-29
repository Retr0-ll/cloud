from ftp_client.core.client import FtpClient

if __name__ == '__main__':
    ftp = FtpClient()
    ftp.connect('localhost', 9999)

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
