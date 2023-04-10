import socket
import logging
import sys 

logging.basicConfig(filename='Logs.log', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filemode='a')


la="abcdefghijklmnopqrstuvwxyz"
ua="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lra=la[::-1]
ura=ua[::-1]


try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 9999))
    server.listen(1)
    logging.info('Servidor escuchando')
except:
    logging.critical('Error en el binding')

try:
    client, addr = server.accept()
    done = False
    print("Conexión exitosa")
except:
    print("Conexión fallida")
    sys.exit()
#logging.info('Servidor y cliente conectados')

while not done: 
    converted_data = ""
    restore_data = ""
    msg = client.recv(8192).decode('utf-8')
    if not msg:
        socket.close()
        break
    for i in range(0, len(msg)):
        if msg[i] in lra:
            restore_data+=la[lra.index(msg[i])]
        elif msg[i] in ura:
            restore_data+=ua[ura.index(msg[i])]
        elif msg[i] == " ":
                restore_data+=" "
        else:
            restore_data+= msg[i]
        
    #logging.info('Mensaje recibido por el servidor')
    
    #if msg == '/quit':
    #    done = True
    #    logging.info('Conexión terminada por el servidor')
    else:
        print(restore_data)
        mensaje = input("Message: ")
        if mensaje == "/quit":
            logging.info('Conexión terminada por el servidor')
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
        logging.info('Mensaje enviado por el servidor')
        
        

