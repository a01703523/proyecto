COSTO_VUELO1 = 50000 #costo individual
COSTO_VUELO2 = 10000 #costo individual
COSTO_VUELO3 = 8500 #costo individual

COSTO_HOTEL_LUJO = 6500 #costo por noche
COSTO_HOTEL_ECONOMICO = 2000 #costo por noche

def costo_noches(costo_hotel, num_noches):
    return costo_hotel*num_noches

def costo_total(costo_vuelo, personas, costo_hotel, num_noches):
    costo_n=costo_noches(costo_hotel, num_noches)*(personas/2)
    return (costo_vuelo*personas)+(costo_n)

print("Gracias por usar nuestro programa señor/a: ")
nom_usuario = str(input())

print("Estimado/a",nom_usuario,"""¿Cuánto dinero tiene disponible?
     (entre $8,500 y $50,000 MXN): """)
dinero=int(input("$"))

if dinero >= 8500:
    print("""Le alcanza para ir a ixtapa, monterrey, barcelona y londres.
    Elija su destino:""")
    
dest=""
while not(dest=="ixtapa" or dest=="monterrey" or dest=="barcelona" or
          dest=="londres"):
    dest=str(input())
    
    desglose_lista = []
         
    if dest == "ixtapa":
        print("El costo del vuelo redondo idividual es $", COSTO_VUELO3,
              "y el costo de una noche es $", COSTO_HOTEL_ECONOMICO,"-",
              "Total $", COSTO_VUELO3 + COSTO_HOTEL_ECONOMICO)
        print("¿Cuántas noches se va a quedar?")
        num_noches=int(input())
        print("El costo de hotel se ha actualizado a $",
              costo_noches(COSTO_HOTEL_ECONOMICO, num_noches))
        print("¿Cuántas personas son?")
        personas=int(input())
        print("El costo total del viaje ha subido a $",
              costo_total(COSTO_VUELO3, personas, COSTO_HOTEL_ECONOMICO,
              num_noches))

        print("¿Desea imprimir los precios desglosados?")
     
   
    #    print(desglose_lista[])

    elif dest == "monterrey":          
        print("El costo del vuelo redondo es $", COSTO_VUELO2,
              "y el costo de una noche es $", COSTO_HOTEL_ECONOMICO,"-",
              "Total $", COSTO_VUELO2 + COSTO_HOTEL_ECONOMICO)
        print("¿Cuántas noches se va a quedar?")
        num_noches=int(input())
        print("El costo de hotel se ha actualizado a $",
              costo_noches(COSTO_HOTEL_LUJO, num_noches))
        print("¿Cuántas personas son?")
        personas=int(input())
        print("El costo total del viaje ha subido a $",
              costo_total(COSTO_VUELO2, personas,COSTO_HOTEL_ECONOMICO,
              num_noches))
        print("¿Desea imprimir los precios desglosados?")

    elif dest == "barcelona":          
        print("El costo del vuelo redondo es $", COSTO_VUELO1,
              "y el costo de una noche es $", COSTO_HOTEL_ECONOMICO,
              "-","Total $",COSTO_VUELO1 + COSTO_HOTEL_ECONOMICO)
        print("¿Cuántas noches se va a quedar?")
        num_noches=int(input())
        print("El costo de hotel se ha actualizado a $",
              costo_noches(COSTO_HOTEL_ECONOMICO, num_noches))
        print("¿Cuántas personas son?")
        personas=int(input())
        print("El costo total del viaje ha subido a $",
              costo_total(COSTO_VUELO1, personas,COSTO_HOTEL_ECONOMICO,
              num_noches))
        print("¿Desea imprimir los precios desglosados?")


    elif dest == "londres":
        print("El costo del vuelo redondo es $", COSTO_VUELO1,
              "y el costo de una noche es $", COSTO_HOTEL_ECONOMICO,
              "-","Total $",COSTO_VUELO1 + COSTO_HOTEL_ECONOMICO)
        print("¿Cuántas noches se va a quedar?")
        num_noches=int(input())
        print("El costo de hotel se ha actualizado a $",
              costo_noches(COSTO_HOTEL_LUJO, num_noches))
        print("¿Cuántas personas son?")
        personas=int(input())
        print("El costo total del viaje ha subido a $",
              costo_total(COSTO_VUELO1, personas,COSTO_HOTEL_ECONOMICO,
              num_noches))
        print("¿Desea imprimir los precios desglosados?")        
