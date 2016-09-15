import sys
import json
import urllib2 

# mtaKey = "6a40826c-4f43-4d81-834d-c20d8dc72a1d"
mtaKey = sys.argv[1]
# busLine = "B52"
busLine = sys.argv[2]

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s"%(mtaKey, busLine)

response = urllib2.urlopen(url)
data = response.read().decode("utf-8")
busDict = json.loads(data)
# print busDict.keys()

# with open('test_data.json') as data:
# 	 busDict = json.load(data)
activeBusData = busDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
busName = activeBusData[0]['MonitoredVehicleJourney']['PublishedLineName']
busCount = 0
locations = ""
for i in activeBusData:
	lat = i['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
	lon = i['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
	locations = locations + "Bus " + str(busCount) + " is at latitude " + str(lat) + " and longitude " + str(lon) + "\n"
	busCount+=1
print "Bus Line : " + busName
print "Number of Active Buses : " + str(busCount)
print locations