class MenuItem:
    def __init__(self, item_id, name, price):
        self.item_id = item_id
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.item_id}. {self.name} - ₹{self.price}"


class Menu:
    def __init__(self):
        self.items = {} 

    def add_item(self, item):
        self.items[item.item_id] = item

    def remove_item(self, item_id):
        if item_id in self.items:
            del self.items[item_id]
            return True
        return False

    def display_menu(self):
        print("\n📋 Menu:")
        if not self.items:
            print("Menu is empty.")
            return
        for item in sorted(self.items.values(), key=lambda x: x.item_id):
            print(item)

    def get_item_by_id(self, item_id):
        return self.items.get(item_id)


class Order:
    def __init__(self):
        self.cart = [] 

    def add_item(self, item):
        self.cart.append(item)
        print(f"✅ {item.name} added to your cart.")

    def view_cart(self):
        if not self.cart:
            print("🛒 Your cart is empty.")
            return
        print("\n🛒 Your Cart:")
        total = 0
        for item in self.cart:
            print(f"- {item.name} (₹{item.price})")
            total += item.price
        print(f"Total: ₹{total}")

    def checkout(self):
        print("\n🧾 Checkout Bill:")
        self.view_cart()
        print("Thank you for your order! 🙏")
        self.cart.clear()



class User:
    def __init__(self, name):
        self.name = name
        self.order = Order()

    def view_menu(self, menu):
        menu.display_menu()

    def place_order(self, menu):
        menu.display_menu()
        try:
            item_id = int(input("Enter item ID to add to cart: "))
            item = menu.get_item_by_id(item_id)
            if item:
                self.order.add_item(item)
            else:
                print("❌ Invalid item ID.")
        except ValueError:
            print("❌ Please enter a valid number.")

    def view_cart(self):
        self.order.view_cart()

    def checkout(self):
        self.order.checkout()


class Admin(User):
    def __init__(self, name):
        super().__init__(name)

    def add_menu_item(self, menu):
        try:
            item_id = int(input("Enter new item ID: "))
            name = input("Enter item name: ")
            price = int(input("Enter item price: ₹"))
            if item_id in menu.items:
                print("⚠️ Item ID already exists.")
                return
            item = MenuItem(item_id, name, price)
            menu.add_item(item)
            print(f"✅ Item '{name}' added to menu.")
        except ValueError:
            print("❌ Invalid input.")

    def remove_menu_item(self, menu):
        try:
            item_id = int(input("Enter item ID to remove: "))
            if menu.remove_item(item_id):
                print(f"✅ Item ID {item_id} removed from menu.")
            else:
                print("❌ Item not found.")
        except ValueError:
            print("❌ Invalid input.")


def main():
    menu = Menu()
    menu.add_item(MenuItem(1, "Pizza", 150))
    menu.add_item(MenuItem(2, "Burger", 80))
    menu.add_item(MenuItem(3, "Pasta", 120))
    menu.add_item(MenuItem(4, "Maggie", 60))
    print("👋 Welcome to FoodEase")
    print("Are you:\n1. User\n2. Admin")
    role = input("Enter your role (1 or 2): ")

    name = input("Enter your name: ")
    user = Admin(name) if role == "2" else User(name)

    while True:
        print("\n======== MENU ========")
        if isinstance(user, Admin):
            print("1. View Menu")
            print("2. Add Menu Item")
            print("3. Remove Menu Item")
            print("4. View Cart")
            print("5. Checkout")
            print("6. Exit")
        else:
            print("1. View Menu")
            print("2. Place Order")
            print("3. View Cart")
            print("4. Checkout")
            print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            user.view_menu(menu)

        elif choice == "2":
            if isinstance(user, Admin):
                user.add_menu_item(menu)
            else:
                user.place_order(menu)

        elif choice == "3":
            if isinstance(user, Admin):
                user.remove_menu_item(menu)
            else:
                user.view_cart()

        elif choice == "4":
            if isinstance(user, Admin):
                user.view_cart()
            else:
                user.checkout()

        elif choice == "5" and isinstance(user, Admin):
            user.checkout()

        elif (choice == "5" and not isinstance(user, Admin)) or (choice == "6" and isinstance(user, Admin)):
            print("👋 Exiting. Have a great day!")
            break

        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
