import requests
import json

# Função para validar a estrutura dos campos e seus tipos
def validar_estrutura(dados, campos_esperados):
    for item in dados:
        for campo, tipo_esperado in campos_esperados.items():
            if campo not in item:
                print(f"❌ Campo ausente: {campo}")
                continue
            if not isinstance(item[campo], tipo_esperado) and item[campo] is not None:
                print(f"❌ Tipo inválido para '{campo}'. Esperado: {tipo_esperado}, Obtido: {type(item[campo])}")

# Função para comparar ponto a ponto os valores entre API e mock
def comparar_dados(api_data, mock_data):
    total_diferencas = 0  # Contador de diferenças
    resumo_diferencas = []  # Lista para armazenar as diferenças detectadas

    for mock_breed in mock_data:
        # Verificar se 'name' existe no mock
        if 'name' not in mock_breed:
            print(f"❌ Raça no mock não possui a chave 'name': {mock_breed}")
            continue

        # Encontrar a raça correspondente na API pelo campo "name"
        api_breed = next((breed for breed in api_data if 'name' in breed and breed["name"] == mock_breed["name"]), None)

        if not api_breed:
            print(f"❌ Raça '{mock_breed['name']}' NÃO encontrada na API!")
            resumo_diferencas.append({
                "Raça": mock_breed["name"],
                "Diferenças": ["Raça não encontrada na API"]
            })
            continue

        # Comparar cada campo
        diferencas_para_raca = []
        for campo, valor_esperado in mock_breed.items():
            valor_obtido = api_breed.get(campo)
            if valor_obtido != valor_esperado:
                diferencas_para_raca.append({
                    "Campo": campo,
                    "Esperado": valor_esperado,
                    "Obtido": valor_obtido
                })
                total_diferencas += 1

        if diferencas_para_raca:
            resumo_diferencas.append({
                "Raça": mock_breed["name"],
                "Diferenças": diferencas_para_raca
            })

    # Exibir resumo final das diferenças
    print("\n🔍 Resumo Final:")
    print(f"- Total de diferenças encontradas: {total_diferencas}")
    if resumo_diferencas:
        for raca in resumo_diferencas:
            print(f"\nRaça: {raca['Raça']}")
            for dif in raca["Diferenças"]:
                if isinstance(dif, str):  # Diferença simples (ex.: "Raça não encontrada")
                    print(f"  - {dif}")
                else:
                    print(f"  - Campo: {dif['Campo']}")
                    print(f"    Esperado: {dif['Esperado']}")
                    print(f"    Obtido: {dif['Obtido']}")
    else:
        print("✅ Nenhuma diferença encontrada nos dados.")

# Executando o script
if __name__ == "__main__":
    # Fazer requisição para a API
    url = "https://api.thedogapi.com/v1/breeds"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"❌ Erro na API! Código de status: {response.status_code}")
        exit()

    api_data = response.json()

    # Carregar o mock
    with open("breeds_mock.json", "r", encoding="utf-8") as file:
        mock_data = json.load(file)

    # Validar estrutura dos dados
    print("\n✔ Validando estrutura dos campos:")
    campos_esperados = {
        "id": int,
        "name": str,
        "bred_for": (str, type(None)),
        "breed_group": (str, type(None)),
        "life_span": str,
        "temperament": (str, type(None)),
        "origin": (str, type(None)),
        "weight": dict,
        "height": dict,
        "reference_image_id": (str, type(None))
    }
    validar_estrutura(api_data, campos_esperados)

    # Comparar ponto a ponto
    print("\n🔎 Comparando dados entre API e Mock:")
    comparar_dados(api_data, mock_data)
