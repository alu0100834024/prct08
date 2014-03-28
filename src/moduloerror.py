#!/usr/bin/python
#! encoding: UTF-8
#funcion para determinar el numero de errores
import modulo
import sys
def error(subintervalos,nro_test,umbral):
  p=0
  for i in range(1,nro_test +1):
    t=modulo.numeropi(subintervalos)
    if (abs(t-modulo.Pi) > umbral):
      p+=1
  j=(p*100)/nro_test
  return j
  
  
#invocacion
if __name__ == "__main__": 
  if len(sys.argv)==4:
    subintervalos=int(sys.argv[1])
    nro_test=int(sys.argv[2])
    umbral=float(sys.argv[3])
  else:
    subintervalos=10
    nro_test=5
    umbral=0.0001
  if(subintervalos<=0):
    print 'Error, el subintervalo debe ser mayor que cero'
  j = error(subintervalos,nro_test,umbral)  
  print "El porcentaje de errores es %.5f" % j