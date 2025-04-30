# function which read the products from the text file
def read_products_from_file():
    """
    This function which read the products from the text file and returns the list of products
    """
    # this is a list of disctionary which will store the products
    # each product will be stored in a dictionary
    products = []
    print("----------------------------------------------------")
    print("Reading Products from file")
    # opening the file in reading mode
    try:
        file = open("Data/products.txt", "r")
        # reading the file line by  and storing it in a list
        file_lines = file.readlines()  # list
        # closing file because to prevent memory leak and prevent unintentional changes to the file
        file.close()
        # iterating file line from list file_lines
        for line in file_lines:
            # stripping method removes whitespaces, \n and \t from the string
            product = line.strip()
            # splitting the string into list
            product = product.split(",")
            # creating disctionary and storting in list products
            product_dictionary = {
                "id": int(product[0]),
                "name": product[1],
                "company": product[2],
                "price": float(product[3]),
                "stock": int(product[4]),
                "country": product[5]
            }
            # appending disctionary to list products
            products.append(product_dictionary)
    except:
        print("----------------------------------------------------")
        print("< Something went wrong in reading file >")
        return 0
    # returning the list of products
    return products