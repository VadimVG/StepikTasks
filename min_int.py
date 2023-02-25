# Учитывая список цифр , верните наименьшее число
# , которое можно составить из этих цифр, используя цифры только один раз (игнорируя дубликаты)

import itertools

def min_value(digits):
    s=set(digits)
    pre_total=set(itertools.permutations(s))
    total=[]
    for v in pre_total:
        x=''
        for j in v:
            x+=str(j)
        total.append(int(x))
    return min(total)



if __name__=='__main__':
    print(min_value([1, 3, 1]))
    print(min_value([4, 7, 5, 7]))
    print(min_value([4, 8, 1, 4]))






























































