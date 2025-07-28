# Itertools
# combinations - combinações, ordem não importa
# permitations - permutação, ordem importa
# product - produto, ordem importa e repete valores únicos
from itertools import combinations, permutations, product

pessoas = [
    'Vinicius', 'Gustavo', 'Eduardo', 'Lana'
]

camisetas = [
    ['Preta', 'Branca'],
    ['Masculina', 'Feminina'],
    ['P', 'M', 'G'],
    ['Algodão', 'Dry-fit']
]

print(list(combinations(pessoas, 2)))
print(list(permutations(pessoas, 2)))
print(*list(product(*camisetas)), sep='\n')