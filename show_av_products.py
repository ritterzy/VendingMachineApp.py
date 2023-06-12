

def available_products(data, counter):
    data_av_products = []
    for product in data:
        if counter >= product['price'] and product['amount'] > 0:
            data_av_products.append(product)
        else:pass
    return data_av_products
        

def show_av_products(data):
    for product in data:
        if product['amount'] > 0:
            print(f'{product["number"]} - {product["name"]} : {product["price"]} - {product["amount"]} in stock')

    