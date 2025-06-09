# --------------------------
# append() - adiciona um item ao final da lista
# --------------------------
lista = []  # Cria uma lista vazia
lista.append(1)          # Adiciona o número 1 -> lista = [1]
lista.append("Python")   # Adiciona a string "Python" -> lista = [1, "Python"]
lista.append([40, 20, 30]) # Adiciona uma lista dentro da lista -> lista = [1, "Python", [40, 20, 30]]
print(lista)  # Mostra: [1, 'Python', [40, 20, 30]]

# --------------------------
# clear() - remove todos os itens da lista, deixando ela vazia
# --------------------------
lista = [1, "Python", [40,30, 20]]  # Cria uma lista com 3 itens
print(lista)  # Mostra: [1, 'Python', [40, 30, 20]]
lista.clear()  # Remove tudo da lista
print(lista)  # Mostra: []

# --------------------------
# copy() - cria uma cópia da lista original, independente da original
# --------------------------
lista = [1, "Python", [40,30, 20]]
l2 = lista.copy()  # Faz uma cópia nova da lista (memórias diferentes)
print(lista)  # Lista original
print(id(l2), id(lista))  # Mostra que os endereços na memória são diferentes

# --------------------------
# count() - conta quantas vezes um item aparece na lista
# --------------------------
cores = ['vermelho', 'azul', 'roxo', 'rosa', 'vermelho', 'vermelho', 'roxo']
print(cores.count("vermelho"))  # 3 vezes
print(cores.count("azul"))       # 1 vez
print(cores.count("roxo"))       # 2 vezes
print(cores.count("rosa"))       # 1 vez
print(cores.count("verde"))      # 0 vezes (não existe)

# --------------------------
# extend() - junta elementos de outra lista ao final da lista original
# --------------------------
linguagens = ["python", "js", "c"]
print(linguagens)  # ['python', 'js', 'c']
linguagens.extend(["java", "angular", "c"])
print(linguagens)  # ['python', 'js', 'c', 'java', 'angular', 'c']

# --------------------------
# index() - retorna o índice da primeira ocorrência de um valor
# --------------------------
linguagens = ["python", "js", "c"]
print(linguagens.index('js'))     # 1
print(linguagens.index('c'))      # 2
print(linguagens.index('python')) # 0

# --------------------------
# pop() - remove e retorna um elemento da lista (último por padrão)
# --------------------------
linguagens2 = ["python", "js", "c", "php"]
print(linguagens2.pop())     # 'php'
print(linguagens2.pop())     # 'c'
print(linguagens2.pop())     # 'js'
print(linguagens2.pop(0))    # 'python'

# --------------------------
# remove() - remove a primeira ocorrência do valor informado na lista
# --------------------------
linguagens2 = ["python", "js", "c", "php"]
linguagens2.remove("c")
print(linguagens2)  # ['python', 'js', 'php']

# --------------------------
# reverse() - inverte a ordem dos elementos da lista original
# --------------------------
linguagens2 = ["python", "js", "c", "php"]
linguagens2.reverse()
print(linguagens2)  # ['php', 'c', 'js', 'python']

# --------------------------
# sort() - organiza a lista em ordem alfabética (padrão)
# sort(reverse=True) - ordem reversa
# sort(key=lambda x: len(x)) - ordena pelo tamanho das strings
# --------------------------
linguagens2 = ["python", "js", "c", "php"]
linguagens2.sort()
print("Ordem alfabética:", linguagens2)  # ['c', 'js', 'php', 'python']
linguagens2.sort(reverse=True)
print("Ordem alfabética reversa:", linguagens2)  # ['python', 'php', 'js', 'c']
linguagens2.sort(key=lambda x: len(x))
print("Por tamanho (crescente):", linguagens2)  # ['c', 'js', 'php', 'python']
linguagens2.sort(key=lambda x: len(x), reverse=True)
print("Por tamanho (decrescente):", linguagens2)  # ['python', 'php', 'js', 'c']

# --------------------------
# len() - retorna o número de elementos na lista
# --------------------------
linguagens2 = ["python", "js", "c", "php"]
print("Tamanho:", len(linguagens2))  # 4

# --------------------------
# sorted() - retorna uma nova lista ordenada (não altera a original)
# --------------------------
linguagens2 = ["python", "js", "c", "php"]
lista_ordenada_cresc = sorted(linguagens2, key=lambda x: len(x))
print("Ordenado do menor para o maior:", lista_ordenada_cresc)
lista_ordenada_decresc = sorted(linguagens2, key=lambda x: len(x), reverse=True)
print("Ordenado do maior para o menor:", lista_ordenada_decresc)
print("Lista original:", linguagens2)
