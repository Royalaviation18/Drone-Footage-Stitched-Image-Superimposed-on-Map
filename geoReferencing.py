import folium
from folium.raster_layers import ImageOverlay
from PIL import Image

# Estimated bounds — adjust manually!
bounds = [[30.1140, 78.2825], [30.1170, 78.2880]]  # [SW, NE]

m = folium.Map(location=[30.1158, 78.2853], zoom_start=17)
image = 'stitched_output.png'

ImageOverlay(
    image=image,
    bounds=bounds,
    opacity=0.7,
    interactive=True,
).add_to(m)

m.save('map_with_overlay.html')
