import os

#根目录空间
BASE_DIR = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]

#日志存放目录
LOGS_DIR = os.path.join(BASE_DIR, "logs")

#存放excel 的目录
EXCEL_DIR = os.path.join(BASE_DIR, "excels")

#配置文件存放目录
CONF_DIR = os.path.join(BASE_DIR, "conf")

#图片存放路径
DOCS_DIR = os.path.join(BASE_DIR, "docs")

#存放报告的目录
REPORT_DIR = os.path.join(BASE_DIR, "report")

#测试文件存放路径
CASES_DIR = os.path.join(BASE_DIR, "testcases")