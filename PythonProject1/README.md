# App Biogás nas Escolas

## Descrição do Projeto
Este aplicativo móvel multiplataforma, "Biogás nas Escolas", visa promover a educação ambiental e a sustentabilidade no ambiente escolar.Ele permite o registro, acompanhamento e análise dos resíduos orgânicos gerados nas cozinhas das escolas e sua destinação para biodigestores de baixo custo. O projeto foi desenvolvido com o objetivo de criar uma ferramenta tecnológica educativa que auxilie escolas no controle do descarte de alimentos, possibilitando a mensuração da produção de biogás, a redução da emissão de gases de efeito estufa (GEE) e o impacto ambiental positivo.

## Funcionalidades Principais
* **Registro de Resíduos**: Permite registrar os tipos e quantidades de alimentos descartados.
* **Estimativa de Biogás**: Calcula a estimativa da produção de biogás com base nos resíduos.
* **Estatísticas Ambientais**: Apresenta estatísticas sobre resíduos desviados de aterros sanitários e a redução de GEE.
* **Armazenamento Local**: Todos os dados são armazenados localmente no dispositivo (SQLite), sem necessidade de conexão com servidor.
* **Gerenciamento de Usuários**: Cadastro e login de professores, alunos e gestores escolares.
* **Mídia**: Funcionalidade para upload e visualização de fotos e vídeos associados aos registros.

## Tecnologias Utilizadas
* **Linguagem**: Python 
* **Framework**: Kivy (multiplataforma) 
* **Banco de Dados**: SQLite (para armazenamento local) 
* **Compatibilidade**: Android e iOS 
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
### token de Acesso :
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

# Build Android APK

## Solução dos problemas de build

Este projeto foi ajustado para permitir a compilação do APK Android usando Buildozer, Kivy e Python 3.9. Foram realizadas as seguintes modificações para solucionar incompatibilidades e erros:

- Migração do ambiente para Python 3.9 e Buildozer 1.3.0
- Patch nos recipes locais de Kivy e Pyjnius para compatibilidade
- Remoção do método `__long__` e duplicatas em `weakproxy.pyx` (Kivy)
- Restauração do arquivo `config.pxi` em `local_recipes/kivy/kivy/include/`
- Correção do uso do pip com `--user` no Buildozer
- Configuração do Java 17 como JAVA_HOME
- Limpeza profunda dos artefatos de build
- Build final realizado com sucesso

## Localização do APK

O APK gerado está disponível em:

- [`bin/biogasapp-0.1-arm64-v8a_armeabi-v7a-debug.apk`](bin/biogasapp-0.1-arm64-v8a_armeabi-v7a-debug.apk)

Você pode instalar este APK em seu dispositivo Android para testar o aplicativo.

## Observações

Essas modificações garantem compatibilidade total com o ambiente Android e resolvem os erros de build relacionados a versões de Python, Java e dependências nativas.

