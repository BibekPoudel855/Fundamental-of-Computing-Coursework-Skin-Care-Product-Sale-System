"""4

importing modules from modules folder
which includes various functions to handle features of this system
"""
from modules.display import show_products
from modules.file_io import read_products_from_file
from modules.restock import restock_products
from modules.sales import sell_products
from modules.utils import *
from modules.add_new_products import add_new_products

# ################################################################################
def display_welcome_message():
    """
    This function is used to display the welcome message for the user
    """
    print_horizintal_line_bold(60)
    print(f"🎉🎉🎉 Welcome to We Care Suppliers 🎉🎉🎉")
    print_horizintal_line_bold(60)

# function to print greeting message at last thank you 
def print_exit_message():
    print_horizintal_line_bold(60)
    print("🙏 Thank you for using We Care Skin Care Store")
    print_horizintal_line_bold(60)

def show_choices_message():
    """
    This function is used to show the choices for the user to choose from
    """
    print_horizintal_line_small(60)
    print("💡 Please press number in your keyboard for given operation")
    print_horizintal_line_small()
    print("1 -> Show Products 🧴")
    print("2 -> Sell Products 🛒")
    print("3 -> Restock Products 🔄")
    print("4 -> Add New Product ➕")
    print("5 -> Exit System 🛑")
    print_horizintal_line_small()

def handle_choice(choice, all_products_list):
    if choice == 1:
        show_products(all_products_list)
        # if the user input is 2 then we call sellProducts function 
    elif choice == 2:
        sell_products(all_products_list)
        # if the user input is 3 then call restockProducts function
    elif choice == 3:
        restock_products(all_products_list)
        # if the user input is 4 then we call addNewProducts function
    elif choice == 4:
        add_new_products(all_products_list)
        # if the user input is 5 then we exit the system
    elif choice == 5:
        print_exit_message()
        return 5
        # if the user input not betn 1 to 5 then we print error message
    else :
        print_horizintal_line_small(60)
        print("❌ < Invalid input, please enter number between 1 to 5 >")  # updated to reflect correct range
        return 0
################################################################################
def main() :
    """
    This is a main function or entry point of the skin care store system
    all the operation of the system will started from this function
    Like showing available products, selling products, restocking products and exiting the system
    """
    # calling readProductsFromFile function to read the products from the file which returns the list of products
    all_products_list = read_products_from_file()
    # if products list is empty then we print error message 
    # then user to add new products
    if len(all_products_list) == 0:
        print("❌ No products available in file")
        print("Please add new products to the file")
        add_new_products(all_products_list)
        if(len(all_products_list) == 0):
            print_exit_message()
            return
    # printing the welcome message
    display_welcome_message()
    while True :
        # printing the options for the user to choose operation like showing available products, selling products, restocking products and exiting the system
        show_choices_message()

        """
        taking input choice from the user to perform operation they want to perform
        we are using try and except to make a sure correct input is given by the user
        if the user gives invalid input then we print error then ask them to enter again"""

        choice = user_input_int("Please enter a number : ")  
        # checking the user input  and calling function based on choice variable
        # if the user input is 1 then we call showProducts function to show available products in the store
        if handle_choice(choice, all_products_list) == 5:
            break
# calling main function to start the program
main()# entry point of the program