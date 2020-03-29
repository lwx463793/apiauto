import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header


def send_email(filepath):


    # 第一步，连接到smtp服务器
    s = smtplib.SMTP()

    # 注意163邮箱的smtp用的是25端口，qq用的是465端口
    s.connect(host='smtp.126.com', port=25)
    # 第二步：登录到smtp服务器
    user = "liumeisky@126.com"
    pwd = "APSOHGSPVSGNWWRI"
    s.login(user=user, password=pwd)

    # 构造文本邮件内容
    content = "测试报告附件"
    text_content = MIMEText(content, _charset='utf8')
    # 构造附件
    part = MIMEApplication(open(filepath, 'rb').read(), _subtype=False)
    part.add_header('content-disposition', 'attachment', filename="测试报告附件")

    # 封装一封邮件
    msg = MIMEMultipart()
    # 加入附件和文本内容
    msg.attach(text_content)
    msg.attach(part)
    # 添加发件人
    msg['From'] = "liumeisky@126.com"
    # 添加收件人
    msg['To'] = "skyliumei@foxmail.com"
    # 添加邮件主题：
    msg['Subject'] = Header('18期测试报告', "utf8")
    s.sendmail(from_addr='liumeisky@126.com', to_addrs="skyliumei@foxmail.com", msg=msg.as_string())



send_email("C:\\Users\\lenovo\\PycharmProjects\\lmapi\\report\\2020-03-26_09_10_46.html")
