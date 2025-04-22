import folium

m = folium.Map(
    zoom_snap=0,
    zoom_control=False,
)

sw = [38, -3]
ne = [60, 31]

folium.Rectangle(
    bounds=[sw, ne],
).add_to(m)
m.fit_bounds([sw, ne])
