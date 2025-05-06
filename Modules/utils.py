############################################################
# functions for print lines 
# function which is used to print horizontal line
def print_horizintal_line_small(length=60):
    """
    function which print horizontal line 
    """
    print("-" * length)

def print_horizintal_line_bold(length=60):
    """
    function which print horizontal line 
    """
    print("=" * length)

# functions for take input from user
############################################################
# function which is take int input from user
def user_input_int(prompt):
    """
    function which takes input from user and check if it is int or not
    """
    while True:
        try:
            value = int(input(prompt))
            # check if value is less than 0 or not
            if value < 0:
                print("❌ Number must be positive.")
                continue
            return value
        except ValueError:
            print("❌ Please enter a valid integer.")
############################################################
# function which is take float input from user
def user_input_float(prompt):
    """
    function which takes input from user and check if it is float or not
    """
    while True:
        try:
            value = float(input(prompt))
            # check if value is less than 0 or not
            if value < 0:
                print("❌ Number must be positive.")
                continue
            return value
        except ValueError:
            print("❌ Please enter a valid float number.")
############################################################
# function which is take string input from user
def user_input_string(prompt):
    """
    function which takes input from user and check if it is string or not
    """
    while True:
        value = input(prompt)
        if value.strip() == "":
            print("❌ Please enter a valid string.")
        else:
            #strip remove spaces 
            return value.strip()
    

# functions for validation of data
############################################################
# function which is used to check if the product is in stock or not
def check_product_in_stock(selling_qty, product):
    """
    function which is used to check if the product is in stock or not
    """
    if selling_qty > product["stock"]:
        print(f"❌ Sorry, we don't have enough {product['name']} in stock.")
        return False
    return True

##############################################################
# function which is used to check if the product id is valid or not
def check_product_id_valid(product_id, products):
    for product in products:
        if product["id"] == product_id:
            return product
    return None

# function which check if input is == 0  
def check_input_zero(value):
    if value == 0:
        return True
    return False