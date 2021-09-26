from collections import namedtuple

# 基础

Point = namedtuple("Point", ["x", "y"])

p = Point(11, y=22)

print(Point)
print(p)
print(p[0], p[1])
print(p.x, p.y)

# csv

import csv

ManufacturerInfo = namedtuple("ManufacturerInfo", "Manufacturer, Rating, Speed")

for manu in map(
    ManufacturerInfo._make,
    csv.reader(open("src/data_type/collections/example.csv", "r")),
):
    print(manu.Manufacturer, manu.Rating, manu.Speed)
