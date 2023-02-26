usuario_autentificado = False
usuario_admin = False

if usuario_autentificado:
    if usuario_admin:
        print("acceso total ")
    else:
        print("acceso al sistema")
else:
    print("debes iniciar secion ")

#ejemplo elif

ocupacion ='desempleado'

if ocupacion == 'estudiante':
    print('tienes 50% de descuento')
elif ocupacion == 'jubilado ':
    print('tienes 75% de descuento ')
elif ocupacion == 'desempleado':
    print('tienes un 10% de descuento ')
else:
    print('debes pagar el 100%')

# 08. opereadores logicos
usuario_logeado = True
usuario_admin = True

if usuario_logeado or usuario_admin:
    print('administrardor ')
elif usuario_logeado:
    print('acceso al sistema ')
else:
    print('debes iniciar secion ')

# 09. condicionales for

lenguajes = ['Python', 'Kotlin', 'Java', 'Javascript']
for lenguaje in lenguajes:
    print(lenguaje.upper())
else:
    print(lenguaje)