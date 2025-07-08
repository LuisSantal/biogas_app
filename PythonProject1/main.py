# main.py

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.config import Config
from kivy.metrics import dp # Importe dp para usar as unidades de densidade de pixel
import sqlite3
import datetime
from plyer import filechooser # Para seleção de arquivos de mídia em dispositivos móveis

# Configurações para simulação em desktop (tela de celular)
Config.set('graphics', 'width', '400') # Largura em pixels (ex: 400px para um smartphone)
Config.set('graphics', 'height', '700') # Altura em pixels (ex: 700px para um smartphone)
Config.set('graphics', 'resizable', False) # Impede que a janela seja redimensionada

# Carrega os arquivos .kv da pasta 'kv'.
# Certifique-se de que o caminho 'kv/' esteja correto em relação a este 'main.py'
Builder.load_file('kv/login_screen.kv')
Builder.load_file('kv/register_waste_screen.kv')
Builder.load_file('kv/biogas_estimation_screen.kv')
Builder.load_file('kv/reports_screen.kv')
# Adicione Builder.load_file() para quaisquer outras telas .kv que você criar

# --- Classes das Telas (Python) ---
# Cada classe Kivy Screen precisa ser definida aqui para que o ScreenManager possa usá-la.

class LoginScreen(Screen):
    # Método para lidar com o login do usuário
    def login(self):
        username = self.ids.user_input.text
        password = self.ids.pass_input.text

        conn = None
        try:
            conn = sqlite3.connect('biogas_app.db')
            c = conn.cursor()
            c.execute("CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)")
            c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
            user = c.fetchone()

            if user:
                print("Login bem-sucedido!")
                self.manager.current = 'register_waste'
            else:
                print("Usuário ou senha inválidos.")
                self.show_popup('Erro de Login', 'Usuário ou senha inválidos.')
        except sqlite3.Error as e:
            print(f"Erro no banco de dados: {e}")
            self.show_popup('Erro no Banco de Dados', f'Ocorreu um erro: {e}')
        finally:
            if conn:
                conn.close()

    # Método para lidar com a criação de conta
    def create_account(self):
        username = self.ids.user_input.text
        password = self.ids.pass_input.text

        if not username or not password:
            self.show_popup('Erro de Cadastro', 'Por favor, preencha o usuário e a senha.')
            return

        conn = None
        try:
            conn = sqlite3.connect('biogas_app.db')
            c = conn.cursor()
            c.execute("CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)")
            c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            print("Conta criada com sucesso!")
            self.show_popup('Sucesso!', 'Conta criada com sucesso! Agora você pode fazer login.')
            self.ids.user_input.text = ''
            self.ids.pass_input.text = ''
        except sqlite3.IntegrityError: # Erro de chave primária duplicada (usuário já existe)
            print("Usuário já existe.")
            self.show_popup('Erro de Cadastro', 'Este nome de usuário já existe. Escolha outro.')
        except sqlite3.Error as e:
            print(f"Erro no banco de dados: {e}")
            self.show_popup('Erro no Banco de Dados', f'Ocorreu um erro: {e}')
        finally:
            if conn:
                conn.close()

    # Função auxiliar para exibir popups
    def show_popup(self, title, message):
        popup = Popup(title=title,
                      content=Label(text=message, halign='center', valign='middle'),
                      size_hint=(0.8, 0.3),
                      auto_dismiss=True)
        popup.open()
        # Centraliza o texto no Label do popup
        if isinstance(popup.content, Label):
            popup.content.bind(size=lambda *x: setattr(popup.content, 'text_size', popup.content.size))


