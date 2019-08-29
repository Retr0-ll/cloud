import os, json
from ftp_server.core import settings


def query_user(username):  # 查询用户
    filelist = os.listdir(settings.userinfo_dir)  # 列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
    # print(filelist)
    for filename in filelist:
        if filename == '.DS_Store':
            continue
        with open(os.path.join(settings.userinfo_dir, filename), 'r', encoding='utf-8') as f:
            content = json.load(f)  # json反序列化
            if content['username'] == username:
                dict_info = {'filename': filename, 'content': content}
                # print("查询结果：",dict)
                return dict_info
    return {}
