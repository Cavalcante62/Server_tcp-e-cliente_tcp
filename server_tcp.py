import socket as st
import threading as tg 
from os import system, name

faixa_ip= '0.0.0.0'
port= 9998

def cls():
    system('cls' if name== 'nt' else 'clear')

def handler_client(client:st.socket):
    def hearing():
        while True:
            try:

                request= client.recv(1024)

                if not request:
                    break
                
                elif request.decode()== 'fechar':
                    client.send(b'fechar')
                    client.close()
                    print(f'a conexão foi ecerrada')
                    break

                print(request.decode())


                client.send(b'mensagem recebia\r\n digite: fechar\r\nisso encerrara a conexao')
                
            finally:
                pass
               
    hearing()


def main():
    server= st.socket(st.AF_INET, st.SOCK_STREAM)
    server.bind((faixa_ip, port))
    server.listen(5)
    print(f'[*] Escutando faixas {faixa_ip} pela porta {port}')

    while True:
        client, address= server.accept()

        print(f'[*] Conexão {address[0]}:{address[1]}')

        client_handler= tg.Thread(target= handler_client, args= (client,))
        client_handler.start()

if __name__== '__main__':
    main()