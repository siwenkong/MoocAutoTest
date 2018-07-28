# -*-coding:utf-8 -*-
import os
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from public.common.log import Log
from config import globalparam

#测试报告的路径
reportPath = globalparam.report_path
logger = Log()
#配置收件人
recvaddress = ['632989169@qq.com', '496249272@qq.com']
#163邮箱的用户名和密码
sendaddr_name = 'kongsiwen0818@163.com'
#这里是开启POP3的客户端授权码，不是真正的密码
sendaddr_pswd = 'kongsiwen123456'

class SendMail:
    def __init__(self, recver=None):
        """"接收邮件的人：list or tuple"""
        if recver is None:
            self.sendTo = recvaddress
        else:
            self.sendTo = recver

    def __get_report(self):
        """"在测试报告的路径下获取最新测试报告报告"""
        dirs = os.listdir(reportPath)
        dirs.sort()
        newreportname = dirs[-1]
        print('The new report name:{0}'.format(newreportname))
        #返回的是测试报告的名字
        return newreportname

    def __take_messages(self):
        """"生成邮件的内容，和html报告附件"""
        newreport = self.__get_report()
        self.msg = MIMEMultipart()
        #邮件的标题
        self.msg['Subject'] = '测试报告主题'
        self.msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')

        with open(os.path.join(reportPath, newreport), 'rb') as f:
            mailbody = f.read()  #获取测试报告的内容
        html = MIMEText(mailbody, _subtype='html', _charset='utf-8')
        self.msg.attach(html)
        #html附件  下面是将测试报告放在附件中发送
        att1 = MIMEText(mailbody,'base64','gb2312')
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment; filename="TestReport.html"'  # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        self.msg.attach(att1)

    def send(self):
        """发送邮件"""
        self.__take_messages()
        self.msg['from'] = sendaddr_name
        try:
            # 链接服务器
            smtp = smtplib.SMTP('smtp.163.com', 25)
            # 登陆的用户名和密码（密码是设置客户端授权码，因为使用用户密码不稳定，又是无法认证成功，导致登陆不上）
            smtp.login(sendaddr_name, sendaddr_pswd)
            # 发送邮件
            smtp.sendmail(self.msg['from'], self.sendTo, self.msg.as_string())
            smtp.close()
            logger.info("发送邮件成功")
        except Exception:
            logger.error('发送邮件失败')
            raise

if __name__ == '__main__':
    sendMail = SendMail()
    sendMail.send()
