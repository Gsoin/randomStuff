
class ShoppingCart:
    
    def __init__(self):
        self.dict = {}
            
    def addItem(self, name, price):
        
        self.name = name
        self.price = price
        self.dict[name] =  price

    def removeItem(self, name):
        del self.dict[product]

cart = ShoppingCart()

print("Welcome to your shopping cart!!")
print(" ----------------------------- ")

print("1.Add items to cart")
print("2.Remove items from cart")
print("3.View items in cart")
print("4.Exit")


select = int(input('Please select a task: '))
while select <=3:
    if select == 1:
        product = input('Enter product name: ')
        price = input('Enter product price: ')
        cart.addItem(product, price)
        print("Item Added!!")

    elif select == 2:
        product = input('Enter product name to delete: ')
        cart.removeItem(product)
        print("Item Deleted!!")

    elif select == 3:
        print(cart.dict)
    
    print(" -------------------------- ")

    print("1.Add items to cart")
    print("2.Remove items from cart")
    print("3.View items in cart")
    print("4.Exit")

    select = int(input('Please select a task: '))

sys.exit()



        