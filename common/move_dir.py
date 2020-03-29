import os
import time
import re
from common.constant import REPORT_DIR, LOGS_DIR
import shutil


def file_report(filepath=REPORT_DIR) -> None:  # 打包归档文件
    file = os.path.join(os.path.join(filepath, "history"), time.strftime("%Y%m%d"))
    if not os.path.exists(file):
        os.makedirs(file)
    p = r"\w+.html"
    dirs = str(os.listdir(filepath))
    dir = re.findall(p, dirs)
    for i in dir:
        shutil.move("{}/{}".format(filepath, i), file)


def file_log(filepath=LOGS_DIR) -> str:
    dir = os.path.join(filepath, time.strftime("%Y-%m"))
    if not os.path.exists(dir):
        os.makedirs(dir)
    return os.path.join(dir, "{}.log".format(time.strftime('%Y-%m-%d')))
