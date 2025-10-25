# Instruções para Gerar APK do Biogás nas Escolas

## Problemas Identificados no Projeto

### 1. **Problemas de Build no Windows**
- O Buildozer não funciona corretamente no Windows para builds Android
- Apenas o target "ios" está disponível
- Python-for-Android não está instalado corretamente

### 2. **Problemas no Código**
- **Falta da tabela `gas_measurements`** no banco de dados
- **Propriedades depreciadas do Kivy** que podem causar warnings
- **Caminhos hardcoded** no buildozer.spec original

### 3. **Solução Recomendada**
Usar **Google Colab** para fazer o build do APK, que é a abordagem mais confiável para Windows.

## Método 1: Google Colab (Recomendado)

### Passo a Passo:

1. **Acesse o Google Colab**: https://colab.research.google.com/

2. **Faça upload do notebook**:
   - Arquivo: `colab_build_apk.ipynb`
   - No Colab, clique em "Arquivo" → "Fazer upload do notebook"

3. **Execute o notebook**:
   - Execute cada célula sequencialmente
   - Quando solicitado, faça upload do arquivo: `biogas_app_colab.zip`

4. **Aguarde o build**:
   - O processo pode levar 20-40 minutos
   - O Colab instalará todas as dependências automaticamente

5. **Faça download do APK**:
   - Após o build concluído, o APK será baixado automaticamente
   - O arquivo estará na pasta `bin/` com nome `biogasapp-0.1-arm64-v8a-debug.apk`

## Método 2: Correções Manuais (Avançado)

### Correções Necessárias no Código:

1. **Adicionar tabela gas_measurements**:
```python
# Adicione este código no método save_measurements() da classe MedidasScreen
# ou execute manualmente no banco de dados:
conn = sqlite3.connect('biogas_app.db')
c = conn.cursor()
c.execute("""
    CREATE TABLE IF NOT EXISTS gas_measurements (
        date TEXT,
        methane REAL,
        co2 REAL,
        h2s REAL,
        volatile_solids REAL
    )
""")
conn.commit()
conn.close()
```

2. **Corrigir propriedades depreciadas do Kivy**:
- Verifique e atualize qualquer propriedade marcada como depreciada

### Para Build Local (Linux/macOS apenas):

1. **Instale Buildozer corretamente**:
```bash
pip install buildozer
sudo apt-get install -y \
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
```

2. **Configure JAVA_HOME**:
```bash
export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
export PATH=$JAVA_HOME/bin:$PATH
```

3. **Execute o build**:
```bash
buildozer android debug
```

## Arquivos Gerados para Colab

- `colab_build_apk.ipynb`: Notebook do Google Colab pronto para uso
- `biogas_app_colab.zip`: Arquivo ZIP com todos os arquivos do projeto

## Estrutura do Projeto Corrigida

```
biogas_app/
├── PythonProject1/
│   ├── main.py              # Aplicativo principal
│   ├── requirements.txt     # Dependências
│   ├── kv/                  # Interface Kivy
│   ├── assets/              # Recursos visuais
│   └── biogas_app.db        # Banco de dados
├── buildozer.spec           # Configuração de build corrigida
├── build_apk_colab.py       # Script de preparação para Colab
├── colab_build_apk.ipynb    # Notebook para Google Colab
└── biogas_app_colab.zip     # Arquivo ZIP para upload
```

## Observações Importantes

1. **O build no Windows é problemático** - Use Google Colab
2. **Verifique se a tabela gas_measurements existe** antes de usar a funcionalidade
3. **Teste o APK** em um dispositivo Android após o build
4. **Para produção**, considere usar GitHub Actions para builds automáticos

## Suporte

Se encontrar problemas:
1. Verifique os logs do Colab
2. Confirme se todos os arquivos foram incluídos no ZIP
3. Certifique-se de que o banco de dados tem a tabela gas_measurements
