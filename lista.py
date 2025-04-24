# 1. Crie uma lista com os nomes de 5 objetos:
objetos = ["lampada", "mesa", "bolsa", "garrafa", "mouse"]
print("lista de nomes criada")
print("-"*25)

# 2. Adicione mais um objeto ao final da lista:
objetos.append("lapis")
print("objeto adicionado")
print("-"*25)

# 3. Acesse o objeto que está na 2a posição:
segunda = objetos[1]
print("segundo objeto anotado e é:", segunda)
print("-"*25)

# 4. Remova um objeto da lista:
objetos.remove("bolsa")
print("objeto removido")
print("-"*25)

# 5. Exiba o tamanho da lista:
for n in range(5):
    print(n)
print("-"*25)

# 6. Mostre todos os itens com um laço for:
for objeto in objetos:
    print(objeto)
print("-"*25)

# 7. Verifique se 'cadeira' está na lista. Se sim remova-a, senão adicione:
if"cadeira" in objetos:
    objetos.remove("cadeira")
    print("objeto removido")
    print("-"*25)
else:
    objetos.append("cadeira")
    print("objeto Adicionado")
    print("-" * 25)


# 8. Ordene a lista em ordem alfabética:
objetos.sort()
print("objeto em ordem")
print("-"*25)

# 9. Exiba o primeiro e o último objeto:
primeiro = objetos[0]
ultimo = objetos[-1]
print("o primeiro objeto é:",primeiro, "o segundo objeto é:", ultimo)
print("-"*25)

# 10. Limpe toda a lista:
objetos.clear()
print("todos os objetos estão removidos")
print("-"*25)