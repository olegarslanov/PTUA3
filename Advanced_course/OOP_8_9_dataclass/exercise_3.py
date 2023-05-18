# Create a dataclass named "Product" that has the following attributes:
#     product_id: int
#     name: str
#     price: float
#     quantity: int

# The class should also have a method named "total_cost" that calculates and returns
#  the total cost of the product, which is the price multiplied by the quantity.

# Create a list of Product objects and write a function that takes this list as input
# and returns the product with the highest total cost.

# Write a program that creates a list of 5 Product objects, prints out their attributes,
# and then calls the function to find the product with the highest total cost.


from dataclasses import dataclass
from typing import List


@dataclass
class Product:
    product_id: int
    name: str
    price: float
    quantity: int

    def total_cost(self):
        total_cost_of_product = self.price * self.quantity
        return total_cost_of_product


class ProductList:
    product_list: List = []

    def add_to_list(self, product):
        self.product_list.append(product)

    def max_total_cost(self):
        max_cost = 0
        for product in self.product_list:
            total_cost = product.total_cost()
            if total_cost > max_cost:
                max_cost = total_cost
        return max_cost


product1 = Product(1, "Morkos", 1.00, 10)
product2 = Product(2, "Arbuzai", 1.50, 12)
product3 = Product(3, "Melionai", 2.50, 8)
product4 = Product(4, "Bulves", 0.50, 50)
product5 = Product(5, "Kapustai", 0.60, 20)

product_list = ProductList()
product_list.add_to_list(product1)
product_list.add_to_list(product2)
product_list.add_to_list(product3)
product_list.add_to_list(product4)
product_list.add_to_list(product5)

print(product1.product_id, product1.name, product1.price, product1.quantity)

print(product_list.max_total_cost())

for product in product_list.product_list:
    print(product.product_id, product.name, product.price, product.quantity)
