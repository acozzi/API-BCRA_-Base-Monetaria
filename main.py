import requests
import json

"""
Trabaja sobre un json que aporta la base monetaria desde el 01 de febrero de 1996 hasta la fecha actual.
{'d': '2020-01-10', 'v': 1606490}
Formato aaaa-mm-dd
"""

url='https://api.estadisticasbcra.com/base'
response = requests.get(
    url,
    headers={'Authorization': 'BEARER eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MTA1Nzk2NjgsInR5cGUiOiJleHRlcm5hbCIsInVzZXIiOiJhY296enppQGdtYWlsLmNvbSJ9.TClLhOu_vNjAlUfSHk8PhypfvpstbzMK4Jfv8ZbADeB1DbRy9iG0VKe11unFrv3L9YLrPeAf7YIp3XrsR-_MoA'}
)

# Funciones
def imprimeOrdenado(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

def busquedaBinaria(obj, dato):
    contador=0
    minimo=0
    maximo=len(obj)
    pista=int((maximo-minimo)/2+minimo)

    while(obj[pista].get('d')!=dato):
        if(obj[pista].get('d')>dato):
            maximo=pista 
        elif(obj[pista].get('d')<dato):
            minimo=pista
        
        pista=int((maximo-minimo)/2+minimo)
        if(maximo-minimo==1 and obj[pista].get('d')!=dato):
            return -1
        contador=contador+1
    print("Iteraciones en búsqueda binaria: "+str(contador))
    return pista

print(response.status_code) 
#imprimeOrdenado(response.json())
baseMonetaria=response.json()


print("Base disponible desde el " + baseMonetaria[0].get('d') + " hasta el " + baseMonetaria[len(baseMonetaria)-1].get('d'))

solicitud= input("Ingrese la fecha en formato aaaa-mm-dd: ")
#print(solicitud)
ubicacion= busquedaBinaria(baseMonetaria, solicitud)
if(ubicacion==-1):
    print("El día solicitado no se encuentra en la base de datos")
else:
    print("La base monetaria para el día solicitado fue de $" + str(baseMonetaria[ubicacion].get('v'))+ ".00")


for i in range(len(baseMonetaria)):
    if(baseMonetaria[i].get('d')==solicitud):
        print("Iteraciones en búsqueda secuencial: "+str(i))
        print("La base monetaria para el día solicitado fue de $" + str(baseMonetaria[i].get('v'))+ ".00")

