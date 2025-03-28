Este código cria um sistema automatizado para pesquisa e redação de artigos em português usando inteligência artificial. 
Sabrina Bet

**Como Funciona na Prática:**
1. O pesquisador coleta informações sobre IA e mercado de trabalho
1. O redator recebe esses dados e escreve um artigo completo
1. Todo o conteúdo é gerado em português brasileiro
1. O resultado final é exibido no console e salvo em um arquivo .md


Vamos analisar cada parte:

**1. Configuração Inicial**
- Importa as bibliotecas necessárias
- load\_dotenv() carrega variáveis de ambiente do arquivo .env (onde deve estar sua API key do Groq)

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