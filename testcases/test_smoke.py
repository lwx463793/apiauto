import unittest
from librarys.ddt import ddt,data
from common.read_excel import ReadExcel
from common.constant import EXCEL_DIR
from common.http_request import request_not_cookie
import os
from common.logger import logger
filename=os.path.join(EXCEL_DIR, "casesliumei.xlsx")
re =ReadExcel(filename, "liumei")
cases = re.read_excel_obj()
@ddt
class LoginTestCase(unittest.TestCase):


    @data(*cases)
    def test_login_pass(self, cases):
        response = request_not_cookie(method=cases.method,url="http://test.lemonban.com/futureloan/mvc/api"+cases.api,data=cases.request)

        try:

            self.assertEqual(response.json(), cases.expected)
            logger.info("预期是：{}".format(cases.expected))

        except AssertionError as e:
            logger.exception("预期 {} ".format(cases.expected))
            logger.exception("实际结果是 {} ".format(response.json()))
            raise e
        else:
            logger.info("成功")



    # #def test_passd(self):
    #     self.assertEqual(2,2)
    #
    # #def test_opp(self):
    #     self.assertEqual(2,1)

