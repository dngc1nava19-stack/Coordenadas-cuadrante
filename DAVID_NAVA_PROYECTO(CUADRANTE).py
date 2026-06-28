#Crear un programa que en base a 2 números de entrada, coordenadas,
#identifique en cuál de los 4 cuadrantes se encuentra el punto. El programa
#debe verificar que ninguna coordenada sea 0. 

y = float(input("Ingrese Y: "))

# Verificar que ninguna coordenada sea 0 ya que solo es logico mas no grafico 
if x == 0 or y == 0:
    print("Error: ninguna coordenada puede ser 0.")
else:
    # Determina el cuadrante , con 4 validaciones para cada cuadrante del plano 
    if x > 0 and y > 0:
        print("El punto se encuentra en el cuadrante I")
    elif x < 0 and y > 0:
        print("El punto se encuentra en el cuadrante II")
    elif x < 0 and y < 0:
        print("El punto se encuentra en el cuadrante III")
    else: #x > 0 and y < 0  Al haver ocupado todas las convinacuones posibles con dichos elementos , por logica la ultima validacion quedaria en automatico solo utilizando el ELSE .
        print("El punto se encuentra en el cuadrante IV")