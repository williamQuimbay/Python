# strings

mensaje = "hola"  # asignacion de la variable
mensaje += " "  # se asigna un espacio a la variable de mensaje
mensaje += "william"  # se asigna un nuevo valor a la variable de mensaje
print(mensaje)

mensaje = "hola"
espacio = " "
nombre = "william"
print(mensaje + espacio + nombre)

print("\nconcatenacion")
num1 = 2
num2 = 3
resultado = num1 + num2
resultado = str(resultado)
print("El resulstado de la suma es: " + resultado)

# busqueda

mensaje1 = "hola como estas william"
buscar_subcadena = mensaje1.find("busqueda" + "william")
print(buscar_subcadena)

# estración

estraer_subcadena = mensaje1[16:23]
print(estraer_subcadena)

# comparacion
mensaje_uno = "william"
mensaje_dos = "william"
print(mensaje_uno == mensaje_dos)
