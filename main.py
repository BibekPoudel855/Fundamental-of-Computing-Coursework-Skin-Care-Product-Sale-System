"""
importing modules from modules folder
which includes various functions to handle features of this system
"""
from modules.display import show_products
from modules.file_io import read_products_from_file
from modules.restock import restock_products
from modules.sales import sell_products

"""
This is a main function or entry point of the skin care store system
all the operation of the system will started from this function
Like showing available products, selling products, restocking products and exiting the system
"""
################################################################################
def main() :
    # calling readProductsFromFile function to read the products from the file which returns the list of products
    all_products_list = read_products_from_file()
    if len(all_products_list) == 0:
        print("No products available in file")
        return
    # printing the welcome message and options for the user
    print("-"*50)
    print("Welcome to We Care skin care store")
    while True :
        # printing the options for the user to choose operation like showing available products, selling products, restocking products and exiting the system
        print("----------------------------------------------------")
        print("Please press number in your keyboard for given operation")
        print("----------------------------------------------------")
        print("1 -> Show Products")
        print("2 -> Sell Products")
        print("3 -> Restock Products")
        print("4 -> Exit System")
        # taking input choice from the user to perform operation they want to perform
        # we are using try and except to make a sure correct input is given by the user
        # if the user gives invalid input then we print error then ask them to enter again
        try :
            print("-"*50)
            choice = int(input("Please enter a number : "))
        except :
            print("----------------------------------------------------")
            print("< Enter Number only >")
            continue
        # checking the user input  and calling function based on choice variable
        # if the user input is 1 then we call showProducts function to show available products in the store
        if choice == 1:
            show_products(all_products_list)
        # if the user input is 2 then we call sellProducts function 
        elif choice == 2:
            sell_products(all_products_list)
        # if the user input is 3 then call restockProducts function
        elif choice == 3:
            restock_products(all_products_list)
        # if the user input is 4 then we exit the system
        elif choice == 4:
            print("----------------------------------------------------")
            print("Thank you")
            break
        # if the user input not betn 1 to 4 then we print error message
        else :
            print("----------------------------------------------------")
            print("< Invalid input, please enter number between 1 to 4 >")

# calling main function to start the program
main()# entry point of the program

















