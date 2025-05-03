def get_valid_int(prompt, error_msg="Invalid input. Please enter a number."):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(error_msg)

def find_product_by_id(products, product_id):
    for product in products:
        if product["id"] == product_id:
            return product
    return None

def is_positive_number(n):
    return isinstance(n, int) and n > 0
