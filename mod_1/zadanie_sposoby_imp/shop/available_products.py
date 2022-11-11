products = {
    "chleb": {
        "quantity": 100,
        "price": 3.5
    },
    "jabłka": {
        "quantity": 50,
        "price": 3.2
    },
    "cukier": {
            "quantity": 50,
            "price": 4.2
        }
}

def update_product_quantity(product_name, ordered_quantity):
    products[product_name]["quantity"] -= ordered_quantity