stock = 3

while True:
    print("\n--- Menú Biblioteca ---")
    print("1. Ver stock")
    print("2. Solicitar préstamo")
    print("3. Devolver libro")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        print(f"Libros disponibles: {stock}")

    elif opcion == "2":
        if stock > 0:
            stock -= 1
            print("Préstamo realizado. Stock actualizado:", stock)
        else:
            print("No hay libros disponibles para préstamo.")

    elif opcion == "3":
        stock += 1
        print("Libro devuelto. Stock actualizado:", stock)

    elif opcion == "4":
        print("Gracias por usar el sistema.")
        break

    else:
        print("Opción inválida, intenta nuevamente.")
