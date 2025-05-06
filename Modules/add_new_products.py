from modules.utils import print_horizintal_line_small,user_input_float,user_input_string,user_input_int
from modules.file_io import read_products_from_file
from modules.file_io import add_new_product_to_file
from modules.display import show_products
def add_new_products():
    """
    Function which add new products to the file.
    """
    while True: 
        # taking user input 
        product_name = user_input_string("🛍️  Enter product name or ↩️  0 to exit : ")
        # if user press 0 then exit
        if(product_name == "0"):
            print("↩️ Exiting... ")
            break
        product_company = user_input_string("🏢 Enter product company: ")
        product_price = user_input_float("💰 Enter product price: ")
        product_qty = user_input_int("📦 Enter product quantity: ")
        product_country = user_input_string("🌍 Enter product country: ")
        # update file with new product
        add_new_product_to_file(product_name, product_company, product_price, product_qty, product_country)