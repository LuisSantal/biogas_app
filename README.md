# Biogás App - Guia de Compilação para Android

Este guia documenta os passos necessários para compilar o projeto Biogás App em um APK para Android a partir de um ambiente WSL (Windows Subsystem for Linux).

## 1. Configuração do Ambiente WSL (Ubuntu)

O ambiente de compilação pode ser sensível a pacotes de desenvolvimento instalados no sistema. Para garantir um processo limpo, remova as bibliotecas de desenvolvimento do SDL2 que podem causar conflitos:

```sh
sudo apt-get remove libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev libfreetype6-dev libharfbuzz-dev
```

## 2. Configuração do Java Development Kit (JDK)

O Android Gradle Plugin exige uma versão específica do Java.

### 2.1. Instale o OpenJDK 17
```sh
sudo apt-get update
sudo apt-get install openjdk-17-jdk
```

### 2.2. Defina o JDK 17 como Padrão
Use o seguinte comando para configurar o Java 17 como a versão padrão do sistema:
```sh
sudo update-java-alternatives --set java-1.17.0-openjdk-amd64
```

### 2.3. Verifique a Versão
Confirme se a versão padrão foi alterada corretamente:
```sh
java -version
```
A saída deve indicar "openjdk version "17..."".

## 3. Preparação do Projeto

### 3.1. Crie e Ative um Ambiente Virtual
É crucial isolar as dependências do projeto. A partir da raiz do projeto (`PythonProject1`), execute:
```sh
# Criar o ambiente virtual
python3 -m venv venv_buildozer

# Ativar o ambiente virtual
source venv_buildozer/bin/activate
```
**Lembre-se:** Sempre ative o ambiente virtual antes de executar qualquer comando de compilação.

### 3.2. Instale as Dependências Python
Com o ambiente virtual ativo, instale o Buildozer e suas dependências de compilação:
```sh
pip install buildozer "cython<3.0"
```
Usar uma versão do Cython anterior à 3.0 é fundamental para garantir a compatibilidade com as receitas do Kivy.

## 4. Configuração do `buildozer.spec`

O arquivo `buildozer.spec` precisa ser ajustado para incluir as dependências corretas e excluir arquivos desnecessários do APK.

As linhas mais importantes a garantir no seu `buildozer.spec` são:

```ini
# (Na seção [app])
# Lista de requisitos para o python-for-android
requirements = python3,kivy==2.3.0,sqlite3,plyer,pyjnius

# Exclui diretórios para não empacotá-los no APK
source.exclude_dirs = .buildozer,bin,venv,venv_buildozer,venv_buildozer_py39,dist,tests,docs,examples
source.exclude_patterns = *.pyc,*.swp,venv*/*
```

## 5. Compilação do APK

Com tudo configurado, você pode iniciar o processo de compilação.

### 5.1. Limpeza (Opcional, recomendado na primeira vez)
Se você já teve tentativas de compilação que falharam, é uma boa prática limpar os builds antigos:
```sh
buildozer android clean
```

### 5.2. Compilar o APK de Debug
Execute o comando principal. Na primeira vez, este processo será **muito longo**, pois o Buildozer irá baixar o Android NDK e compilar todas as receitas. Nas próximas vezes, será significativamente mais rápido.
```sh
buildozer android debug
```

### 5.3. Encontre seu APK
Se tudo correr bem, a compilação terminará com a mensagem:
`# APK ... available in the bin directory`

O seu arquivo `.apk` estará localizado em: `bin/biogasapp-0.1-arm64-v8a_armeabi-v7a-debug.apk`.

Agora você pode transferir este arquivo para o seu dispositivo Android e instalá-lo.
