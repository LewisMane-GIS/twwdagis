import streamlit as st
import geopandas as gpd
import folium
from folium import plugins
from streamlit_folium import folium_static

st.set_page_config(page_title='Tana Web GIS')

st.write("""
# TANA WATER WORKS DEVELOPMENT AGENCY WEB GIS

This web app consists of a web map displaying projects under TWWDA coverage area
""")

# creation of map object
m_2 = folium.Map(location=[-1.25, 36.8888], min_zoom=4, max_zoom=15, zoom_start=6, control_scale=True)

#loading the layers
# loading polygon layers
forest = gpd.read_file("./data/Forest Cover.geojson")
mawasco = gpd.read_file("./data/Mawasco.geojson")
mathira = gpd.read_file("./data/Mathira.geojson")
mewass = gpd.read_file("./data/Mewass.geojson")
Imetha = gpd.read_file("./data/Imetha.geojson")
Kiriwasco = gpd.read_file("./data/Kiriwasco.geojson")
Kyeni = gpd.read_file("./data/Kyeniwasco.geojson")
MDE = gpd.read_file("./data/Multipurpose dams in Embu.geojson")
MM = gpd.read_file("./data/Murugi-Mugumango.geojson")
Muthambi = gpd.read_file("./data/Muthambi_4K.geojson")
Naruwasco = gpd.read_file("./data/Naruwasco.geojson")
Ndamunge = gpd.read_file("./data/Ndamunge.geojson")
NN = gpd.read_file("./data/Nginda Ngandori.geojson")
Nithi = gpd.read_file("./data/Nithiwasco.geojson")
Nyewasco = gpd.read_file("./data/Nyewasco.geojson")
Omwasco = gpd.read_file("./data/Omwasco.geojson")
RW = gpd.read_file("./data/Rukanga WSP.geojson")
TW = gpd.read_file("./data/Teawasco.geojson")
Kenya = gpd.read_file("./data/Counties.geojson")

# loading all point layers first

BH_EQ = gpd.read_file("./data/borehole equiping.geojson")
CC_P  = gpd.read_file("./data/cross-county.geojson")
EEP_P = gpd.read_file("./data/Existing Embu Projects.geojson")
PnD = gpd.read_file("./data/Planning and design Stage.geojson")
PPE = gpd.read_file("./data/Proposed project in Embu.geojson")
UHC = gpd.read_file("./data/universal Health Care projects.geojson")
ADB = gpd.read_file("./data/ADB_PROJECT.geojson")


# trial 1 clusterin adb
cluster_adb = plugins.MarkerCluster(name='Africa Development Bank Projects').add_to(m_2)
for _, r in ADB.iterrows():
    lat = r['geometry'].y
    lon = r['geometry'].x
    folium.Marker(location=[lat, lon],
                  tooltip='Click for ADB',
                  popup='Id: {} <br> Name: {}'.format(r['Id'], r['Name']),
                  icon=folium.Icon(color='green', icon='ok-sign', prefix='glyphicon')).add_to(cluster_adb)

# clustering uhc
cluster_uhc = plugins.MarkerCluster(name='Universal Health Care Projects').add_to(m_2)
for _, r in UHC.iterrows():
    lat = r['geometry'].y
    lon = r['geometry'].x
    folium.Marker(location=[lat, lon],
                  tooltip='Click for UHC',
                  popup='Id: {} <br> Name: {}'.format(r['Id'], r['Name']),
                  icon=folium.Icon(color='darkpurple', icon='glyphicon-tint', prefix='glyphicon')).add_to(cluster_uhc)

# clustering cc
cluster_cc = plugins.MarkerCluster(name='Cross County Projects').add_to(m_2)
for _, r in CC_P.iterrows():
    lat = r['geometry'].y
    lon = r['geometry'].x
    folium.Marker(location=[lat, lon],
                  tooltip='Click for CC',
                  popup='Id: {} <br> Name: {}'.format(r['Id'], r['Names']),
                  icon=folium.Icon(color='orange', icon='glyphicon-info-sign', prefix='glyphicon')).add_to(cluster_cc)

