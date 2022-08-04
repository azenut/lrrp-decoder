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
def get_gmaps_link(pos):
    return f"https://www.google.com/maps/search/{pos[0]}+{pos[1]}"

# extract latitudes and longitudes from radio output
def parse_dsd_file(pos):
    with open("./parsing/logfile.txt", "r") as file:
        
        lines = file.readlines()
        packets = []
        
        for line in lines: # filter the data bytes with locations from file
            if "Rate" in line:
                splt_line = [x for x in line.split() if len(x) == 2 and x != "BS"]
                packets.append(splt_line)
   
    packets = "".join([x for y in packets for x in y if x]).split("4500002D") # splitting by IPv4 header
    
    for x in packets:
        src = int(x[22:24], 16)
        coord = [x[66:74], x[74:82]]
        if coord[0] and coord[1] and "." not in coord[0] and "." not in coord[1]: #removing invalid positions
            pos.append([src, [lat_decode(coord[0]), long_decode(coord[1])]])            

# MAIN                   

positions = []
parse_dsd_file(positions)

last_positions = {}
for x in positions:
    last_positions[f"{x[0]}"] = x[1]

m = folium.Map(location=[40.828301550404994, 16.553154320679383], tiles="OpenStreetMap", zoom_start=14)
for x in last_positions:
    folium.Marker(
        last_positions[x],
        tooltip = f"{x}",
        popup = f'<a href="{get_gmaps_link(last_positions[x])}">gmaps</a>'
        ).add_to(m)
m.save("map.html")