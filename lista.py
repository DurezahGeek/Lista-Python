#======================================================================================================================
# Em Python, lista é uma estrutura de dados usada para armazenar múltiplos valores em uma única variável. 
# Ela é mutável, ou seja, pode ser alterada depois de criada (podemos adicionar, remover ou modificar elementos). 
# As listas são definidas usando colchetes [].
#======================================================================================================================

# Cria uma lista com três frutas
frutas = ["laranja", "banana", "morango"]
# Acesso direto: usa índices positivos para acessar os elementos da esquerda para a direita
print(frutas[0]) # Mostra: laranja (primeiro item)
# Acesso negativo: usa índices negativos para acessar os elementos da direita para a esquerda
print(frutas[-1])# Mostra: morango (último item)
print(frutas)  

# Esvazia a lista anterior
frutas = []
print(frutas)  

# Cria uma lista com cada letra da palavra "python"
letras = list("python")
print(letras)  

# Cria uma lista de números de 0 a 9
numeros = list(range(10))
print(numeros)  

# Cria uma lista com informações sobre um carro:
# [marca, modelo, valor_tabela_fipe, ano_fabricacao, km_rodados, cidade, disponivel]
carro = ["FIAT", "UNO", 8000, 1998, 122000, "Rio de Janeiro", True]
print(carro)  

#======================================================================================================================
#Em Python, lista alinhada (também chamada de lista aninhada) é uma lista dentro de outra lista.
#Ela permite representar estruturas em formato de tabela ou matriz, por exemplo:

# Lista aninhada (alinhada)
matriz = [
    [1, 2, "C"],
    [4, 5, 6],
    [7, "H", 9]
]
print(matriz[0])     # Mostra: [1, 2, 'C'] (primeira linha)
print(matriz[0][1])  # Mostra: 2 (linha 0, coluna 1)
print(matriz[-1])     # Mostra: [7, 'H', 9] (última linha)
print(matriz[0][0])  # Mostra: 1 (linha 0, coluna 0)
print(matriz[0][-1])  # Mostra: 'C' (linha 0, coluna -1)
print(matriz[-1][-1])  # Mostra: 9 (linha -1, coluna -1)
#======================================================================================================================

#======================================================================================================================
#Fatiamento em Python é uma forma de acessar partes (fatias) de uma lista, 
# string ou tupla, usando a notação [início:fim:passo]

# Índices:           0    1    2    3    4    5
letras =           ["C", "A", "V", "A", "L", "O"] 
# Índices Negativo: -6   -5   -4   -3   -2   -1

print(letras[1:4])      # ['A', 'V', 'A'] - do índice 1 até o 3 (4 não inclui)
print(letras[:1:4])     # ['C'] - do início até o índice 0, pulando de 4 em 4 (pega só o índice 0)
print(letras[:5:3])     # ['C', 'A'] - do início até o índice 4 (5 não inclui), pulando de 3 em 3 (índices 0 e 3)
print(letras[:3])       # ['C', 'A', 'V'] - do início até o índice 2 (3 não inclui)
print(letras[::2])      # ['C', 'V', 'L'] - da lista toda, pulando de 2 em 2 (índices 0, 2, 4)
print(letras[::-1])     # ['O', 'L', 'A', 'V', 'A', 'C'] - lista invertida
print(letras[0:3:2])    # ['C', 'V'] - do índice 0 até 2, pulando de 2 em 2 (3 não inclui)
print(letras[0:-4:2])   # ['C'] - do índice 0 até o -4 (2 não inclui), pulando de 2 em 2 (apenas índice 0)
print(letras[5:0:-2])   # ['O', 'A', 'A'] - do índice 5 até o 1 (0 não inclui), pulando de 2 em 2 (índices 5, 3, 1)
print(letras[-1:-3:-2]) # ['O'] - do índice -1 até o -2 (não inclui), pulando de 2 em 2 (apenas índice -1)
print(letras[::])       # ['C', 'A', 'V', 'A', 'L', 'O'] - lista inteira
print(letras[:])        # ['C', 'A', 'V', 'A', 'L', 'O'] - lista inteira

#======================================================================================================================
# Lista de frutas
frutas = ["maçã", "banana", "laranja"]

# ------------------------------
# EXEMPLO 1: Iterando com for
# ------------------------------
# Percorre cada fruta da lista e imprime o valor

for fruta in frutas:
    print(fruta)  # Saída: maçã, depois banana, depois laranja

# ------------------------------
# EXEMPLO 2: Iterando com enumerate()
# ------------------------------
# enumerate() devolve o índice (posição) e o valor (fruta) ao mesmo tempo

for indice, fruta in enumerate(frutas):
    print(indice, fruta)  
    # Saída:
    # 0 maçã
    # 1 banana
    # 2 laranja


# ------------------------------
# EXEMPLO 3: enumerate() começando do 1 (índice personalizado)
# ------------------------------
for indice, fruta in enumerate(frutas, start=1):
    print(indice, fruta)
    # Saída:
    # 1 maçã
    # 2 banana
    # 3 laranja

#======================================================================================================================
# Compreensão de listas é uma forma rápida e compacta de criar listas usando for e if em uma linha só.

# ----------------------------
# FILTRO VERSÃO 1 - Usando append()
# ----------------------------

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # Lista de números
pares = []  # Lista vazia para guardar os números pares

for numero in numeros:       # Para cada número na lista "numeros"
    if numero % 2 == 0:      # Verifica se o número é par (divisível por 2)
        pares.append(numero) # Se for par, adiciona na lista "pares"

print(pares)  # Saída: [2, 4, 6, 8]


# ----------------------------
# FILTRO VERSÃO 2 - Compreensão de lista (forma resumida)
# ----------------------------

# Mesma lógica acima, mas tudo em uma linha:
pares = [numero for numero in numeros if numero % 2 == 0]

print(pares)  # Saída: [2, 4, 6, 8]

# Explicando a linha acima:
# [numero      → o valor que queremos guardar
#  for numero  → percorre cada item na lista
#  in numeros  → origem dos dados
#  if numero % 2 == 0]  → condição para filtrar (apenas pares)
