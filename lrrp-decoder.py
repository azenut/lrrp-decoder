def lat_decode(lat):
    lat = ''.join(lat.upper().split())
    lat = int(lat, 16)
    lat = lat * (180/0xFFFFFFFF)
    return lat

def long_decode(long):
    long = ''.join(long.upper().split())
    long = int(long, 16)
    long = long * (360/0xFFFFFFFF)
    return long

def get_gmaps_link(lat, long):
    return f"https://www.google.com/maps/search/{lat_decode(lat)}+{long_decode(long)}"

x = "44 66 3A 10"
y = "1D 44 0B C1"

print("40.xxxxx 16.xxxxx -- planned location lat and long")
print(f"{lat_decode(x)} {long_decode(y)}\n" + get_gmaps_link(x, y))
