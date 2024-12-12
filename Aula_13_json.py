import json

dados_cadastrais = {
    "pablo":{
        "sobrenome":"Abreu",
        "idade":30,
        "profissão":"Engenheiro",
        "empresa": "MBB"

    }
}

with open('dados.json','w') as meu_arquivo:
    json.dump(dados_cadastrais, meu_arquivo)

with open('dados.json','r') as arquivo:
    print(json.load(arquivo))
