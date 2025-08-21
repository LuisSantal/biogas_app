from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.config import Config
from kivy.metrics import dp
import sqlite3
import datetime
from plyer import filechooser
import csv
import os

# Configurações para simulação em desktop (tela de celular)
# Config.set('graphics', 'width', '400')
# Config.set('graphics', 'height', '700')
# Config.set('graphics', 'resizable', True)

# Carrega os arquivos .kv da pasta 'kv'.
Builder.load_file('PythonProject1/kv/login_screen.kv')
Builder.load_file('PythonProject1/kv/main_menu_screen.kv') # Carrega a nova tela de menu
Builder.load_file('PythonProject1/kv/register_waste_screen.kv')
Builder.load_file('PythonProject1/kv/biogas_estimation_screen.kv')
Builder.load_file('PythonProject1/kv/reports_screen.kv')
Builder.load_file('PythonProject1/kv/medidas_screen.kv')

# --- Classes das Telas (Python) ---

class LoginScreen(Screen):
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
                self.manager.current = 'main_menu' # Redireciona para o novo menu principal
            else:
                print("Usuário ou senha inválidos.")
                self.show_popup('Erro de Login', 'Usuário ou senha inválidos.')
        except sqlite3.Error as e:
            print(f"Erro no banco de dados: {e}")
            self.show_popup('Erro no Banco de Dados', f'Ocorreu um erro: {e}')
        finally:
            if conn:
                conn.close()

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
        except sqlite3.IntegrityError:
            print("Usuário já existe.")
            self.show_popup('Erro de Cadastro', 'Este nome de usuário já existe. Escolha outro.')
        except sqlite3.Error as e:
            print(f"Erro no banco de dados: {e}")
            self.show_popup('Erro no Banco de Dados', f'Ocorreu um erro: {e}')
        finally:
            if conn:
                conn.close()

    def show_popup(self, title, message):
        popup = Popup(title=title,
                      content=Label(text=message, halign='center', valign='middle'),
                      size_hint=(0.8, 0.3),
                      auto_dismiss=True)
        popup.open()
        if isinstance(popup.content, Label):
            popup.content.bind(size=lambda *x: setattr(popup.content, 'text_size', popup.content.size))

# --- Nova Classe de Menu Principal ---
class MainMenuScreen(Screen):
    pass # Esta tela apenas contém botões para navegação, sem lógica Python complexa aqui.

