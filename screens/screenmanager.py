from kivymd.uix.dialog import MDDialog
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from database import DataBase
from database_1 import DataBase1
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screen import MDScreen
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
import requests
import json
from bs4 import BeautifulSoup
from kivymd.uix.snackbar import Snackbar
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import OneLineListItem

# class UserName(FakeRectangularElevationBehavior, MDFloatLayout):
#     pass

# class Password(FakeRectangularElevationBehavior, MDFloatLayout):
#     pass
class LoginScreen(MDScreen):
    pass

class LoginScreen1(MDScreen):
    pass

class LoginScreen2(MDScreen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def loginBtn(self):
        if self.email.text != "" and self.password.text != "":
            if db.validate(self.email.text, self.password.text):
                MainWindow.current = self.email.text
                self.reset()
                self.manager.current = "main"            
            else:
                invalidLogin()
        else:
            invalidLogin()

    def reset(self):
        self.email.text = ""
        self.password.text = ""

class LoginScreen3(MDScreen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count("@") == 1 and self.email.text.count(".") > 0:
            if self.password.text != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)
                self.reset()
                self.manager.current = "loginscreen2"
            else:
                invalidForm()
        else:
            invalidForm()

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

class MainWindow(Screen):
    n = ObjectProperty(None)
    f_st = ObjectProperty(None)
    t_st = ObjectProperty(None)
    date = ObjectProperty(None)
    month = ObjectProperty(None)
    day = ObjectProperty(None)
    details = ObjectProperty(None)
    current = ""

    def on_enter(self, *args):
        password, name, created = db.get_user(self.current)
        self.n.text = "Hi, " + name
    def check(self):
        url1 = "https://indianrailways.p.rapidapi.com/findstations.php"
        st1 = self.f_st.text
        querystring1 = {"station":st1}
        headers1 = {
            'x-rapidapi-host': "indianrailways.p.rapidapi.com",
            'x-rapidapi-key': "d1fb13fbb2msh6b11d47bc02c3aep17e760jsn49deee70a758"
            }
        response = requests.request("GET", url1, headers=headers1, params=querystring1)
        i1 = response.__dict__['_content'].decode("utf-8")
        res1 = json.loads(i1)["stations"]

        if len(res1)>1:
            invalidStation()
        else:
            for i1 in res1:
                s = st1
                if i1["stationName"] == s or s in i1["stationName"]:
                    n1 = i1["stationCode"]
            validStation()
    def check2(self):
        url2 = "https://indianrailways.p.rapidapi.com/findstations.php"
        st2 = self.t_st.text
        querystring2 = {"station":st2}
        headers2 = {
            'x-rapidapi-host': "indianrailways.p.rapidapi.com",
            'x-rapidapi-key': "d1fb13fbb2msh6b11d47bc02c3aep17e760jsn49deee70a758"
            }
        response = requests.request("GET", url2, headers=headers2, params=querystring2)
        i2 = response.__dict__['_content'].decode("utf-8")
        res2 = json.loads(i2)["stations"]
        
        if len(res2)>1:
            invalidStation()         
        else:
            for i2 in res2:
                s2 = st2
                if i2["stationName"] == s2 or s2 in i2["stationName"]:
                    n2 = i2["stationCode"]
            validStation()

    def Show(self):
        if self.f_st.text != "" and self.t_st.text != "" and self.date.text != "" and self.month.text != "" and self.day.text != "":
            
            url1 = "https://indianrailways.p.rapidapi.com/findstations.php"
            st1 = self.f_st.text
            querystring1 = {"station":st1}
            headers1 = {
                'x-rapidapi-host': "indianrailways.p.rapidapi.com",
                'x-rapidapi-key': "d1fb13fbb2msh6b11d47bc02c3aep17e760jsn49deee70a758"
                }
            response = requests.request("GET", url1, headers=headers1, params=querystring1)
            i1 = response.__dict__['_content'].decode("utf-8")
            res1 = json.loads(i1)["stations"]

            if len(res1)>1:
                invalidStation()
            else:
                for i1 in res1:
                    s = st1
                    if i1["stationName"] == s or s in i1["stationName"]:
                        n1 = i1["stationCode"]
            url2 = "https://indianrailways.p.rapidapi.com/findstations.php"
            st2 = self.t_st.text
            querystring2 = {"station":st2}
            headers2 = {
                'x-rapidapi-host': "indianrailways.p.rapidapi.com",
                'x-rapidapi-key': "d1fb13fbb2msh6b11d47bc02c3aep17e760jsn49deee70a758"
                }
            response = requests.request("GET", url2, headers=headers2, params=querystring2)
            i2 = response.__dict__['_content'].decode("utf-8")
            res2 = json.loads(i2)["stations"]
            
            if len(res2)>1:
                invalidStation()
                
            else:
                for i2 in res2:
                    s2 = st2
                    if i2["stationName"] == s2 or s2 in i2["stationName"]:
                        n2 = i2["stationCode"]
            def getdata(url):
                r = requests.get(url)
                return r.text
            date = self.date.text
            month = self.month.text
            day = self.day.text
            from_Station_code = n1
            from_Station_name = st1

            To_station_code = n2
            To_station_name = st2
            url = "https://www.railyatri.in/booking/trains-between-stations?from_code="+from_Station_code+"&from_name="+from_Station_name+"JN+&journey_date="+date+"+"+month+"+"+day+"&src=tbs&to_code="+To_station_code+"&to_name="+To_station_name+"+&user_id=-1639744636&user_token=41639744636&utm_source=dwebsearch_tbs_search_trains"

            htmldata = getdata(url)
            soup = BeautifulSoup(htmldata, 'html.parser')

            div = soup.find_all("div", class_="namePart")
  
            l = []
            for i in div:            
                try:
                    j= (i.text)
                    l.append(j)
                except IndexError:
                    pass
            db1.add_train(self.f_st.text, self.t_st.text, self.date.text, self.month.text, self.day.text)
            def z(x):
                z1 = x.text
                print(z1)
                return z1
            # st = z
            # print(st)
            # # z = lambda x: print(x.text)
            #MainWindow.Show.nxt = z
            for i in l:
                
                self.ids.details.add_widget(OneLineListItem(text=i, on_press=z))
            

                
            
            
            self.reset()
        else:
            invalidForm()

    def reset(self):
        self.f_st.text = ""
        self.t_st.text = ""
        self.date.text = ""
        self.month.text = ""
        self.day.text = ""
        from_Station_code = ""
        from_Station_name = ""

        To_station_code = ""
        To_station_name = ""
class MainWindow1(Screen):
    na = ObjectProperty(None)
    def on_enter(self, *args):
        self.na.text = str(MainWindow.Show.nxt)
class MainScreenManager(ScreenManager):
    pass

def invalidLogin():
    d1 = MDDialog(title='Invalid Login',text='Invalid username or password.',radius=[20,20,20,20])                  
    d1.open()

def invalidForm():
    d2 = MDDialog(title='Invalid Form',text='Please fill in all inputs with valid information.',radius=[20,20,20,20])
    d2.open()
def invalidStation():
    Snackbar(
    text="Invalid Station! Try Again..",
    snackbar_x="10dp",
    snackbar_y="10dp",
    ).open()
def validStation():
    Snackbar(
    text="Valid Station!",
    snackbar_x="10dp",
    snackbar_y="10dp",
    ).open()


sm = MainScreenManager()
db = DataBase("users.txt")
db1 = DataBase1("train.txt")
