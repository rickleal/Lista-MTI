#Rick Leal

inscritos = []
vencedor = ''
tam_venc = 0

while True:
    #simple entrada em lista
    entrada = input().split()
    if entrada[0] == 'FIM':
        break
    inscritos.append(entrada[0])
    tam_nome = len(entrada[0])
    #trocaa
    if tam_nome > tam_venc:
        vencedor = entrada[0]
        tam_venc = len(vencedor)

inscritos = set(inscritos)

for nome in sorted(inscritos):
    print(nome)

print()
print('Amigo do Habay:')
print(vencedor)
