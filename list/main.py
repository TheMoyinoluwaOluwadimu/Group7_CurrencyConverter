RandomNumber = [1, 2, 4, 5, 6, 8, 9, 7, 1, 0]
print(RandomNumber[2])
Menu = ["Coffee", "Tea", "Beans", "Water", "Drink", "Espresso"]
print(Menu[3])
Price = ["$2", "$5", "$7", "$3", "$6", "$3"]
string = "Order: "
print(string + Menu[0])
print(len(Menu))
print(Menu * 3)
print(Menu[3] + " " + Price[3])
Menu.append("Soda")
print(Menu[6])
print(Menu)
print("Tea" in Menu)
print(sorted(RandomNumber))
Menu.pop(3)
print(Menu.pop())
menu = ("Yam", "Beans", "Rice", "Eggs", "Ramen")
print(menu[2])
print(menu)
slice(menu[1])
print(menu [0:-1])