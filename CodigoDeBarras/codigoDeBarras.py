# COMPRUEBA SI EL NUMERO ES MENOR QUE 13 CIFRAS Y LLAMA A DOS FUNCIONES DEVUELELVE BOOOLEAN 
def codigoDeBarras(cod): 
    res = False 
    if (cod < 9999999999999 and cod > 0):
        #AQUI PASA EL CODIGO A CADENAs
        cod = str(cod)
        if len(cod) > 8:
            res = EAN13(cod)
        else:
            res = EAN8(cod)
    return res
# EAN8 
def EAN8(cod):
    res = False 
    # MIENTRAS QYE LA CADENA SEA MENOR A 8 QUE SIGA CONCATNADO 0
    while len(cod) < 8:  
        cod += "0"  

    digitoComprobacion = 0
    # USA EL RESTO PARA SABER SI ES PAR Y DEPENDIENTO DE ESO LO MULTIPLICA Y LO SUMA A digitoComprobacion
    for i in range(7):  
        if i % 2 == 0:  
            digitoComprobacion += int(cod[i]) * 3
        else:           
            # NO SE PR QUE MULTIPLICO POR UNO PERO EL EJERCICIO LO PIDE
            digitoComprobacion += int(cod[i]) * 1

    digitoComprobacion %= 10
    digitoControl = (10 - digitoComprobacion) % 10
     # COMPRUEBA SI ES CORRETO 
    if digitoControl == int(cod[7]):
        res = True
    return res
# fUNCIONA IGUAL QUE ENA8 PERO CON UN LIMITE DE 13 
def EAN13(cod):
    res = False 
    while len(cod) < 13: 
        cod += "0"  
    digitoComprobacion = 0
    for i in range(12):
        if i % 2 == 0:  
            digitoComprobacion += int(cod[i]) * 1
        else:           
            digitoComprobacion += int(cod[i]) * 3
            
    digitoComprobacion %= 10
    digitoControl = (10 - digitoComprobacion) % 10


    if digitoControl == int(cod[12]):
        res = True
    return res

# def main():
#     print(codigoDeBarras(65839522))     
#     print(codigoDeBarras(65839521))     
#     print(codigoDeBarras(8414533043847)) 
#     print(codigoDeBarras(5029365779425)) 
#     print(codigoDeBarras(5129365779425)) 

# if __name__ == "__main__":
#   main()