# clustering bh_eq
cluster_teb = plugins.MarkerCluster(name='Borehole Equiping').add_to(m_2)
for _, r in BH_EQ.iterrows():
    lat = r['geometry'].y
    lon = r['geometry'].x
    folium.Marker(location=[lat, lon],
                  tooltip='Click for BH_Eq',
                  popup='Id: {} <br> Name: {}'.format(r['Id'],r['Name']),
                  icon=folium.Icon(color='red', icon='glyphicon-info-sign', prefix='glyphicon')).add_to(cluster_teb)

# clustering eep
cluster_eep = plugins.MarkerCluster(name='Existing Embu Project').add_to(m_2)
for _, r in EEP_P.iterrows():
    lat = r['geometry'].y
    lon = r['geometry'].x
    folium.Marker(location=[lat, lon],
                  tooltip='Click for EEP',
                  popup='Name: {} <br> Type: {} <br> NameType: {}'.format(r['name'], r['type'], r['nametype']),
                  icon=folium.Icon(color='darkgreen', icon='glyphicon-info-sign', prefix='glyphicon')).add_to(cluster_eep)

# clustering pnd
cluster_pnd = plugins.MarkerCluster(name='Planning & Design stage').add_to(m_2)
for _, r in PnD.iterrows():
    lat = r['geometry'].y
    lon = r['geometry'].x
    folium.Marker(location=[lat, lon],
                 tooltip='click for p&d',
                 popup='Id: {} <br> <strong>Name:</strong> {}'.format(r['Id'], r['Name']),
                 icon=folium.Icon(color='lightgray', icon='glyphicon-tint', prefix='glyphicon')).add_to(cluster_pnd)

# clustering ppe
cluster_ppe = plugins.MarkerCluster(name='Proposed Projects in Embu').add_to(m_2)
for _, r in PPE.iterrows():
    lat = r['geometry'].y
    lon = r['geometry'].x
    folium.Marker(location=[lat, lon],
                  tooltip='click for ppe',
                  popup='Name: {} <br> Location: {}'.format(r['name_type'], r['location']),
                  icon=folium.Icon(color='black', icon='glyphicon-tint', prefix='glyphicon')).add_to(cluster_ppe)


# loading and styling polygon layers
style_1 = {'fillColor': '#00FF00', 'color': '#78AB46'}    
forest_cover = folium.GeoJson(forest, name='Forest Cover', style_function= lambda x: style_1, control=False).add_to(m_2)

style_2 = {'fillColor': '#FFA500', 'color': '#FF8C00'}
Mawasco = folium.GeoJson(mawasco, name='Mawasco WSC', style_function= lambda x: style_2,
                         tooltip='Mawasco', control=False).add_to(m_2)

style_3 = {'fillColor': '#2F4F4F', 'color': '#2F4F4F'}
Mathira = folium.GeoJson(mathira, name='Mathira WSC', style_function= lambda x: style_3,
                         tooltip='Mathira', control=False).add_to(m_2)

style_4 = {'fillColor': '#CD853F', 'color': '#CD853F'}
Mewass = folium.GeoJson(mewass, name='MEWASS', style_function= lambda x: style_4,
                        tooltip='Mewass', control=False).add_to(m_2)

style_5 = {'fillColor': '#CD853F', 'color': '#CD853F'}
imetha = folium.GeoJson(Imetha, name='Imetha', style_function = lambda x: style_5,
                        tooltip='Imetha', control=False).add_to(m_2)

style_6 = {'fillColor': '#CD853F', 'color': '#CD853F'}
kiriwasco = folium.GeoJson(Kiriwasco, name='Kiriwasco', style_function = lambda x: style_6,
                           tooltip='Kiriwasco', control=False).add_to(m_2)

style_7 = {'fillColor': '#CD853F', 'color': '#CD853F'}
kyeni = folium.GeoJson(Kyeni, name='Kyeni', style_function = lambda x: style_7,
                       tooltip='Kyeni', control=False).add_to(m_2)

style_8 = {'fillColor': '#CD853F', 'color': '#CD853F'}
mde = folium.GeoJson(MDE, name='Multipurpose Dams in Embu', style_function = lambda x: style_8,
                     tooltip='Multipurpose Dams in Embu', control=False).add_to(m_2)

style_9 = {'fillColor': '#CD853F', 'color': '#CD853F'}
mm = folium.GeoJson(MM, name='Murugi-Mugumango', style_function = lambda x: style_9,
                    tooltip='Murugi-Mugumango', control=False).add_to(m_2)