# --- As classes RegisterWasteScreen, BiogasEstimationScreen, ReportsScreen e MedidasScreen
# --- permanecem as mesmas que você tem, mas com a alteração no botão "Voltar" no KV
# --- para apontar para 'main_menu' em vez de uma tela específica ou barra inferior.

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
        estimated_biogas = total_waste_weight * 0.04
        avoided_ghg = total_waste_weight * 0.1

        self.ids.biogas_output.text = f'{estimated_biogas:.2f} m³'
        self.ids.ghg_output.text = f'{avoided_ghg:.2f} kg CO2eq'

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

    def load_waste_records(self):
        conn = None
        records = []
        try:
            conn = sqlite3.connect('biogas_app.db')
            c = conn.cursor()
            c.execute("CREATE TABLE IF NOT EXISTS waste_records (date TEXT, category TEXT, weight REAL)")
            c.execute("SELECT date, category, weight FROM waste_records ORDER BY date DESC LIMIT 20")
            records = c.fetchall()
        except sqlite3.Error as e:
            print(f"Erro ao carregar registros de descarte: {e}")
            self.show_popup('Erro de Dados', f'Não foi possível carregar os registros: {e}')
        finally:
            if conn:
                conn.close()

        if self.ids.waste_records_list:
            self.ids.waste_records_list.clear_widgets()

            if records:
                self.ids.waste_records_list.add_widget(
                    Label(text='[b]Data | Categoria | Peso (kg)[/b]',
                          halign='left', text_size=(self.ids.waste_records_list.width - dp(20), None),
                          size_hint_y=None, height=dp(30), markup=True, color=(0.1, 0.1, 0.1, 1))
                )
                for record in records:
                    date_str, category, weight = record
                    formatted_date = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S").strftime("%d/%m/%Y")
                    self.ids.waste_records_list.add_widget(
                        Label(
                            text=f'{formatted_date} | {category} | {weight:.1f} kg',
                            halign='left',
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


class MedidasScreen(Screen):
    def save_measurements(self):
        methane_str = self.ids.methane_input.text
        co2_str = self.ids.co2_input.text
        h2s_str = self.ids.h2s_input.text
        vs_str = self.ids.vs_input.text

        if not all([methane_str, co2_str, h2s_str, vs_str]):
            self.show_popup('Erro de Registro', 'Por favor, preencha todos os campos.')
            return

        try:
            methane = float(methane_str)
            co2 = float(co2_str)
            h2s = float(h2s_str)
            vs = float(vs_str)

            if not all(val >= 0 for val in [methane, co2, h2s, vs]):
                self.show_popup('Erro de Entrada', 'Todos os valores devem ser positivos.')
                return

        except ValueError:
            self.show_popup('Erro de Entrada', 'Valores inválidos. Use apenas números.')
            return

        conn = None
        try:
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
            c.execute("INSERT INTO gas_measurements (date, methane, co2, h2s, volatile_solids) VALUES (?, ?, ?, ?, ?)",
                      (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), methane, co2, h2s, vs))
            conn.commit()
            self.show_popup('Sucesso!', 'Medidas registradas com sucesso!')
            self.ids.methane_input.text = ''
            self.ids.co2_input.text = ''
            self.ids.h2s_input.text = ''
            self.ids.vs_input.text = ''
            print(f"Medidas registradas: CH4={methane}%, CO2={co2}%, H2S={h2s}ppm, SV={vs}%")
        except sqlite3.Error as e:
            print(f"Erro no banco de dados: {e}")
            self.show_popup('Erro no Banco de Dados', f'Ocorreu um erro: {e}')
        finally:
            if conn:
                conn.close()

    def export_measurements_to_csv(self):
        conn = None
        try:
            conn = sqlite3.connect('biogas_app.db')
            c = conn.cursor()
            c.execute("SELECT date, methane, co2, h2s, volatile_solids FROM gas_measurements ORDER BY date DESC")
            records = c.fetchall()

            if not records:
                self.show_popup('Nenhum Dado', 'Não há medidas para exportar.')
                return

            csv_file_path = os.path.join(os.getcwd(), 'gas_measurements.csv')

            with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(['Data', 'Metano (%)', 'Dióxido de Carbono (%)', 'Gás Sulfídrico (ppm)', 'Sólidos Voláteis (%)'])
                csv_writer.writerows(records)

            self.show_popup('Exportação Concluída', f'Medidas exportadas para:\n{csv_file_path}\nVocê pode baixar este arquivo.')
            print(f"Medidas exportadas para: {csv_file_path}")

        except sqlite3.Error as e:
            print(f"Erro ao exportar para CSV: {e}")
            self.show_popup('Erro de Exportação', f'Não foi possível exportar os dados: {e}')
        except Exception as e:
            print(f"Erro inesperado ao exportar: {e}")
            self.show_popup('Erro Inesperado', f'Ocorreu um erro: {e}')
        finally:
            if conn:
                conn.close()

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
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(MainMenuScreen(name='main_menu')) # Adiciona a nova tela de menu
        sm.add_widget(RegisterWasteScreen(name='register_waste'))
        sm.add_widget(BiogasEstimationScreen(name='biogas_estimation'))
        sm.add_widget(ReportsScreen(name='reports'))
        sm.add_widget(MedidasScreen(name='medidas'))

        # A tela inicial do aplicativo
        sm.current = 'login' # O aplicativo começa na tela de login
        return sm

# --- Execução do Aplicativo ---
if __name__ == '__main__':
    BiogasApp().run()