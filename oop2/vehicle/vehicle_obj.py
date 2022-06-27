from bus import Bus

from motocycle import motocycle

bus = Bus("Bus",4,120,"v1234")
#bus.color = 'Blue'
bus.set_color('Blue')
#bus.capacity = 34
bus.set_capacity(34)
bus.bus_detail()

bike = motocycle("Motocycle",2,100,"v5678")
#bike.cc = 1200
bike.set_cc(1200)
bike.bike_detail()