from modules.utils import *
from modules.file_io import add_new_product_to_file
from modules.display import show_products

# ################################################################################
# function which add new products to the file
def add_new_products(all_products_list):
    """
    Function which add new products to the file.
    """
    while True: 
        # taking user input 
        print_horizintal_line_small(60)
        product_name = user_input_string("🛍️  Enter product name to add or ↩️  0 to exit : ")
        # if user press 0 then exit
        if(product_name == "0"):
            print("↩️ Exiting... ")
            break
        print_horizintal_line_small(60)
        product_company = user_input_string("🏢 Enter product company: ")
        print_horizintal_line_small(60)
        product_price = user_input_float("💰 Enter product price: ", True)
        print_horizintal_line_small(60)
        product_qty = user_input_int("📦 Enter product quantity: ", True)
        print_horizintal_line_small(60)
        product_country = user_input_string("🌍 Enter product country: ")
        # update file with new product
        add_new_product_to_file(product_name, product_company, product_price, product_qty, product_country)
        # appending new product to list of products
        all_products_list.append({
            "id": len(all_products_list) + 1,
            "name": product_name,
            "company": product_company,
            "cost_price": product_price,
            "price": product_price * 2,
            "stock": product_qty,
            "country": product_country
        })
        print_horizintal_line_small()
        print(f"✅ Successfully added {product_name}")
        print_horizintal_line_small()
        # display product adding new product
        show_products(all_products_list)