import requests
import math

def calc_dist(lat1, lon1, lat2, lon2):
        lat1 = math.radians(lat1)
        lon1 = math.radians(lon1)
        lat2 = math.radians(lat2)
        lon2 = math.radians(lon2)
        h = math.sin( (lat2 - lat1) / 2 ) ** 2 + \
            math.cos(lat1) * \
            math.cos(lat2) * \
            math.sin( (lon2 - lon1) / 2 ) ** 2

        return 6372.8 * 2 * math.asin(math.sqrt(h))

def get_dist(meteor):
        return meteor.get('distance',float('inf'))

met_landings = requests.get('https://data.nasa.gov/resource/y77d-th95.json')
error_list=[]
if (met_landings.status_code==200):
    print ('obtained_data_successfully')
    met_lands_list = met_landings.json()
    for met in met_lands_list:
        if not ('reclat' in met or 'reclong' in met):
            print('**No Lat and Long **'+str(met))
            error_list.append(met)
            continue
        met['distance']= calc_dist(38.969555,-77.386098,float(met['reclat']), float(met['reclong']))
    met_lands_list.sort(key=get_dist)
    print(met_lands_list[0:5])
    print ('****************')
    print ('The locations that have no latitude and longitude are')
    print('length is '+str(len(error_list)))
    for met in error_list:
        print(met)
