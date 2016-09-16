import sys
import json
import urllib2 
import csv

mtaKey = "6a40826c-4f43-4d81-834d-c20d8dc72a1d"
# mtaKey = sys.argv[1]
busLine = "B52"
# busLine = sys.argv[2]

# format response url with api key and bus line variables from command line input
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s"%(mtaKey, busLine)

# load api response data into python dict
response = open('test_data.json')
# response = urllib2.urlopen(url)
data = response.read().decode("utf-8")
busDict = json.loads(data)

# set variable to access individual bus data in nested dict structure
activeBusData = busDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

# empy array for data from all buses
allBuses = []

# get lat/lon for each active bus, and next stop info
for i in activeBusData:
	lat = i['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
	lon = i['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
	stopName = i['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
	stopStatus = i['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
	singleBus = [lat, lon, stopName, stopStatus]
	allBuses.append(singleBus)

print allBuses

# # format output
# print "Bus Line : " + busName
# print "Number of Active Buses : " + str(busCount)
# print locations