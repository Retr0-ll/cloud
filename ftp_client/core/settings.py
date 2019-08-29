# Author:Zheng Na

import os, configparser, logging

# 读取配置文件 #
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_file = os.path.join(base_dir, 'conf/client.conf')
cf = configparser.ConfigParser()
cf.read(config_file, encoding='utf-8')

# 设定日志目录 #
if os.path.exists(cf.get('log', 'logfile')):
    logfile = cf.get('log', 'logfile')
else:
    default_logdir = os.path.join(base_dir, 'log')
    if not os.path.exists(default_logdir):
        os.mkdir(default_logdir)
    logfile = os.path.join(base_dir, 'log/client.log')

# 设定下载/上传目录 #
if os.path.exists(cf.get('download', 'download_dir')):
    download_dir = cf.get('download', 'download_dir')
else:
    download_dir = os.path.join(base_dir, 'temp')

# 设置日志格式 #
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename=logfile,
                    filemode='a+')
