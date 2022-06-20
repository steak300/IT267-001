from cafe import Dessert,Drink

Dessert_menu = Dessert()
print(Dessert_menu.show_dessert())

drink_menu = Drink()
print(drink_menu.show_drink())

drink_menu.add_drink('juice')
drink_menu.add_drink('smoothy')
print(drink_menu.show_drink())
