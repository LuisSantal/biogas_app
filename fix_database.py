#!/usr/bin/env python3
"""
Script para corrigir problemas no banco de dados do aplicativo Biogás nas Escolas
"""

import sqlite3
import os

def fix_database():
    """Corrige problemas no banco de dados"""
    
    db_path = 'PythonProject1/biogas_app.db'
    
    if not os.path.exists(db_path):
        print(f"Erro: Banco de dados não encontrado em {db_path}")
        return False
    
    try:
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        
        print("Conectado ao banco de dados...")
        
        # 1. Criar tabela gas_measurements se não existir
        print("Verificando tabela gas_measurements...")
        c.execute("""
            CREATE TABLE IF NOT EXISTS gas_measurements (
                date TEXT,
                methane REAL,
                co2 REAL,
                h2s REAL,
                volatile_solids REAL
            )
        """)
        print("✓ Tabela gas_measurements criada/verificada")
        
        # 2. Verificar estrutura da tabela waste_records
        print("Verificando tabela waste_records...")
        c.execute("PRAGMA table_info(waste_records)")
        waste_columns = [col[1] for col in c.fetchall()]
        print(f"Colunas de waste_records: {waste_columns}")
        
        # 3. Verificar estrutura da tabela users
        print("Verificando tabela users...")
        c.execute("PRAGMA table_info(users)")
        users_columns = [col[1] for col in c.fetchall()]
        print(f"Colunas de users: {users_columns}")
        
        # 4. Verificar dados existentes
        print("\nDados existentes:")
        
        # Users
        c.execute("SELECT COUNT(*) FROM users")
        user_count = c.fetchone()[0]
        print(f"Total de usuários: {user_count}")
        
        # Waste records
        c.execute("SELECT COUNT(*) FROM waste_records")
        waste_count = c.fetchone()[0]
        print(f"Total de registros de resíduos: {waste_count}")
        
        # Gas measurements
        c.execute("SELECT COUNT(*) FROM gas_measurements")
        gas_count = c.fetchone()[0]
        print(f"Total de medições de gás: {gas_count}")
        
        conn.commit()
        conn.close()
        
        print("\n✓ Banco de dados verificado e corrigido com sucesso!")
        return True
        
    except sqlite3.Error as e:
        print(f"Erro no banco de dados: {e}")
        return False

def create_sample_data():
    """Cria dados de exemplo para teste"""
    
    try:
        conn = sqlite3.connect('PythonProject1/biogas_app.db')
        c = conn.cursor()
        
        print("Criando dados de exemplo...")
        
        # Dados de exemplo para waste_records
        sample_waste = [
            ('2024-01-15 10:30:00', 'Frutas', 5.2),
            ('2024-01-16 14:45:00', 'Vegetais', 3.8),
            ('2024-01-17 09:15:00', 'Carnes', 2.1),
        ]
        
        c.executemany(
            "INSERT INTO waste_records (date, category, weight) VALUES (?, ?, ?)",
            sample_waste
        )
        print("✓ Dados de resíduos de exemplo criados")
        
        # Dados de exemplo para gas_measurements
        sample_gas = [
            ('2024-01-15 16:20:00', 65.5, 30.2, 150, 68.3),
            ('2024-01-16 17:30:00', 62.8, 32.1, 180, 65.7),
        ]
        
        c.executemany(
            "INSERT INTO gas_measurements (date, methane, co2, h2s, volatile_solids) VALUES (?, ?, ?, ?, ?)",
            sample_gas
        )
        print("✓ Dados de medições de gás de exemplo criados")
        
        conn.commit()
        conn.close()
        
        print("✓ Dados de exemplo criados com sucesso!")
        return True
        
    except sqlite3.Error as e:
        print(f"Erro ao criar dados de exemplo: {e}")
        return False

if __name__ == "__main__":
    print("=== CORREÇÃO DO BANCO DE DADOS ===\n")
    
    # Corrigir estrutura do banco
    if fix_database():
        # Perguntar se deseja criar dados de exemplo
        resposta = input("\nDeseja criar dados de exemplo? (s/n): ")
        if resposta.lower() == 's':
            create_sample_data()
    
    print("\n=== CORREÇÃO CONCLUÍDA ===")
