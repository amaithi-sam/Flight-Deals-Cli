# from twilio.rest import Client
#
# tio_acc_sid = "---------------"
# tio_auth_token = "---------------"
# reg_ph_no = "+---------------"
import smtplib
my_email = "@gmail.com"
password= ""


class NotificationManager:
    # def __init__(self):
        # self.tio_client = Client(tio_acc_sid, tio_auth_token)
    def send_emails(self, msg1, to_email, link):
        with smtplib.SMTP("smtp.gmail.com") as conncetion:
            conncetion.starttls()
            conncetion.login(user=my_email,password=password)
            conncetion.sendmail(
                from_addr=my_email,
                to_addrs=to_email,
                msg= f"Subject : New Low Price Flight\n\n{msg1}\n{link}"
            )
        print(msg1)


    # def send_message(self, msg):
    #
    #     # message = self.tio_client.messages.create(
    #     #     body= msg,
    #     #     from_= f"{reg_ph_no}",
    #     #     to='+---------')
    #     # print(message.status)
    #     print(msg)
