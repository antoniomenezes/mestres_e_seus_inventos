# Mestres e Seus Inventos - Álbum de Figurinhas Digital

Este é um projeto interativo de um Álbum de Figurinhas Digital desenvolvido durante a Imersão Alura de Desenvolvimento Web com Inteligência Artificial (Julho 2026). O álbum é dedicado a homenagear 50 das mentes mais brilhantes e revolucionárias da história da ciência, física, química, biologia, medicina, matemática e computação.

O visual adota uma atmosfera **Dark Premium** inspirada no estilo Cyberpunk e Sci-Fi, com brilhos neon nas cores fuchsia e azul, efeitos de reflexão de fonte, descargas elétricas dinâmicas e efeitos sonoros imersivos.

---

## 🚀 Funcionalidades Principais

*   **Tema Dark & Estética Premium**: Toda a interface foi adaptada para um fundo escuro profundo (`#0D0C15`) com detalhes neon fuchsia (`#D946EF`) e azul (`#3B82F6`), criando alto contraste e visual futurista.
*   **Capacidade de 50 Figurinhas**: Expandido de 30 para 50 slots de figurinhas, distribuídos em 10 páginas temáticas (5 figurinhas por página: 4 slots normais e 1 slot especial destacado centralizado na base).
*   **Agrupamento e Ordenação por Relevância**: Os cientistas foram divididos em áreas do conhecimento correlatas e organizados internamente em ordem de importância baseada em seu ranking histórico (`Pos.`).
*   **Moldura Especial para Cientistas do Brasil**: As figurinhas de personalidades brasileiras ou com atuação marcante no Brasil (como Carlos Chagas, Nise da Silveira, Johanna Döbereiner, Vital Brazil e Albert Sabin) possuem uma borda especial na cor **verde esmeralda** (`#10B981`) com efeitos glow personalizados, tanto no estado vazio (dashed) quanto colado (solid).
*   **Efeito Reflexo & Eletricidade na Capa**:
    *   O título principal "MESTRES" possui uma reflexão espelhada vertical (`-webkit-box-reflect`) e bordas brilhantes.
    *   O texto "SEUS INVENTOS" conta com um efeito de raios elétricos horizontais em SVG com animações de piscadas rápidas e silenciosas que ocorrem em tempos assimétricos e aleatórios (utilizando tempos matemáticos de ciclo primos: `4s` e `5.3s`).
*   **Efeitos Sonoros & Música de Fundo**:
    *   Música de fundo ambiental (`lab_window_music_loop.mp3`) que inicia em loop contínuo assim que a página é carregada (com suporte a ativação no primeiro gesto do usuário se bloqueado pelo navegador).
    *   Efeito sonoro realístico de papel virando (`page_flipping.mp3`) acionado em qualquer virada de página, incluindo o arrastar e soltar (drag and drop), cliques nas setas ou teclas direcionais.
    *   Botão de controle de áudio (Mute/Unmute) no cabeçalho com feedback visual dinâmico.
*   **Navegação Fluida de Página**: Integração com a biblioteca `St.PageFlip` para virada realista em 3D, combinada com controle de arraste manual personalizado que simula física de papel.

---

## 📂 Estrutura das Páginas e Categorias

O álbum é composto por 12 páginas no total (Capa + 10 Páginas Internas + Contracapa):

1.  **Capa (Pág. 0)**: Título com reflexão, efeitos elétricos nos raios em SVG e colagem de miniaturas.
2.  **Física Clássica & Cosmos (Pág. 1)**: Gravitação, relatividade e astrofísica.
3.  **Química & Elementos (Pág. 2)**: Tabela periódica, leis de conservação de massa e radioatividade.
4.  **Matemática & Astronomia (Pág. 3)**: Ciência experimental moderna, heliocentrismo e cálculo orbital de trajetórias espaciais.
5.  **Física Moderna & Biofísica (Pág. 4)**: Corrente alternada, radiação quântica, modelo atômico e a difração do DNA.
6.  **Eletrônica & Semicondutores (Pág. 5)**: A física do transistor e o desenvolvimento de LEDs eficientes.
7.  **Fundamentos da Computação (Pág. 6)**: Lógica computacional, algoritmos primordiais, compressão de dados e engenharia de software do Apollo 11.
8.  **Informação, Mente & Sociedade (Pág. 7)**: A criação da Web, epidemiologia espacial com dados, psiquiatria humanizada e debates éticos de inteligência artificial.
9.  **Biologia & Ciências da Vida (Pág. 8)**: Seleção natural, genética hereditária, Revolução Verde e nutrição molecular.
10. **Microbiologia & Imunologia (Pág. 9)**: Vacinação moderna, bacteriologia clínica e desenvolvimento de soros antiofídicos.
11. **Medicina Clínica & Virologia (Pág. 10)**: Higienização médica, terapia de diabetes com insulina e as revolucionárias células imortais HeLa.
12. **Contracapa (Pág. 11)**: Indexador de categorias e código de barras simulado.

---

## 🛠️ Tecnologias Utilizadas

*   **HTML5**: Estrutura semântica para todas as páginas e slots.
*   **Vanilla CSS3**: Estilização do tema dark, gradientes, efeitos neon, reflexão, eletricidade dinâmica e responsividade.
*   **Vanilla Javascript (ES6+)**: Controle de áudio, desvio de restrições de autoplay, carregamento dinâmico e integração com a biblioteca gráfica.
*   **StPageFlip**: Biblioteca de terceiros utilizada para a simulação tridimensional realista de virada física de livro.

---

## ⚙️ Como Executar o Projeto

1.  Certifique-se de iniciar a API do backend contendo os arquivos de imagem das figurinhas.
2.  Para rodar o frontend localmente, você pode abrir diretamente o arquivo `index.html` em qualquer navegador moderno ou utilizar uma extensão de servidor local (ex: *Live Server* do VS Code).
3.  Utilize os botões de seta nas laterais da tela, as setas direcionais do teclado (`Esquerda` e `Direita`) ou faça o gesto de arrastar as bordas das páginas com o mouse/touchscreen para folhear o álbum.
