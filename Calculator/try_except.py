#try exception

menu = ["manazana", "platano", "naranja"]

try:
    user_input = int(input("0:manzana, 1:platano, 2:naranja >> "))
    order = menu[user_input]
except IndexError:
    print("wrong number")
except ValueError:
    print("Please enter an number 1~3.")
else:
    print(f"{order} juice ordered.")
finally:
    print("Gracias")


