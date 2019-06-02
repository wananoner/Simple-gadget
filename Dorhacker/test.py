import smtplib
import time
import imaplib
import email

ORG_EMAIL = "@gmail.com"
FROM_EMAIL = "" + ORG_EMAIL
FROM_PWD = ""
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT = 993


def read_email_from_gmail():
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL, FROM_PWD)
        mail.select('inbox')
        print('done!')
        type, data = mail.search(None, 'ALL')
        # mail_ids 应该是邮件数量的列表
        mail_ids = data[0]
        print(mail_ids)
        id_list = mail_ids.split()
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])
        print('id_list:', id_list)
        print('first_email_id:', first_email_id)
        print('latest_email_id', latest_email_id)
        for i in range(latest_email_id, first_email_id, -1):
            print(i)
            typ, data = mail.fetch(str(i), '(RFC822)')
            print('!!!!!!!!!!')
            print('typ:', typ)
            print('data:', data)

            for response_part in data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_string(response_part[1])
                    email_subject = msg['subject']
                    email_from = msg['from']
                    print('From : ' + email_from + '\n')
                    print('Subject : ' + email_subject + '\n')

    except Exception as e:
        print(str(e))
