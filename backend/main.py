# Importa a classe FastAPI do framework fastapi
from fastapi import FastAPI
# Importa a classe StaticFiles para servir arquivos estáticos
from fastapi.staticfiles import StaticFiles
# Importa o módulo os para manipulação de caminhos de arquivos
import os

# Cria uma instância da aplicação FastAPI
app = FastAPI()

# Define o caminho absoluto da pasta de imagens (para encontrar a pasta independentemente de onde o código for executado)
PASTA_BASE = os.path.dirname(os.path.abspath(__file__))
PASTA_IMAGENS = os.path.join(PASTA_BASE, "figurinhas")

# Configura e monta o diretório de arquivos estáticos na rota "/imgs"
app.mount("/imgs", StaticFiles(directory=PASTA_IMAGENS), name="imgs")

# Lista contendo as 50 figurinhas com seus respectivos dados e caminho das imagens
figurinhas = [
    {"id": 1, "nome": "Isaac Newton", "categoria": "Física", "imagem_url": "/imgs/01-isaac-newton.jpg", "brasil": False},
    {"id": 2, "nome": "Michael Faraday", "categoria": "Física", "imagem_url": "/imgs/02-michael-faraday.jpg", "brasil": False},
    {"id": 3, "nome": "James Clerk Maxwell", "categoria": "Física", "imagem_url": "/imgs/03-james-clerk-maxwell.jpg", "brasil": False},
    {"id": 4, "nome": "Albert Einstein", "categoria": "Física", "imagem_url": "/imgs/04-albert-einstein.jpg", "brasil": False},
    {"id": 5, "nome": "Stephen Hawking", "categoria": "Física", "imagem_url": "/imgs/05-stephen-hawking.jpg", "brasil": False},
    {"id": 6, "nome": "Fritz Haber", "categoria": "Química", "imagem_url": "/imgs/06-fritz-haber.jpg", "brasil": False},
    {"id": 7, "nome": "Antoine Lavoisier", "categoria": "Química", "imagem_url": "/imgs/07-antoine-lavoisier.jpg", "brasil": False},
    {"id": 8, "nome": "Dmitri Mendeleev", "categoria": "Química", "imagem_url": "/imgs/08-dmitri-mendeleev.jpg", "brasil": False},
    {"id": 9, "nome": "Marie Curie", "categoria": "Química", "imagem_url": "/imgs/09-marie-curie.jpg", "brasil": False},
    {"id": 10, "nome": "John Walker", "categoria": "Química", "imagem_url": "/imgs/10-john-walker.jpg", "brasil": False},
    {"id": 11, "nome": "Galileu Galilei", "categoria": "Cálculo", "imagem_url": "/imgs/11-galileu-galilei.jpg", "brasil": False},
    {"id": 12, "nome": "Leonardo Fibonacci", "categoria": "Cálculo", "imagem_url": "/imgs/12-leonardo-fibonacci.jpg", "brasil": False},
    {"id": 13, "nome": "Nicolau Copérnico", "categoria": "Cálculo", "imagem_url": "/imgs/13-nicolau-copernico.jpg", "brasil": False},
    {"id": 14, "nome": "Katherine Johnson", "categoria": "Cálculo", "imagem_url": "/imgs/14-katherine-johnson.jpg", "brasil": False},
    {"id": 15, "nome": "Eratóstenes", "categoria": "Cálculo", "imagem_url": "/imgs/15-eratostenes.jpg", "brasil": False},
    {"id": 16, "nome": "Nikola Tesla", "categoria": "Quântica", "imagem_url": "/imgs/16-nikola-tesla.jpg", "brasil": False},
    {"id": 17, "nome": "Max Planck", "categoria": "Quântica", "imagem_url": "/imgs/17-max-planck.jpg", "brasil": False},
    {"id": 18, "nome": "Ernest Rutherford", "categoria": "Quântica", "imagem_url": "/imgs/18-ernest-rutherford.jpg", "brasil": False},
    {"id": 19, "nome": "Niels Bohr", "categoria": "Quântica", "imagem_url": "/imgs/19-niels-bohr.jpg", "brasil": False},
    {"id": 20, "nome": "Rosalind Franklin", "categoria": "Quântica", "imagem_url": "/imgs/20-rosalind-franklin.jpg", "brasil": False},
    {"id": 21, "nome": "John Bardeen", "categoria": "Eletrônica", "imagem_url": "/imgs/21-john-bardeen.jpg", "brasil": False},
    {"id": 22, "nome": "William Shockley", "categoria": "Eletrônica", "imagem_url": "/imgs/22-william-shockley.jpg", "brasil": False},
    {"id": 23, "nome": "Walter Brattain", "categoria": "Eletrônica", "imagem_url": "/imgs/23-walter-brattain.jpg", "brasil": False},
    {"id": 24, "nome": "Shuji Nakamura", "categoria": "Eletrônica", "imagem_url": "/imgs/24-shuji-nakamura.jpg", "brasil": False},
    {"id": 25, "nome": "Nick Holonyak", "categoria": "Eletrônica", "imagem_url": "/imgs/25-nick-holonyak.jpg", "brasil": False},
    {"id": 26, "nome": "Alan Turing", "categoria": "Computação", "imagem_url": "/imgs/26-alan-turing.jpg", "brasil": False},
    {"id": 27, "nome": "Margaret Hamilton", "categoria": "Computação", "imagem_url": "/imgs/27-margaret-hamilton.jpg", "brasil": False},
    {"id": 28, "nome": "Ada Lovelace", "categoria": "Computação", "imagem_url": "/imgs/28-ada-lovelace.jpg", "brasil": False},
    {"id": 29, "nome": "Joseph-Marie Jacquard", "categoria": "Computação", "imagem_url": "/imgs/29-joseph-marie-jacquard.jpg", "brasil": False},
    {"id": 30, "nome": "David Huffman", "categoria": "Computação", "imagem_url": "/imgs/30-david-huffman.jpg", "brasil": False},
    {"id": 31, "nome": "Tim Berners-Lee", "categoria": "Sociedade", "imagem_url": "/imgs/31-tim-berners-lee.jpg", "brasil": False},
    {"id": 32, "nome": "John Snow", "categoria": "Sociedade", "imagem_url": "/imgs/32-john-snow.jpg", "brasil": False},
    {"id": 33, "nome": "Carlos Chagas", "categoria": "Sociedade", "imagem_url": "/imgs/33-carlos-chagas.jpg", "brasil": True},
    {"id": 34, "nome": "Nise da Silveira", "categoria": "Sociedade", "imagem_url": "/imgs/34-nise-da-silveira.jpg", "brasil": True},
    {"id": 35, "nome": "Joseph Weizenbaum", "categoria": "Sociedade", "imagem_url": "/imgs/35-joseph-weizenbaum.jpg", "brasil": False},
    {"id": 36, "nome": "Charles Darwin", "categoria": "Biologia", "imagem_url": "/imgs/36-charles-darwin.jpg", "brasil": False},
    {"id": 37, "nome": "Norman Borlaug", "categoria": "Biologia", "imagem_url": "/imgs/37-norman-borlaug.jpg", "brasil": False},
    {"id": 38, "nome": "Gregor Mendel", "categoria": "Biologia", "imagem_url": "/imgs/38-gregor-mendel.jpg", "brasil": False},
    {"id": 39, "nome": "Johanna Döbereiner", "categoria": "Biologia", "imagem_url": "/imgs/39-johanna-dobereiner.jpg", "brasil": True},
    {"id": 40, "nome": "Nikolai Lunin", "categoria": "Biologia", "imagem_url": "/imgs/40-nikolai-lunin.jpg", "brasil": False},
    {"id": 41, "nome": "Louis Pasteur", "categoria": "Microbiologia", "imagem_url": "/imgs/41-louis-pasteur.jpg", "brasil": False},
    {"id": 42, "nome": "Alexander Fleming", "categoria": "Microbiologia", "imagem_url": "/imgs/42-alexander-fleming.jpg", "brasil": False},
    {"id": 43, "nome": "Edward Jenner", "categoria": "Microbiologia", "imagem_url": "/imgs/43-edward-jenner.jpg", "brasil": False},
    {"id": 44, "nome": "Robert Koch", "categoria": "Microbiologia", "imagem_url": "/imgs/44-robert-koch.jpg", "brasil": False},
    {"id": 45, "nome": "Vital Brazil", "categoria": "Microbiologia", "imagem_url": "/imgs/45-vital-brazil.jpg", "brasil": True},
    {"id": 46, "nome": "Ignaz Semmelweis", "categoria": "Medicina", "imagem_url": "/imgs/46-ignaz-semmelweis.jpg", "brasil": False},
    {"id": 47, "nome": "Frederick Banting", "categoria": "Medicina", "imagem_url": "/imgs/47-frederick-banting.jpg", "brasil": False},
    {"id": 48, "nome": "Jonas Salk", "categoria": "Medicina", "imagem_url": "/imgs/48-jonas-salk.jpg", "brasil": False},
    {"id": 49, "nome": "Albert Sabin", "categoria": "Medicina", "imagem_url": "/imgs/49-albert-sabin.jpg", "brasil": True},
    {"id": 50, "nome": "Henrietta Lacks", "categoria": "Medicina", "imagem_url": "/imgs/50-henrietta-lacks.jpg", "brasil": False}
]

# Define um endpoint para requisições GET no caminho "/figurinhas"
# Retorna a lista contendo as 50 figurinhas cadastradas
@app.get("/figurinhas")
def listar_figurinhas():
    # Retorna a lista de figurinhas
    return figurinhas
