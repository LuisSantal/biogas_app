# App Biogás nas Escolas

## Descrição do Projeto
Este aplicativo móvel multiplataforma, "Biogás nas Escolas", visa promover a educação ambiental e a sustentabilidade no ambiente escolar.Ele permite o registro, acompanhamento e análise dos resíduos orgânicos gerados nas cozinhas das escolas e sua destinação para biodigestores de baixo custo. O projeto foi desenvolvido com o objetivo de criar uma ferramenta tecnológica educativa que auxilie escolas no controle do descarte de alimentos, possibilitando a mensuração da produção de biogás, a redução da emissão de gases de efeito estufa (GEE) e o impacto ambiental positivo.

## Funcionalidades Principais
* **Registro de Resíduos**: Permite registrar os tipos e quantidades de alimentos descartados[cite: 28].
* **Estimativa de Biogás**: Calcula a estimativa da produção de biogás com base nos resíduos[cite: 29].
* **Estatísticas Ambientais**: Apresenta estatísticas sobre resíduos desviados de aterros sanitários e a redução de GEE[cite: 30, 31].
* **Armazenamento Local**: Todos os dados são armazenados localmente no dispositivo (SQLite), sem necessidade de conexão com servidor[cite: 33].
* **Gerenciamento de Usuários**: Cadastro e login de professores, alunos e gestores escolares.
* **Mídia**: Funcionalidade para upload e visualização de fotos e vídeos associados aos registros.

## Tecnologias Utilizadas
* **Linguagem**: Python [cite: 40]
* **Framework**: Kivy (multiplataforma) [cite: 41]
* **Banco de Dados**: SQLite (para armazenamento local) [cite: 41]
* **Compatibilidade**: Android e iOS [cite: 41]
* **Ferramentas Adicionais**: Plyer (para acesso a recursos do dispositivo como câmera/galeria).

## Estrutura do Projeto
biogas_app/

├── .venv/                  # Ambiente virtual Python

├── media/                  # Fotos e vídeos dos usuários

├── assets/  # Imagens, fontes e outros recursos estáticos

│   ├── images/

│   └── fonts/

├── kv/                     # Arquivos de design de UI (Kivy Language)

│   ├── login_screen.kv

│   ├── register_waste_screen.kv

│   ├── biogas_estimation_screen.kv

│   ├── reports_screen.kv

├── main.py                 # Lógica principal e execução do aplicativo

├── biogas_app.db           # Banco de dados SQLite (gerado pelo app)

├── README.md               # Este arquivo

├── requirements.txt        # Dependências do projeto Python

└── .gitignore              # Arquivo para o Git ignorar diretórios/arquivos

## Como Configurar e Executar

### Pré-requisitos
* Python 3.x instalado

### Configuração do Ambiente
1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/biogas_app.git](https://github.com/seu-usuario/biogas_app.git)
    cd biogas_app
    ```
2.  **Crie e ative o ambiente virtual:**
    ```bash
    python -m venv .venv
    # No Windows:
    .venv\Scripts\activate
    # No macOS/Linux:
    source .venv/bin/activate
    ```
3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

### Executando o Aplicativo
Após a instalação das dependências e com o ambiente virtual ativado:
```bash
python main.py
