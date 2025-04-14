# function which read the products from the text file
def  readProductsFromFile() :
    """
    This function which read the products from the text file and returns the list of products
    """
    print("----------------------------------------------------")
    print("Reading Products from file")

# function which generate invoices
def generateInvoice() :
    """
    This function is used to generate invoice for the products sold
    """
    print("----------------------------------------------------")
    print("Generating Invoice")


# function which shows the available products in the store
def showProducts() :
    """
    This function is used to show available products in the text file or store
    first code will read data then it will print the data in a formatted
    """
    print("----------------------------------------------------")
    print("Showing available products")
    print("Product No.  Product Name        Compant       Price   Stock     Country")
    print("----------------------------------------------------")


# function which is used to restock products
def restockProducts() :
    """
    This function is used to restock products in the store
    """
    print("----------------------------------------------------")
    print("Restocking Products")

# fuction which is used to sell products
def sellProducts() : 
    """
    This function is used to sell products from the store and reduces 
    stock after sales succes
    """
    print("----------------------------------------------------")
    print("Selling Products")



"""
This is a main function or entry point of the skin care store system
all the operation of the system will started from this function
Like showing available products, selling products, restocking products and exiting the system
"""
def main() :
    # calling readProductsFromFile function to read the products from the file which returns the list of products
    allProducts = readProductsFromFile()
    while True :
        # printing the welcome message and options for the user
        print("----------------------------------------------------")
        print("Welcome to bibek inc skin care store")

        # printing the options for the user to choose operation like showing available products, selling products, restocking products and exiting the system
        print("----------------------------------------------------")
        print("Please press number in your keyboard for given operation")
        print("----------------------------------------------------")
        print("1 -> Show available products in the store")
        print("2 -> Sell Procucts")
        print("3 -> Restock products in store")
        print("4 -> Exit system")
        print("----------------------------------------------------")

        # taking input choice from the user to perform operation they want to perform
        # we are using try and except to make a sure correct input is given by the user
        # if the user gives invalid input then we print error then ask them to enter again
        try :
            choice = int(input("Please enter a number : "))
        except :
            print("----------------------------------------------------")
            print("< Enter Number only >")
            print("----------------------------------------------------")
            continue


        # checking the user input  and calling function based on choice variable
        # if the user input is 1 then we call showProducts function to show available products in the store
        if(choice == 1) :
            print("Showing Products")
            showProducts()

        # if the user input is 2 then we call sellProducts function 
        elif(choice == 2) :
            print("Selling Products")
            sellProducts()

        # if the user input is 3 then call restockProducts function
        elif(choice == 3) :
            print("Restocking Products")
            restockProducts()

        # if the user input is 4 then we exit the system
        elif(choice == 4) :
            print("----------------------------------------------------")
            print("Thank you for using bibek inc skin care store system")
            print("----------------------------------------------------")
            break
        # if the user input not betn 1 to 4 then we print error message
        else :
            print("----------------------------------------------------")
            print("< Invalid input, please enter number between 1 to 4 >")

# calling main function to start the program
main()# entry point of the program