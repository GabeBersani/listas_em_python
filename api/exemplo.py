import requests

def exemplo_cep():

    cep = "16708134"
    url = f"http://viacep.com.br/ws/{cep}/json"
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json() #dados do cep
        print(f"Logradouro: {dados['logradouro']}\n") #escolhemos o campo que qro e colocamos as { e os [
        print(f"Bairro: {dados['bairro']}\n")
        print(f"Regiao: {dados['regiao']}\n")
        print(f"Localidade: {dados['localidade']}\n")
        print(f"ddd: {dados['ddd']}\n")
        print(f"Estado: {dados['estado']}\n")

    else:
        print(f"Erro: {response.status_code}")


def exemplo_get():
    url = f"https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    if response.status_code == 200:
        dados_postagem_get = response.json()
        print(f"ID: {dados_postagem_get['id']}\n")
        print(f"Titulo: {dados_postagem_get['title']}\n")
        print(f"Conteudo: {dados_postagem_get['body']}\n")
    else:
        print(f"Erro: {response.status_code}")


def exemplo_get_com_parametro(id): #colocamos o parametro d id para mostrar o resultado no final dps / mais facil de procurar
    url = f"https://jsonplaceholder.typicode.com/posts/{id}" #id do conteudo
    response = requests.get(url)

    if response.status_code == 200:
        dados_postagem_get = response.json()
        print(f"Titulo: {dados_postagem_get['title']}\n")
        print(f"Conteudo: {dados_postagem_get['body']}\n")
    else:
        print(f"Erro: {response.status_code}")
# exemplo_get_com_parametro(6) - para ter o resultado colocamos o id


def exemplo_post():
    url = "https://jsonplaceholder.typicode.com/posts"
    nova_postagem = {
        #criamos um novo post:
        "title": "Novo Titulo",
        "body": "Novo conteudo",
        "userId": 1 #user que tem disponivel, por exemplo vai do 1 ao 10
    }
    response = requests.post(url, json=nova_postagem)
    if response.status_code == 201: #quando cria alguma coisa vai no 201
        dados_postagem_get = response.json()
        print(f"Titulo: {dados_postagem_get['title']}\n")
        print(f"Conteudo: {dados_postagem_get['body']}\n")
    else:
        print(f"Erro: {response.status_code}")

# exemplo_post() -- para testar


def exemplo_put(id):
    url = f"https://jsonplaceholder.typicode.com/posts/{id}"
    #vamos reformular/atualizar ele (igual do banco

    nova_postagem = {
        "id": id,
        "title": "Novo Titulo Atualizado",
        "body": "Novo conteudo Atualizado",
        "userId": 1
    }
    #fazer um get para mostrar antes e dps de atualizar
    antes = requests.get(url) #antes
    response = requests.put(url, json=nova_postagem) #nova

    if response.status_code == 200:

        if antes.status_code == 200:
            dados_antes = antes.json()
            print(f"Titulo Antigo: {dados_antes['title']}\n")
            print(f"Conteudo Antigo: {dados_antes['body']}\n")
        else:
            print(f"Erro: {response.status_code}")

        dados_postagem_get = response.json()
        print(f"Titulo: {dados_postagem_get['title']}\n")
        print(f"Conteudo: {dados_postagem_get['body']}\n")
    else:
        print(f"Erro: {response.status_code}")

exemplo_put(1)


