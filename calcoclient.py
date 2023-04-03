import socket
import json

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005
BUFFER_SIZE = 1024
NUM_MESSAGES=5
#creazione del socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for i in range(NUM_MESSAGES):

  primoNumero=float(input("Inserisci il primo numero: "))
  operazione=input("Inserisci l'operazione (+,-,/,%): ")
  secondoNumero=float(input("Inserisci il secondo numero: "))
  messaggio={'primoNumero':primoNumero,
  'operazione':operazione,
  'secondoNumero':secondoNumero}
  messaggio=json.dumps(messaggio)#trasformo l'oggetto in una stringa
  #sock.sendall(messaggio.encode("UTF-8"))
  sock.sendto(messaggio.encode(), (SERVER_IP, SERVER_PORT))
  data=sock.recv(1024)
  print("Risultato: ", data.decode())

#chiusura del socket
sock.close()