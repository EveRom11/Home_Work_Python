# Реализуйте алгоритм перемешивания списка.

def mix(array):
    import random as rm
    ar_mix=[None]*len(array)
    for i in range(len(array)):
        ind=rm.randint(0, len(array)-1)
        if ar_mix[ind]==None:
            ar_mix[ind]=array[i]
        else:
            x=ar_mix.index(None)
            ar_mix[x]=array[i]
    return ar_mix

# mas=[1,2,3,4,5,6,7,8,9,10]
mas=[11,12,13,14,15,16,17,18,19,20]
print(mix(mas))