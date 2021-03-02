import xmlrpc.client
from xmlrpc.client import ServerProxy
from _thread import *
import json,socket

def printnews():
    print('noticias disponibles: ')
    for i in range(len(s.listTile())):
        print(s.listTile()[i])
def menu(user,admin) :
    if op=='True':
        print('1 Para ver noticias \n2 para eliminar una publicacion\n0 para finalizar')
        opcion = int(input('Dijite la opcion que quiere realizar: '))
        while opcion != 0:
            if opcion == 1:
                printnews()
            if opcion == 2:
                index = int(input('cual publicacion quiere eliminar: '))
                ans = s.delete(index, user, admin)
                if ans:
                    print('Registro eliminado')
                else:
                    print('No puedes eliminar esta publicacion')
            opcion = int(input('Dijite la opcion que quiere realizar: '))


    if op == 'False':
        print('1 Para ver noticias\n2 para publicar una noticia \n3 para eliminar una publicacion\n4 editar una publicacion\n0 para finalizar')
        opcion = int(input('Dijite la opcion que quiere realizar: '))
        while opcion != 0:
            if opcion == 1:
                printnews()
                #----------llamada a aldair-----------#

            if opcion == 2:
                titulo = input('Escriba el titulo de la noticia: ')
                contenido = input('Escriba el contenido de la noticia: ')
                s.post(titulo+','+contenido,user)
            if opcion == 3:
                index=int(input('cual publicacion quiere eliminar: '))
                ans=s.delete(index, user, op)
                if ans:
                    print('Registro eliminado')
                else:
                    print('No puedes eliminar esta publicacion')
            if opcion == 4:
                index = int(input('cual publicacion quiere modificar: \n'))
                titulo = input('Que cambio quieres hacer al  titulo de la noticia \n')
                contenido = input('Que cambio quiere hacer al contenido de la noticia? \n')

                ans=s.edit(index,user, str(titulo+','+contenido))
                if ans == False: print('No existe esa noticia')
            opcion = int(input('Dijite la opcion que quiere realizar: '))
alda_socket = socket.socket()
alda_socket.connect(('localhost', 1200))#--------------------------------------------------------------clientedeAlda
mi_socket = socket.socket()
mi_socket.bind(('localhost', 1100))  #-----------------------------------------------------------------server
s = ServerProxy('http://localhost:8000', allow_none= True)
op = 1 #int(input("Bienvenido al blog \n1 para iniciar sesion \n2 para crear un nuevo usuario\n"))
sesion={}
if(op==1):
    nombre = input('Digite su nombre de usuario: \n')
    clave = input('Digite su clave: \n')

    try:
        if(s.login(str(nombre+','+clave))):
            a= s.searchUser(str(nombre + ',' + clave)).split(',')
            admin = a[2].strip("\n")
            sesion = {'nombre': nombre, 'admin': admin}
            print('Bienvenido ' + nombre)
            printnews()
        else:
            print('No se pudo iniciar sesión')
    except xmlrpc.client.Fault as err:
        print(err.faultString)

    menu(sesion['nombre'],sesion['admin'])
    op=input('Dijite la opcion que quiere realizar')

"""
if(op==2):
    nombre = input('Digite su nombre de usuario: \n')
    clave = input('Digite su clave: \n')
    data = str(nombre+','+clave)
    if s.signin(data):
        print("inicio de sesion completado")
        print('Bienvenido ' + nombre)
        a = s.searchUser(str(nombre + ',' + clave)).split(',')
        admin = a[2].strip("\n")
        sesion = {'nombre': nombre, 'admin': admin}
    else:
        print('Se ha provocado un error Tipografico o el nombre de usuario ya ha sido tomado ')
    menu(sesion['nombre'],sesion['admin'])
"""

