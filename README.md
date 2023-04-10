# Proyecto-validacion-verificacion

## Super Chat 3000


### Descripción

Super Chat 3000 es un software hecho en python el cual a través de la librería Socket genera una conexión Peer to Peer entre dos sistemas y les permite comunicarse por Chat a través de la consola, la conexión está pensada únicamente para la interacción entre dos sistemas por turnos utilizando una codificación en los mensajes por seguridad.

### Instalación

El software no requiere instalación alguna salvo una versión actualizada de Python 3.x

### Como usar

El software se divide en dos ejecutables: 

* cliente.py 
* server.py

Primer se ejecuta server.py de la siguiente forma: 

> python3 server.py

Lo cual abrirá el servidor y lo dejará escuchando en espera de la conexión del cliente, luego ejecutamos el cliente.

> python3 cliente.py

Si todo está en orden el sistema notificará con un mensaje la conexión existosa entre servidor y cliente permitiendo comenzar el intercambio de mensajes.

En caso de querer conectarse a desde otros computadores será necesario especificar la IP correspondiente al nuevo sistema en el código del archivo "cliente.py" o "servidor.py"

### Como contribuir 

En caso de querer contribuir al código basta con realizar un fork a este proyecto y levantar uan solicitud de incorporación de cambios.




