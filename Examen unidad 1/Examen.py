"""
Computo distribuido


Gonzalez Barragan Francisco Adrian
Rivera Arano Luis Enrique

"""

#!/usr/bin/python
#! -*- coding: utf-8 -*-
import gevent.monkey, os, sys
from urllib2 import urlopen
gevent.monkey.patch_all()
import tornado.ioloop
from tornado.httpclient import AsyncHTTPClient


#definimos el arreglo
urls = []
def menu():

    """
    limpiar pantalla
    """
    os.system('clear')
    print("Selecione una opcion")
    print("")
    print("\t 1- green thread")
    print("\t 2- callback")
    print("\t 3- Salir")
    print("")

while True:
    #mostrar menu
    menu()

    #solicitamos una opcion al usuario
    opcionMenu = input("Teclear una opcion: ")
#gevent
    if opcionMenu==1:
        agregar = input("Cuantos trabajos desea tener en la pila?: ")
        print("")
        for i in range(agregar):
            elem = raw_input("Cual es el url del trabajo: ")
            urls.append(elem)

        def print_head(url):
            print('Starting {}'.format(url))
            data = urlopen(url).read()
            print('{}: {} bytes: {}'.format(url, len(data), data))

        jobs = [gevent.spawn(print_head, _url) for _url in urls]
        gevent.wait(jobs)
        sys.exit()

#callback
    if opcionMenu==2:
        agregar = input("Cuantos trabajos desea tener en la pila?: ")
        print("")
        for i in range(agregar):
            elem = raw_input("Cual es el url del trabajo: ")
            urls.append(elem)
        def handle_response(response):
            if response.error:
                print("error", response.error)
            else:
                url = response.request.url
                data = response.body
                print('{}: {} bytes: {}'.format(url, len(data), data))

        http_client = AsyncHTTPClient()
        for url in urls:
            http_client.fetch(url, handle_response)

        tornado.ioloop.IOLoop.instance().start()
        sys.exit()

    if opcionMenu==3:
        break

    else:
        print("")
        input("No ha pulsado una opcion correcta... \npulse cualquier tecla para continuar")
        menu()
