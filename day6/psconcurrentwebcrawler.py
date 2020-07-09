# ipc/sync uisng queue
import multiprocessing
from smtplib import SMTP
from email.mime.text import MIMEText
import requests
from os import environ

#  /home/ravijaya/anaconda3/bin/python

smtp_server_address = 'localhost'


def send_alert_mail(from_addr, to_addr, subject, message, debug=False):
    mesg = MIMEText(message)
    mesg['From'] = from_addr
    mesg['To'] = to_addr
    mesg['Subject'] = subject

    smtp = SMTP(smtp_server_address)
    smtp.debuglevel = debug
    smtp.sendmail(from_addr, to_addr, mesg.as_string())
    smtp.close()


def web_crawler(q):
    """child process"""
    try:
        p_name = multiprocessing.current_process().name
        url = q.get()  # get an item from the queue, blocked
        response = requests.get(url)
        print(f'{p_name}: {url}: {response.content[:128]}')
    except requests.exceptions.ConnectionError as error:
        subject = f'{p_name}: {url}: failed http request'
        send_alert_mail('ravijaya@localhost', 'training@localhost', subject, str(error), debug=True)


def main():
    urls = ['http://linux.org', 'http://kernel.org', 'http://python.org', 'http://golang.org',
            'http://perllang.org']

    queue = multiprocessing.Queue()  # empty queue

    for url in urls:
        multiprocessing.Process(target=web_crawler, args=(queue,)).start()

    for url in urls:
        queue.put(url)  # add item into the queue

    for child in multiprocessing.active_children():
        child.join()


if __name__ == '__main__':
    main()
