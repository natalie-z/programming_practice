#1.	Дан список чисел.
# Определите, сколько в этом списке элементов, которые больше двух своих соседей,
# и выведите количество таких элементов. Крайние элементы списка никогда не учитываются,
# поскольку у них недостаточно соседей.  (pythontutor.ru, занятие 7, «Больше своих соседей»)

a=[int(s) for s in input().split()]

def biggerthanneib(a):
    '''bigger than neighbours выводит количество элементов в списке, которые больше двух сових соседей.
     (исключая первый и последний элемент) '''
    n=0
    for i in range(len(a)-2):
        if a[i]<a[i+1]>a[i+2]:
            n+=1

    return n
print(biggerthanneib(a))

