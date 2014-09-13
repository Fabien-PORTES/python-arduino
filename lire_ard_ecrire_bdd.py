import serial
import string
import time
from datetime import datetime
import MySQLdb
import fonction



arduinoPort = '/dev/ttyACM0' #check in the /dev folder the Arduino Serial Port
ser = serial.Serial()
ser.setPort(arduinoPort) #boundRate 9600 automatically set
ser.setTimeout(1)




db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="root", # your username
                     passwd="u69yah5l", # your password
                     db="Arduino") # name of the data base
cur = db.cursor() 




try:
	ser.open()
	time.sleep(2)
	ser.readlines() #pour enlever la première ligne avec le setup
except: 
	print('Erreur sur le port !')
else:
	
	while 1:
	
		while ser.inWaiting() :		#tant que le buffer n'est pas vide, on le lit ligne a ligne
			ardString=ser.readline()  
			ligne= ardString.split('=') 
			(date_temps,variable,valeur)=(str(datetime.now().replace(microsecond=0)),ligne[0],ligne[1].replace("\r\n",""))
			(table,nom)=fonction.corresp_var_bdd(variable)
			print(date_temps+"  "+variable+"  "+table+ "  "+ nom + "  "+valeur)
			sql = "insert into %s (ID, date_temps, nom, valeur) values (%s)" % (table, "%s, %s, %s, %s")  
			cur.execute(sql,(0, date_temps, nom, valeur))
			db.commit()
		time.sleep(1)
			
			
			
			
			
			