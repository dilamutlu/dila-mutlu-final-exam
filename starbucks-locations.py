import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import leafmap.foliumap as leaf

df = pd.read_csv("dila-mutlu-final-exam/starbucks-data.csv")
print(df.head())

turkiyeStarbucks = df[df['Country'] == "TR"]

# Filtrelenmiş verileri ekrana yazdır
print(turkiyeStarbucks.head())

starbucks_count = len(turkiyeStarbucks)
print(starbucks_count)

i=turkiyeStarbucks[turkiyeStarbucks['Longitude'].isna()].index
turkiyeStarbucks=turkiyeStarbucks.drop(i)

geometry = gpd.points_from_xy(turkiyeStarbucks.Longitude,turkiyeStarbucks.Latitude)
turkiyeStarbucks=gpd.GeoDataFrame(turkiyeStarbucks,crs = 'EPSG:4326',geometry = geometry)
print(turkiyeStarbucks)

m = leaf.Map(width=900,height = 500)
turkiyeStarbucks.explore(m=m)

m.to_html("starbucks-locations-map.html")

import webbrowser
webbrowser.open("starbucks-locations-map.html")