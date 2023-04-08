import socket
import logging
import sys 

logging.basicConfig(filename='Logs.log', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filemode='a')


la="abcdefghijklmnopqrstuvwxyz:.,;-_[]"
ua="ABCDEFGHIJKLMNOPQRSTUVWXYZ:.,;-_[]"
lra=la[::-1]
ura=ua[::-1]


try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 9999))
    server.listen()
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
    msg = client.recv(1024).decode('utf-8')
    for i in range(0, len(msg)):
        if msg[i] in lra:
            restore_data+=la[lra.index(msg[i])]
        elif msg[i] in ura:
            restore_data+=ua[ura.index(msg[i])]
        else:
            restore_data+=" "
        
    #logging.info('Mensaje recibido por el servidor')
    
    if msg == '/quit':
        done = True
        logging.info('Conexión terminada por el servidor')
    else:
        print(restore_data)
        mensaje = input("Message: ")
        for i in range(0, len(mensaje)):
            if mensaje[i] in la:
                converted_data+=lra[la.index(mensaje[i])]
            elif mensaje[i] in ua:
                converted_data+=ura[ua.index(mensaje[i])]
            else:
                converted_data+=" "

        client.send(converted_data.encode('utf-8'))
        logging.info('Mensaje enviado por el servidor')
        
        

