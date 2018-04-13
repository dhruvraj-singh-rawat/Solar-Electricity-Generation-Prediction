import urllib2
import json

year=format(2018,"02")
month=format(1,"02")
day=format(1,"02")

out = open('out1.csv', 'w')
out.write('dy','mnt','yr','minute','hour','temperature','humidity','wind_speed','visibility')
out.write('\n')

url='http://api.wunderground.com/api/d75d43d07ecfed90/history_'+year+month+day+'/q/zmw:00000.257.42348.json'

f = urllib2.urlopen(url)
json_string = f.read()
parsed_json = json.loads(json_string)

info_date = parsed_json['history']['date']

yr= info_date['year']
mnt= info_date['mon']
dy= info_date['mday']

info_imp = parsed_json['history']['observations']

abc=len(info_imp)-1
#temp_f = parsed_json['current_observation']['temp_f']
print " %s  %s %s ``" % (info_imp[abc] )
print " %s  " % (info_imp[abc] )



out.write('\n')

for i in range(1,32):
	with open(str(i)+'.json') as data_file:    
		data = json.load(data_file)

		

		for step in range(min(len(value_1),len(value_2),len(value_3),len(value_4),len(value_5),len(value_6))):

			out.write('%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,' % (day[step],month[step],year[step],hour[step],minute[step],value_1[step],value_2[step],value_3[step],value_4[step],value_5[step],value_6[step]))
			out.write('\n')

out.close()

f.close()