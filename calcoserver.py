import socket
import json

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005
BUFFER_SIZE = 1024

#creazione del socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SERVER_IP,SERVER_PORT))

print("Server in attesa di messaggi...")
while True:
    data,addr = sock.recvfrom(1024)
    #if len(data)==0:
    if not data:
        break
    data=data.decode()
    data=json.loads(data)
    primoNumero=data['primoNumero']
    operazione=data['operazione']
    secondoNumero=data['secondoNumero']
    print(primoNumero)
    print(secondoNumero)
    risultato = " "
    if operazione == '+':
        risultato = primoNumero + secondoNumero
    elif operazione == '-':
        risultato = primoNumero - secondoNumero
    elif operazione == '/':
        if secondoNumero == 0:
            risultato = "Non è possibile eseguire una divisione per 0"
        else:
            risultato = primoNumero / secondoNumero
    else:
        risultato = primoNumero / secondoNumero*100
    print(risultato)

    risultato=str(risultato)
    sock.sendto(risultato.encode(),addr)