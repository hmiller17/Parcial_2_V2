def punto_1():
    lista = ["a",5,"q",5.4344,"1",-5,5/2]        #Ejemplo 1
    #lista = ["q","c",33,34,"quert",-90,45*-2]   #Ejemplo 2
    for i  in lista:
        j = lista.count(i)
        if(j > 1):
            print("Hay elementos repetidos en la lista")
            break
        else:
            next
    if(j == 1):
        print("No hay elementos repetidos en la lista")



def punto_2():
    lista = ["Sur","bus","And","CAL"]                   #Ejemplo 1
    #lista = ["Hola","CARRO","ruta","Atleta","Luz"]     #Ejemplo 2
    vocales = ["a","e","i","o","u","A","E","I","O","U"]
    cadenas = []
    for i in lista:
        c = 0
        list(i)
        for j in i:
            if(j in vocales):
                c += 1
                if(c >= 2):
                    str(i)
                    cadenas.append(i)
                    break
    if(len(cadenas) == 0):
        print("No existe")
    else:
        print(cadenas)



def punto_3():
    lista1 = ["a","x","c","c",-2,6.45,8/2]  
    lista2 = ["a","b","b","c",2,6.45]
    
    lista_unica = []
    if(len(lista1) >= len(lista2)):
        lista_mayor = lista1
        lista_menor = lista2
    else:
        lista_mayor = lista2
        lista_menor = lista1
    for i in lista_mayor:
        if(i not in lista_menor):
            lista_unica.append(i)
        else:
            next
    print(lista_unica)
    


def punto_4():
    lista_reales = [1/4, 0.4, 23, 3.4, 1, 56, -34, 0.34/8.9]    #Ejemplo 1
    #lista_reales = [1,2,3,4,5]                                  #Ejemplo 2
    j = 0
    for i in lista_reales:
        j += i

    promedio = j / len(lista_reales)
    print(f"El promedio de {lista_reales} es: {promedio}")



def punto_5():
    lista = [-2,2,-3,4,20,6,-8]  #Ejemplo 1
    #lista = [1,2,3,4]   #Ejemplo 2
    lista.sort()
    a = len(lista)//2
    if (a % 2 == 0):
        print((lista[a-1]+lista[a])/2)
    else:
        print(lista[a])



def main():
    punto_1()
    punto_2()
    punto_3()
    punto_4()
    punto_5()

if(__name__ == "__main__"):
    main()