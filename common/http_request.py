import requests
from requests.sessions import Session
from common.logger import logger
import os
from common.constant import DOCS_DIR
from urllib3 import encode_multipart_formdata
from requests_toolbelt import MultipartEncoder



#不带cookie
def request_not_cookie(method,url,**kwargs):
    logger.info("正在以 {} 方式 请求 {}，参数是 {} ".format(method,url,kwargs))
    return requests.request(method=method, url=url, **kwargs)

def updoad_file(url, photo_type, token, app_name):

    file_path = os.path.join(DOCS_DIR, "1.jpg")
    files = {"upload": ("image.png", open(file_path, "rb").read(), "multipart/form-data"), "type": photo_type}
    encode_data = encode_multipart_formdata(files)
    headers = {'content-type': encode_data[1], 'token': token, 'app_name': app_name}
    data = encode_data[0]
    print(data)
    logger.info("正在请求上传文件 URL:{}".format(url))
    return requests.post(url=url, headers=headers, data=data)


#用来请求接口
class HTTPRequest:

    def __init__(self):
        self.session = Session()

    def request_with_cookie(self,method,url,**kwargs):
        logger.info("正在以 {} 方式 请求 {}，参数是 {} ".format(method,url,kwargs))
        return self.session.request(method=method,url=url,**kwargs)


    def upload(self, url, token, account_id, use_type, file_name="1.jpg", **kwargs):
        file_path = os.path.join(DOCS_DIR, file_name)
        # 因为后端采用的是 multipart/form-data方式,其中有 内容分隔符(boundary), 原生request不支持此方式
        file = {"file": ("1.jpg", open(file_path, "rb"), "multipart/form-data"), "use_type": use_type}
        #file = {"upload": ("1.jpg", open(file_path, "rb"), "multipart/form-data"), "type": use_type}
        file = MultipartEncoder(fields=file)
        #headers = {"Content-Type": file.content_type, "token": token}
        #print(headers)
        headers = {"Content-Type": file.content_type, "token": token, "account_id": account_id}
        response = self.session.request("post", url=url, headers=headers, data=file, **kwargs)
        print(file)# 因为转化过了 所以不能用files
        logger.info("正在请求上传文件 URL:{}, file_name:{}".format(url, file_name))
        return response

    #用于在测试类结束的时候，关闭seesion
    def session_close(self):
        self.session.close()


