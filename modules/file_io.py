from datetime import datetime as dt
################################################################################
# function which read the products from the text file
def read_products_from_file():
    """
    This function which read the products from the text file and returns the list of products
    """
    # this is a list of disctionary which will store the products
    # each product will be stored in a dictionary
    products = []
    # opening the file in reading mode
    try:
        file = open("data/products.txt", "r")
        # reading the file line by  and storing it in a list
        file_lines = file.readlines()  # list
        # iterating file line from list file_lines
        for line in file_lines:
            # stripping method removes whitespaces, \n and \t from the string
            product = line.strip()
            # splitting the string into list
            product = product.split(",")
            # this try catch help to avoid error when empty space or line found in file
            try :
            # creating dictionary and sorting in list products
                product_dictionary = {
                    "id": int(product[0]),
                    "name": product[1],
                    "company": product[2],
                    "cost_price": float(product[3]),
                    "price": float(product[3])*2,
                    "stock": int(product[4]),
                    "country": product[5]
                }
                # appending disctionary to list products
                products.append(product_dictionary)
            except :
                # we keep pass keyword because it allows us to keep block empty mean help to skip the error
                pass
        # closing file because to prevent memory leak and prevent unintentional changes to the file
        file.close()

    except FileNotFoundError:
        print("----------------------------------------------------")
        print("❌ < File Not Found >")
        return []    
    except :
        print("----------------------------------------------------")
        print("❌ < Something went wrong in reading file >")
        return []
    # returning the list of products
    return products
################################################################################
# function which writes updated products to the text file
def write_products_to_file(products):
    try:
        file = open("data/products.txt", "w")
        for product in products:
            # converting dictionary to string and writing to file
            # we convert because without converting to string it will give error because we are concating to string
            line = str(product['id']) + "," + product['name'] + "," + product['company'] + "," + str(product['cost_price']) + "," + str(product['stock']) + "," + product['country'] + "\n"
            file.write(line)
        file.close()
        print("✅ Products updated to file.")
    except :
        print("❌ Can't write file.")
################################################################################
# function which generate invoice
def generate_invoice(cart, name, mode):
    """
    Generates a simple invoice and saves it in data/invoices/
    with filename as <customer_name>_<cleaned-datetime>.txt
    """
    # getting current date and time
    date = dt.now()
    # converting date and time to string and removing space and colon to avioid error when creating file
    date_time_str = str(date).replace(":", "_").replace(" ", "_")
    """
    # making the filename for invoice
    # before  / python know it is path and after / it is filename
    # removing space betn customer name and keeping _
    """
    # setting the filename based on mode
    if(mode == "sale"):
        file_name = "sale_invoices"
        name_category = "Customer"
    else:
        file_name = "restock_invoices"
        name_category = "Supplier"

    # setting the filename based on mode  
    filename = f"data/invoices/{file_name}/{name.strip().replace(' ', '_')}_{date_time_str}.txt"
    # Calculate total
    total_before_vat = 0
    try :
        file = open(filename, "w")
        file.write("========= We Care SKIN CARE ========\n")
        file.write(f"{name_category} Name: {name}\n")
        file.write(f"Date: {date.year}-{date.month}-{date.day} {date.hour}:{date.minute}:{date.second}\n")
        file.write("-" * 70 + "\n")

        if mode == "sale":
            file.write(f"{'ID':<5} {'Product':<20} {'Price':<8} {'Qty':<6} {'Free':<6} {'Total':<10}\n")
        else:
            file.write(f"{'ID':<5} {'Product':<20} {'Company':<10} {'Price':<8} {'Qty':<6} {'Amount':<10}\n")

        file.write("-" * 70 + "\n")

        total_before_vat = 0
        for item in cart:
            if mode == "sale":
                total = item["total_amount_sold_exclude_free_items"]
                total_before_vat += total
                file.write(f"{item['id']:<5} {item['name']:<20} {item['price']:<8} {item['quantity']:<6} {item['free']:<6} {total:<10}\n")
            elif mode == "restock":
                total = item["amount"] 
                total_before_vat += total
                file.write(f"{item['id']:<5} {item['name']:<20} {item['company']:<10} {item['price']:<8} {item['quantity']:<6} {total:<10}\n")
    
        file.write("-" * 70 + "\n")
        file.write(f"Grand Total: Rs {total_before_vat}\n")
        file.write("! Thank you\n")
        file.close()
        # printing the invoice filename
        print(f"📄 Invoice saved in: {filename}")
    except :
        print("❌ Something went wrong in invoice:")
