def delete(list_, index=None):
    if index is None:
        list_ = list_[:-1]
    elif index > 0 or index < -1:
        list_ = list_[:index] + list_[index+1:]
    elif index == 0:
        list_ = list_[index + 1:]
    else:
        list_ = list_[:index]  # если индекс -1
    return list_


print(delete([0, 1, 2], index=0))  # [1, 2]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]
# для сохранения последней строки
