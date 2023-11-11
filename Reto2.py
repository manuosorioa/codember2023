#Reto n°2 de Codember

# Pedir al usuario que ingrese una cadena de código
codigo = "&###@&*&###@@##@##&######@@#####@#@#@#@##@@@@@@@@@@@@@@@*&&@@@@@@@@@####@@@@@@@@@#########&#&##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@&"

# Inicializar el valor numérico a 0
valor = 0

# Recorrer cada carácter de la cadena de código
for caracter in codigo:
  # Si el carácter es "#", incrementar el valor en 1
  if caracter == "#":
    valor += 1
  # Si el carácter es "@", decrementar el valor en 1
  elif caracter == "@":
    valor -= 1
  # Si el carácter es "*", multiplicar el valor por sí mismo
  elif caracter == "*":
    valor *= valor
  # Si el carácter es "&", imprimir el valor actual
  elif caracter == "&":
    print("El valor actual es:", valor)
  # Si el carácter es otro, ignorarlo
  else:
    pass
print("El valor actual es:", valor)

