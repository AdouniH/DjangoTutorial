from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def arrange(l):

    b = []
    for i in l:
        b.append(i["comparator"])
        b = list(set(b))

    dico = {}
    c = []
    for j in b:
        toto = {}
        for i in l:
            if i["comparator"] == j:
                if not toto:
                    toto = {
                            "day": i["day"],
                            "day_name": i["day_name"],
                            "comparator": i["comparator"],
                            "hours": [{"hour": i["hour"], "id": i["id"]}]
                        }
                else:
                    toto["hours"].append({"hour": i["hour"], "id": i["id"]})
        c.append(toto)

    b.sort()
    sorted = []
    for i in b:
        for j in c:
            if i == j["comparator"]:
                sorted.append(j)
    return sorted

def send_mail(to_email, subject, message):
    """
    :param to_email: (eg. "houssemadouni11@gmail.com")
    :param subject: (eg. "Subscription")
    :param message: (eg. "Thank you for ur registration")
    """

    # create message object instance
    msg = MIMEMultipart()

    # setup the parameters of the message
    f = open("/home/houssem/Documents/pwd.txt", "r")
    password = (f.read()).strip()
    msg['From'] = "automatedemails.houssemadouni@gmail.com"
    msg['To'] = to_email
    msg['Subject'] = subject
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
    # create server
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    # Login Credentials for sending the mail
    server.login(msg['From'], password)
    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()
