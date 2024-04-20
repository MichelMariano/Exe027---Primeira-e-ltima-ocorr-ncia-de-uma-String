# Faça um programa que leia a frase pelo teclado e mostre:
# Quantas vezes aparce a letra 'A'
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a última vez

a = str(input('Escreva Algo: ').strip()).upper()

print(a)
print('A letra A aparece {} na frase '.format(a.count('A')))
print('A letra A apareceu a primeira vez na posição {} '.format(a.find('A')+1))
print('A letra A apareceu a última vez na posição {} '.format(a.rfind('A')+1))
