
#login basico para principiantes 


#definir el usuario y la contrasena
usuario_correcto = "1"
contrasena_correcta = "2"

usuario = input("ingresar usuario: ")
contrasena = input("ingresar contrasena: ")

# 2 == significan comparar 
if usuario == usuario_correcto and contrasena == contrasena_correcta:
    print("Datos correctos, Bienvenido")
else:
     print("datos incorrectos ")