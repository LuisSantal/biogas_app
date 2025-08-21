#!/usr/bin/env python3
"""
Teste completo do aplicativo Biogás nas Escolas
Testa todas as funcionalidades antes do build
"""

import sqlite3
import sys
import os
from unittest.mock import Mock, patch

# Adicionar o diretório PythonProject1 ao path
sys.path.insert(0, 'PythonProject1')

def test_database():
    """Testa a estrutura e dados do banco de dados"""
    print("=== TESTE DO BANCO DE DADOS ===")
    
    try:
        conn = sqlite3.connect('PythonProject1/biogas_app.db')
        c = conn.cursor()
        
        # Verificar tabelas
        c.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = [table[0] for table in c.fetchall()]
        print(f"✓ Tabelas encontradas: {tables}")
        
        # Verificar dados
        for table in tables:
            c.execute(f"SELECT COUNT(*) FROM {table}")
            count = c.fetchone()[0]
            print(f"✓ {table}: {count} registros")
        
        conn.close()
        return True
        
    except Exception as e:
        print(f"✗ Erro no banco de dados: {e}")
        return False

def test_imports():
    """Testa se todos os imports funcionam"""
    print("\n=== TESTE DE IMPORTS ===")
    
    try:
        # Testar imports principais
        from kivy.app import App
        from kivy.uix.screenmanager import ScreenManager, Screen
        from kivy.lang import Builder
        import sqlite3
        import datetime
        from plyer import filechooser
        
        print("✓ Todos os imports funcionam")
        return True
        
    except ImportError as e:
        print(f"✗ Erro de import: {e}")
        return False

def test_screen_classes():
    """Testa se as classes de tela podem ser instanciadas"""
    print("\n=== TESTE DE CLASSES DE TELA ===")
    
    try:
        # Mock para evitar problemas de inicialização do Kivy
        with patch('kivy.app.App'), patch('kivy.uix.screenmanager.ScreenManager'):
            # Importar e testar classes
            from main import LoginScreen, MainMenuScreen, RegisterWasteScreen
            from main import BiogasEstimationScreen, ReportsScreen, MedidasScreen
            
            # Testar instanciação
            screens = [
                LoginScreen(name='test'),
                MainMenuScreen(name='test'), 
                RegisterWasteScreen(name='test'),
                BiogasEstimationScreen(name='test'),
                ReportsScreen(name='test'),
                MedidasScreen(name='test')
            ]
            
            print("✓ Todas as classes de tela podem ser instanciadas")
            return True
            
    except Exception as e:
        print(f"✗ Erro nas classes de tela: {e}")
        return False

def test_kv_files():
    """Testa se os arquivos KV existem e são válidos"""
    print("\n=== TESTE DE ARQUIVOS KV ===")
    
    kv_files = [
        'PythonProject1/kv/login_screen.kv',
        'PythonProject1/kv/main_menu_screen.kv',
        'PythonProject1/kv/register_waste_screen.kv', 
        'PythonProject1/kv/biogas_estimation_screen.kv',
        'PythonProject1/kv/reports_screen.kv',
        'PythonProject1/kv/medidas_screen.kv'
    ]
    
    all_exists = True
    for kv_file in kv_files:
        if os.path.exists(kv_file):
            print(f"✓ {kv_file} existe")
        else:
            print(f"✗ {kv_file} não encontrado")
            all_exists = False
    
    return all_exists

def test_assets():
    """Testa se os assets existem"""
    print("\n=== TESTE DE ASSETS ===")
    
    assets = [
        'PythonProject1/assets/images/app_icon.png'
    ]
    
    all_exists = True
    for asset in assets:
        if os.path.exists(asset):
            print(f"✓ {asset} existe")
        else:
            print(f"✗ {asset} não encontrado")
            all_exists = False
    
    return all_exists

def test_requirements():
    """Testa se os requirements estão consistentes"""
    print("\n=== TESTE DE REQUIREMENTS ===")
    
    try:
        with open('PythonProject1/requirements.txt', 'r') as f:
            requirements = f.read()
        
        # Verificar se as principais dependências estão listadas
        # sqlite3 não precisa estar nos requirements pois é parte da stdlib
        required = ['kivy', 'plyer']
        missing = []
        
        for req in required:
            if req not in requirements.lower():
                missing.append(req)
        
        if missing:
            print(f"✗ Requirements faltando: {missing}")
            return False
        else:
            print("✓ Requirements consistentes")
            return True
            
    except Exception as e:
        print(f"✗ Erro ao verificar requirements: {e}")
        return False

def run_complete_test():
    """Executa todos os testes"""
    print("🧪 EXECUTANDO TESTE COMPLETO DO APLICATIVO\n")
    
    tests = [
        test_database,
        test_imports, 
        test_screen_classes,
        test_kv_files,
        test_assets,
        test_requirements
    ]
    
    results = []
    for test in tests:
        try:
            result = test()
            results.append(result)
        except Exception as e:
            print(f"✗ Erro inesperado no teste: {e}")
            results.append(False)
    
    print("\n" + "="*50)
    print("📊 RESULTADO DOS TESTES")
    print("="*50)
    
    passed = sum(results)
    total = len(results)
    
    print(f"Testes passados: {passed}/{total}")
    
    if passed == total:
        print("🎉 TODOS OS TESTES PASSARAM! O aplicativo está pronto para build.")
        return True
    else:
        print("⚠️  Alguns testes falharam. Verifique os problemas acima.")
        return False

if __name__ == "__main__":
    success = run_complete_test()
    sys.exit(0 if success else 1)
