# Mestres e Seus Inventos — Álbum de Figurinhas Digital

Este é um projeto interativo de um **Álbum de Figurinhas Digital** desenvolvido durante a **Imersão Alura de Desenvolvimento Web com Inteligência Artificial** (Julho de 2026). O álbum é dedicado a homenagear 50 das mentes mais brilhantes e revolucionárias da história da ciência, física, química, biologia, medicina, matemática e computação.

O visual e a experiência do usuário adotam uma atmosfera **Dark Premium** inspirada nos estilos Cyberpunk e Sci-Fi, contendo brilhos neon, efeitos de reflexão de texto, descargas elétricas animadas e efeitos sonoros imersivos.

---

## 🎨 Efeitos Visuais & UX Premium
*   **Interface Dark Premium**: Fundo escuro profundo (`#0D0C15`) com brilhos e realces em tons neon de Fuchsia (`#D946EF`) e Azul (`#3B82F6`), oferecendo alta legibilidade e contraste futurista.
*   **Capa com Eletricidade e Reflexos**:
    *   O título principal `"MESTRES"` possui um reflexo vertical espelhado (`-webkit-box-reflect`) e uma aura suave de brilho neon.
    *   O subtítulo `"SEUS INVENTOS"` conta com raios elétricos em formato SVG animados via CSS. As descargas ocorrem de maneira rápida, sutil e em tempos alternados (usando ciclos matemáticos primos de `4s` e `5.3s`), simulando faíscas elétricas de laboratório.
*   **Física de Papel & Virada 3D**: Navegação ultra-realista baseada na biblioteca `St.PageFlip`, combinada com suporte avançado a gestos manuais (arrastar com o mouse ou deslizar em telas touchscreen) que imitam o comportamento físico de uma folha de papel.
*   **Borda Especial Verde Esmeralda (Cientistas Brasileiros)**: Em comemoração aos cientistas de destaque no Brasil (Carlos Chagas, Vital Brazil, Johanna Döbereiner, Nise da Silveira e Albert Sabin), os slots correspondentes contam com uma borda neon esmeralda (`#10B981`) personalizada, que transiciona de pontilhada (dashed) no estado vazio para sólida (solid) no estado colado.
*   **Destaque na Base (Special Slot)**: Cada página temática do álbum conta com 5 slots de figurinhas, sendo 4 normais de tamanho médio e 1 **Slot Especial** maior, posicionado centralizadamente na base inferior da página, reservado para a personalidade mais impactante daquela área específica.
*   **Imersão Sonora Completa**:
    *   Música de fundo instrumental de laboratório (`lab_window_music_loop.mp3`) iniciada em loop contínuo (com tratamentos de contorno para o bloqueio de reprodução automática de navegadores modernos).
    *   Efeito sonoro realístico de papel folheando (`page_flipping.mp3`) que é reproduzido sempre que o usuário muda de página.
    *   Controles de volume/mute localizados de maneira elegante no canto superior do site com atualização imediata do ícone.

---

## 📂 Estrutura das Páginas e Categorias
O álbum é composto por 12 páginas no total (Capa + 10 Páginas Internas Temáticas + Contracapa):

1.  **Capa (Pág. 0)**: Título com reflexão, efeitos elétricos nos raios em SVG, esfera tecnológica iluminada em 3D e colagem de miniaturas holográficas.
2.  **Física Clássica & Cosmos (Pág. 1)**: Gravitação, eletromagnetismo e cosmologia espacial.
    *   *Slots*: `#01` Isaac Newton, `#02` Michael Faraday, `#03` James Clerk Maxwell, `#04` Albert Einstein, `#05` Stephen Hawking (Destaque Especial).
3.  **Química & Elementos (Pág. 2)**: Reações, tabela periódica e leis de massas.
    *   *Slots*: `#06` Fritz Haber, `#07` Antoine Lavoisier, `#08` Dmitri Mendeleev, `#09` Marie Curie (Destaque Especial), `#10` John Walker.
4.  **Matemática & Astronomia (Pág. 3)**: Ciência experimental moderna, heliocentrism e cálculo de trajetórias.
    *   *Slots*: `#11` Galileu Galilei, `#12` Leonardo Fibonacci, `#13` Nicolau Copérnico, `#14` Katherine Johnson (Destaque Especial), `#15` Eratóstenes.
