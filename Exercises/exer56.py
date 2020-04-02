from time import sleep
print('Analisador Completo')
sleep(0.7)
quantidade_de_pessoas = int(input('Quantas pessoas você quer analisar? '))
somaidade = 0
quantidade_mulher = 0
idademaisvelho = 0
nomevelho = ''
for p in range(1, quantidade_de_pessoas + 1):
    print('{}ª Pessoa' .format(p))
    nome = str(input('Nome: '))
    idade = int(input('Idade:'))
    sexo = str(input('Sexo M/F: ')).strip().upper()
    somaidade += idade
    if p == 1 and sexo == 'M':
        idademaisvelho = idade
        nomevelho = nome
    if sexo == 'M' and idade > idademaisvelho:
        idademaisvelho = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        quantidade_mulher += 1
media = somaidade / quantidade_de_pessoas
print('A média de idade foi de {} anos' .format(media))
sleep(0.7)
print('O homem mais velho tem {} anos e se chama {}' .format(idademaisvelho, nomevelho))
sleep(0.7)
print('Ao todo há {} mulheres com menos de 20 anos' .format(quantidade_mulher))
