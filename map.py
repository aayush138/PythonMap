import folium
import pandas

def script(r):
   if r<1000:
       return "green"
   elif 1000<=r<=3000:
       return "orange"
   else:
       return "red"

data=pandas.read_csv("Volcano.txt")
lat=list(data["Latitude"])
lon=list(data["Longitude"])
ele=list(data["Elevation"])
nme=list(data["Volcano Name"])

map=folium.Map(location=[0,0],zoom_start=2,method="OpenStreetMap")

fgv=folium.FeatureGroup("Volcanoes")
for i,j,k,l in zip(lat,lon,ele,nme):
    fgv.add_child(folium.Marker(location=[i,j],popup=str(l)+'\n'+str(k)+"m" , icon=folium.Icon(color=script(k))))

fgp=folium.FeatureGroup("population")
fgp.add_child(folium.GeoJson(data=open("world.json","r",encoding="utf-8-sig").read(),
style_function=lambda x:{"fillColor":"green" if x["properties"]["POP2005"]<10000000 else "yellow"
if 10000000<=x["properties"]["POP2005"]<20000000 else "red"}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("map.html")
