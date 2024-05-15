'''Este algoritmo permite administrar el stock de la tienda'''
import os 
print('***********************\nadministrador de stock\n***********************')
productos = {'escoba': 5, 'huevo': 25, 'leche': 9}
menup = ['ver stock productos', 'añadir nuevo producto','ajustar stock','eliminar producto','salir']
while True:
    for ind in range(len(menup)):
        print(f'{ind+1}. {menup[ind]}')
    ans = input('Que quieres hacer:\n')
    if ans == '1':
        os.system('cls')
        for a,b in productos.items():
            print(f'{a}:{b}')
        print()    
    elif ans == '2':
        os.system('cls')
        while True:
            nom = input('Ingresa el nombre del producto nuevo:\n')
            if nom.replace(' ', '').isalpha():
                break
        if nom.lower() in productos:
            os.system('cls')
            print('Error:El producto ya existe\n')
            continue
        else:
            os.system('cls')
            productos[nom.lower()] = 0
            print('Producto agregado exitosamente')
    elif ans == '3':
        modificado = input('ingresa el nombre del producto a modificar\n')
        newstock = input('ingresa el nuevo stock')
        productos[newstock]
    elif ans == '4':
        os.system('cls')
        while True:
            nom = input('Indique el nombre del producto a eliminar\n')
            if nom.replace(' ', '').isalpha():
                break
        if nom.lower() in productos:
            os.system('cls')
            del productos[nom.lower()]
            continue
        else:
            os.system('cls')
            productos[nom.lower()] = 0
            print('erro:producto inexcistente')
    elif ans == '5':
        os.system('cls')
        exit('adios')
    else:
        os.system('cls')
        print('Error: opcion invalida:\n')
        