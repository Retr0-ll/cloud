#Author:Zheng Na

import os,json
import core.settings

def query_user(username):  ####查询用户
    filelist = os.listdir(core.settings.userinfo_dir)  ####列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
    dict = {}
    #print(filelist)
    for filename in filelist:
        if filename == '.DS_Store':
            continue
        with open (os.path.join( core.settings.userinfo_dir,filename),'r',encoding='utf-8') as f:
            content = json.load(f)  ####json反序列化
            if content['username'] == username:
                dict = {'filename':filename,'content':content}
                # print("查询结果：",dict)
                return dict
