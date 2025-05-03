from modules.display import show_products
from modules.file_io import write_products_to_file,generate_invoice
################################################################################
# function which is used to restock products
def restock_products(products) :
    """
    This function is used to restock products in the store
    """
    supplier_name = input("Enter the supplier name : ")
    # strip method removes whitespace or space 
    supplier_name= supplier_name.strip()
    #cart of restocked items
    restocked_item=[]
    while True :
        # displaying available products
        show_products(products)
        try:
        # taking input from user to restock product
            product_id = int(input("Enter the product id to restock <0 to stop restock> : "))
            # if user enter 0 then break the loop
            if product_id == 0:
                break
            # checking if product id is valid or not
            selected_product = None
            for product in products:
                if product["id"] == product_id:
                    selected_product = product
                    break
            # checking if the product id is in the list products or not
            if not selected_product:
                print("Enter correct product id.")
                continue

            # input qty to restock product
            restock_qty = int(input(f"Enter the quantity to restock {selected_product['name']} : "))
            if restock_qty <= 0:
                print("Please enter a valid quantity.")
                continue
            # input new price of product 
            new_price = float(input(f"Enter new price for {selected_product['name']} <current: {selected_product['price']}>: "))
            if new_price <= 0:
                print("❌ Price must be positive.")
                continue
            """
            # updating the stock of the product & price as well
            # by updating selected product variable it will update the original product dictionary
            # because it points to the same memory that original product dictionary points
            """
            selected_product['stock'] += restock_qty
            selected_product['price'] = new_price

            # Track for invoice
            restocked_item.append({
                "id": selected_product["id"],
                "name": selected_product["name"],
                "company": selected_product["company"],
                "price": new_price,
                "quantity": restock_qty,
                "amount": restock_qty * new_price
            })

            # printing success message
            print(f"✅ Restocked {restock_qty} units of {selected_product['name']} at Rs. {new_price}.")
        except ValueError:
            print("Please enter a valid ID.")
            continue
    if restocked_item:
         # writing the updated products to file
        write_products_to_file(products)
        generate_invoice(restocked_item, supplier_name,"restock")
        


