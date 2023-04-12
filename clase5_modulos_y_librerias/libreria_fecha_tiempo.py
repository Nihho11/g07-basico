"""Uso de libreria de fecha y tiempo"""

from datetime import datetime, date

"""Obtener la fecha actual"""

fecha = date.today()

print("La fecha a manejar es la siguiente: {}".format(fecha))

tiempo = datetime.now()

print(tiempo)

anio = tiempo.year
mes = tiempo.month
dia = tiempo.day

print("La fecha de hoy es {} del mes {} del año {}.".format(dia, mes, anio))

"""Uso del datetime para extraer la hora, el minuto y el segundo actual"""

hora = tiempo.hour
minuto = tiempo.minute
segundo = tiempo.second

print("La hora es {}, con {} minutos y {} segundos.".format(hora, minuto, segundo))