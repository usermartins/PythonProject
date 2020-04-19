from time import sleep
print('Gerador de PA')
sleep(0.7)
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
c = 0
p = primeiro_termo
print('{} ->' .format(primeiro_termo), end=' ')
while c < 9:
    p += razao
    print('{} ->' .format(p), end=' ')
    c += 1
print('Fim!')