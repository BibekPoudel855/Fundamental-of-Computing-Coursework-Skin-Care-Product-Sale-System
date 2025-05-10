############################################################
# functions for print lines 
def print_horizintal_line_small(length=60):
    """
    print function print small single line for length provided by other functions
    if leght not provided then default parameter is 60 will be used
    """
    print("-" * length)

def print_horizintal_line_bold(length=60):
    """
    print function print bold line for given length provided by other functions
    if leght not provided then default parameter is 60 will used
    """
    print("=" * length)

# functions for take input from user
############################################################
# function which is take int input from user
def user_input_int(prompt, exclue_zero=False):
    """
    function which takes input from user and check if it is int or not
    it takes prompt as paramerter and prompr used in input function
    and if it is int then it will return the value
    otherwise loop continue 

    if exclude_zero is True then 0 is not allowed
    in input otherwise it will be allowed
    """
    while True:
        try:
            # takeing input from user and check if int or not
            value = int(input(prompt))
            if exclue_zero:
                if value <= 0:
                    print("❌ Number must be greater than zero.")
                    continue
            elif value < 0:
                print("❌ Number cant be negative.")
                continue
            return value
        # if value not int then goes to catch then raise ValueError
        except ValueError:
            print("❌ Please enter a valid integer.")

############################################################
# function which is take float input from user
def user_input_float(prompt, exclude_zero=False):
    """
    function which takes input from user and check if it is float or not
    it takes prompt paramerter and prompr used in input function
    if exclude_zero is True then 0 is not allowed
    in input otherwise it will be allowed
    """
    while True:
        try:
            value = float(input(prompt))
            # check if value is less than 0 or not
            if exclude_zero:
                if value <= 0:
                    print("❌ Number must be greater than zero.")
                    continue
            elif value < 0:
                print("❌ Number cant be negative.")
                continue
            return value
        except ValueError:
            print("❌ Please enter a valid float number.")

############################################################
# function which is take string input from user
def user_input_string(prompt, validate_person_name=False, validate_alpha = False, allow_zero_exit = False):
    """
    it return string input from user with proper validation
    it takes prompt as paramerter and prompr used in input function
    if validate_person_name is True then name shuould be full name
    if validate_alpha is True then name cannt have alpha numeric characters
    if allow_zero_exit is True then 0 is allowed in input
    otherwise it will be not allowed
    """
    while True:
        # strip input value to remove unnecessary space when user enter the input
        value = input(prompt).strip()
        # checking input empty or
        if value == "":
            print("❌ Please enter valid string.")
            continue

        if allow_zero_exit:
            if value == "0":
                return value
        if validate_person_name:
            # check there is space between the name or not
            if len(value.split(" ")) < 2:
                print("❌ Please Enter full name.")
                continue

        if validate_alpha:
            split_name = value.split(" ")
            is_alpha = True
            for i in range(len(split_name)):
                # aplha check if the stirng contain letter from  a to z 
                if not split_name[i].isalpha():
                    is_alpha = False
                    print("❌ Enter alphanumeric name.")
                    break
            if not is_alpha:
                continue
        return value
# functions for validation of data
############################################################
# function which is used to check if the product is in stock or not
def check_product_in_stock(selling_qty, product):
    """
    function which is used to check if the product is in stock or not
    """
    # check if selling quantity is greater than stock or not
    # if selling quantity is greater than stock then we print error message
    # and return false
    if selling_qty > product["stock"]:
        print(f"❌ Sorry, we don't have enough {product['name']} in stock.")
        return False
    return True
##############################################################
# function which is used to check if the product id is valid or not
def check_product_id_valid(product_id, products):
    # checking if the product id given in function is valid or not
    # if product id not valid or it is not in list of disctionary then we print error message

    for product in products:
        if product["id"] == product_id:
            return product
    return None
# function which check if input is == 0  
def check_input_zero(value):
    # function which check if input is == 0
    if value == 0:
        return True
    return False