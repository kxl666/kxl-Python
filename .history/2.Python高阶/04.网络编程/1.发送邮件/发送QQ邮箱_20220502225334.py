import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender = '2244951869@qq.com'  # 发件人邮箱账号
my_pass = 'eezkyozvtsgpdjad'  # 发件人邮箱密码
my_user = '1816685273@qq.com'  # 收件人邮箱账号，我这边发送给自己


def mail():
    ret = True
    try:
        mail_msg = """
        <p>Python 邮件发送测试...</p>
        <p><a href="http://www.baidu.com">这是一个百度链接</a></p>
        """
        msg = MIMEText(mail_msg, 'plain', 'utf-8')  # 邮件内容
        msg['From'] = formataddr(["卖断货的柯小乐",
                                  my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["卖断货的柯小乐", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "柯小乐发送邮件测试"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [
            my_user,
        ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret


ret = mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")
