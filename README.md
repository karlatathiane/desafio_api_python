# 🐍 Validação da API The Dog API com Python

Este projeto utiliza **Python** para realizar uma validação completa dos dados retornados pela API **The Dog API**, comparando-os com os dados mockados armazenados localmente no arquivo `mock.json`.

---

## 🚀 Funcionalidades

- **Validação de estrutura:** Verifica se os campos retornados pela API estão de acordo com os esperados.
- **Comparação de valores:** Compara os dados da API com um arquivo `mock.json` contendo os valores esperados.
- **Resumo detalhado:** Exibe:
  - Total de diferenças encontradas.
  - Detalhes sobre quais campos e valores estão divergentes.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.9+**
- **Requests Library** (para requisições HTTP)
- **JSON** (para manipulação de dados)

---

## 📂 Estrutura do Projeto

📁 Projeto 
├── mock.json   
├── get.py  


---

## 🐕‍🦺 Como Usar

### Pré-requisitos
Certifique-se de que possui:
- **Python 3.9+** instalado em sua máquina.
- A biblioteca `requests` instalada:
  ```bash
  pip install requests

**Passos para rodar o script**
Clone este repositório:

bash
git clone https://github.com/karlatathiane/desafio_api_python.git
cd nome-do-repositorio
Certifique-se de que o arquivo mock.json está no mesmo diretório do script get.py.

Execute o script:

bash
python get.py

🔍 Resumo Final:
- Total de diferenças encontradas: 3

Raça: Golden Retriever
  - Campo: origin
    Esperado: Reino Unido
    Obtido: Escócia

Raça: Labrador Retriever
  - Campo: breed_group
    Esperado: Sporting
    Obtido: Working

📜 Licença
Este projeto está sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.

