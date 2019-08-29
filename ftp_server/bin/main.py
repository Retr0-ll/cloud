####os.path.abspath(__file__) 获取当前当前文件的绝对路径
####os.path.dirname()获取当前文件上一层目录
import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  ####获取当前文件的上一级的上一级目录
sys.path.append(BASE_DIR)


import socketserver
from ftp_server.core.server import MyTCPHandler
from ftp_server.core.usermanagement import UserOpr
from ftp_server.core.server import MySSLThreadingTCPServer

if __name__ == '__main__':

    mainpage = '''
    主页
        1、启动服务器
        2、进入用户管理
        退出请按q
    '''

    while True:
        print('\033[1;35m{}\033[0m'.format(mainpage))
        choice = input('>>>:')
        if choice == 'q':
            exit()
        elif choice == '1':
            HOST, PORT = "localhost", 9999
            server = MySSLThreadingTCPServer((HOST, PORT), MyTCPHandler)
            #server = socketserver.ThreadingTCPServer((HOST,PORT),MyTCPHandler)
            server.serve_forever()
        elif choice == '2':
            useropr = UserOpr()
            # useropr.query_all_user()  ####查询所有用户信息
            useropr.interactive()
        else:
            print("\033[1;31m输入错误，请重新输入\033[0m")
            continue
