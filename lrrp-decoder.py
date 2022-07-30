import folium

def lat_decode(lat):
    lat = ''.join(lat.upper().split())
    lat = int(lat, 16)
    lat = lat * (180/0xFFFFFFFF)
    return lat

def long_decode(lng):
    lng = ''.join(lng.upper().split())
    lng = int(lng, 16)
    lng = lng * (360/0xFFFFFFFF)
    return lng

# generate a link to see the coordinates on Google Maps
def get_gmaps_link(x, y):
    return f"https://www.google.com/maps/search/{lat_decode(x)}+{long_decode(y)}"

# extract latitudes and longitudes from radio output
def parse_dsd_file(pos):
    with open("./parsing/logfile.txt", "r") as file:
        
        lines = file.readlines()
        data = []
        
        for line in lines: # filter the data bytes only
            if "Rate" in line:
                splt_line = [x for x in line.split() if len(x) == 2 and x != "BS"]
                data.append(splt_line)
        data = [x for x in data if len(x) == 9]

        for x in data:
            coord = [lat_decode("".join(x[-8:-4])), long_decode("".join(x[-4:]))]
            pos.append(coord)
        

# MAIN                   

positions = []

parse_dsd_file(positions)

m = folium.Map(location=[40.828301550404994, 16.553154320679383], tiles="OpenStreetMap", zoom_start=14)
for x in positions:
    folium.Marker(x).add_to(m)
m.save("map.html")