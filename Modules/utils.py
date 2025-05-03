############################################################
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
    

    

