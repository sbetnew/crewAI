# 🚀 Projeto CrewAI - Gerador de Conteúdo Automatizado

<div align="center">
  <img src="https://media.licdn.com/dms/image/v2/D4D12AQE88NdPMRH-Lw/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1715302082269?e=2147483647&v=beta&t=qzfY-i7VTiIIOpaQ8kDHApida_Nj3mu62C_c4licItw" width="300" alt="CrewAI Logo">
</div>

## 📋 Visão Geral

Sistema automatizado para geração de conteúdo em português utilizando agentes de IA especializados:

- **Pesquisador**: Coleta dados e informações atualizadas
- **Redator**: Produz artigos completos e engajadores

## Funcionalidades

- Geração de conteúdo 100% em português
- Fluxo automatizado pesquisa → redação
- Saída formatada em Markdown
- Configuração simplificada

## Pré-requisitos

- Python 3.13
- Conta no [Groq Cloud](https://console.groq.com/)

## Instalação
Versão 12
https://www.python.org/ftp/python/3.12.9/python-3.12.9-amd64.exe

- Clone do código git
  >> git clone https://github.com/sbetnew/crewAI.git 

- Criar Pasta Output
- Renomear .env.example   para   .env
- Incluir a Chave GROQ no .env (https://console.groq.com/)
- CTRL + J (Abrir terminal)
- Verificar Versão Python:   >> python --version    //Precisa ser a versão 3.12

- Configure ambiente virtual
  >>  py -3.12 -m venv venv
  >>  venv\Scripts\activate

- Instalar os Requerimentos
  >> pip install -r requirements.txt

- Executar o main.py

<hr>


<div align="center"> <sub>Criado com ❤️ por Sabrina Bet<br>https://www.linkedin.com/in/sabrina-bet/</sub> </div>

<hr>

**Como Funciona na Prática:**

1. O pesquisador coleta informações sobre IA e mercado de trabalho
1. O redator recebe esses dados e escreve um artigo completo
1. Todo o conteúdo é gerado em português brasileiro
1. O resultado final é exibido no console e salvo em um arquivo .md

Vamos analisar cada parte:

**1. Configuração Inicial**

- Importa as bibliotecas necessárias
- load_dotenv() carrega variáveis de ambiente do arquivo .env (onde deve estar sua API key do Groq)

**2. Configuração do Modelo de Linguagem**

- Configura o modelo Llama 3 da Groq
- temperature=0.6 controla a criatividade (valores mais altos = mais criativo)

**3. Criação dos Agentes**

- Define dois agentes especializados:
  - **Pesquisador**: Busca informações em português
  - **Redator**: Escreve artigos em português
- Cada agente tem:
  - Um papel (role)
  - Um objetivo (goal) específico
  - Um histórico (backstory) que direciona seu comportamento
  - verbose=True para mostrar logs detalhados

**4. Criação das Tarefas**

- Define duas tarefas encadeadas:
  - Pesquisa sobre IA no mercado de trabalho
  - Redação do artigo baseado na pesquisa
- context=[pesquisa\_task] faz a tarefa de redação usar o resultado da pesquisa

**5. Criação da Equipe (Crew)**

- Organiza os agentes e tarefas em um fluxo de trabalho
- verbose=True mostra detalhes da execução

**6. Execução**

- Executa o fluxo completo
- Imprime o resultado ou trata erros
