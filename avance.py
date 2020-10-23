#Biblioteca extra investigada
#Esta biblioteca se utiliza para abrir paginas web con informacion adicional,
#en caso que el usuario no se conforme con los resultados del programa.
#Cuando la uso abre en un buscador la liga indicada.
import webbrowser

ligas=["""https://www.trivago.com.mx/?aDateRange%5Barr%5D=2020-11-03&aDateRang
e%5Bdep%5D=2020-11-04&aPriceRange%5Bfrom%5D=0&aPriceRange%5Bto%5D=0&iRoomType=
1&aRooms%5B0%5D%5Badults%5D=1&cpt2=423819%2F200&hasList=1&hasMap=1&bIsSeoPage=
0&sortingId=1&slideoutsPageItemId=&iGeoDistanceLimit=20000&address=&addressGeo
Code=&offset=0&ra=&overlayMode=""",
      
      """https://www.trivago.com.mx/?aDateRange%5Barr%5D=2020-11-03&aDateRange
%5Bdep%5D=2020-11-04&aPriceRange%5Bfrom%5D=0&aPriceRange%5Bto%5D=0&iRoomType=1
&aRooms%5B0%5D%5Badults%5D=1&cpt2=32143%2F200&hasList=1&hasMap=1&bIsSeoPage=0&
sortingId=1&slideoutsPageItemId=&iGeoDistanceLimit=20000&address=&addressGeoCo
de=&offset=0&ra=&overlayMode=""",
      
      """https://www.trivago.com.mx/?aDateRange%5Barr%5D=2020-11-05&aDateRange
%5Bdep%5D=2020-11-06&aPriceRange%5Bfrom%5D=0&aPriceRange%5Bto%5D=0&iRoomType=7
&aRooms%5B0%5D%5Badults%5D=2&cpt2=13437%2F200&hasList=1&hasMap=1&bIsSeoPage=0&
sortingId=1&slideoutsPageItemId=&iGeoDistanceLimit=20000&address=&addressGeoCo
de=&offset=0&ra=&overlayMode=""",
      
      """https://www.trivago.com.mx/?aDateRange%5Barr%5D=2020-11-03&aDateRange
%5Bdep%5D=2020-11-04&aPriceRange%5Bfrom%5D=0&aPriceRange%5Bto%5D=0&iRoomType=1
&aRooms%5B0%5D%5Badults%5D=1&cpt2=17399%2F200&hasList=1&hasMap=1&bIsSeoPage=0&
sortingId=1&slideoutsPageItemId=&iGeoDistanceLimit=20000&address=&addressGeoCo
de=&offset=0&ra=&overlayMode="""]
 

COSTO_VUELO1 = 50000 #costo individual
COSTO_VUELO2 = 10000 #costo individual
COSTO_VUELO3 = 8500 #costo individual
COSTO_HOTEL_LUJO = 6500 #costo por noche
COSTO_HOTEL_ECONOMICO = 2000 #costo por noche


#Esta funcion calcula el costo del hotel, ya sea de lujo o economico,
#multiplicando por el numero de noches ingresadas por el usuario.
def costo_noches(costo_hotel, num_noches):
    return costo_hotel*num_noches


#Esta funcion calcula el costo total del viaje considerando todos los aspectos
#de variables, constantes y pasa como parametro la funcion anterior.
#Calcula el costo total de vuelos y suma el costo de noches de hotel.
def costo_total(costo_vuelo, personas, costo_hotel, num_noches):
    costo_n=costo_noches(costo_hotel, num_noches)*(personas/2)
    return (costo_vuelo*personas)+(costo_n)

       
print("Gracias por usar nuestro programa señor/a: ")
nom_usuario = str(input())

print("Estimado/a",nom_usuario,"""¿Cuánto dinero tiene disponible?
     (entre $8,000 y $50,000 MXN): """)
dinero=int(input("$"))

if dinero >= 40000:
    print("""Le alcanza para ir a ixtapa, monterrey, barcelona o londres.
    Elija su destino:""")    
    dest=""
    while not(dest=="ixtapa" or dest=="monterrey" or dest=="barcelona" or
              dest=="londres"):
        dest=str(input())
        
elif dinero < 40000 and dinero >= 30000:
    print("""Le alcanza para ir a ixtapa, monterrey o barcelona.
    Elija su destino:""")    
    dest=""
    while not(dest=="ixtapa" or dest=="monterrey" or dest=="barcelona"):
        dest=str(input())
        
elif dinero < 30000 and dinero >= 15000:
    print("""Le alcanza para ir a ixtapa o monterrey.
    Elija su destino:""")    
    dest=""
    while not(dest=="ixtapa" or dest=="monterrey"):
        dest=str(input())
        
elif dinero < 15000 and dinero >= 8000:
    print("""Le alcanza para ir a ixtapa.
    Escriba su destino:""")    
    dest=""
    while not(dest=="ixtapa"):
        dest=str(input())
        
