import json
import time
from datetime import datetime as dt

mn=10
dy=1
yr=2017
out = open('out1.csv', 'w')
out.write('Day,Month,Year,Hour,Minute,Acedamic_Eco_1,Library_Eco_1,Acedamic_Eco_2,Library_Eco_2,Acedamic_Eco_3,l_Acedamic_Symo,')
out.write('\n')

for i in range(1,32):
	with open(str(i)+'.json') as data_file:    
		data = json.load(data_file)

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
		
			a=row[0]/1000	
			stamp=dt.fromtimestamp(a)

			day.append(stamp.day)
			month.append(stamp.month)
			year.append(stamp.year)
			hour.append(stamp.hour)
			minute.append(stamp.minute)

			abc=(dt(yr,mn,i,6)-dt(1970,1,1)).total_seconds()
			start_time=int(abc-19800)

			abc=(dt(yr,mn,i,18)-dt(1970,1,1)).total_seconds()
			end_time=int(abc-19800)

			# print ('The start time is '+str(start_time))
			# print ('The end time is '+str(end_time))

			print ('The day is: '+str(i))

			if int(row[0]) in range(start_time*1000,end_time*1000):

				value_3.append(row[1])

		for row in l_Acedamic_Eco_1:

			abc=(dt(yr,mn,i,6)-dt(1970,1,1)).total_seconds()
			start_time=int(abc-19800)

			abc=(dt(yr,mn,i,18)-dt(1970,1,1)).total_seconds()
			end_time=int(abc-19800)

			if row[0] in range(start_time*1000,end_time*1000):							
				value_1.append(row[1])

		for row in l_Acedamic_Eco_3:
			abc=(dt(yr,mn,i,6)-dt(1970,1,1)).total_seconds()
			start_time=int(abc-19800)

			abc=(dt(yr,mn,i,18)-dt(1970,1,1)).total_seconds()
			end_time=int(abc-19800)

			if row[0] in range(start_time*1000,end_time*1000):

							
				value_5.append(row[1])

		for row in l_Acedamic_Symo:
			abc=(dt(yr,mn,i,6)-dt(1970,1,1)).total_seconds()
			start_time=int(abc-19800)

			abc=(dt(yr,mn,i,18)-dt(1970,1,1)).total_seconds()
			end_time=int(abc-19800)

			if row[0] in range(start_time*1000,end_time*1000):


				value_6.append(row[1])

		for row in l_Library_Eco_1:
			abc=(dt(yr,mn,i,6)-dt(1970,1,1)).total_seconds()
			start_time=int(abc-19800)

			abc=(dt(yr,mn,i,18)-dt(1970,1,1)).total_seconds()
			end_time=int(abc-19800)

			if row[0] in range(start_time*1000,end_time*1000):


				value_2.append(row[1])

		for row in l_Library_Eco_2:
			abc=(dt(yr,mn,i,6)-dt(1970,1,1)).total_seconds()
			start_time=int(abc-19800)

			abc=(dt(yr,mn,i,18)-dt(1970,1,1)).total_seconds()
			end_time=int(abc-19800)

			if row[0] in range(start_time*1000,end_time*1000):

				
				value_4.append(row[1])


		print ('The length of value 1 is '+str(len(value_1)))
		print ('The length of value 2 is '+str(len(value_2)))
		print ('The length of value 3 is '+str(len(value_3)))
		print ('The length of value 4 is '+str(len(value_4)))
		print ('The length of value 5 is '+str(len(value_5)))
		print ('The length of value 6 is '+str(len(value_6)))

		

		for step in range(min(len(value_1),len(value_2),len(value_3),len(value_4),len(value_5),len(value_6))):

			out.write('%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,' % (day[step],month[step],year[step],hour[step],minute[step],value_1[step],value_2[step],value_3[step],value_4[step],value_5[step],value_6[step]))
			out.write('\n')

out.close()
