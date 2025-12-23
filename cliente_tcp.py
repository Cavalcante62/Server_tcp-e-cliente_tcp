import socket as st
from os import system, name

def cls():
    system('cls' if name== 'nt' else 'clear')

target_host= '127.0.0.1'
target_port= 9998

client=st.socket(st.AF_INET, st.SOCK_STREAM)
client.connect((target_host, target_port))


def enviar():
    while True:
        try:
            print('digite "fechar" para encerrar\n')
            mensagem= input('Digite a mensagem que quer enviar\n'
                    'Mensagem:')
            
            client.send(mensagem.encode('utf-8'))
            response= client.recv(4090)
            
            if response.decode()== 'fechar':
                break

            print(response.decode())
            cls()

        except KeyboardInterrupt:
            client.send(b'fechar')
            client.close()
            cls()
            break

enviar()