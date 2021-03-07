from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json, glob
from datetime import datetime
from pathlib import Path
import random

# Builder.load_file('main.kv')

# All  classes match the  markup by the same name in the kv file  
# And control the methods tied to root in the kv file  

class LoginScreen(Screen):
    # self refers to this class and the properties from Screen 
    def sign_up(self):
        self.manager.current = "sign_up_screen"
    def login(self,userN, passW):
        # remove white spaces in the verification 
        user_name = userN.strip()
        pass_word = passW.strip()
        
        with open('users.json') as file:
            users = json.load(file)
            if user_name in users and users[user_name]['password'] ==  pass_word:
                self.manager.current = 'login_screen_success'
            else:
                self.ids.login_wrong.text = "Wrong username or password"
            

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
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"

class LoginScreenSuccess(Screen):
    def go_log_out(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'login_screen'
    def get_quote(self, feel):
        feel = feel.strip().lower()
        available_feelings = glob.glob('quotes/*')
        #  using the glob mod to  access all the files in the directory 
        # then using path libray  and the stem method to extract the file names
        available_feelings =[Path(filename).stem for filename 
                            in available_feelings]
        
        #  now check our array for valid feelings 
        if feel in available_feelings:
            with open(f"quotes/{feel}.txt") as file:
                quotes = file.readlines()
            # access the space in the ky file with our matching id
            # random.choice is a built in method that accepts a list 
            self.ids.quote.text = random.choice(quotes)
        else:
            self.ids.quote.text = "Pick a different feeling"
        
        
        
class MainApp(App):
    def build(self):
        return RootWidget()
    
    
if __name__ == "__main__":
    MainApp().run()
