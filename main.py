import time

# Inicializo las variables hora y minutos y las convierto a strings
hora = time.strftime('%H')
minutos = time.strftime('%M')

# Se comprueba si es hora de ir a casa  o no
if int(hora) >= 19:
	print ("Es hora de ir a casa")
else:
	print ("Faltan {} horas y {} minutos para irse a casa".format(18- int(hora), 59-int(minutos)))