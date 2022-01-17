import os
from kivymd.app import MDApp
from kaki.app import App
from kivy.factory import Factory
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

Window.size = (1920,1080)
# main app class for kaki app with kivymd modules
class Railway(MDApp, App):

    DEBUG = 0 # set this to 0 make live app not working

    # *.kv files to watch
    KV_FILES = {
        os.path.join(os.getcwd(), "screens\\screenmanager.kv"),
        os.path.join(os.getcwd(), "screens\\login_screen\\loginscreen.kv"),
        os.path.join(os.getcwd(), "screens\\login_screen\\loginscreen1.kv"),
        os.path.join(os.getcwd(), "screens\\login_screen\\loginscreen2.kv"),
        os.path.join(os.getcwd(), "screens\\login_screen\\loginscreen3.kv"),
        os.path.join(os.getcwd(), "screens\\login_screen\\mainwindow.kv"),
        os.path.join(os.getcwd(), "screens\\login_screen\\mainwindow1.kv"),
        os.path.join(os.getcwd(), "screens\\login_screen\\book.kv"),
        os.path.join(os.getcwd(), "screens\\login_screen\\twochoice.kv"),
        os.path.join(os.getcwd(), "screens\\login_screen\\pnrcheck.kv"),
        os.path.join(os.getcwd(), "screens\\login_screen\\payment.kv")
    }

    # class to watch from *.py files
    CLASSES = {
        "MainScreenManager": "screens.screenmanager",
        "LoginScreen": "screens.screenmanager",
        "LoginScreen1": "screens.screenmanager",
        "LoginScreen2": "screens.screenmanager",
        "LoginScreen3": "screens.screenmanager",
        "MainWindow": "screens.screenmanager",
        "MainWindow1": "screens.screenmanager",
        "Book": "screens.screenmanager",
        "Payment": "screens.screenmanager"
    }

    # auto reload path
    AUTORELOADER_PATHS = [
        (".", {"recursive": True}),
    ]

    def build_app(self):
        return Factory.MainScreenManager()
    
    def show(self):
        close = MDFlatButton(text="OK", on_release=self.dialog_close)       
        self.d = MDDialog(title="COVID 19 Alert:",text="\u2022 Passengers are advised to wear a mask, carry sanitizer, and follow social distancing norms\n\n\u2022 All Passenger to kindly note that on arrival at their destination, the traveling passengers will have to adhere to such health protocols as are prescribed by the destination State/UT.For other states, State Govt websites may be visited to ascertain the same.\n\n\u2022 No blanket and linen shall be provided in the train. Although Take Away Bedroll Kit is available in some trains on payment basis.",radius=[20,20,20,20], buttons=[close])
        self.d.open()
    def dialog_close(self, obj):
        self.d.dismiss()

# finally, run the app
if __name__ == "__main__":
    LabelBase.register(name="TPoppins", fn_regular="Poppins-Black.ttf")
    LabelBase.register(name="SPoppins", fn_regular="Poppins-Regular.ttf")
    LabelBase.register(name="BPoppins", fn_regular="Poppins-Medium.ttf")
    LabelBase.register(name="MPoppins", fn_regular="Poppins-Bold.ttf")
    LabelBase.register(name="LPoppins", fn_regular="Poppins-Light.ttf")
    LabelBase.register(name="Signature", fn_regular="D:\\project\\Railway-Reservation-System\\bedtime stories.ttf")
    Railway().run()