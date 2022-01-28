def lolpercent():

    partidas   = int(input("Total:                 "))
    porcentaje = float(input("Porcentaje de ganadas: "))
    deseado    = float(input("Porcentaje deseado:    "))

    ganadas = float(porcentaje*partidas/100)
    print("\nActuales:   ",int(ganadas),"/",int(partidas)," = ",porcentaje)

    while porcentaje < deseado:
        partidas+=1
        ganadas+=1
        porcentaje = ganadas*100/partidas
            
    print("Necesarias: ",int(ganadas),"/",int(partidas)," = ",porcentaje)

print()
lolpercent()

