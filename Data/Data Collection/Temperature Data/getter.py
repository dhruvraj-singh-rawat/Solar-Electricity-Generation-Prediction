import urllib2
import json

out = open('october.csv', 'w')
out.write('day, month ,year ,hour ,minute ,temperature ,humidity ,wind_speed ,visibility,')
out.write('\n')

for i in range(1,32):

	year=format(2017,"02")
	month=format(10,"02")
	day=format(i,"02")




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
	# print " %s  %s %s ``" % (info_imp[abc] )
	# print " %s  " % (info_imp[abc] )



	for step in range(abc):

		hrs= info_imp[step]['date']['hour']
		mnts= info_imp[step]['date']['min']

		temperature= info_imp[step]['hum']
		humidity=info_imp[step]['hum']

		wind_speed=info_imp[step]['wspdm']

		visibility=info_imp[step]['visi']

		out.write(str(dy)+','+str(mnt)+','+str(yr)+','+str(hrs)+','+str(mnts)+','+str(temperature)+','+str(humidity)+','+str(wind_speed)+','+str(visibility)+',')

		

		#out.write('%r,%r,%r,%r,%r,%r,%r,%r,%r,\n' % (dy,mnt,yr,hrs,mnts,temperature,humidity,wind_speed,visibility)
		out.write('\n')

out.close()

f.close()