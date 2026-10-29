print ("verificador de contraseñas")
contraseñas_inseguras = ["123456", "password", "123456789", "12345678", "12345", "111111", "1234567", "sunshine", "qwerty", "iloveyou"]
contraseña = input("ingrese su contraseña: ")
intentos = 0

while contraseña in contraseñas_inseguras:
    intentos = intentos + 1

    if intentos == 3:
        print ("limite de intentos alcanzado")
        break
    print("contraseña debil")
    contraseña = input("ingrese su contraseña: ")

if contraseña not in contraseñas_inseguras:
    print ("contraseña segura")