5.  **Física Moderna & Biofísica (Pág. 4)**: Corrente alternada, radiação quântica, modelo atômico e a difração do DNA.
    *   *Slots*: `#16` Nikola Tesla, `#17` Max Planck, `#18` Ernest Rutherford, `#19` Niels Bohr, `#20` Rosalind Franklin (Destaque Especial).
6.  **Eletrônica & Semicondutores (Pág. 5)**: O nascimento dos transistores e diodos emissores de luz (LED).
    *   *Slots*: `#21` John Bardeen (Destaque Especial), `#22` William Shockley, `#23` Walter Brattain, `#24` Shuji Nakamura, `#25` Nick Holonyak.
7.  **Fundamentos da Computação (Pág. 6)**: Lógica computacional, algoritmos primordiais, compressão e engenharia de software do Apollo 11.
    *   *Slots*: `#26` Alan Turing (Destaque Especial), `#27` Margaret Hamilton, `#28` Ada Lovelace, `#29` Joseph-Marie Jacquard, `#30` David Huffman.
8.  **Informação, Mente & Sociedade (Pág. 7)**: Rede mundial (Web), epidemiologia com dados, psiquiatria humanizada e debates éticos de IA.
    *   *Slots*: `#31` Tim Berners-Lee, `#32` John Snow, `#33` Carlos Chagas (Brasil), `#34` Nise da Silveira (Brasil - Destaque Especial), `#35` Joseph Weizenbaum.
9.  **Biologia & Ciências da Vida (Pág. 8)**: Seleção natural, genética hereditária, Revolução Verde e nutrição molecular.
    *   *Slots*: `#36` Charles Darwin (Destaque Especial), `#37` Norman Borlaug, `#38` Gregor Mendel, `#39` Johanna Döbereiner (Brasil), `#40` Nikolai Lunin.
10. **Microbiologia & Imunologia (Pág. 9)**: Vacinação moderna, bacteriologia clínica e desenvolvimento de soros específicos.
    *   *Slots*: `#41` Louis Pasteur (Destaque Especial), `#42` Alexander Fleming, `#43` Edward Jenner, `#44` Robert Koch, `#45` Vital Brazil (Brasil).
11. **Medicina Clínica & Virologia (Pág. 10)**: Higienização médica, terapia com insulina e células imortais HeLa.
    *   *Slots*: `#46` Ignaz Semmelweis, `#47` Frederick Banting, `#48` Jonas Salk (Destaque Especial), `#49` Albert Sabin (Brasil), `#50` Henrietta Lacks.
12. **Contracapa (Pág. 11)**: Indexador elegante das categorias e código de barras simulado.

---

## 🛠️ Arquitetura e Tecnologias
O projeto está dividido entre uma API no backend e uma aplicação rica baseada no frontend:

### Backend (`/backend`)
Desenvolvido em **Python** utilizando o framework assíncrono **FastAPI** e banco de dados relacional **SQLite**:
*   **Banco de Dados SQLite (`banco_album.sqlite`)**: Armazena as figurinhas de forma persistente com os campos `id` (INTEGER PRIMARY KEY), `nome` (TEXT), `categoria` (TEXT), `imagem_url` (TEXT), `descricao` (TEXT) e `brasil` (INTEGER).
*   **Script de Inicialização (`criar_banco.py`)**: Script utilizado para criar a tabela e popular o banco de dados inicial a partir da lista estática do código.
*   **API `/figurinhas`**: Expõe um endpoint HTTP `GET /figurinhas` que retorna a lista de figurinhas em memória (hardcoded).
*   **API `/figs`**: Expõe o endpoint HTTP `GET /figs` que busca dinamicamente as figurinhas a partir do banco de dados SQLite, convertendo os campos necessários e ordenando os resultados por ID.
*   **Static Serving**: Montagem do diretório `/imgs` apontando para `backend/figurinhas/` para servir as imagens físicas das figurinhas coladas de forma rápida e cacheável.

