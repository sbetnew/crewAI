import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew
from langchain_groq import ChatGroq

# 1. Configuração inicial - carregar variaveis do ambiente
load_dotenv()

# 2. Configurar o LLM com instrução de idioma
llm = ChatGroq(
    model="groq/llama3-70b-8192",
    groq_api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.6    # 0 a 1 indica o grau de alucinação
)

# 3. Criar Agentes com instruções em português
pesquisador = Agent(
    role="Pesquisador Especialista",
    goal="Realizar pesquisas detalhadas sobre tópicos solicitados em português",
    backstory="""Você é um pesquisador brasileiro experiente com habilidade para encontrar informações 
    relevantes e atualizadas sobre qualquer tópico. Sempre produz conteúdo em português brasileiro.""",
    verbose=True,
    llm=llm,
    allow_delegation=False
)

redator = Agent(
    role="Redator Criativo",
    goal="Escrever artigos engajadores e informativos para blog em português",
    backstory="""Você é um redator brasileiro premiado com anos de experiência em criação de conteúdo
    digital em português que cativa a audiência.""",
    verbose=True,
    llm=llm,
    allow_delegation=False
)

# 4. Criar Tarefas com instruções explícitas de idioma
pesquisa_task = Task(
    description="""Realize uma pesquisa detalhada em português sobre os impactos da IA no mercado de trabalho em 2024.
    Inclua estatísticas recentes e tendências. IMPORTANTE: Todo conteúdo deve ser em português brasileiro.""",
    expected_output="Um relatório em português com 5-6 parágrafos contendo fatos e dados relevantes.",
    agent=pesquisador,
    output_file="output/pesquisa_ia.md"  # Opcional: salva em arquivo
)

redacao_task = Task(
    description="""Com base na pesquisa fornecida, escreva um artigo para blog em português com título chamativo.
    O artigo deve ter introdução, desenvolvimento e conclusão, em linguagem acessível. 
    IMPORTANTE: Todo conteúdo deve ser em português brasileiro coloquial.""",
    expected_output="Artigo completo em português com pelo menos 3 parágrafos e um título criativo.",
    agent=redator,
    output_file="output/redacao_ia.md",
    context=[pesquisa_task]  # Recebe o resultado da pesquisa
)

# 5. Criar a Equipe (Crew)
equipe_blog = Crew(
    agents=[pesquisador, redator],
    tasks=[pesquisa_task, redacao_task],
    verbose=True  #habilitar DEBUG
)

# 6. Executar
try:
    print("⏳ Processando conteúdo em português...")
    resultado = equipe_blog.kickoff()
    
    print("\n📝 Conteúdo em Português Gerado:")
    print(resultado)
    
except Exception as e:
    print(f"\n❌ Erro: {e}")


# Como Funciona:

# Gerador de conteúdos de Blog
# Dois Agentes Especializados:
# - Pesquisador: Busca informações atualizadas
# - Redator: Transforma os dados em conteúdo atraente

# Fluxo Automatizado:
# A pesquisa é feita primeiro
# O resultado é passado automaticamente para o redator
# Gera um artigo completo pronto para publicação

# Personalização Fácil:
# Basta mudar o tópico na pesquisa_task para gerar conteúdo sobre outros assuntos

#ATIVIDADE:
# Adicione um terceiro agente Tradutor (saída do redator e traduzir para inglês)
# Salvar a saída em um arquivo .md

# LLM - Crew - Agents - Tasks