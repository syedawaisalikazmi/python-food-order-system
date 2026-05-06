menu={"biryani":1.3,
      "pasta":4.5,
      "chicken":2.3,
      "fries":1.2,
      "korma":4.3}
      
cart=[]
total=0
# .keys()   = sirf keys
# .values() = sirf values
# .items()  = key + value dono

print("-------MENU-------")
print("FOODS      PRICES")
print("..................")
for key,value in menu.items() :
    print(f"{key:10} ${value:.2f}")
    
while True:
    food = input("enter the food name (q for quit):").lower()
    if food=="q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
    else:
        print("item is not avaliable")

print("--------YOUR ORDER-------")

for food in cart:
    total += menu.get(food)
    print(f" --{food}",end=" ")

print()
print(f"your total bill is ${total:.2f}")
