#4.	Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
# Элементы нужно выводить в том порядке, в котором они встречаются в списке. (pythontutor.ru, занятие 7, «Уникальные элементы»)

a=input().split()
def uniq(a):
    '''создает новую последовательность, включающие лишь те элементы,
     что встречались в исходной последовательности один раз'''
    uniq_a=[]
    for symbol in a:
        if a.count(symbol) == 1:
            uniq_a.append(symbol)
    print(uniq_a)

uniq(a)