from modules.utils import print_horizintal_line_bold,print_horizintal_line_small
################################################################################
def display_table_header():
    """
    This function is used to display the table header for the products
    """
    print_horizintal_line_bold(100)
    print(f"{"Product ID":^15}{"Product Name" :^20}{"Company":^20}{"Selling Price":^15}{"Stock":^15}{"Country":^15}")
    print_horizintal_line_bold(100)

################################################################################
def display_table_body(all_products_list):
    """
    This function is used to display the table body for the products
    """
    for product in all_products_list:
        print(f"{(product['id']):^15}{product['name']:^20}{product['company']:^20}{str(product['price']):^15}{str(product['stock']):^15}{product['country']:^20}")
################################################################################
# function which shows the available products in the store
def show_products(all_products_list) :
    """
    This function is used to show available products in the text file or store
    first code will read data then it will print the data in a formatted
    """
    if len(all_products_list)==0:
        print("No products available")
        return 
    # calling function to display table header & body
    display_table_header()
    display_table_body(all_products_list)
    