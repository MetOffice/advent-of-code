import numpy as np
import bokeh.plotting as bk
from hydrothermalventure_jam import Map, FileReader

reader = FileReader("2021/day_05/input.txt")
lines = reader.getLines()

map = Map()
map.add_lines(lines)

data = np.zeros((1000,1000))

for point, value in map.map.items():
    data[point.x, point.y] = value

data = data > 0

fig = bk.figure(x_range=(0,1), y_range=(0,1))
fig.image(image=[data], x=0, y=0, dw=1, dh=1, palette="Spectral11")

bk.show(fig)