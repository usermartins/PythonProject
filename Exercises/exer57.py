sexo = str(input('Qual o seu sexo? M/F: ')).strip().upper()[0]
while sexo not in 'FM':
    sexo = str(input('Dado inválido. Informe seu sexo: ')).strip().upper()[0]
print('Sexo {} cadastrado' .format(sexo))
        