else:
    print("No tiene suficiente dinero :(")
    
    
desglose_lista = [0,1,2,3,4,5,6]
         
if dest == "ixtapa":
    desglose_lista[0]="Vuelo redondo:",COSTO_VUELO3
    desglose_lista[3]="Precio de la noche hotel",COSTO_HOTEL_ECONOMICO
    print("El costo del vuelo redondo idividual es $", COSTO_VUELO3,
          "y el costo de una noche es $", COSTO_HOTEL_ECONOMICO,"-",
          "Total $", COSTO_VUELO3 + COSTO_HOTEL_ECONOMICO)
    print("¿Cuántas noches se va a quedar?")
    num_noches=int(input())
    desglose_lista[4]="Noches",num_noches
    desglose_lista[5]="TOTAL = $",costo_noches(COSTO_HOTEL_ECONOMICO,
                                                   num_noches) 
    print("El costo de hotel se ha actualizado a $",
          costo_noches(COSTO_HOTEL_ECONOMICO, num_noches))
    print("¿Cuántas personas son?")
    personas=int(input())
    desglose_lista[1]="Personas:",personas
    desglose_lista[2]="TOTAL = $",COSTO_VUELO3*personas
    print("El costo total del viaje ha subido a $",
          costo_total(COSTO_VUELO3, personas, COSTO_HOTEL_ECONOMICO,
          num_noches))
    desglose_lista[6]="COSTO TOTAL DEL VIAJE:",costo_total(COSTO_VUELO3,
                                                               personas,
                                                               COSTO_HOTEL_ECONOMICO,
                                                               num_noches)

    print("¿Desea imprimir los precios desglosados?")
    desglose=str(input())
    if desglose=="si":
        print(desglose_lista[0],"",desglose_lista[1],"",desglose_lista[2])
        print(desglose_lista[3],"",desglose_lista[4],"",desglose_lista[5])
        print(desglose_lista[6])

        print("""Esperamos haya estado satisfecho con los resultados
        ¿Quiere ver otro tipo de resultados""")
        mas_resultados=str(input("¿si o no? "))
        if mas_resultados=="si":
            webbrowser.open(ligas[0], new=1, autoraise=True)
        else:
            print("¡Nos vemos en Ixtapa!")
    else:
        print("""Esperamos haya estado satisfecho con los resultados
        ¿Quiere ver otro tipo de resultados""")
        mas_resultados=str(input("¿si o no? "))
        if mas_resultados=="si":
            #Aqui se manda a llamar la biblioteca
            webbrowser.open(ligas[0], new=1, autoraise=True)
        else:
            print("¡Nos vemos en Ixtapa!")


elif dest == "monterrey":
    desglose_lista[0]="Vuelo redondo:",COSTO_VUELO2
    desglose_lista[3]="Precio de la noche hotel",COSTO_HOTEL_LUJO
    print("El costo del vuelo redondo es $", COSTO_VUELO2,
          "y el costo de una noche es $", COSTO_HOTEL_LUJO,"-",
          "Total $", COSTO_VUELO2 + COSTO_HOTEL_LUJO)
    print("¿Cuántas noches se va a quedar?")
    num_noches=int(input())
    desglose_lista[4]="Noches",num_noches
    desglose_lista[5]="TOTAL = $",costo_noches(COSTO_HOTEL_LUJO,
                                                   num_noches)
    print("El costo de hotel se ha actualizado a $",
          costo_noches(COSTO_HOTEL_LUJO, num_noches))
    print("¿Cuántas personas son?")
    personas=int(input())
    desglose_lista[1]="Personas:",personas
    desglose_lista[2]="TOTAL = $",COSTO_VUELO2*personas
    print("El costo total del viaje ha subido a $",
          costo_total(COSTO_VUELO2, personas,COSTO_HOTEL_LUJO,
          num_noches))
    desglose_lista[6]="COSTO TOTAL DEL VIAJE:",costo_total(COSTO_VUELO2,
                                                               personas,
                                                               COSTO_HOTEL_LUJO,
                                                               num_noches)
    
    print("¿Desea imprimir los precios desglosados?")
    desglose=str(input())
    if desglose=="si":
        print(desglose_lista[0],"",desglose_lista[1],"",desglose_lista[2])
        print(desglose_lista[3],"",desglose_lista[4],"",desglose_lista[5])
        print(desglose_lista[6])
        
        print("""Esperamos haya estado satisfecho con los resultados
        ¿Quiere ver otro tipo de resultados""")
        mas_resultados=str(input("¿si o no? "))
        if mas_resultados=="si":
            webbrowser.open(ligas[1], new=1, autoraise=True)
        else:
            print("¡Nos vemos en Monterrey!")
    else:
        print("""Esperamos haya estado satisfecho con los resultados
        ¿Quiere ver otro tipo de resultados""")
        mas_resultados=str(input("¿si o no? "))
        if mas_resultados=="si":
            webbrowser.open(ligas[1], new=1, autoraise=True)
        else:
            print("¡Nos vemos en Monterrey!")
 
 
