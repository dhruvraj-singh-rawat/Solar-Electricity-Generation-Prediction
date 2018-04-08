import json
#from pprint import pprint
import time
from datetime import datetime as dt

mn=2
dy=1
yr=2018
out = open('out1.csv', 'w')
for i in range(1,32):
	######################################################################################
	with open(str(i)+'.json') as data_file:    
	    data = json.load(data_file)

		######################################################################################

		#print data["chart"][1] Acedamic Eco 30.5kWp (# 1)
		#l_Acedamic_Eco_1= data["chart"]["series"][3]["data"]
		l_Acedamic_Eco_1= data["settings"]["series"][0]["data"]
		l_Acedamic_Eco_2= data["settings"]["series"][1]["data"]
		l_Acedamic_Eco_3= data["settings"]["series"][2]["data"]
		l_Acedamic_Symo= data["settings"]["series"][3]["data"]

		l_Library_Eco_1= data["settings"]["series"][5]["data"]
		l_Library_Eco_2= data["settings"]["series"][6]["data"]



		day=[]
		month=[]
		year=[]

		hour=[]
		minute=[]

		value_1=[]
		value_2=[]
		value_3=[]
		value_4=[]
		value_5=[]
		value_6=[]

		for row in l_Acedamic_Eco_2:
			# a=row[0]-(300000*66)	
			# date.append(time.strftime('%d %m %Y', time.localtime(a/1000)))
			# #time.append(time.strftime('%H:%M:%S', time.localtime(row[0]/1000)))
			# timer.append(time.strftime('%H:%M:%S', time.localtime(a/1000)))

			a=row[0]/1000	
			stamp=dt.fromtimestamp(a)

			day.append(stamp.day)
			month.append(stamp.month)
			year.append(stamp.year)
			hour.append(stamp.hour)
			minute.append(stamp.minute)





			value_3.append(row[1])

		for row in l_Acedamic_Eco_1:
			value_1.append(row[1])

		for row in l_Acedamic_Eco_3:
			value_5.append(row[1])

		for row in l_Acedamic_Symo:
			value_6.append(row[1])

		for row in l_Library_Eco_1:
			value_2.append(row[1])

		for row in l_Library_Eco_2:
			value_4.append(row[1])
		# print l[0][0]
		# time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(1464739200000/1000))


		######################################################################################
		
		######################################################################################

		print ('The length of value 1 is '+str(len(value_1)))
		print ('The length of value 2 is '+str(len(value_2)))
		print ('The length of value 3 is '+str(len(value_3)))
		print ('The length of value 4 is '+str(len(value_4)))
		print ('The length of value 5 is '+str(len(value_5)))
		print ('The length of value 6 is '+str(len(value_6)))


		out.write('Day,Month,Year,Hour,Minute,Acedamic_Eco_1,Library_Eco_1,Acedamic_Eco_2,Library_Eco_2,Acedamic_Eco_3,l_Acedamic_Symo,')
		out.write('\n')
		for step in range(140):

		    out.write('%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,' % (day[step],month[step],year[step],hour[step],minute[step],value_1[step],value_2[step],value_3[step],value_4[step],value_5[step],value_6[step]))
		    out.write('\n')
		out.close()


# out.write('Date,Time,Acedamic_Eco_1,')
# out.write('\n')
# for step in range(len(value_1)):

#     out.write('%r,%r,%r,' % (date[step],timer[step],value_1[step]))
#     out.write('\n')
# out.close()