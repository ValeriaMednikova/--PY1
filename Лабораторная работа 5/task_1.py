from pprint import pprint
list_ = []
for num in range(16):
    dict_ = dict({'bin': bin(num), 'dec': num, 'hex': hex(num), 'oct': oct(num)})
    list_.append(dict_)

pprint(list_)
# для сохранения последней строки
