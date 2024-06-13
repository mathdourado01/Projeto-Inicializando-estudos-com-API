import requests
import json
url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)
print(response)

if response.status_code == 200:
    dados_json = response.json()
    dados_restaurante = {}
    for item in dados_json:
        nome = item['Company']
        if nome not in dados_restaurante:
            dados_restaurante[nome] = [] 

        dados_restaurante[nome].append({"item":'Item',
                                        "price":'price',
                                        "description":'description'
                                        })
    
    print(dados_json)
else:
    print(f"Erro foi {response.status_code}")

for nome,dados in dados_restaurante.items():
    nome_do_arquivo = f"{nome}.json"
    with open(nome_do_arquivo,'w') as arquivo_restaurante:
        json.dump(dados,arquivo_restaurante,indent=4)

