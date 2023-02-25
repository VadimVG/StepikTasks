#Сгеренировать все комбинации строки

import itertools


def permutations(s):
    perm=set(itertools.permutations(s)) #ф-ция permutations генерирует все комбинации строки, преобразование в множество для удаления дублей
    total=[]
    for i in perm:
        total.append(''.join(i))
    return total

if __name__=='__main__':
    print(permutations('a'))
    print(permutations('ab'))
    print(permutations('aabb'))





























