class RegisterWasteScreen(Screen):
    def save_waste(self):
        category = self.ids.food_category_spinner.text
        weight_str = self.ids.weight_input.text

        if category == 'Selecione a categoria' or not weight_str:
            self.show_popup('Erro de Registro', 'Por favor, preencha todos os campos.')
            return

        try:
            weight = float(weight_str)
            if weight <= 0:
                self.show_popup('Erro de Entrada', 'O peso deve ser um valor positivo.')
                return
        except ValueError:
            self.show_popup('Erro de Entrada', 'Peso inválido. Use apenas números.')
            return

        conn = None
        try:
            conn = sqlite3.connect('biogas_app.db')
            c = conn.cursor()
            c.execute("CREATE TABLE IF NOT EXISTS waste_records (date TEXT, category TEXT, weight REAL)")
            c.execute("INSERT INTO waste_records (date, category, weight) VALUES (?, ?, ?)",
                      (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), category, weight))
            conn.commit()
            self.show_popup('Sucesso!', 'Descarte registrado com sucesso!')
            # Limpa os campos após o registro
            self.ids.food_category_spinner.text = 'Selecione a categoria'
            self.ids.weight_input.text = ''
            print(f"Descarte registrado: Categoria={category}, Peso={weight}kg")
        except sqlite3.Error as e:
            print(f"Erro no banco de dados: {e}")
            self.show_popup('Erro no Banco de Dados', f'Ocorreu um erro: {e}')
        finally:
            if conn:
                conn.close()

    def add_media(self):
        try:
            # filters=[("All files", "*.*")] permite qualquer tipo de arquivo
            path = filechooser.open_file(title="Selecione um arquivo de mídia", filters=[
                ("Imagens", "*.png", "*.jpg", "*.jpeg"),
                ("Vídeos", "*.mp4", "*.mov")
            ])
            if path:
                selected_file = path[0]
                file_name = selected_file.split('/')[-1]
                self.show_popup('Mídia Selecionada', f'Mídia: {file_name}')
                print(f"Mídia selecionada: {selected_file}")
            else:
                print("Nenhum arquivo de mídia selecionado.")
        except Exception as e:
            self.show_popup('Erro de Mídia', f'Não foi possível acessar a mídia: {e}\n(Verifique as permissões ou a compatibilidade do Plyer).')

    def show_popup(self, title, message):
        popup = Popup(title=title,
                      content=Label(text=message, halign='center', valign='middle'),
                      size_hint=(0.8, 0.3),
                      auto_dismiss=True)
        popup.open()
        if isinstance(popup.content, Label):
            popup.content.bind(size=lambda *x: setattr(popup.content, 'text_size', popup.content.size))


class BiogasEstimationScreen(Screen):
    def on_enter(self, *args):
        self.update_estimation_data()

    def update_estimation_data(self):
        total_waste_weight = self.calculate_total_waste()
        # Fatores de conversão simulados (ajuste com base em dados reais do manual ou pesquisa)
        # O manual menciona que o biodigestor foi dimensionado para processar
        # [cite_start]aproximadamente 25 kg por semana de resíduos orgânicos[cite: 56].
        # Os fatores de conversão abaixo são exemplos; você precisará de dados mais precisos.
        estimated_biogas = total_waste_weight * 0.04 # Exemplo: 0.04 m³ de biogás por kg de resíduo
        avoided_ghg = total_waste_weight * 0.1 # Exemplo: 0.1 kg CO2eq por kg de resíduo

        self.ids.biogas_output.text = f'{estimated_biogas:.2f} m³'
        self.ids.ghg_output.text = f'{avoided_ghg:.2f} kg CO2eq'

        # Lógica para atualizar a altura do indicador de nível de biogás no KV:
        # A altura do Rectangle com id 'biogas_level_indicator' deve ser atualizada
        # para refletir a proporção do biogás estimado em relação a um valor máximo.
        # Exemplo (necessita de um valor MAX_BIOGAS definido):
        # MAX_BIOGAS = 100.0 # m³
        # if total_waste_weight > 0:
        #     # Calcula a altura como uma fração da altura total do contêiner do tanque
        #     # self.ids.biogas_level_indicator.height = self.ids.biogas_level_container.height * (estimated_biogas / MAX_BIOGAS)
        # else:
        #     # Reseta o nível se não houver resíduos
        #     # self.ids.biogas_level_indicator.height = 0

    def calculate_total_waste(self):
        conn = None
        total_weight = 0
        try:
            conn = sqlite3.connect('biogas_app.db')
            c = conn.cursor()
            c.execute("CREATE TABLE IF NOT EXISTS waste_records (date TEXT, category TEXT, weight REAL)")
            c.execute("SELECT SUM(weight) FROM waste_records")
            result = c.fetchone()
            if result and result[0] is not None:
                total_weight = result[0]
            print(f"Total de resíduos calculados: {total_weight} kg")
        except sqlite3.Error as e:
            print(f"Erro ao calcular total de resíduos: {e}")
        finally:
            if conn:
                conn.close()
        return total_weight

    def show_popup(self, title, message):
        popup = Popup(title=title,
                      content=Label(text=message, halign='center', valign='middle'),
                      size_hint=(0.8, 0.3),
                      auto_dismiss=True)
        popup.open()
        if isinstance(popup.content, Label):
            popup.content.bind(size=lambda *x: setattr(popup.content, 'text_size', popup.content.size))


