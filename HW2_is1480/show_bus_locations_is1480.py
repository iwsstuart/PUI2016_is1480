import sys
import json

# key = 6a40826c-4f43-4d81-834d-c20d8dc72a1d
# key = sys.argv[1]

# data = http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=B52%(key)

with open('test_data.json') as data:
	 busDict = json.load(data)
	 busCount = 0
	 for i in busDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']:
	 	busCount+=1

	 print busCount