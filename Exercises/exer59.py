value_one = int(input('Primeiro valor: '))
value_two = int(input('Segundo valor: '))
i = 1
while i < 5:
    print('[1] Soma')
    print('[2] Multiplicador')
    print('[3] Maior')
    print('[4] Novos números')
    print('[5] Sair do programa')
    option = int(input('Qual é sua opção? '))
    if option == 1:
        print('A soma entre {} e {} é {}' .format(value_one, value_two, value_one + value_two))
    if option == 2:
        print('O produto entre {} e {} é {}' .format(value_one, value_two, value_one * value_two))
    if option == 3:
        if value_one > value_two:
            print('{} é maior que {}' .format(value_one, value_two))
        if value_two > value_one:
            print('{} é maior que {}' .format(value_two, value_one))
    if option == 4:
        print('Informe os números novamente')
        value_one = int(input('Primeiro valor: '))
        value_two = int(input('Segundo valor: '))
    if option > 5:
        print('Opção inválida')
    if option == 5:
        print('Terminou')