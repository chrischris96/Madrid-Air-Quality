#importing all libraries
import geopandas as gpd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pyqtgraph as pg

from shapely.geometry import Point, LineString

#add data from a .csv file
#stations contains the location of the stations where the air pollution is recorded
path = r'C:\Users\Chris\Desktop\Machine Learning Raw Data\air-quality-madrid\stations.csv'
stations = pd.read_csv(path)

#transforming longitude and latitude to an other projection
geometry = [Point(xy) for xy in zip(stations['lon'], stations['lat'])]
crs = {'init': 'epsg:4326'}
geoDF_stations = gpd.GeoDataFrame(stations, crs=crs, geometry=geometry)
geoDF_stations_new = geoDF_stations.to_crs({'init': 'epsg:25830'}) 

#reading and extracting data from the complete street map of Madrid
#selecting only the most used street names in order to a cleaner map
streetsystem = gpd.read_file('C:/Users/Chris/Desktop/Machine Learning Raw Data/900BTQKCJT/call2016.shp')
calleselected = streetsystem.loc[streetsystem['VIA_TVIA'] == "Calle"]
avdselected = streetsystem.loc[streetsystem['VIA_TVIA'] == "Avda"]
ctraselected = streetsystem.loc[streetsystem['VIA_TVIA'] == "Ctra"]
calleandavd = calleselected.append(avdselected)
streetselected = calleandavd.append(ctraselected)

#merge the two layers and plot them in one plot
base = geoDF_stations_new.plot(figsize=(32,20), marker='o',color='red',markersize=100.0,label='Stations');
mapMadrid = streetselected.plot(figsize=(32,20), ax=base,color='blue', edgecolor='blue',markersize=0.01,label='Streets');

plt.ylim((4465000,4485000))
plt.xlim((430000,455000))
plt.legend(loc = 'lower right', framealpha=1)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Madrid city center street map with measurement stations")
plt.show(mapMadrid)

path_pollution = r'C:\Users\Chris\Desktop\Machine Learning Raw Data\air-quality-madrid\csvs_per_year\csvs_per_year\madrid_2001.csv'
data2001 = pd.read_csv(path_pollution)

station_28079001 = data2001.loc[data2001['station'] == 28079001]
dates_28079001 = station_28079001['date']
CO_28079001 = station_28079001['CO']

#d01array = dates_28079001(~isfinite(dates_28079001))=0
#CO_01array = CO_28079001(~isfinite(CO_28079001))=0

#dates_28079001_array = np.asarray(d01array)
#CO_28079001_array    = np.asarray(CO_01array) 

#pg.plot(d01array,CO_01arrays)
#plt.plot(dates_28079001, CO_28079001)
#plt.show()


station_28079003 = data2001.loc[data2001['station'] == 28079003]
plt.figure(figsize=(32,20))
#plt.plot(station_28079003['CO'])
#plt.plot(station_28079004['CO'])
#plt.plot(station_28079006['CO'])
#plt.plot(station_28079007['CO'])
#plt.plot(station_28079008['CO'])
#plt.plot(station_28079009['CO'])
#plt.plot(station_28079011['CO'])
#plt.plot(station_28079012['CO'])
#plt.plot(station_28079014['CO'])
#plt.plot(station_28079015['CO'])
#plt.plot(station_28079016['CO'])
#plt.plot(station_28079017['CO'])
plt.plot(station_28079018['CO'])
#plt.plot(station_28079019['CO'])
#plt.plot(station_28079021['CO'])
#plt.plot(station_28079022['CO'])
#plt.plot(station_28079023['CO'])
#plt.plot(station_28079024['CO'])
#plt.plot(station_28079025['CO'])
plt.legend()


station_28079004 = data2001.loc[data2001['station'] == 28079004]
station_28079006 = data2001.loc[data2001['station'] == 28079006]
station_28079007 = data2001.loc[data2001['station'] == 28079007]
station_28079008 = data2001.loc[data2001['station'] == 28079008]
station_28079009 = data2001.loc[data2001['station'] == 28079009]
station_28079011 = data2001.loc[data2001['station'] == 28079011]
station_28079012 = data2001.loc[data2001['station'] == 28079012]
station_28079014 = data2001.loc[data2001['station'] == 28079014]
station_28079015 = data2001.loc[data2001['station'] == 28079015]
station_28079016 = data2001.loc[data2001['station'] == 28079016]
station_28079017 = data2001.loc[data2001['station'] == 28079017]
station_28079018 = data2001.loc[data2001['station'] == 28079018]
station_28079019 = data2001.loc[data2001['station'] == 28079019]
station_28079021 = data2001.loc[data2001['station'] == 28079021]
station_28079022 = data2001.loc[data2001['station'] == 28079022]
station_28079023 = data2001.loc[data2001['station'] == 28079023]
station_28079024 = data2001.loc[data2001['station'] == 28079024]
station_28079025 = data2001.loc[data2001['station'] == 28079025]
station_28079035 = data2001.loc[data2001['station'] == 28079035]
station_28079036 = data2001.loc[data2001['station'] == 28079036]
station_28079038 = data2001.loc[data2001['station'] == 28079038]
station_28079039 = data2001.loc[data2001['station'] == 28079039]
station_28079040 = data2001.loc[data2001['station'] == 28079040]
station_28079099 = data2001.loc[data2001['station'] == 28079099]












