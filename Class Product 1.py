class Product:
    def __init__(self, name, price, quantity):
        self.name = name  # Public for easy access
        self.__price = self._validate_price(price)  # Private with validation
        self.__quantity = self._validate_quantity(quantity) # Private with validation

    def _validate_price(self, price):  # Private helper method
        if price >= 0:
            return price
        else:
            raise ValueError("Price cannot be negative.")

    def _validate_quantity(self, quantity): # Private helper method
        if quantity >= 0:
            return quantity
        else:
            raise ValueError("Quantity cannot be negative.")

    def get_price(self):
        return self.__price

    def get_quantity(self):
        return self.__quantity

    def update_quantity(self, amount):
        self.__quantity = self._validate_quantity(self.__quantity + amount)

# Usage
try:
    product = Product("Laptop", 15000, 10)
    print(f"Product: {product.name}, Price: {product.get_price()}, Quantity: {product.get_quantity()}")
    product.update_quantity(5)
    print(f"Updated Quantity: {product.get_quantity()}")
    invalid_product = Product("Mouse", -5, 20) # This will raise a ValueError
except ValueError as e:
    print("Error:", e)