#!/bin/python3
#Tokatl significa araña
import getopt
import sys
import requests
from os import path
from bs4 import BeautifulSoup

global lista_enlaces

lista_enlaces = []

def ayuda():
	print("Modo de uso:\n {} -i (input_file | URL) -o output_file".format(sys.argv[0]))
	sys.exit()

def enumerar_urls(input_source,output_file,verbose):
	global lista_enlaces
	
	if output_file == None:
		output_file = "Scraped-URLs.txt"

	if path.isfile(input_source):
		archivo_entrada = open(input_source, 'r')
		lineas = archivo_entrada.readlines()
		for linea in lineas:
			enumerar_urls(linea, output_file, verbose)
			if verbose:
				print("Trabajando en: %s"%linea)
	else:
		archivo_salida = open(output_file,'a')
		peticion = requests.get(input_source)
		sopa = BeautifulSoup(peticion.text, 'lxml')

		for enlace in sopa.find_all('a'):
			item = enlace.get('href')
			if item != None and len(item) > 0 and item[0] != "#" and 'javascript' not in item and item not in lista_enlaces:
				lista_enlaces.append(item)
				archivo_salida.writelines(item+'\n')
				if verbose:
					print("url encontrada: %s"%item)

		archivo_salida.close()



if __name__ == '__main__':

	argumentos = sys.argv[1:]

	if argumentos != []:
		try:
			opts, args = getopt.getopt(argumentos, 'hvu:i:o:', ["help","verbose","url","input-file","output-file"])
		except getopt.GetoptError as e:
			print (e)
			ayuda()
			sys.exit(2)

		verbose=False
		input_source=None
		output_file=None
		for opt, arg in opts:
			if opt in ("-h", "--help"):
				ayuda()
			elif opt in ("-v","--verbose"):
				verbose=True
			elif opt in ("-i","--input"):
				input_source=arg
			elif opt in ("-o","--output-file"):
				output_file=arg

		enumerar_urls(input_source,output_file,verbose)
		print("Total de URLs encontradas: %d"%(len(lista_enlaces)))
	else:
		ayuda()
