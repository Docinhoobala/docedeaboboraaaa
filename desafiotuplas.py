estoque = (
     ('mouse lG Tech', 10),
     ('Mic Hyper X', 5),
     ('Acer Nitro 5', 3),
     ('Wedcam HD', 0)
)

print('produtos com menos de 5 unidades')
#percorendo a tupla
for i in estoque:
    if i[1] < 5:
        print(f'- {i[0]}')

print('produtos esgotados')
for i in estoque:
    if i[1] == 0:
        print(f'- {i[0]}')

soma = 0
#faça um for para percorer os nmeros da tupla e em seguida some os numeros a variavel soma

print(f'O numeto total de itens é: {soma}')
for i in estoque:
    soma += i[1]