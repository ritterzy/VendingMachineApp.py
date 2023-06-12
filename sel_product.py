from show_av_products import show_av_products, available_products
from VM_prod_list import product_list
class SelProductErr(Exception):
    pass


def select_product(data, counter):
    if int(counter) == 0:
        print("Your balance is 0!")
        return
    elif len(data) == 0:
        print("You cannot buy any product for your current balance!")
        return
    else: show_av_products(data)
    while True:
        try:
            a = int(input("Select product by it's number: "))
            for product in data:
                if a == int(product['number']):
                    print(f'Please get your {product["name"]}')
                    return [int(product['price']), product['number']]
            else: raise SelProductErr
        except:
            print("Please select correct product by its number!")


