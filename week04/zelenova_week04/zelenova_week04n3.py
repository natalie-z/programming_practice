#3.	Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. (pythontutor.ru, занятие 7, «Количество совпадающих пар»)

a=[int(s) for s in input().split()]
def pairs(a):
    '''pairs считает количество пар элементов равных друг другу'''
    p=0
    for i in range (len(a)-1):
        b=a[i+1:]
        n=b.count(a[i])
        p+=n
    print('элементы списка образуют',p,'пар')
pairs(a)
