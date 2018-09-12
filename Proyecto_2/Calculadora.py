#calculadora
#hecho por: julio leiva
#!/usr/bin/python

numeros = list()

def v_c_v():
    res = input().lower().strip()
    while res == "":
        print("debe ingresar algo")
        print("------------------")
        res = input().lower().strip()

    return res

def v_c_v_n():
    while True:
        try:
            nume = float(input("").strip())
            return nume
        except ValueError:
            print("solo numeros porfavor")

def ingreso():
    nums = dict()
    print("ingrese numeros decimales")
    print("-------------------------------")

    print("ingrese el primer numero")
    n1 = v_c_v_n()
    nums["num1"] = n1

    print("ingrese el segundo numero")
    n2 = v_c_v_n()
    nums["num2"] = n2
    numeros.append(nums)

def sumar():
    ingreso()
    for l in numeros:
        suma = float(l["num1"] + l["num2"])
    print("El resultado es:", suma)
    print("-------------------------------")

def restar():
    ingreso()
    for j in numeros:
        resta = float(j["num1"] - j["num2"])
    print("El resultado es:", resta)
    print("-------------------------------")

def multiplicar():
    ingreso()
    for h in numeros:
        multi = float(h["num1"] * h["num2"])
    print("El resultado es:", multi)
    print("-------------------------------")

def dividir():
    ingreso()
    for g in numeros:
        div = float(g["num1"] / g["num2"])
    print("El resultado es:", div)
    print("-------------------------------")

def elevar():
    print("primero debe ingresar la base y despues el exponente")
    ingreso()
    for d in numeros:
        potencia = float(d["num1"] ** d["num2"])
    print("El resultado es:", potencia)
    print("-------------------------------")

def menu():
    print("caculadora basica")
    print("por favor elija su opcion")

    while True:
        print("a) sumar")
        print("b) restar")
        print("c) multiplicar")
        print("d) dividir")
        print("e) elevar")
        print("para salir presione x")

        opcion = v_c_v()

        if opcion == "a":
            sumar()
        elif opcion == "b":
            restar()
        elif opcion == "c":
            multiplicar()
        elif opcion == "d":
            dividir()
        elif opcion == "e":
            elevar()
        elif opcion == "x":
            break

menu()