elif dest == "barcelona":
    desglose_lista[0]="Vuelo redondo:",COSTO_VUELO1
    desglose_lista[3]="Precio de la noche hotel",COSTO_HOTEL_ECONOMICO
    print("El costo del vuelo redondo es $", COSTO_VUELO1,
          "y el costo de una noche es $", COSTO_HOTEL_ECONOMICO,
          "-","Total $",COSTO_VUELO1 + COSTO_HOTEL_ECONOMICO)
    print("¿Cuántas noches se va a quedar?")
    num_noches=int(input())
    desglose_lista[4]="Noches",num_noches
    desglose_lista[5]="TOTAL = $",costo_noches(COSTO_HOTEL_ECONOMICO,
                                                   num_noches)
    print("El costo de hotel se ha actualizado a $",
          costo_noches(COSTO_HOTEL_ECONOMICO, num_noches))
    print("¿Cuántas personas son?")
    personas=int(input())
    desglose_lista[1]="Personas:",personas
    desglose_lista[2]="TOTAL = $",COSTO_VUELO1*personas
    print("El costo total del viaje ha subido a $",
          costo_total(COSTO_VUELO1, personas,COSTO_HOTEL_ECONOMICO,
          num_noches))
    desglose_lista[6]="COSTO TOTAL DEL VIAJE:",costo_total(COSTO_VUELO1,
                                                               personas,
                                                               COSTO_HOTEL_ECONOMICO,
                                                               num_noches)
    
    print("¿Desea imprimir los precios desglosados?")
    desglose=str(input())
    if desglose=="si":
        print(desglose_lista[0],"",desglose_lista[1],"",desglose_lista[2])
        print(desglose_lista[3],"",desglose_lista[4],"",desglose_lista[5])
        print(desglose_lista[6])

        print("""Esperamos haya estado satisfecho con los resultados
        ¿Quiere ver otro tipo de resultados""")
        mas_resultados=str(input("¿si o no? "))
        if mas_resultados=="si":
            webbrowser.open(ligas[2], new=1, autoraise=True)
        else:
            print("¡Nos vemos en Barcelona!")
    else:
        print("""Esperamos haya estado satisfecho con los resultados
        ¿Quiere ver otro tipo de resultados""")
        mas_resultados=str(input("¿si o no? "))
        if mas_resultados=="si":
            webbrowser.open(ligas[2], new=1, autoraise=True)
        else:
            print("¡Nos vemos en Barcelona!")


elif dest == "londres":
    desglose_lista[0]="Vuelo redondo:",COSTO_VUELO1
    desglose_lista[3]="Precio de la noche hotel",COSTO_HOTEL_LUJO
    print("El costo del vuelo redondo es $", COSTO_VUELO1,
          "y el costo de una noche es $", COSTO_HOTEL_LUJO,
          "-","Total $",COSTO_VUELO1 + COSTO_HOTEL_LUJO)
    print("¿Cuántas noches se va a quedar?")
    num_noches=int(input())
    desglose_lista[4]="Noches",num_noches
    desglose_lista[5]="TOTAL = $",costo_noches(COSTO_HOTEL_LUJO,
                                                   num_noches)
    print("El costo de hotel se ha actualizado a $",
          costo_noches(COSTO_HOTEL_LUJO, num_noches))
    print("¿Cuántas personas son?")
    personas=int(input())
    desglose_lista[1]="Personas:",personas
    desglose_lista[2]="TOTAL = $",COSTO_VUELO1*personas
    print("El costo total del viaje ha subido a $",
          costo_total(COSTO_VUELO1, personas,COSTO_HOTEL_LUJO,
          num_noches))
    desglose_lista[6]="COSTO TOTAL DEL VIAJE:",costo_total(COSTO_VUELO1,
                                                               personas,
                                                               COSTO_HOTEL_LUJO,
                                                               num_noches)
    print("¿Desea imprimir los precios desglosados?")
    desglose=str(input())
    if desglose=="si":
        print(desglose_lista[0],"",desglose_lista[1],"",desglose_lista[2])
        print(desglose_lista[3],"",desglose_lista[4],"",desglose_lista[5])
        print(desglose_lista[6])
        
        print("""Esperamos haya estado satisfecho con los resultados
        ¿Quiere ver otro tipo de resultados""")
        mas_resultados=str(input("¿si o no? "))
        if mas_resultados=="si":
            webbrowser.open(ligas[3], new=1, autoraise=True)
        else:
            print("¡Nos vemos en Londres!")
    else:
        print("""Esperamos haya estado satisfecho con los resultados
        ¿Quiere ver otro tipo de resultados""")
        mas_resultados=str(input("¿si o no? "))
        if mas_resultados=="si":
            webbrowser.open(ligas[3], new=1, autoraise=True)
        else:
            print("¡Nos vemos en Londres!")