# Los dias Sabado y Domingo:
# - Es fin de semana, no trabajar
# Los dias pares regresar: martes y jueves
# - Hacer tareas
# Los dias impares regresar: los demas
# - Date tiempo para ir al parque a pasear
dia='martes'

if dia=='sabado' or dia=='domingo':
  print('es fin de semana, no trabajar')
elif dia=='martes' or dia =='jueves':
  print('Hacer tareas')
else:
  print('Date tiempo para ir al parque a pasear')