style_10 = {'fillColor': '#CD853F', 'color': '#CD853F'}
muthambi = folium.GeoJson(Muthambi, name='Muthambi', style_function = lambda x: style_10,
                          tooltip='Muthambi', control=False).add_to(m_2)

style_11 = {'fillColor': '#CD853F', 'color': '#CD853F'}
naruwasco = folium.GeoJson(Naruwasco, name='Naruwasco', style_function = lambda x: style_10,
                           tooltip='Naruwasco', control=False).add_to(m_2)

style_12 = {'fillColor': '#CD853F', 'color': '#CD853F'}
ndamunge = folium.GeoJson(Ndamunge, name='Ndamunge', style_function = lambda x: style_12,
                          tooltip='Ndamunge Area', control=False).add_to(m_2)

style_13 = {'fillColor': '#CD853F', 'color': '#CD853F'}
nn = folium.GeoJson(NN, name='Nginda Ngandori', style_function = lambda x: style_13,
                    tooltip='Nginda Ngandori Region', control=False).add_to(m_2)

style_14 = {'fillColor': '#CD853F', 'color': '#CD853F'}
nithi = folium.GeoJson(Nithi, name='Nithi', style_function = lambda x: style_14,
                       tooltip='Nithi Coverage Area', control=False).add_to(m_2)

style_15 = {'fillColor': '#CD853F', 'color': '#CD853F'}
nyewasco = folium.GeoJson(Nyewasco, name='Nyewasco', style_function = lambda x: style_15,
                          tooltip='Nyewasco Coverage Area ', control=False, overlay=True, show=True).add_to(m_2)

style_16 = {'fillColor': '#CD853F', 'color': '#CD853F'}
omwasco = folium.GeoJson(Omwasco, name='Omwasco', style_function = lambda x: style_16,
                         tooltip='Omwasco Water & Sanitation', control=False).add_to(m_2)

style_17 = {'fillColor': '#CD853F', 'color': '#CD853F'}
rw = folium.GeoJson(RW, name='Rukanga', style_function = lambda x: style_17,
                    tooltip='Rukanga Water Service Providers', control=False).add_to(m_2)

style_18 = {'fillColor': '#CD853F', 'color': '#CD853F'}
tw = folium.GeoJson(TW, name='Teawasco', style_function = lambda x: style_18,
                    tooltip='Teawasco Service Area', control=False).add_to(m_2)

style_19 = {'fillColor': '#FFFFFF', 'color': '#696969'}
kenya = folium.GeoJson(Kenya, name='Counties',
                       style_function = lambda x: {
                           'color': 'black',
                           'weight': 1,
                           "opacity": 1,
                           'fillOpacity': 0,
                           'interactive': False
                       },
                       control=True).add_to(m_2)


# adding functionalities to the map
# mini map, scrol zoom, drawing tools, measure tools, tile layers, 
# plugin for mini map
mini_map = plugins.MiniMap(tile_layer='cartodb positron', 
                           position='bottomright')

# adding the mini map to the main map
m_2.add_child(mini_map)

# add full screen toggle button
plugins.Fullscreen(position='topleft').add_to(m_2)


# adding the drawing tools
draw = plugins.Draw(export=True)

m_2.add_child(draw)

#########################
## adding the measure tools
measure_control = plugins.MeasureControl(position='topleft',
                                        active_color='red',
                                        completed_color='green',
                                        primary_area_unit='meters')


m_2.add_child(measure_control)

# add scroll and zoom toggler in map
plugins.ScrollZoomToggler().add_to(m_2)


#adding basemap layers
folium.raster_layers.TileLayer('Open Street Map').add_to(m_2)
folium.raster_layers.TileLayer('Stamen Terrain').add_to(m_2)
folium.raster_layers.TileLayer('Stamen Toner').add_to(m_2)
folium.raster_layers.TileLayer('Stamen Watercolor').add_to(m_2)
folium.raster_layers.TileLayer('Cartodb Positron').add_to(m_2)
folium.raster_layers.TileLayer('Cartodb Dark_Matter').add_to(m_2)

####################################
folium.LayerControl(collapsed=True, position='topright').add_to(m_2)



# final display
folium_static(m_2, width=900, height=600)
