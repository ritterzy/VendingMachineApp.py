

def product_list(file):
    data = []
    with open(file, 'r', encoding='utf-8') as rf:
        i = 1
        while True:
            line = rf.readline().strip().split(' ') 
            if len(line) == 1:
                break
            product = {
                'number' : int(line[0]),
                'name' : line[1],
                'price' : int(line[2]),
                'amount' : int(line[3])
            }
            data.append(product)
            i += 1
    return data


def prod_amount_minus(data, number):
    for product in data:
        if int(product['number']) == number:
            product['amount'] -= 1
            return
        else:
            continue


def write_prod_file(file, data):
    with open(file, 'w', encoding='utf-8') as wf:
        for product in data:
            wf.write(str(product['number']) + ' ')
            wf.write(str(product['name']) + ' ')
            wf.write(str(product['price']) + ' ')
            wf.write(str(product['amount']))
            wf.write('\n')
            