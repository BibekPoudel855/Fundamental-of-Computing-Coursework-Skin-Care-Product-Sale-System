from modules.file_io import generate_invoice
from modules.display import show_products
from modules.file_io import write_products_to_file
from modules.utils import *

################################################################################
def append_sold_item(cart, target_product, selling_qty):
    # Adding to cart
    cart.append({
        "id": target_product["id"],
        "name": target_product["name"],
        "company": target_product["company"],
        "price": target_product["price"],
        "quantity": selling_qty,
        "free": selling_qty // 3,
        "total_amount_sold_exclude_free_items": (target_product["price"]) * selling_qty
    })
    #printing details of the sold product
    print(f"✅ Sold {selling_qty} Units {target_product['name']} & Given {selling_qty // 3} for free)")

################################################################################
def update_product(target_product, total_qty_after_free):
    """
    updating the stock of the product quantity
    """
    target_product["stock"] -= total_qty_after_free

################################################################################
# fuction which is used to sell products
def sell_products(products) :
    """
    This function is used to sell products from the store and reduces
    stock after sales success
    """
    #ask for customer name 
    customer_name = user_input_string("🧑‍🤝‍🧑Enter customer name: ")
    cart = []
    while True:
        # displaying products on stock
        print("Available Products: ")
        # shows products before selling 
        show_products(products)
        # used try and except to make a sure correct input is enter by the user
        try:
            """ 
            taking input from the user to which product to sell
            if the user enter 0 then we break the loop and exit
            """
            product_id = user_input_int("📦 Enter product ID or enter <0 to finish sale> : ")
            if product_id == 0:
            # if user enter 0 then we break the loop and exit
                break
            """extracting the product from the list based on the product id given by user
            if entered invalid product id then print error msg and continue the loop"""
            target_product = None
            for product in products:
                if product["id"] == product_id:
                    target_product = product
                    break
            # checking if the product id is in the list products or not
            if not target_product:
                print("❌ Enter correct product id.")
                continue
            # asking user to enter the quantity of product they want to sell
            
            selling_qty = user_input_int(f"📦 How many {target_product['name']} you want to sell: ")
            # calculating total stock with free items 
            total_qty_after_free = selling_qty + (selling_qty // 3)
            # checking if the stock is available or not
            if total_qty_after_free > target_product["stock"]:
                print(f"❌ Not Sufficient Stock. Only {target_product['stock']} available")
                continue

            # Update stock after selling
            update_product(target_product, total_qty_after_free)

            # appending sold item to the cart
            append_sold_item(cart, target_product, selling_qty)

        except :
            print("❌ Something went wrong. Please try again.")
            continue
    if cart:
        # if cart is not empty then we call generate_invoice function
        generate_invoice(cart, customer_name, "sale")
        # we call this method from here because if cart is not it means we have sold products 
        write_products_to_file(products)


