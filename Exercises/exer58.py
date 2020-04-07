from time import sleep
from random import randint
print('Sou seu computador...')
sleep(0.7)
print('Acabei de pensar em um número entre 0 e 10')
sleep(0.6)
print('Será que você consegue adivinhar qual é?')
x = randint(0, 10)
palpite = int(input('Qual é seu palpite? '))
cont = 0
while palpite != x:
    if palpite < x:
        print('Mais... Tente mais uma vez')
        palpite = int(input('Qual é seu palpite? '))
        cont += 1
    if palpite > x:
        print('Menos... Tente mais uma vez')
        palpite = int(input('Qual é seu palpite? '))
        cont += 1
print('Você tentou {} vezes e acertou! O número era {}' .format(cont + 1, x))