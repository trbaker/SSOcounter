from urllib.parse import urlparse
from arcgis.gis import GIS

gis = GIS("https://education.maps.arcgis.com")
print(gis._product_version)
flyr_list = gis.content.search(query="*", item_type ="Feature Layer")
flyr_item = flyr_list[0]
flyr = flyr_item.layers[0]
hive_inferred = urlparse(flyr.url).netloc
print(hive_inferred)
