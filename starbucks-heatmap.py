import pandas as pd
import folium
from folium.plugins import HeatMap

file_path = 'starbucks-data.csv'  
data = pd.read_csv("dila-mutlu-final-exam/starbucks-data.csv")

turkey_data = data[data['Country'] == 'TR']

province_group = turkey_data.groupby('State/Province')[['Latitude', 'Longitude']].mean().reset_index()

m = folium.Map(location=[39.92077, 32.85411], zoom_start=6)
HeatMap(data=province_group[['Latitude', 'Longitude']].values, radius=15, blur=20, gradient={0.2: 'blue', 0.5: 'lime', 0.8: 'orange', 1: 'red'}).add_to(m)

m.save('starbucks-heatmap.html')

import webbrowser
webbrowser.open("starbucks-heatmap.html")
