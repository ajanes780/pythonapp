from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json
from datetime import datetime

Builder.load_file('main.kv')


class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "sign_up_screen"

class RootWidget(ScreenManager):
    pass 

class SignUpScreen(Screen):
    def add_user(self, u_name, p_word):
        with open ("users.json") as file:
            users = json.load(file)
                
        users[u_name.strip()] = {'username':u_name.strip(),
                         'password':p_word.strip(),
                         'created':datetime.now().strftime("%Y-%m-%d %H-%M-%S" )}
        
        with open ('users.json', 'w') as file:
            json.dump(users, file)        
        self.manager.current = "sign_up_screen_success"
        
        
class SignUpScreenSuccess(Screen):
    def go_to_login(self):
        self.manager.current = "login_screen"
    pass

class MainApp(App):
    def build(self):
        return RootWidget()
    
    
if __name__ == "__main__":
    MainApp().run()
