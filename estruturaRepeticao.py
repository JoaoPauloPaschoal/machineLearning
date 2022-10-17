soma = 0
cont = 0

for c in range (1, 4):
    num= int(input('Digite o {}o valor: '.format(c)))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1 
    print('Você informou {} números pares e a soma deles é igual a {}'.format(cont, soma))