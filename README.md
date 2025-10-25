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

## Estrutura do Projeto (Simplificada)
```
biogas_app/
├── PythonProject1/           # Código fonte do aplicativo
│   ├── assets/               # Imagens, fontes, etc.
│   ├── kv/                   # Arquivos de design da UI (Kivy)
│   ├── main.py               # Lógica principal do app
│   └── requirements.txt      # Dependências Python do app
├── buildozer.spec            # Especificações de compilação do Buildozer
├── README.md                 # Este arquivo
└── .gitignore                # Arquivos ignorados pelo Git
```

## Como Configurar e Executar (Localmente)

### Pré-requisitos
* Python 3.x instalado

### Configuração do Ambiente
1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/LuisSantal/biogas_app.git
    cd biogas_app/PythonProject1
    ```
2.  **Crie e ative o ambiente virtual:**
    ```bash
    python -m venv venv
    # No Windows:
    venv\Scripts\activate
    # No macOS/Linux:
    source venv/bin/activate
    ```
3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

### Executando o Aplicativo
Após a instalação das dependências e com o ambiente virtual ativado:
```bash
python main.py
```

## Como Compilar o APK para Android

Este guia documenta os passos para compilar o projeto em um APK a partir de um ambiente WSL (Windows Subsystem for Linux).

### 1. Configuração do Ambiente WSL (Ubuntu)
Para evitar conflitos, remova bibliotecas de desenvolvimento do SDL2 que possam estar instaladas:
```sh
sudo apt-get remove libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev libfreetype6-dev libharfbuzz-dev
```

### 2. Configuração do Java Development Kit (JDK)
O Gradle exige uma versão específica do Java.

#### 2.1. Instale o OpenJDK 17
```sh
sudo apt-get update
sudo apt-get install openjdk-17-jdk
```

#### 2.2. Defina o JDK 17 como Padrão
```sh
sudo update-java-alternatives --set java-1.17.0-openjdk-amd64
```
Confirme a versão com `java -version`.

### 3. Preparação do Projeto para Compilação
A partir da **raiz do projeto** (`biogas_app`):

#### 3.1. Crie e Ative um Ambiente Virtual para o Buildozer
```sh
# Criar o ambiente virtual
python3 -m venv venv_buildozer

# Ativar o ambiente virtual
source venv_buildozer/bin/activate
```

#### 3.2. Instale o Buildozer
Com o ambiente virtual ativo, instale o Buildozer e o Cython (versão < 3.0 é crucial):
```sh
pip install "buildozer>=1.5.0" "cython<3.0"
```

### 4. Compilação do APK
Com tudo configurado, inicie a compilação.

#### 4.1. Limpeza (Opcional, mas recomendado)
Para limpar builds antigos:
```sh
buildozer android clean
```

#### 4.2. Compilar o APK de Debug
Execute o comando na **raiz do projeto**. A primeira compilação seria um pouco longa, pois o Buildozer  vai baixar o Android NDK e outras dependências.
```sh
buildozer android debug
```

Se tudo correr bem, o APK estará disponível no diretório `bin/`.

### Observações sobre a Compilação
Este projeto foi ajustado para garantir a compatibilidade com o ambiente Android, resolvendo erros de build relacionados a versões de Python, Java e dependências nativas. As configurações no arquivo `buildozer.spec` e os patches aplicados localmente são resultado desse processo.

