arenas = [[1200, 1500, 1100, 1800,1700],
          [1000, 950, 1100, 1050, 980],
          [2000, 1900, 1950, 2100, 2200]
          ]

contador = 1

listamedias = []

for e in arenas:
    media = sum(e) / len(e)
    listamedias.append(media)

    print(f'arena {contador}: {media}')    
    contador += 1


print(f'Arena com melhor desempenho tem: {max(listamedias)}')

