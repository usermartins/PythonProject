from time import sleep
print('Super Progressão Aritmética')
sleep(0.8)
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
c = 0
p = primeiro_termo
mais = 9
total = 0
while mais != 0:
    total += mais
    while c <= total:
        print('{} -' .format(p), end=' ')
        p += razao
        c += 1
    print('Pausa')
    mais = int(input('Quer adicionar mais quantos termos? '))
print('Fim. Finalizado com {} termos' .format(total))
