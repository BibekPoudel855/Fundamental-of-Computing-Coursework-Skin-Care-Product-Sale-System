from datetime import datetime as dt
from modules.utils import print_horizintal_line_small
################################################################################
# function who extract products from file lines and store in list of dictionary
def append_product_to_list_dictn(file, products):
            product_id = 0
            # list of lines
            file_lines = file.readlines()  
            # reading the file line by  and storing it in a list
            for line in file_lines:
                # stripping method removes whitespaces, \n and \t from the string
                product = line.strip()
                # checking if product is empty if it is empty then it is consider as line is empty so skip
                if not product:
                    continue
                # splitting the string into list
                product = product.split(",")
                # skipping line if it not correct
                if len(product) != 5:
                    continue
            # this try catch help to avoid error when empty space or line found in file
                try :
                    #increase product id by one
                    product_id += 1
                # creating dictionary and sorting in list products
                    product_dictionary = {
                        "id": (product_id),
                        "name": product[0],
                        "company": product[1],
                        "cost_price": float(product[2]),
                        "price": float(product[2])*2,
                        "stock": int(product[3]),
                        "country": product[4]
                    }
                    # appending disctionary to list products
                    products.append(product_dictionary)
                except ValueError:
                # if error occurs then print the error and continue to next line
                    continue
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
        # reading file lines then store in list of dictionary
        append_product_to_list_dictn(file, products)
        # closing file because to prevent memory leak and prevent unintentional changes to the file
        file.close()
    
    except FileNotFoundError:
        print_horizintal_line_small(60)
        print("❌ < File Not Found >")
        return []    
    except :
        print_horizintal_line_small()
        print("❌ < Something went wrong in reading file >")
        return []
    # returning the list of products
    return products



################################################################################
# function which writes updated products to the text file
def write_products_to_file(products):
    try:
        # opening the file in write mode & it will  create new file if not exist
        # if file exist then it will override the file
        file = open("data/products.txt", "w")
        for product in products:
            # converting dictionary data to string and writing to file
            # we convert because without converting to string it will give error because we are concating to string
            line = product['name'] + "," + product['company'] + "," + str(product['cost_price']) + "," + str(product['stock']) + "," + product['country'] + "\n"
            file.write(line)
        # closing the file to improve performance from small and low devices
        file.close()
        print_horizintal_line_small(60)
        print("✅ Products updated to file.")
    except :
        print_horizintal_line_small(60)
        print("❌ Can't write file.")


################################################################################
def get_date_time_str():
    """
    function to get date and time in string format
    """
    # getting current date and time
    date = dt.now()
    # converting date and time to string and removing space and colon to avoid error when creating file
    date_time_str = str(date).replace(":", "_").replace(" ", "_")
    # returning date_time_str, date object 
    return date_time_str, date

################################################################################
# function which assign file category name based on mode
def assign_file_category_name(mode, date_time_str, name):
    """
    # making the main_file for invoice
    # main_file is the folder where we want to save the file
    # before  / python know it is path and after / it is filename
    # removing space betn customer name and keeping _
    """
    if mode == "sale":
        main_file = "sale_invoices"
        name_category = "Customer"
    else:
        main_file = "restock_invoices"
        name_category = "Supplier"
    file_name = f"data/invoices/{main_file}/{name.strip().replace(' ', '_')}_{date_time_str}.txt"
    return file_name, name_category

################################################################################
# function write invoice header
def write_invoice_header(file, name_category, name, date, mode, width=60):
    """
    function to write invoice header section
    file.write method is used to write the data in file
    we have displayd detail of shop and customer name in header
    """
    file.write("=" * width + "\n")
    file.write(f"{'========= We Care SKIN CARE =========' :^{width}}\n")
    file.write(f"{'Pokhara-1, Bagar, Kaski, Nepal':^{width}}\n")
    file.write(f"{'Phone: 061-412014':^{width}}\n")
    file.write(f"{'Email: wecare@gmai.com' :^{width}}\n")
    file.write(f"{'Website: www.wecareskincare.com' :^{width}}\n")
    file.write("="* width + "\n")
    file.write(f"{'Invoice':^{width}}\n")
    file.write("=" * width + "\n")
    file.write("\n")
    file.write(f"{name_category} Name: {name:<15} {'Date:':>8} {date.year}-{date.month}-{date.day} {date.hour}:{date.minute}:{date.second}\n")
    file.write("\n")
    file.write("=" * width + "\n")

    if mode == "sale":
        file.write(f"{'ID':<5} {'Product':<20} {'Price':<8} {'Qty':<6} {'Free':<6} {'Total':<10}\n")
    else:
        file.write(f"{'ID':<5} {'Product':<20} {'Company':<10} {'Price':<8} {'Qty':<6} {'Amount':<10}\n")

    file.write("-" * width + "\n")


################################################################################
# function write invoice items
def write_invoice_items(file, cart, mode, width=60):
    """
    function to write items from cart to the invoice file.
    it write data based on mode like sale or restock
    calculated toal before vat amount
    """
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
    file.write("-" * width + "\n")
    return total_before_vat


################################################################################
# function write invoice totals
def write_invoice_totals(file, total_before_vat, width=60):
    """
    function to write total amount before vat and vat amount in invoice file
    """
    vat = total_before_vat * 0.13
    grand_total = total_before_vat + vat
    file.write(f"{'Total Before Vat:':>{width-15}} Rs {total_before_vat:>.2f}\n")
    file.write(f"{'VAT (13%):':>{width-15}} Rs {vat:>.2f}\n")
    file.write(f"{'Grand Total:':>{width-15}} Rs {grand_total:>.2f}\n")
    file.write("=" * width + "\n")

################################################################################
# main generate_invoice function
def generate_invoice(cart, name, mode):
    """
    Generates a simple invoice and saves it in data/invoices/
    with filename as <customer_name>_<cleaned-datetime>.txt
    """
    # total width for invoice table line 
    width = 62
    # Getting current date object and date_time_str in string format
    date_time_str, date = get_date_time_str()  # tuple unpacking
    # Getting the filename & name_category based on mode
    #tuple unpacking
    file_name, name_category = assign_file_category_name(mode, date_time_str, name)

    try:
        # Open the file for writing
        with open(file_name, "w") as file:
            # write header
            write_invoice_header(file, name_category, name, date, mode, width)

            # write items and gives total before vat
            total_before_vat = write_invoice_items(file, cart, mode, width)

            # write the totals
            write_invoice_totals(file, total_before_vat, width)

        # Print the invoice filename
        print_horizintal_line_small(60)
        print(f"📄 Invoice saved in: {file_name}")

    except Exception as e:
        print_horizintal_line_small()
        print(f"❌ Something went wrong in invoice: {e}")


################################################################################
def add_new_product_to_file(product_name, product_company, product_price, product_qty, product_country):
    """
    function to add new product to the file.
    """
    try:
        # opening the file in append mode will not override and it will add new line
        # if file not exist then it will create new file
        file = open("data/products.txt", "a")
        file.write(f"{product_name},{product_company},{product_price},{product_qty},{product_country}\n")
        file.close()
        print_horizintal_line_small()

    except Exception as e:
        print_horizintal_line_small()
        print(f"❌ Something went wrong: {e}")