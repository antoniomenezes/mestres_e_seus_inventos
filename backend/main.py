# Importa a classe FastAPI do framework fastapi
from fastapi import FastAPI
# Importa a classe StaticFiles para servir arquivos estáticos
from fastapi.staticfiles import StaticFiles
# Importa o módulo os para manipulação de caminhos de arquivos
import os
# Importa o módulo sqlite3 para conexão com o banco de dados
import sqlite3

# Cria uma instância da aplicação FastAPI
app = FastAPI()

# Define o caminho absoluto da pasta de imagens (para encontrar a pasta independentemente de onde o código for executado)
PASTA_BASE = os.path.dirname(os.path.abspath(__file__))
PASTA_IMAGENS = os.path.join(PASTA_BASE, "figurinhas")
# Define o caminho para o banco de dados SQLite
DB_PATH = os.path.join(PASTA_BASE, "banco_album.sqlite")

# Configura e monta o diretório de arquivos estáticos na rota "/imgs"
app.mount("/imgs", StaticFiles(directory=PASTA_IMAGENS), name="imgs")

# Lista contendo as 50 figurinhas com seus respectivos dados e caminho das imagens
figurinhas = [
    {"id": 1, "nome": "Isaac Newton", "categoria": "Física", "imagem_url": "/imgs/01-isaac-newton.jpg", "descricao": "Fundou a mecânica clássica e a gravitação.", "brasil": False},
    {"id": 2, "nome": "Michael Faraday", "categoria": "Física", "imagem_url": "/imgs/02-michael-faraday.jpg", "descricao": "Viabilizou motores, geradores e eletrificação.", "brasil": False},
    {"id": 3, "nome": "James Clerk Maxwell", "categoria": "Física", "imagem_url": "/imgs/03-james-clerk-maxwell.jpg", "descricao": "Fundamentou eletromagnetismo e telecomunicações.", "brasil": False},
    {"id": 4, "nome": "Albert Einstein", "categoria": "Física", "imagem_url": "/imgs/04-albert-einstein.jpg", "descricao": "Reformulou espaço, tempo, energia e gravidade.", "brasil": False},
    {"id": 5, "nome": "Stephen Hawking", "categoria": "Física", "imagem_url": "/imgs/05-stephen-hawking.jpg", "descricao": "Avançou a física dos buracos negros e sua divulgação.", "brasil": False},
    {"id": 6, "nome": "Fritz Haber", "categoria": "Química", "imagem_url": "/imgs/06-fritz-haber.jpg", "descricao": "Viabilizou fertilizantes e ampliou a produção agrícola.", "brasil": False},
    {"id": 7, "nome": "Antoine Lavoisier", "categoria": "Química", "imagem_url": "/imgs/07-antoine-lavoisier.jpg", "descricao": "Estabeleceu as bases quantitativas da química.", "brasil": False},
    {"id": 8, "nome": "Dmitri Mendeleev", "categoria": "Química", "imagem_url": "/imgs/08-dmitri-mendeleev.jpg", "descricao": "Organizou os elementos na tabela periódica.", "brasil": False},
    {"id": 9, "nome": "Marie Curie", "categoria": "Química", "imagem_url": "/imgs/09-marie-curie.jpg", "descricao": "Avançou a radioatividade e suas aplicações médicas.", "brasil": False},
    {"id": 10, "nome": "John Walker", "categoria": "Química", "imagem_url": "/imgs/10-john-walker.jpg", "descricao": "Popularizou o fósforo de fricção no cotidiano.", "brasil": False},
    {"id": 11, "nome": "Galileu Galilei", "categoria": "Cálculo", "imagem_url": "/imgs/11-galileu-galilei.jpg", "descricao": "Consolidou a ciência experimental moderna.", "brasil": False},
    {"id": 12, "nome": "Leonardo Fibonacci", "categoria": "Cálculo", "imagem_url": "/imgs/12-leonardo-fibonacci.jpg", "descricao": "Popularizou o sistema numérico indo-arábico.", "brasil": False},
    {"id": 13, "nome": "Nicolau Copérnico", "categoria": "Cálculo", "imagem_url": "/imgs/13-nicolau-copernico.jpg", "descricao": "Impulsionou o heliocentrismo e a Revolução Científica.", "brasil": False},
    {"id": 14, "nome": "Katherine Johnson", "categoria": "Cálculo", "imagem_url": "/imgs/14-katherine-johnson.jpg", "descricao": "Calculou trajetórias essenciais para missões espaciais.", "brasil": False},
    {"id": 15, "nome": "Eratóstenes", "categoria": "Cálculo", "imagem_url": "/imgs/15-eratostenes.jpg", "descricao": "Mediu a Terra e avançou geografia e cartografia.", "brasil": False},
    {"id": 16, "nome": "Nikola Tesla", "categoria": "Quântica", "imagem_url": "/imgs/16-nikola-tesla.jpg", "descricao": "Impulsionou corrente alternada e motores elétricos.", "brasil": False},
    {"id": 17, "nome": "Max Planck", "categoria": "Quântica", "imagem_url": "/imgs/17-max-planck.jpg", "descricao": "Iniciou a física quântica com os quanta of energia.", "brasil": False},
    {"id": 18, "nome": "Ernest Rutherford", "categoria": "Quântica", "imagem_url": "/imgs/18-ernest-rutherford.jpg", "descricao": "Descobriu o núcleo atômico e fundou a física nuclear.", "brasil": False},
    {"id": 19, "nome": "Niels Bohr", "categoria": "Quântica", "imagem_url": "/imgs/19-niels-bohr.jpg", "descricao": "Avançou o modelo atômico e a teoria quântica.", "brasil": False},
    {"id": 20, "nome": "Rosalind Franklin", "categoria": "Quântica", "imagem_url": "/imgs/20-rosalind-franklin.jpg", "descricao": "Produziu dados essenciais para revelar o DNA.", "brasil": False},
    {"id": 21, "nome": "John Bardeen", "categoria": "Eletrônica", "imagem_url": "/imgs/21-john-bardeen.jpg", "descricao": "Criou o transistor que sustenta a eletrônica moderna.", "brasil": False},
    {"id": 22, "nome": "William Shockley", "categoria": "Eletrônica", "imagem_url": "/imgs/22-william-shockley.jpg", "descricao": "Ajudou a criar o transistor e os semicondutores.", "brasil": False},
    {"id": 23, "nome": "Walter Brattain", "categoria": "Eletrônica", "imagem_url": "/imgs/23-walter-brattain.jpg", "descricao": "Construiu experimentalmente o primeiro transistor.", "brasil": False},
    {"id": 24, "nome": "Shuji Nakamura", "categoria": "Eletrônica", "imagem_url": "/imgs/24-shuji-nakamura.jpg", "descricao": "Viabilizou LEDs azuis e iluminação branca eficiente.", "brasil": False},
    {"id": 25, "nome": "Nick Holonyak", "categoria": "Eletrônica", "imagem_url": "/imgs/25-nick-holonyak.jpg", "descricao": "Criou o primeiro LED visível de uso prático.", "brasil": False},
    {"id": 26, "nome": "Alan Turing", "categoria": "Computação", "imagem_url": "/imgs/26-alan-turing.jpg", "descricao": "Fundamentou computação e inteligência artificial.", "brasil": False},
    {"id": 27, "nome": "Margaret Hamilton", "categoria": "Computação", "imagem_url": "/imgs/27-margaret-hamilton.jpg", "descricao": "Consolidou a engenharia de software nas missões Apollo.", "brasil": False},
    {"id": 28, "nome": "Ada Lovelace", "categoria": "Computação", "imagem_url": "/imgs/28-ada-lovelace.jpg", "descricao": "Antecipou algoritmos e a programação de computadores.", "brasil": False},
    {"id": 29, "nome": "Joseph-Marie Jacquard", "categoria": "Computação", "imagem_url": "/imgs/29-joseph-marie-jacquard.jpg", "descricao": "Criou automação programável com cartões perfurados.", "brasil": False},
    {"id": 30, "nome": "David Huffman", "categoria": "Computação", "imagem_url": "/imgs/30-david-huffman.jpg", "descricao": "Criou um método essencial de compressão de dados.", "brasil": False},
    {"id": 31, "nome": "Tim Berners-Lee", "categoria": "Sociedade", "imagem_url": "/imgs/31-tim-berners-lee.jpg", "descricao": "Criou a Web e ampliou o acesso à informação.", "brasil": False},
    {"id": 32, "nome": "John Snow", "categoria": "Sociedade", "imagem_url": "/imgs/32-john-snow.jpg", "descricao": "Fundou a epidemiologia moderna com dados e mapas.", "brasil": False},
    {"id": 33, "nome": "Carlos Chagas", "categoria": "Sociedade", "imagem_url": "/imgs/33-carlos-chagas.jpg", "descricao": "Descreveu integralmente a doença de Chagas.", "brasil": True},
    {"id": 34, "nome": "Nise da Silveira", "categoria": "Sociedade", "imagem_url": "/imgs/34-nise-da-silveira.jpg", "descricao": "Humanizou a psiquiatria e combateu práticas violentas.", "brasil": True},
    {"id": 35, "nome": "Joseph Weizenbaum", "categoria": "Sociedade", "imagem_url": "/imgs/35-joseph-weizenbaum.jpg", "descricao": "Criou o ELIZA e antecipou debates éticos sobre IA.", "brasil": False},
    {"id": 36, "nome": "Charles Darwin", "categoria": "Biologia", "imagem_url": "/imgs/36-charles-darwin.jpg", "descricao": "Explicou a evolução por seleção natural.", "brasil": False},
    {"id": 37, "nome": "Norman Borlaug", "categoria": "Biologia", "imagem_url": "/imgs/37-norman-borlaug.jpg", "descricao": "Impulsionou a Revolução Verde contra a fome.", "brasil": False},
    {"id": 38, "nome": "Gregor Mendel", "categoria": "Biologia", "imagem_url": "/imgs/38-gregor-mendel.jpg", "descricao": "Fundamentou a genética e as leis da hereditariedade.", "brasil": False},
    {"id": 39, "nome": "Johanna Döbereiner", "categoria": "Biologia", "imagem_url": "/imgs/39-johanna-dobereiner.jpg", "descricao": "Reduziu fertilizantes com fixação biológica de nitrogênio.", "brasil": True},
    {"id": 40, "nome": "Nikolai Lunin", "categoria": "Biologia", "imagem_url": "/imgs/40-nikolai-lunin.jpg", "descricao": "Antecipou a descoberta das vitaminas essenciais.", "brasil": False},
    {"id": 41, "nome": "Louis Pasteur", "categoria": "Microbiologia", "imagem_url": "/imgs/41-louis-pasteur.jpg", "descricao": "Transformou microbiologia, vacinas e higiene.", "brasil": False},
    {"id": 42, "nome": "Alexander Fleming", "categoria": "Microbiologia", "imagem_url": "/imgs/42-alexander-fleming.jpg", "descricao": "Abriu a era dos antibióticos com a penicilina.", "brasil": False},
    {"id": 43, "nome": "Edward Jenner", "categoria": "Microbiologia", "imagem_url": "/imgs/43-edward-jenner.jpg", "descricao": "Inaugurou a vacinação moderna contra a varíola.", "brasil": False},
    {"id": 44, "nome": "Robert Koch", "categoria": "Microbiologia", "imagem_url": "/imgs/44-robert-koch.jpg", "descricao": "Relacionou microrganismos específicos a doenças.", "brasil": False},
    {"id": 45, "nome": "Vital Brazil", "categoria": "Microbiologia", "imagem_url": "/imgs/45-vital-brazil.jpg", "descricao": "Criou soros específicos contra animais peçonhentos.", "brasil": True},
    {"id": 46, "nome": "Ignaz Semmelweis", "categoria": "Medicina", "imagem_url": "/imgs/46-ignaz-semmelweis.jpg", "descricao": "Provou que lavar as mãos evita infecções.", "brasil": False},
    {"id": 47, "nome": "Frederick Banting", "categoria": "Medicina", "imagem_url": "/imgs/47-frederick-banting.jpg", "descricao": "Tornou o diabetes tratável com a insulina.", "brasil": False},
    {"id": 48, "nome": "Jonas Salk", "categoria": "Medicina", "imagem_url": "/imgs/48-jonas-salk.jpg", "descricao": "Criou a primeira vacina eficaz contra a poliomielite.", "brasil": False},
    {"id": 49, "nome": "Albert Sabin", "categoria": "Medicina", "imagem_url": "/imgs/49-albert-sabin.jpg", "descricao": "Viabilizou vacinação oral em massa contra a pólio.", "brasil": True},
    {"id": 50, "nome": "Henrietta Lacks", "categoria": "Medicina", "imagem_url": "/imgs/50-henrietta-lacks.jpg", "descricao": "Suas células HeLa revolucionaram a pesquisa biomédica.", "brasil": False}
]

# Define um endpoint para requisições GET no caminho "/figurinhas"
# Retorna a lista contendo as 50 figurinhas cadastradas
@app.get("/figurinhas")
def listar_figurinhas():
    # Retorna a lista de figurinhas
    return figurinhas

# Define um endpoint alternativo "/figs" que recupera as figurinhas do banco de dados SQLite
@app.get("/figs")
def listar_figurinhas_banco():
    # Conecta ao banco de dados SQLite
    conn = sqlite3.connect(DB_PATH)
    # Define a row factory para podermos acessar os dados como dicionário
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    # Seleciona todas as figurinhas da tabela correspondente
    cursor.execute("SELECT * FROM figurinhas ORDER BY id ASC")
    rows = cursor.fetchall()
    
    # Formata a lista convertendo Row em dicionário e normalizando o campo boolean 'brasil'
    figurinhas_db = []
    for row in rows:
        fig = dict(row)
        fig["brasil"] = bool(fig["brasil"])
        figurinhas_db.append(fig)
        
    conn.close()
    return figurinhas_db
