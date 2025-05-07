from modules.utils import print_horizintal_line_bold, print_horizintal_line_small

################################################################################
def display_table_header():
    """
    function which is used to display the table header
    """
    print_horizintal_line_bold(120)
    print(f"| {'Product ID':^12} | {'Product Name':^25} | {'Company':^20} | {'Selling Price':^15} | {'Stock':^10} | {'Country':^15} |")
    print_horizintal_line_small(120)

################################################################################
def display_table_body(all_products_list):
    """
    function which used to display the table body 
    """
    for product in all_products_list:
        print(f"| {product['id']:^12} | {product['name']:^25} | {product['company']:^20} | Rs {product['price']:^12.2f} | {product['stock']:^10} | {product['country']:^15} |")

################################################################################
# Function to show the available products in the store
def show_products(all_products_list):
    """
    function which is used to show products in CLI
    first checks products available, then displays them 
    """
    if len(all_products_list) == 0:
        print("❌ No products available in the store.")
        return

    # display table header and body
    display_table_header()
    display_table_body(all_products_list)
    print_horizintal_line_bold(120)
