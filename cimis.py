#import requests

import json
import urllib.request
import settings

#a3485319-254d-49b2-8dd5-793d779282df
def function1():

    headers = {'Content-type': 'application/json'}
        #in the url below change the date to the current date
    url = "http://et.water.ca.gov/api/data?appKey=a3485319-254d-49b2-8dd5-793d779282df&targets=75&startDate=2019-06-04&endDate=2019-06-04&dataItems=hly-eto,hly-rel-hum,hly-air-tmp"
    req = urllib.request.Request(url,headers=headers)
    response = urllib.request.urlopen(req)

    r = urllib.request.urlopen(req).read()

        #
    data = json.loads(r.decode('utf-8'))

        #print((data['Data']['Providers'][0]['Records'][2]['HlyAirTmp']))
        #print(len(data['Data']['Providers'][0]['Records']))

    count = 0
    for x in data['Data']['Providers'][0]['Records']:
        settings.hlytemp.insert(count,x['HlyAirTmp']['Value'])
        settings.hlyhum.insert(count,x['HlyRelHum']['Value'])
        settings.eto.insert(count,x['HlyEto']['Value'])
        count = count + 1

    for x in range(len(settings.hlytemp)):
        print (settings.hlytemp[x])

#calculating irrigation
#ETO = CIMIS ET0/((local humidity/CIMIS humidity))
#gallons of water per day = (ET0 x PF(1.0) x SF (200) x (0.62))/IE(0.75)

#print(type(data['Data']['Providers'][0]['Records'][0]['HlyAirTmp']['Value']))
#print(json.dumps(data,indent=2))
#print((data['Data']['Providers'][0]['Records'][0]['HlyAirTmp'].keys()))




        