### Frontend (`/frontend`)
Construído com tecnologia nativa de navegador (**Vanilla Web Stack**):
*   **HTML5 Semântico**: Estruturação de todas as 12 páginas, containers do livro e marcação de slots vazios com classes CSS identificadoras.
*   **Vanilla CSS3**: Design em gradientes escuros, animações neon e elétricas personalizadas, transições de hover e redimensionamento responsivo.
*   **JavaScript (ES6+)**:
    *   Busca as informações no backend de modo assíncrono e popula dinamicamente os slots de figurinhas, adicionando a tag `<img>` e aplicando a classe `.slot-preenchido` após o carregamento da imagem.
    *   Inicializa a biblioteca `St.PageFlip` a partir de uma CDN, aplicando uma lógica personalizada de drag-and-drop para mouse e toques mobile que elimina conflitos em cliques simples.
    *   Controla a reprodução dos áudios (`flipSound` e `bgMusic`), aplicando mute dinâmico e contornando bloqueios de reprodução automática.

---

## 🚀 Como Configurar e Executar o Projeto Localmente

### Pré-requisitos
*   **Python 3.10 ou superior** instalado.
*   Navegador Web atualizado.

### 1. Inicializar o Servidor de API (Backend)
1. Navegue até o diretório `backend`:
   ```bash
   cd backend
   ```
