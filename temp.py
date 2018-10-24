
import geopandas as gpd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.colors import Normalize
from shapely.geometry import Point, LineString

path = r'C:\Users\Chris\Desktop\Machine Learning Raw Data\air-quality-madrid\stations.csv'
stations = pd.read_csv(path)
stations.head()

geometry = [Point(xy) for xy in zip(stations['lon'], stations['lat'])]
crs = {'init': 'epsg:4326'}
geoDF_stations = gpd.GeoDataFrame(stations, crs=crs, geometry=geometry)
geoDF_stations_new = geoDF_stations.to_crs({'init': 'epsg:25830'}) 

streetsystem = gpd.read_file('C:/Users/Chris/Desktop/Machine Learning Raw Data/900BTQKCJT/call2016.shp')
calleselected = streetsystem.loc[streetsystem['VIA_TVIA'] == "Calle"]
avdselected = streetsystem.loc[streetsystem['VIA_TVIA'] == "Avda"]
ctraselected = streetsystem.loc[streetsystem['VIA_TVIA'] == "Ctra"]
calleandavd = calleselected.append(avdselected)
streetselected = calleandavd.append(ctraselected)

#xlim=(420000,460000)
#ylim=(4460000,4490000)

base = geoDF_stations_new.plot(figsize=(32,20), marker='o',color='red',markersize=100.0,label='Stations')

mapMadrid = streetselected.plot(figsize=(32,20), ax=base,color='blue', edgecolor='blue',markersize=0.01,label='Streets') 

plt.ylim((4465000,4485000))
plt.xlim((430000,455000))
plt.legend(loc = 'lower right', framealpha=1)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Madrid city center street map with measurement stations")
plt.plot(mapMadrid)