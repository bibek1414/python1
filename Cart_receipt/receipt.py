import datetime

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Supermarket:
    def __init__(self):
        self.inventory = {
            'Bread': Product('Bread', 2.50, 50),
            'Milk': Product('Milk', 3.00, 40),
            'Eggs': Product('Eggs', 4.50, 30),
            'Cheese': Product('Cheese', 5.00, 25),
            'Apples': Product('Apples', 1.50, 100)
        }
        self.customers = []

    def display_inventory(self):
        """Display current inventory with prices and quantities."""
        print("\nCurrent Inventory:")
        for name, product in self.inventory.items():
            print(f"{name}: ${product.price:.2f} - {product.quantity} in stock")

    def create_cart(self):
        """Create a shopping cart for a customer."""
        cart = {}
        while True:
            self.display_inventory()
            product_name = input("Enter product name (or 'done' to finish shopping): ").strip()
            
            if product_name.lower() == 'done':
                break

            if product_name not in self.inventory:
                print("Product not found. Please choose from available items.")
                continue

            # Get quantity input with error handling
            try:
                quantity = int(input(f"Enter quantity of {product_name}: "))
                if quantity <= 0:
                    print("Quantity must be a positive number.")
                    continue
            except ValueError:
                print("Please enter a valid number.")
                continue

            product = self.inventory[product_name]
            if quantity > product.quantity:
                print(f"Insufficient stock. Only {product.quantity} {product_name} available.")
                continue

            # Update cart and inventory
            cart[product_name] = cart.get(product_name, 0) + quantity
            product.quantity -= quantity

        return cart

    def generate_receipt(self, cart):
        """Generate a receipt for the current cart."""
        if not cart:
            print("Cart is empty.")
            return None

        total = 0
        print("\n--- RECEIPT ---")
        print(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("-" * 30)
        
        for product_name, quantity in cart.items():
            product = self.inventory[product_name]
            item_total = product.price * quantity
            total += item_total
            print(f"{product_name}: {quantity} x ${product.price:.2f} = ${item_total:.2f}")
        
        print("-" * 30)
        print(f"Total: ${total:.2f}")
        
        return {
            'items': cart,
            'total': total,
            'timestamp': datetime.datetime.now()
        }

    def run(self):
        """Main application loop."""
        while True:
            print("\n--- Virtual Supermarket ---")
            print("1. Start Shopping")
            print("2. View Inventory")
            print("3. View Past Receipts")
            print("4. Exit")
            
            choice = input("Choose an option: ")

            if choice == '1':
                cart = self.create_cart()
                if cart:
                    receipt = self.generate_receipt(cart)
                    if receipt:
                        self.customers.append(receipt)
            elif choice == '2':
                self.display_inventory()
            elif choice == '3':
                self.view_past_receipts()
            elif choice == '4':
                print("Thank you for shopping!")
                break
            else:
                print("Invalid option. Please try again.")

    def view_past_receipts(self):
        """Display past customer receipts."""
        if not self.customers:
            print("No past receipts.")
            return

        print("\n--- Past Receipts ---")
        for i, receipt in enumerate(self.customers, 1):
            print(f"\nReceipt {i}:")
            print(f"Date: {receipt['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"Total: ${receipt['total']:.2f}")
            print("Items:")
            for item, qty in receipt['items'].items():
                print(f"  {item}: {qty}")

def main():
    """Entry point of the application."""
    supermarket = Supermarket()
    supermarket.run()

# Ensure the script can be run directly
if __name__ == "__main__":
    main()  