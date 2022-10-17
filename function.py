#def identificacao (nome,idade):
    #print('Olá,', nome, '\nVocê é jovem, tem apenas', idade, 'anos!')

#identificacao('João Paulo', 36)

def maior (x, y):
    if x < y:
        print('O maior é', y)
    elif x == y:
        print('Os números sao iguais')
    else:
        print('O maior número é', x)

maior(16, 21)

def pitagoras (cat1, cat2, hip):
    if hip =='?':
        hip = (cat1**2+cat2**2)**(1/2)
        print('A hipotenusa é', hip)
    elif cat1 == '?':
        cat1 = (hip**2-cat2**2)**(1/2)
        print('O cateto é', cat1)
    elif cat2 == '?':
        cat2 = (hip**2-cat1**2)**(1/2)
        print('O cateto é', cat2)

pitagoras(6, 8, '?')