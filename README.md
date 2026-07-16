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
Desenvolvido em **Python** utilizando o framework assíncrono **FastAPI**:
*   **Static Serving**: Montagem do diretório `/imgs` apontando para `backend/figurinhas/` para servir as imagens físicas das figurinhas coladas de forma rápida e cacheável.
*   **API `/figurinhas`**: Expõe um endpoint HTTP `GET /figurinhas` que retorna um array de objetos JSON mapeando dados como `id`, `nome`, `categoria`, `imagem_url` e o indicador booleano `brasil` (usado no destaque de cientistas brasileiros).

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
4. Inicie o servidor:
   ```bash
   uvicorn main:app --reload
   ```
   *O backend ficará ativo por padrão em [http://localhost:8000](http://localhost:8000).*

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

| ID | Personalidade | Área Principal | Razão Principal da Posição / Realização Histórica | Especial Brasil? |
| :---: | :--- | :--- | :--- | :---: |
| **01** | Isaac Newton | Física | Fundou a mecânica clássica e a gravitação universal. | Não |
| **02** | Michael Faraday | Física | Viabilizou motores, geradores e a eletrificação moderna. | Não |
| **03** | James Clerk Maxwell | Física | Fundamentou a teoria do eletromagnetismo e telecomunicações. | Não |
| **04** | Albert Einstein | Física | Reformulou espaço, tempo, energia e gravidade com a relatividade. | Não |
| **05** | Stephen Hawking | Física (Destaque) | Avançou o estudo de buracos negros e a cosmologia teórica. | Não |
| **06** | Fritz Haber | Química | Viabilizou fertilizantes sintéticos e ampliou a produção agrícola mundial. | Não |
| **07** | Antoine Lavoisier | Química | Estabeleceu as bases quantitativas da química moderna. | Não |
| **08** | Dmitri Mendeleev | Química | Organizou os elementos na tabela periódica de forma preditiva. | Não |
| **09** | Marie Curie | Química (Destaque) | Pioneira nos estudos sobre a radioatividade e tratamentos médicos. | Não |
| **10** | John Walker | Química | Desenvolveu o fósforo de fricção, popularizando o fogo seguro e barato. | Não |
| **11** | Galileu Galilei | Cálculo | Consolidou a ciência experimental moderna e o método científico. | Não |
| **12** | Leonardo Fibonacci | Cálculo | Introduziu e popularizou o sistema numérico indo-arábico no Ocidente. | Não |
| **13** | Nicolau Copérnico | Cálculo | Apresentou e estruturou o heliocentrismo, iniciando a revolução científica. | Não |
| **14** | Katherine Johnson | Cálculo (Destaque) | Computadora humana cujos cálculos viabilizaram as primeiras missões espaciais da NASA. | Não |
| **15** | Eratóstenes | Cálculo | Mediu a circunferência da Terra com precisão impressionante no mundo antigo. | Não |
| **16** | Nikola Tesla | Quântica | Projetou o sistema de transmissão por corrente alternada e motores de indução. | Não |
| **17** | Max Planck | Quântica | Propôs a quantização de energia, fundando a física quântica. | Não |
| **18** | Ernest Rutherford | Quântica | Descobriu o núcleo atômico e a natureza da radiação alfa e beta. | Não |
| **19** | Niels Bohr | Quântica | Criou o modelo atômico orbital quântico estável. | Não |
| **20** | Rosalind Franklin | Quântica (Destaque) | Capturou a famosa Fotografia 51, provando a estrutura de dupla hélice do DNA. | Não |
| **21** | John Bardeen | Eletrônica (Destaque)| Coinventor do primeiro transistor prático e da teoria da supercondutividade. | Não |
| **22** | William Shockley | Eletrônica | Cocriador e promotor do transistor e do silício no desenvolvimento de semicondutores. | Não |
| **23** | Walter Brattain | Eletrônica | Físico que construiu fisicamente o primeiro protótipo operacional de transistor. | Não |
| **24** | Shuji Nakamura | Eletrônica | Inventou o LED azul de alto brilho, abrindo portas para telas modernas e iluminação eficiente. | Não |
| **25** | Nick Holonyak | Eletrônica | Criou o primeiro diodo emissor de luz (LED) visível na faixa vermelha. | Não |
| **26** | Alan Turing | Computação (Destaque)| Pai da ciência da computação e inteligência artificial teórica com a Máquina de Turing. | Não |
| **27** | Margaret Hamilton | Computação | Diretora de engenharia de software da missão Apollo 11, pioneira da engenharia de software. | Não |
| **28** | Ada Lovelace | Computação | Escreveu o primeiro algoritmo destinado a ser processado por uma máquina. | Não |
| **29** | Joseph-Marie Jacquard | Computação | Criou o tear automático operado por cartões perfurados, antecedente da programação. | Não |
| **30** | David Huffman | Computação | Desenvolveu o algoritmo de codificação Huffman para compressão de dados sem perdas. | Não |
| **31** | Tim Berners-Lee | Sociedade | Criou o protocolo HTTP e a World Wide Web (WWW). | Não |
| **32** | John Snow | Sociedade | Identificou o surto de cólera por água em Londres, fundando a epidemiologia. | Não |
| **33** | Carlos Chagas | Sociedade | Descobriu o ciclo completo da doença de Chagas (agente, vetor e patologia). | **Sim** |
| **34** | Nise da Silveira | Sociedade (Destaque)| Revolucionou a psiquiatria ao abolir tratamentos cruéis e introduzir terapia ocupacional e arte. | **Sim** |
| **35** | Joseph Weizenbaum | Sociedade | Criou o chatbot ELIZA e tornou-se um crítico dos perigos éticos da IA. | Não |
| **36** | Charles Darwin | Biologia (Destaque)| Formulou a teoria da evolução das espécies por meio da seleção natural. | Não |
| **37** | Norman Borlaug | Biologia | Liderou a Revolução Verde com trigo de alto rendimento, salvando milhões da fome. | Não |
| **38** | Gregor Mendel | Biologia | Descobriu os mecanismos básicos de herança genética com experiências em ervilhas. | Não |
| **39** | Johanna Döbereiner | Biologia | Desenvolveu pesquisas em fixação biológica de nitrogênio na soja, poupando bilhões ao país. | **Sim** |
| **40** | Nikolai Lunin | Biologia | Demonstrou a existência de substâncias acessórias essenciais à vida (futuras vitaminas). | Não |
| **41** | Louis Pasteur | Microbiologia (Destaque)| Criou a pasteurização, germologia clínica e a vacina contra a raiva. | Não |
| **42** | Alexander Fleming | Microbiologia | Descobriu acidentalmente a penicilina, inaugurando a era antibiótica. | Não |
| **43** | Edward Jenner | Microbiologia | Desenvolveu a primeira vacina moderna da história (contra a varíola). | Não |
| **44** | Robert Koch | Microbiologia | Formulou os postulados de Koch isolando agentes causadores de cólera e tuberculose. | Não |
| **45** | Vital Brazil | Microbiologia | Descobriu a especificidade de soros antiofídicos e araneídicos e fundou o Instituto Butantan. | **Sim** |
| **46** | Ignaz Semmelweis | Medicina | Propôs a higienização de mãos de médicos para prevenir febre puerperal, salvando parturientes. | Não |
| **47** | Frederick Banting | Medicina | Isolou a insulina, tornando o diabetes uma condição de saúde perfeitamente tratável. | Não |
| **48** | Jonas Salk | Medicina (Destaque) | Desenvolveu a primeira vacina injetável inativada contra a poliomielite. | Não |
| **49** | Albert Sabin | Medicina | Criou a vacina oral de vírus atenuado contra a pólio, permitindo vacinação em massa. | **Sim** |
| **50** | Henrietta Lacks | Medicina | Origem involuntária da linhagem celular HeLa, crucial para o desenvolvimento de vacinas e terapias contra o câncer. | Não |

---

## 📄 Licença
Este projeto é distribuído sob os termos da licença incluída no diretório raiz do projeto. Sinta-se à vontade para expandir, alterar e enriquecer a lista de cientistas e o design do seu álbum de figurinhas!
