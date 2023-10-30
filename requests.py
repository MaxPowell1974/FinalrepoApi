import requests
import json

#def guardar_contenido_archivo(ubicacion, contenido):
#Variable: todo en minuscula seeparado por guiones bajos
#Objetos con Mayuscula CamelCase
#usar diccionario o vector para urls y variables en general

#funciòn getmovie que reciba argumentos y me devuelve el contenido
#dividir en main logica guardar y funciones 
#investigar reglas de escritura de python 
#investigar subirlo a Git

def guardar_contenido_archivo(ubicacion, contenido):

    #Guardo el json obtenido en un archivo
         #usar a para append  
        t = open(ubicacion,"a") 
        t.write(contenido)
        t.close()
        return True

def guardar_titulo_Search(rta, file):
        
                for rta  in rta['Search']:
                        titulo = rta['Title'] + '\n'
                        f = open(file, "a")
                        f.write(titulo)
                        f.close()     
                return True

def llamar_endpoint(d, ubicacion):
        #for url in d.values():
        for Key in d.keys():
            rtas[Key] = requests.get(d[Key])
            if rtas[Key].status_code ==200:
                    #data = rtas[Key]
                    ls_pelis= json.dumps(rtas[Key].json(), indent=4)       
                    if (guardar_contenido_archivo(ubicacion,ls_pelis)):
                            print(r"grabo bien")




d = {
  "urlTitu": 'http://www.omdbapi.com/?apikey=dfb74b32&t=spiderman&plot=full&r=json',
  "urlBusc": 'http://www.omdbapi.com/?apikey=dfb74b32&plot=full&r=json&S=spider'
}

rtas = {
        "urlTitu": '',
        "urlBusc": ''
}


file_Out = r"pelis\output.json"
file_title_search = r"pelis\titles.json"

#ejecuta EndPoint y guarda la respuesta
llamar_endpoint(d, file_Out)
    
#Filtramos solo los titulos y los guardamos en un archivo
guardar_titulo_Search(rtas.get('urlBusc').json(), file_title_search)

