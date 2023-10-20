import json

nome_antigo = 'nacional'
nome_novo = 'kkkkkkkkk'

with open('playlist_tst.json', 'r') as arquivo:

    dados = json.load(arquivo)

if nome_antigo in dados:

    dados[nome_novo] = dados[nome_antigo]

    del dados[nome_antigo]        

    with open('playlist_tst.json', 'w') as arquivo:

        json.dump(dados, arquivo, indent=4)

else:


    print('Playlist inexistente . Por favor, verifique a sua ortografia .')  