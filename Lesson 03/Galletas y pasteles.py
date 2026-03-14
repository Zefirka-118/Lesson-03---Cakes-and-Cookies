# Sistema para calcular materiales de galletas y pasteles

print("1. Galletas")
print("2. Pasteles")

opcion = int(input("Elige una opción: "))
cantidad = int(input("¿Cuántos vas a hacer? "))

if opcion == 1:
    harina = cantidad * 100
    mantequilla = cantidad * 50
    huevos = cantidad * 1
    print("Para", cantidad, "galletas necesitas:")
    print(harina, "g de harina")
    print(mantequilla, "g de mantequilla")
    print(huevos, "huevo(s)")

elif opcion == 2:
    harina = cantidad * 500
    mantequilla = cantidad * 250
    huevos = cantidad * 5
    azucar = cantidad * 200
    print("Para", cantidad, "pasteles necesitas:")
    print(harina, "g de harina")
    print(mantequilla, "g de mantequilla")
    print(huevos, "huevo(s)")
    print(azucar, "g de azúcar")

else:
    print("Opción incorrecta. Elige 1 o 2.")