2. Crie e ative um ambiente virtual Python:
   * **Windows**:
     ```powershell
     python -m venv .venv
     .venv\Scripts\activate
     ```
   * **macOS/Linux**:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```
3. Instale as dependências:
   ```bash
   pip install fastapi uvicorn
   ```
4. Inicialize e popule o banco de dados SQLite:
   ```bash
   python criar_banco.py
   ```
5. Inicie o servidor:
   ```bash
   uvicorn main:app --reload
   ```
   *O backend ficará ativo por padrão em [http://localhost:8000](http://localhost:8000). O endpoint `/figurinhas` retornará os dados em memória e o endpoint `/figs` retornará os dados vindos do banco SQLite.*

### 2. Inicializar o Álbum Digital (Frontend)
Você pode abrir o frontend de duas maneiras:
*   **Modo Rápido**: Abra diretamente o arquivo [index.html](file:///c:/Users/anton/pessoal/alura/imersao/des_web_ia/mestres_e_seus_inventos/frontend/index.html) no seu navegador.
*   **Modo Servidor Local (Recomendado)**: Abra a pasta `frontend` no VS Code e clique em "Go Live" (usando a extensão *Live Server*). Ou, de dentro do diretório `frontend`, execute no terminal:
    ```bash
    python -m http.server 3000
    ```
    *Acesse o álbum em [http://localhost:3000](http://localhost:3000).*

---

## 📚 Tabela Geral das 50 Figurinhas
Aqui está a catalogação completa dos cientistas presentes no álbum, incluindo seu número de slot correspondente, área científica, realização histórica de relevância e se recebem a moldura especial brasileira:

| ID | Personalidade | Área Principal | Descrição / Realização Histórica | Especial Brasil? |
| :---: | :--- | :--- | :--- | :---: |
| **01** | Isaac Newton | Física | Fundou a mecânica clássica e a gravitação. | Não |
| **02** | Michael Faraday | Física | Viabilizou motores, geradores e eletrificação. | Não |
| **03** | James Clerk Maxwell | Física | Fundamentou eletromagnetismo e telecomunicações. | Não |
| **04** | Albert Einstein | Física | Reformulou espaço, tempo, energia e gravidade. | Não |
| **05** | Stephen Hawking | Física (Destaque) | Avançou a física dos buracos negros e sua divulgação. | Não |
| **06** | Fritz Haber | Química | Viabilizou fertilizantes e ampliou a produção agrícola. | Não |
| **07** | Antoine Lavoisier | Química | Estabeleceu as bases quantitativas da química. | Não |
| **08** | Dmitri Mendeleev | Química | Organizou os elementos na tabela periódica. | Não |
| **09** | Marie Curie | Química (Destaque) | Avançou a radioatividade e suas aplicações médicas. | Não |
| **10** | John Walker | Química | Popularizou o fósforo de fricção no cotidiano. | Não |
| **11** | Galileu Galilei | Cálculo | Consolidou a ciência experimental moderna. | Não |
| **12** | Leonardo Fibonacci | Cálculo | Popularizou o sistema numérico indo-arábico. | Não |
| **13** | Nicolau Copérnico | Cálculo | Impulsionou o heliocentrismo e a Revolução Científica. | Não |
| **14** | Katherine Johnson | Cálculo (Destaque) | Calculou trajetórias essenciais para missões espaciais. | Não |
| **15** | Eratóstenes | Cálculo | Mediu a Terra e avançou geografia e cartografia. | Não |
| **16** | Nikola Tesla | Quântica | Impulsionou corrente alternada e motores elétricos. | Não |
| **17** | Max Planck | Quântica | Iniciou a física quântica com os quanta of energia. | Não |
| **18** | Ernest Rutherford | Quântica | Descobriu o núcleo atômico e fundou a física nuclear. | Não |
| **19** | Niels Bohr | Quântica | Avançou o modelo atômico e a teoria quântica. | Não |
| **20** | Rosalind Franklin | Quântica (Destaque) | Produziu dados essenciais para revelar o DNA. | Não |
| **21** | John Bardeen | Eletrônica (Destaque)| Criou o transistor que sustenta a eletrônica moderna. | Não |
| **22** | William Shockley | Eletrônica | Ajudou a criar o transistor e os semicondutores. | Não |
| **23** | Walter Brattain | Eletrônica | Construiu experimentalmente o primeiro transistor. | Não |
| **24** | Shuji Nakamura | Eletrônica | Viabilizou LEDs azuis e iluminação branca eficiente. | Não |
| **25** | Nick Holonyak | Eletrônica | Criou o primeiro LED visível de uso prático. | Não |
| **26** | Alan Turing | Computação (Destaque)| Fundamentou computação e inteligência artificial. | Não |
| **27** | Margaret Hamilton | Computação | Consolidou a engenharia de software nas missões Apollo. | Não |
| **28** | Ada Lovelace | Computação | Antecipou algoritmos e a programação de computadores. | Não |
| **29** | Joseph-Marie Jacquard | Computação | Criou automação programável com cartões perfurados. | Não |
| **30** | David Huffman | Computação | Criou um método essencial de compressão de dados. | Não |
| **31** | Tim Berners-Lee | Sociedade | Criou a Web e ampliou o acesso à informação. | Não |
| **32** | John Snow | Sociedade | Fundou a epidemiologia moderna com dados e mapas. | Não |
| **33** | Carlos Chagas | Sociedade | Descreveu integralmente a doença de Chagas. | **Sim** |
| **34** | Nise da Silveira | Sociedade (Destaque)| Humanizou a psiquiatria e combateu práticas violentas. | **Sim** |
| **35** | Joseph Weizenbaum | Sociedade | Criou o ELIZA e antecipou debates éticos sobre IA. | Não |
| **36** | Charles Darwin | Biologia (Destaque)| Explicou a evolução por seleção natural. | Não |
| **37** | Norman Borlaug | Biologia | Impulsionou a Revolução Verde contra a fome. | Não |
| **38** | Gregor Mendel | Biologia | Fundamentou a genética e as leis da hereditariedade. | Não |
| **39** | Johanna Döbereiner | Biologia | Reduziu fertilizantes com fixação biológica de nitrogênio. | **Sim** |
| **40** | Nikolai Lunin | Biologia | Antecipou a descoberta das vitaminas essenciais. | Não |
| **41** | Louis Pasteur | Microbiologia (Destaque)| Transformou microbiologia, vacinas e higiene. | Não |
| **42** | Alexander Fleming | Microbiologia | Abriu a era dos antibióticos com a penicilina. | Não |
| **43** | Edward Jenner | Microbiologia | Inaugurou a vacinação moderna contra a varíola. | Não |
| **44** | Robert Koch | Microbiologia | Relacionou microrganismos específicos a doenças. | Não |
| **45** | Vital Brazil | Microbiologia | Criou soros específicos contra animais peçonhentos. | **Sim** |
| **46** | Ignaz Semmelweis | Medicina | Provou que lavar as mãos evita infecções. | Não |
| **47** | Frederick Banting | Medicina | Tornou o diabetes tratável com a insulina. | Não |
| **48** | Jonas Salk | Medicina (Destaque) | Criou a primeira vacina eficaz contra a poliomielite. | Não |
| **49** | Albert Sabin | Medicina | Viabilizou vacinação oral em massa contra a pólio. | **Sim** |
| **50** | Henrietta Lacks | Medicina | Suas células HeLa revolucionaram a pesquisa biomédica. | Não |


---

## 📄 Licença
Este projeto é distribuído sob os termos da licença incluída no diretório raiz do projeto. Sinta-se à vontade para expandir, alterar e enriquecer a lista de cientistas e o design do seu álbum de figurinhas!
