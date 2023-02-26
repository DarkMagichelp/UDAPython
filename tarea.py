
def faltas():

    falta = int(input("ingrese el numero de faltas: \n"))
    if (falta <= 2):
        falt = 3 - falta  
        print(f"tienes {falta} falta(s), {falt} mas y estaras reprobado ")
        print("\n")
        

    if (falta >= 3): 
         
        print("Estas reprobado por faltas ")
        
    else:
        def adeudo():
            debe = input("el alumno tiene adeudo: \n")
            si = True
            no = False
            if  debe == "si" : 
                    print("Tienes una falta por adeudo, favor de ponerte al corriente ")
            else: print("estas al corriente , gracias por su pago oportuno ")
        adeudo()
                    
faltas()
        













   

    


