#
# 13 May 2014. Use the new osmapi python package to upload the eighty traffic camera locations into OSM.
import osmapi
import geojson
import time

# read a geojson file into loclist.
f = open("Baltimore_Fixed_Speed_Cameras.geojson")
mm = geojson.load(f)
# now each speed camera is an instance of a class
# easiest to use the browser's dev tools to see the class's structure.

# these tags will be part of every new node I create:
default_dict = {
    'highway' : 'speed_camera',
    'source' : 'Open data of the city of Baltimore from data.baltimorecity.gov as of March 2014.',
    'note' : ''
}

def directionmap(s):
    if s == 'E/B': 
        return 'eastbound'
    elif s == 'W/B': 
        return 'westbound'
    elif s=='N/B': 
        return 'northbound'
    elif s=='S/B': 
        return 'southbound'
    else:
        return 'unknown'

#api = osmapi.OsmApi(api="api06.dev.openstreetmap.org", username = u"borbash", password = u”***”) # didnt work
#api = osmapi.OsmApi(api="api06.dev.openstreetmap.org", username = u"borbash@ieee.org", password = u”***”) # didnt work
api = osmapi.OsmApi(username = u"borbash", password = u"***") # need to replace with actual password
print api
#time.sleep(10)
api.ChangesetCreate({u"comment": u"Uploading eighty traffic camera locations in the city of Baltimore"})
for feat in mm.features:
    ds = directionmap(feat.properties['direction'])
    ads = feat.properties['address']
    s = "Speed camera measuring traffic in " + ds + " direction at intersection of " + ads
    default_dict.update({'note' : s})
#    print "LAT,LNG: "+ str(feat.geometry.coordinates[1]) +"  "+ str(feat.geometry.coordinates[0])
#    print "NOTE:"+ default_dict['note']
    print api.NodeCreate({u"lon":feat.geometry.coordinates[0], 
                          u"lat":feat.geometry.coordinates[1], 
                          u"tag": default_dict})
# expect to see something like {u'changeset': 532907, u'lon': 1, u'version': 1, u'lat': 1, u'tag': {}, u'id': 164684}
api.ChangesetClose()
