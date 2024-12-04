cars=[
    {"id":1,"name":"fronx","price":1200000,"brand":"nexa","colors":["red","blue","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":2,"name":"baleno","price":1100000,"brand":"nexa","colors":["grey","blue","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":3,"name":"3xo","price":900000,"brand":"mahindra","colors":["red","white","black"],"transmissions":["amt","cvt"]},
    {"id":4,"name":"punch","price":700000,"brand":"tata","colors":["red","blue","white","green"],"transmissions":["manuel","cvt"]},
    {"id":5,"name":"nexon","price":1400000,"brand":"tata","colors":["red","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":6,"name":"kiger","price":1000000,"brand":"renault","colors":["blue","white"],"transmissions":["manuel","cvt"]},
    {"id":7,"name":"taigun","price":2300000,"brand":"volkswagon","colors":["red","blue","white"],"transmissions":["manuel","cvt"]},
]

#print count of vechicles
# print(f"total vehicle==>{len(cars)}")

# #print availale colour of baleno

# availale_colours=[c.get("colors") for c in cars if c.get ("name")=="baleno"]

# print(availale_colours)

# #print all brands

# all_brand={c.get("brand") for c in cars } #---> for remove duplicates list -->set {} or set(all_brand)
# print(all_brand)

# #print car names available in amt transmission

# availale_cars=[c.get("name") for c in cars if "amt" in c.get("transmissions")]
# print(availale_cars)

# #available cars n blue colur
# availale_in_blue=[c.get("name") for c in cars if "blue" in c.get("colors")]
# print(availale_in_blue)

# #print all transmmition
# all_transmissions={t for c in cars for t in c.get("transmissions")}
# print(all_transmissions)

# # print all colors
# all_color={color for c in cars for color in c.get("colors")}
# print(all_color)

# #most popular color

# all_clr=[color for c in cars for color in c.get("colors")]

# grp={clr:all_clr.count(clr) for clr in all_clr}
# print(grp)
# print(max(grp))

#{"blue":4,"red":2}

#costly car
costly_car=max(cars,key=lambda d:d.get("price"))
print(costly_car.get("name"))
#car with minimum cost
min_costly_car=min(cars,key=lambda d:d.get("price"))
print(min_costly_car.get("name"))
#sort cars wrt price
sorted_car=sorted(cars,key=lambda d:d.get("price"),reverse=True)
# sorted_car_name=[c.get("name") for c in sorted_car]
sorted_car_name={c.get("name"):[c.get("price"),c.get("brand")] for c in cars}
print(sorted_car_name)