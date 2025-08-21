#!/usr/bin/env python3
"""
Script para gerar APK do aplicativo Biogás nas Escolas usando Google Colab
Este script pode ser executado no Google Colab para construir o APK
"""

import os
import shutil
import zipfile
import requests

def prepare_colab_script():
    """Prepara um script para ser executado no Google Colab"""
    
    colab_script = """# Build APK para Biogás nas Escolas no Google Colab

# Instalar Buildozer
!pip install buildozer

# Instalar dependências do sistema
!sudo apt update
!sudo apt install -y \
    git \
    zip \
    unzip \
    openjdk-17-jdk \
    python3-pip \
    autoconf \
    libtool \
    pkg-config \
    zlib1g-dev \
    libncurses5-dev \
    libncursesw5-dev \
    libtinfo5 \
    cmake \
    libffi-dev \
    libssl-dev

# Configurar variáveis de ambiente
import os
os.environ['JAVA_HOME'] = '/usr/lib/jvm/java-17-openjdk-amd64'
os.environ['PATH'] = f"{os.environ['JAVA_HOME']}/bin:{os.environ['PATH']}"

# Clonar o repositório (substitua pela URL do seu repositório)
!git clone https://github.com/seu-usuario/biogas_app.git
%cd biogas_app

# Copiar arquivos do projeto para o Colab
# (Você precisará fazer upload dos arquivos manualmente ou conectar com Google Drive)

# Criar buildozer.spec se não existir
!buildozer init

# Configurar buildozer.spec para Android
buildozer_spec = '''
[app]
title = Biogás nas Escolas
package.name = biogasapp
package.domain = br.edu.unila
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,db
source.include_patterns = assets/*,kv/*,media/*
version = 0.1
requirements = python3,kivy==2.3.1,plyer,sqlite3
orientation = portrait
fullscreen = 0
android.permissions = INTERNET,CAMERA,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE
android.api = 30
android.minapi = 21
android.ndk_api = 21
android.accept_sdk_license = True
android.arch = arm64-v8a
android.allow_backup = True

[buildozer]
log_level = 2
'''

with open('buildozer.spec', 'w') as f:
    f.write(buildozer_spec)

# Fazer o build do APK
!buildozer -v android debug

# Verificar se o APK foi criado
import glob
apk_files = glob.glob('bin/*.apk')
if apk_files:
    print(f"APK criado com sucesso: {apk_files[0]}")
    # Fazer download do APK
    from google.colab import files
    files.download(apk_files[0])
else:
    print("Erro: APK não foi criado")
"""

    # Salvar o script
    with open('colab_build_apk.ipynb', 'w') as f:
        f.write(colab_script)
    
    print("Script para Google Colab criado: colab_build_apk.ipynb")
    print("1. Abra o Google Colab: https://colab.research.google.com/")
    print("2. Faça upload deste arquivo .ipynb")
    print("3. Execute todas as células")
    print("4. Faça upload dos arquivos do projeto quando solicitado")
    print("5. O APK será baixado automaticamente")

def create_zip_for_colab():
    """Cria um arquivo ZIP com todos os arquivos do projeto para upload no Colab"""
    
    zip_filename = "biogas_app_colab.zip"
    
    # Arquivos e pastas para incluir
    include_files = [
        'PythonProject1/main.py',
        'PythonProject1/requirements.txt',
        'PythonProject1/kv/',
        'PythonProject1/assets/',
        'PythonProject1/biogas_app.db'
    ]
    
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for item in include_files:
            if os.path.isdir(item):
                for root, dirs, files in os.walk(item):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, os.path.dirname(item))
                        zipf.write(file_path, arcname)
            elif os.path.isfile(item):
                zipf.write(item, os.path.basename(item))
    
    print(f"Arquivo ZIP criado: {zip_filename}")
    print("Faça upload deste arquivo no Google Colab quando solicitado")

if __name__ == "__main__":
    print("Preparando build para Google Colab...")
    prepare_colab_script()
    create_zip_for_colab()
    print("\nInstruções completas:")
    print("1. Execute o script no Google Colab")
    print("2. Faça upload do arquivo ZIP quando solicitado")
    print("3. Aguarde o build ser concluído")
    print("4. Faça download do APK gerado")
