import random
import qrcode

def generar_primer_digito(fecha_nacimiento):
    anio = int(fecha_nacimiento[:4])

    if anio <= 1999:
        return str(random.randint(0, 9)) 
    else:
        return random.choice('A') 

def calcular_digito_verificador(curp_sin_verificador):

    caracteres_validos = '0123456789ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

    equivalencias = {char: index for index, char in enumerate(caracteres_validos)}

    coeficientes = [3, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]

    suma = sum(coef * equivalencias[char] for coef, char in zip(coeficientes, curp_sin_verificador))

    residuo = suma % 10

    if residuo == 0:
        return '0'
    else:
        return str(10 - residuo)

def generar_curp(nombre, apellido_paterno, apellido_materno, fecha_nacimiento, sexo, estado):
    curp = ''

    curp += apellido_paterno[0].upper()

    for letra in apellido_paterno[1:]:
        if letra.upper() in 'AEIOU':
            curp += letra.upper()
            break

    curp += apellido_materno[0]

    curp += nombre[0]

    curp += fecha_nacimiento[2:4]  

    mes = fecha_nacimiento[5:7]
    curp += mes

    curp += fecha_nacimiento[8:10] 

    curp += sexo

    curp += estado

    for letra in apellido_paterno[1:]:
        if letra.upper() not in 'AEIOU':
            curp += letra.upper()
            break

    for letra in apellido_materno[1:]:
        if letra.upper() not in 'AEIOU':
            curp += letra.upper()
            break

    for letra in nombre[1:]:
        if letra.upper() not in 'AEIOU':
            curp += letra.upper()
            break

    primer_digito = generar_primer_digito(fecha_nacimiento)

    curp += primer_digito

    segundo_digito_verificador = calcular_digito_verificador(curp)

    curp += segundo_digito_verificador

    return curp

nombre = input("Ingrese su nombre: ")
apellido_paterno = input("Ingrese su apellido paterno: ")
apellido_materno = input("Ingrese su apellido materno: ")
fecha_nacimiento = input("Ingrese su fecha de nacimiento (AAAA-MM-DD): ")
sexo = input("Ingrese su sexo (H o M): ")
estado = input("Ingrese la clave de su entidad federativa de nacimiento (dos letras en mayúsculas): ")

curp_generada = generar_curp(nombre, apellido_paterno, apellido_materno, fecha_nacimiento, sexo, estado)
print("La CURP generada es:", curp_generada)

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(curp_generada)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img_file = "curp_qr.png"
img.save(img_file)

print("Se ha generado el código QR de la CURP y se ha guardado como:", img_file)
