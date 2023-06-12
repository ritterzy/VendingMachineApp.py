import csv      #!imports csv file with banknotes

class ErrorBanknote(Exception):  #? custom error
    pass


def banknotes_data(file):
    data = [('denomination', 'amount')]
    with open(file, newline= '') as rf:
        reader = csv.DictReader(rf, delimiter = ';')
        for row in reader:
            banknote = [int(row['denomination']), int(row['amount'])]
            data.append(banknote)
    return data


def check_banknote(file):  #? checking banknote function by our banknote list file
    banknotes = []
    with open(file, newline = '') as rf:
        reader = csv.DictReader(rf, delimiter= ';')
        for row in reader:
            banknotes.append(int(row['denomination']))
        return banknotes



def insert_banknote(list): #! insert banknote function returns our banknote
    while True:
        print(f'REMINDER: VM only accept {list} UZS valutes!')   
        try:
            banknote = int(input('Enter your banknote: '))
            if not(banknote in list):
                raise ErrorBanknote('Please enter correct banknote!')
        except:
            print('Please enter correct banknote!')

        else:
            return int(banknote)

def print_balance(balance):
    print(f'Your balance {balance} UZS!')   #! prints our balance



def banknote_amount_plus(data, denomination):
    for banknote in data:
        if banknote[0] == denomination:
            banknote[1] += 1
            return
        else:
            continue


def banknote_write(file, data):
    with open(file, 'w', newline = '') as wf:
        writer = csv.writer(wf, delimiter = ';')
        writer.writerows(data)
    return
    