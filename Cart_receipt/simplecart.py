import datetime

print("......WELCOME TO THE SUPERMARKET ...")

class Supermarket:
    def __init__(self):
        self.inventory = {
            'kukure': 50,    
            'milk': 40,
            'eggs': 30,
            'coke': 25,
            'sandwitch': 100
        }
        self.prices = {
            'kukure': 2.50,
            'milk': 3.00,
            'eggs': 4.50,
            'coke': 5.00,
            'sandwitch': 1.50
        }

    def show_items(self):
        print("\nAvailable Items:")
        for item, quantity in self.inventory.items():
            print(f"{item.capitalize()}: ${self.prices[item]:.2f} - {quantity} left")

    def buy_items(self):    
        cart = {}
        total = 0.0

        while True:
            self.show_items()
            item = input("What do you want to buy? (or 'finish' to finish): ").lower()

            if item == 'finish':
                break

            if item not in self.inventory:
                print("Sorry, item not found!")
                continue

            try:
                quantity = int(input(f"How many {item}s? "))

                if quantity <= 0:
                    print("Please enter a valid quantity.")
                    continue

                if quantity > self.inventory[item]:
                    print(f"Sorry, only {self.inventory[item]} {item}s available.")
                    continue

               
                self.inventory[item] -= quantity

                
                item_total = self.prices[item] * quantity
                total += item_total

                timestamp = datetime.datetime.now()
                cart[item] = cart.get(item, {'quantity': 0, 'timestamp': timestamp})
                cart[item]['quantity'] += quantity

                print(f"Added {quantity} {item}(s) to cart.")

            except ValueError:
                print("Please enter a valid number.")

        
        print("\n--- RECEIPT ---")
        for item, details in cart.items():
            print(f"{item.capitalize()}: {details['quantity']} x ${self.prices[item]:.2f}")

        print(f"Date: {details['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"\nTotal: ${total:.2f}")


def main():
    store = Supermarket()
    store.buy_items()

if __name__ == "__main__":
    main()
