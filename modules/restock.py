from modules.display import show_products
from modules.file_io import write_products_to_file,generate_invoice
from modules.utils import *

################################################################################
def append_restocked_item(restocked_item, target_product, new_price, restock_qty):
    """
    This function is used to append the restocked item to the products list
    """
    # for invoice generation
    restocked_item.append({
        "id": target_product["id"],
        "name": target_product["name"],
        "company": target_product["company"],
        "price": new_price,
        "quantity": restock_qty,
        "amount": restock_qty * new_price
    })
    # printing success message
    print(f"✅ Restocked {restock_qty} units of {target_product['name']} at Rs. {new_price}.")

################################################################################

def update_product(target_product, new_price, restock_qty):
    """
    # updating the stock of the product & price as well
    # by updating selected product variable it will update the original product dictionary
    # because it points to the same memory that original product dictionary points
    """
    target_product['stock'] += restock_qty
    target_product['cost_price'] = new_price
    target_product['price'] = new_price * 2


################################################################################
# function which is used to restock products
def restock_products(products) :
    """
    This function is used to restock products in the store
    """
    supplier_name = user_input_string("🏢 Enter the supplier name : ")
    #cart of restocked items
    restocked_item=[]
    while True :
        # displaying available products
        show_products(products)
        try:
        # taking input from user to restock product
            product_id = user_input_int("📦 Enter the product id to restock <0 to stop restock> : ")
            # if user enter 0 then break the loop
            if product_id == 0:
                break
            # checking if product id is valid or not
            target_product = check_product_id_valid(product_id, products)
            # checking if the product id is in the list products or not
            if not target_product:
                print("❌ Enter correct product id.")
                continue

            # input qty to restock product
            restock_qty = user_input_int(f"📦 Enter the quantity to restock {target_product['name']} : ")
            if restock_qty <= 0:
                print("❌ Please enter a valid quantity.")
                continue
            # input new price of product 
            new_price = user_input_float(f"💵 Enter new price for {target_product['name']} <current cost price: {target_product['cost_price']}>: ")
            if new_price <= 0:
                print("❌ Price must be positive.")
                continue

            # function which update the product in the list of products
            update_product(target_product, new_price, restock_qty)
            # appending the restocked item to the cart
            append_restocked_item(restocked_item, target_product, new_price, restock_qty)
            
    
        except :
            print("❌ Something went wrong.")
            continue
    if restocked_item:
         # writing the updated products to file
        write_products_to_file(products)
        generate_invoice(restocked_item, supplier_name,"restock")
        