class ReportsScreen(Screen):
    def on_enter(self, *args):
        self.load_waste_records()
        # Se você for implementar gráficos com kivy_garden.graph, chamaria o método aqui
        # self.update_graphs()

    def load_waste_records(self):
        conn = None
        records = []
        try:
            conn = sqlite3.connect('biogas_app.db')
            c = conn.cursor()
            c.execute("CREATE TABLE IF NOT EXISTS waste_records (date TEXT, category TEXT, weight REAL)")
            c.execute("SELECT date, category, weight FROM waste_records ORDER BY date DESC LIMIT 20") # Últimos 20 registros
            records = c.fetchall()
        except sqlite3.Error as e:
            print(f"Erro ao carregar registros de descarte: {e}")
            self.show_popup('Erro de Dados', f'Não foi possível carregar os registros: {e}')
        finally:
            if conn:
                conn.close()

        # Limpa widgets antigos antes de adicionar os novos
        # Certifica-se de que self.ids.waste_records_list existe e é um BoxLayout (ou similar)
        if self.ids.waste_records_list:
            self.ids.waste_records_list.clear_widgets()

            if records:
                # Adiciona um cabeçalho para a lista
                self.ids.waste_records_list.add_widget(
                    Label(text='[b]Data | Categoria | Peso (kg)[/b]',
                          halign='left', text_size=(self.ids.waste_records_list.width - dp(20), None), # Ajustado
                          size_hint_y=None, height=dp(30), markup=True, color=(0.1, 0.1, 0.1, 1))
                )
                for record in records:
                    date_str, category, weight = record
                    # Formata a data para exibir apenas dia/mês/ano ou como preferir
                    formatted_date = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S").strftime("%d/%m/%Y")
                    self.ids.waste_records_list.add_widget(
                        Label(
                            text=f'{formatted_date} | {category} | {weight:.1f} kg',
                            halign='left',
                            # Ajusta para o tamanho do BoxLayout pai, considerando padding
                            text_size=(self.ids.waste_records_list.width - dp(20), None),
                            size_hint_y=None,
                            height=dp(25),
                            color=(0.3, 0.3, 0.3, 1)
                        )
                    )
            else:
                self.ids.waste_records_list.add_widget(
                    Label(text='Nenhum registro de descarte ainda.', color=(0.5, 0.5, 0.5, 1))
                )
        else:
            print("Erro: Widget 'waste_records_list' não encontrado na tela de relatórios.")

    def show_popup(self, title, message):
        popup = Popup(title=title,
                      content=Label(text=message, halign='center', valign='middle'),
                      size_hint=(0.8, 0.3),
                      auto_dismiss=True)
        popup.open()
        if isinstance(popup.content, Label):
            popup.content.bind(size=lambda *x: setattr(popup.content, 'text_size', popup.content.size))


# --- Classe Principal do Aplicativo Kivy ---
class BiogasApp(App):
    def build(self):
        # Cria o ScreenManager que gerenciará as diferentes telas do app
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(RegisterWasteScreen(name='register_waste'))
        sm.add_widget(BiogasEstimationScreen(name='biogas_estimation'))
        sm.add_widget(ReportsScreen(name='reports'))
        # Adicione aqui qualquer outra tela que você criar

        # A tela inicial do aplicativo
        return sm

# --- Execução do Aplicativo ---
if __name__ == '__main__':
    BiogasApp().run()