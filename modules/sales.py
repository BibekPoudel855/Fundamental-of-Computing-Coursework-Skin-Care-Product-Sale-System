from modules.file_io import generate_invoice
from modules.display import show_products
from modules.file_io import write_products_to_file
################################################################################
# fuction which is used to sell products
def sell_products(products) :
    """
    This function is used to sell products from the store and reduces
    stock after sales success
    """
    #ask for customer name 
    customer_name = input("Enter customer name: ")
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
            product_id = int(input("Enter product ID or enter <0 to finish sale> : "))
            if product_id == 0:
                # if user enter 0 then we break the loop and exit
                break
            """extracting the product from the list based on the product id given by user
            if entered invalid product id then print error msg and continue the loop"""
            selected_product = None
            for product in products:
                if product["id"] == product_id:
                    selected_product = product
                    break
            # checking if the product id is in the list products or not
            if not selected_product:
                print("Enter correct product id.")
                continue
            # asking user to enter the quantity of product they want to sell
            selling_qty = int(input(f"How many {selected_product['name']} you want to sell "))
            # calculating total stock with free items 
            total_qty_after_free = selling_qty + (selling_qty // 3)
            # checking if the stock is available or not
            if total_qty_after_free > selected_product["stock"]:
                print(f"Not Sufficient Stock. Only {selected_product['stock']} available")
                continue

            #printing details of the sold product
            print(f"✅ Sold {selling_qty} Units {selected_product['name']} & Given {selling_qty // 3} for free)")
        
            # Update stock after selling
            selected_product["stock"] -= total_qty_after_free
            # Adding to cart
            cart.append({
                "id": selected_product["id"],
                "name": selected_product["name"],
                "company": selected_product["company"],
                "price": selected_product["price"],
                "quantity": selling_qty,
                "free": selling_qty // 3,
                "total_amount_sold_exclude_free_items": (selected_product["price"]) * selling_qty
            })
        except ValueError:
            print("Invalid input, Enter number only.")
            continue
    if cart:
        # if cart is not empty then we call generate_invoice function
        generate_invoice(cart, customer_name, "sale")
        # we call this method from here because if cart is not it means we have sold products 
        write_products_to_file(products)

