# Tokatl
Simple script en python para extraer links desde una url inicial

tokatkl obtendrá todos los inks de una pagina siempre y cuando no sean referencias javascript secciones dentro de la pagina, por ejemplo, #Inicio.
Mientras obtiene los links comprueba que no hayan duplicados y los guarda en el archivo de salida.


# Uso
tokatl.py -i (input_file | URL) -o output_file
