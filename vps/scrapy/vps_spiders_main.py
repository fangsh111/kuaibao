import pymongo
import os
import datetime
import time
import sys
import logging
import subprocess

######配置log信息
logging.basicConfig(
    level=logging.INFO,
    filename='main.log',
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt='%a, %d %b %Y %H:%M:%S'
    #    filemode='a',
)

if __name__ == '__main__':
    while 1:
        os.chdir(sys.path[0] + '/baidu')
        subprocess.Popen('scrapy crawl baidu_hot')
        logging.info(str(time.strftime('%Y-%m-%d %H:%M:%S',
                                       time.localtime(time.time()))) + ': chengtai_policy scrapy once  running done!!!')
        ####等待10分钟
        time.sleep(60 * 10)
