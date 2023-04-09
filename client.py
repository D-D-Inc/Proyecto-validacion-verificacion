import socket
import logging
import sys

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
logging.basicConfig(filename='Logs.log', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filemode='a')

try:
    client.connect(("localhost", 9999))
    logging.info('Conexión exitosa con el servidor')
except:
    print("error realizando la conexión")
    logging.critical('Error en la conexión con el servidor')
    sys.exit()
done = False

la="abcdefghijklmnopqrstuvwxyz1234567890"
ua="ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
lra=la[::-1]
ura=ua[::-1]

while not done: 
    converted_data = ""
    restore_data = ""

    mensaje = input("Message: ")
    if mensaje == "/quit":
        logging.info('Conexión terminada por el cliente')
        break 
    if mensaje == "":
        mensaje = " "
    for i in range(0, len(mensaje)):
        if mensaje[i] in la:
            converted_data+=lra[la.index(mensaje[i])]
        elif mensaje[i] in ua:
            converted_data+=ura[ua.index(mensaje[i])]
        elif mensaje[i] == " ":
            converted_data+=" "
        else:
            converted_data+= mensaje[i]

    client.send(converted_data.encode('utf-8'))
    logging.info('Mensaje enviado por cliente')

    msg = client.recv(1024).decode('utf-8')
    #logging.info('Mensaje recibido por el cliente')
    if not msg:
        logging.info('Conexión terminada por el servidor')
        break
    #if msg == "/quit":
    #    done = True
    #    logging.info('Conexión terminada por el cliente')
    else:
        for i in range(0, len(msg)):
            if msg[i] in lra:
                restore_data+=la[lra.index(msg[i])]
            elif msg[i] in ura:
                restore_data+=ua[ura.index(msg[i])]
            elif msg[i] == " ":
                    restore_data+=" "
            else:
                restore_data+= msg[i]
        print(restore_data)
