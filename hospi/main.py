import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.list import OneLineIconListItem
from kivymd.icon_definitions import md_icons
from kivymd.toast import toast
from kivy.uix.anchorlayout import AnchorLayout
import tempfile
import time
import os
from kivy.uix.screenmanager import ScreenManager , Screen,FadeTransition
from kivy.properties import ObjectProperty,NumericProperty,StringProperty
import re
from kivymd.uix.bottomsheet import MDListBottomSheet
from kivy.uix.progressbar import ProgressBar
from kivy.core.text import Label as CoreLabel
from kivy.lang.builder import Builder
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.clock import Clock
from kivy.core.window import Window
import time
from datetime import datetime
import calendar
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFlatButton,MDRaisedButton
from kivymd.uix.bottomsheet import MDCustomBottomSheet
from kivy.factory import Factory
from kivy.uix.boxlayout import BoxLayout
kivy.require('1.11.1')

k=Builder.load_file('hospi1.kv')
class ZeroWindow(Screen):
    t = time.asctime()
    pass

class FirstWindow(Screen):
    dialog= None
    t = time.asctime()
    #def current(self,screen):
     #   self.current=screen

    def submit(self):
        ffg = open("fees.text", "a+")
        fm = open("fees.text", "r")
        ffg1 = open("date.text", "a+")
        m = open("date.text", "r")

        ce = fm.readlines()
        cm = m.readlines()


        j = len(cm)

        if '\n' in ce:
            ce.remove("\n")

        else:
            pass
        if j==0:
            g=0
        else:

            if cm[j - 2] == cm[j - 1]:

                ge = map(int, ce)
                gh = list(ge)
                je = len(gh)
                if gh == []:
                    g = 0
                else:
                    g = sum(gh)
                # print(g)

            else:
                g=0
                m = open("date.text", "r+")
                m.truncate()
                m.close()
                fm = open("fees.text", "r+")
                fm.truncate()
                fm.close()
                je=len(ce)
                f11 = open("date.text", "a+").write(cm[j - 1])
                fe1 = open("fees.text", "a+").write(ce[je - 1])


        if not self.dialog:
            self.dialog = MDDialog(
                title="Daily Report",
                text="Daily Report"+"\nToday Total Number Patient:-  "+str(j)+"\nToday Total Income:-"+str(g),
                buttons=[
                    MDRaisedButton(
                        text="CANCEL",on_release = self.close_dialog
                    ),

                ],
            )
        self.dialog.open()
        fm.close()
        m.close()


    def close_dialog(self,obj):

        self.dialog.dismiss()


        #self.pop.text="Daily Report"+"\nToday Total Number Patient:-  "+str(j)+"\nToday Total Income:-"+str(g)
    pass
class SecondWindow(Screen):
    #autocomplete for clinical features
    fw=[]
    def callback_for_menu_items(self, *args):
        self.fw.append(args[0]+",")
        fg=''
        self.clin.text=fg.join(self.fw)
        toast(f"You are Selected -:{args[0]}")

    def show_example_list_bottom_sheet(self):
        f = self.clin.text

        ff = open("clinical.text","r")
        sd = []
        for g in ff:

            sd.append(g.strip())
        #f1 = ['achin', 'sachin', 'niki','zh']
        jj=sd
        if f == " ":

            d=jj



        else:


            d = []
            gf=len(f)
            for i in jj:
                if f[(gf-1)].lower() in i.lower():
                    d.append(i)


        bottom_sheet_menu = MDListBottomSheet()
        for j in d:
            bottom_sheet_menu.add_item(
                f"{j}",
                lambda x, y=j: self.callback_for_menu_items(
                    y

                ),

            )
        bottom_sheet_menu.open()
    # autocomplete box for dignosis
    def dignosis(self):
        f = self.diag.text

        ff = open("diagnosis.text", "r")
        sd = []
        for g in ff:
            sd.append(g.strip())
        # f1 = ['achin', 'sachin', 'niki','zh']
        jj = sd
        if f == " ":

            d = jj



        else:
            d = []
            gf = len(f)
            for i in jj:
                if f[(gf - 1)].lower() in i.lower():
                    d.append(i)

        bottom_sheet_menu = MDListBottomSheet()
        for j in d:
            bottom_sheet_menu.add_item(
                f"{j}",
                lambda x, y=j: self.callback_for_diagnosis(
                    y

                ),

            )
        bottom_sheet_menu.open()

    fwd = []

    def callback_for_diagnosis(self, *args):
        self.fwd.append(args[0] + ",")
        fg = ''
        self.diag.text = fg.join(self.fwd)
        toast(f"You are Selected -:{args[0]}")

    # autocomplete box for tretment
    def tretment(self):
        f = self.trea.text

        ff = open("tretment.text", "r")
        sd = []
        for g in ff:
            sd.append(g.strip())
        # f1 = ['achin', 'sachin', 'niki','zh']
        jj = sd
        if f == " ":

            d = jj



        else:
            d = []
            gf = len(f)
            for i in jj:
                if f[(gf - 1)].lower() in i.lower():
                    d.append(i)

        bottom_sheet_menu = MDListBottomSheet()
        for j in d:
            bottom_sheet_menu.add_item(
                f"{j}",
                lambda x, y=j: self.callback_for_tretment(
                    y

                ),

            )
        bottom_sheet_menu.open()

    fwt = []

    def callback_for_tretment(self, *args):
        self.fwt.append(args[0] + ",")
        fg = ''
        self.trea.text = fg.join(self.fwt)
        toast(f"You are Selected -:{args[0]}")

    def submit(self):
        t = time.asctime()
        su=self.pn.text
        #su1 = self.tt.text
        #su2 = self.pat.text
        su3 = self.gen.text
        su4 = self.mn.text
        su5 = self.add.text
        su6 = self.birt.text
        su7 = self.ag.text
        su8 = self.com.text
        su9 = self.clin.text

        su10 = self.diag.text

        su11 = self.inv.text
        su12 = self.trea.text
        su13 = self.datt.text
        su14 = self.fee.text
        #self.su = self.lp.hint_text
        #print(self.su)

        savetemp1 ="Date & Time -:"+t+"\nPatient Name -:"+su+"\nMobile Number-:"+su4+"      "+"Gender -:"+su3+"\nAddress -:"+su5+"\nBirthday -:"+su6+"      "+"Age :-"+su7
        savetemp2 = "\nComment -:"+su8+"\nClinical Feature -:"+su9+"\nDiagnosis -:"+su10+"\nInvestigation -:"+su11+"\nTreatmanet -:"+su12+"\nFollow up to Date -:"+su13+"       "+"Fees -:"+su14
        savetemp3 ="\n===================================================================================================================================="
        file=savetemp1+savetemp2+savetemp3
        if su=="" or su3=="" or su4==""or su5=="" or su6=="" or su7=="" or su8=="" or su9=="" or su10=="" or su11=="" or su12=="" or su13=="" or su14=="":
            toast("you miss somthing to write above box")
        else:

            dw=str(su) + '.text'
            f=open(dw,"a+").write(file)

            df=su+"\n"
            f1=open("patient list.text","a+").write(df)
            #fd=str(self.su)
            toast("File is being save by the name-:"+ dw)

            dfe=su+" -: "+su14
            fe = open("patient name & fees.text", "a+").write(dfe)

            #daily progress report
            f = datetime.now()
            # print(f.strftime('%B'))# only month print in output
            # for month write %B year %Y,day %d
            df = str(f.strftime('%d'))
            #print(df)
            de = str(su14) + '\n'
            d = df + '\n'
            f11 = open("date.text", "a+").write(d)


            fe1 = open("fees.text", "a+").write(de)

            dfm = str(f.strftime('%B'))
            # print(df)
            dem = str(su14) + '\n'
            dm = dfm + '\n'
            f11m = open("month.text", "a+").write(dm)

            fe1m = open("monthly fees.text", "a+").write(dem)

            # for year report
            dy = str(f.strftime('%y'))
            # print(df)
            dey = str(su14) + '\n'
            dmy = dy + '\n'
            fy1 = open("year.text", "a+").write(dmy)
            fey1 = open("yearly fees.text", "a+").write(dey)
            #clear text
            self.pn.text=" "

            self.gen.text=" "
            self.mn.text=" "
            self.add.text=" "
            self.birt.text=" "
            self.ag.text=" "
            self.com.text=" "
            self.clin.text=" "

            self.diag.text=" "

            self.inv.text=" "
            self.trea.text=" "
            self.datt.text=" "
            self.fee.text=" "

    t = time.asctime()
    pass
class ThirdWindow(Screen):
    t =time.asctime()

    def callback_for_menu_items(self, *args):
        self.searc.text=args[0]
        toast(f"You Selcted -:{args[0]}")

    def show_example_list_bottom_sheet(self):
        f = self.searc.text

        ff = open("patient list.text")
        sd = []
        for g in ff:

            sd.append(g.strip())
        #f1 = ['achin', 'sachin', 'niki','zh']
        jj=sd
        if f == " ":
            d = jj
        else:
            d = []
            for i in jj:
                if f.lower() in i.lower():
                    d.append(i)
        bottom_sheet_menu = MDListBottomSheet()
        for j in d:
            bottom_sheet_menu.add_item(
                f"{j}",
                lambda x, y=j: self.callback_for_menu_items(
                    y

                ),

            )
        bottom_sheet_menu.open()

    def hell(self):
        f1 = self.searc.text
        if f1 == "":
            toast("First write patient name in search box")
        else:
            ff = open("search.text", "w+")
            ff.truncate(0)
            ff.write(f1)
            ff.close()
            self.searc.text=""

class FourthWindow(Screen):
    g= "hell"

    t = time.asctime()

    def old(self):
        ffg = open("search.text", "a+")
        f3 = open("search.text", "r")
        for f1 in f3:
            if f1=="":
                toast("First write patient name in search box")
            else:
                sdf=str(f1)+".text"
                f2=open(sdf).read()

#os.startfile()
                self.hel.text=f2
        f3.close()
    # autocomplete for clinical features
    fw = []

    def callback_for_menu_items(self, *args):
        self.fw.append(args[0] + ",")
        fg = ''
        self.clin.text = fg.join(self.fw)
        toast(f"You are Selected -:{args[0]}")

    def show_example_list_bottom_sheet(self):
        f = self.clin.text

        ff = open("clinical.text", "r")
        sd = []
        for g in ff:
            sd.append(g.strip())
        # f1 = ['achin', 'sachin', 'niki','zh']
        jj = sd
        if f == " ":

            d = jj



        else:
            d = []
            gf = len(f)
            if gf == 0:

                self.clin.text = ""
            else:
                for i in jj:
                    if f[(gf - 1)].lower() in i.lower():
                        d.append(i)

        bottom_sheet_menu = MDListBottomSheet()
        for j in d:
            bottom_sheet_menu.add_item(
                f"{j}",
                lambda x, y=j: self.callback_for_menu_items(
                    y

                ),

            )
        bottom_sheet_menu.open()

    # autocomplete box for dignosis
    def dignosis(self):
        f = self.diag.text

        ff = open("diagnosis.text", "r")
        sd = []
        for g in ff:
            sd.append(g.strip())
        # f1 = ['achin', 'sachin', 'niki','zh']
        jj = sd
        if f == " ":

            d = jj



        else:
            d = []
            gf = len(f)
            if gf == 0:

                self.diag.text = ""
            else:
                for i in jj:
                    if f[(gf - 1)].lower() in i.lower():
                        d.append(i)

        bottom_sheet_menu = MDListBottomSheet()
        for j in d:
            bottom_sheet_menu.add_item(
                f"{j}",
                lambda x, y=j: self.callback_for_diagnosis(
                    y

                ),

            )
        bottom_sheet_menu.open()

    fwd = []

    def callback_for_diagnosis(self, *args):
        self.fwd.append(args[0] + ",")
        fg = ''
        self.diag.text = fg.join(self.fwd)
        toast(f"You are Selected -:{args[0]}")

    # autocomplete box for tretment
    def tretment(self):
        f = self.treat.text

        ff = open("tretment.text", "r")
        sd = []
        for g in ff:
            sd.append(g.strip())
        # f1 = ['achin', 'sachin', 'niki','zh']
        jj = sd
        if f == " ":

            d = jj



        else:
            d = []
            gf = len(f)
            if gf == 0:

                self.treat.text = ""
            else:
                for i in jj:
                    if f[(gf - 1)].lower() in i.lower():
                        d.append(i)

        bottom_sheet_menu = MDListBottomSheet()
        for j in d:
            bottom_sheet_menu.add_item(
                f"{j}",
                lambda x, y=j: self.callback_for_tretment(
                    y

                ),

            )
        bottom_sheet_menu.open()

    fwt = []

    def callback_for_tretment(self, *args):
        self.fwt.append(args[0] + ",")
        fg = ''
        self.treat.text = fg.join(self.fwt)
        toast(f"You are Selected -:{args[0]}")

    def add(self):
        c1=self.clin.text
        c2=self.diag.text
        c3=self.inves.text
        c4=self.treat.text
        c5=self.fud.text
        c6=self.fee.text
        fg=open("search.text","a+")
        f3 = open("search.text", "r")
        for f1 in f3:
            sdf = str(f1) + ".text"
        savetemp2 = "----------Patient next Treatment---------" + "\nClinical Feature -:" + c1 + "\nDiagnosis -:" + c2 + "\nInvestigation -:" + c3 + "\nTreatment -:" + c4 + "\nFollow up to Date -:" + c5+"    "+"Fees -:"+c6
        savetemp3 = "\n===================================================================================================================================="
        file = savetemp2 + savetemp3
        if c1=="" or c2=="" or c3=="" or c4=="" or c5=="" or c6=="":
            toast("you miss somthing to write above box")
        else:
            f2 = open(sdf,"a+").write(file)
            # daily progress report
            f = datetime.now()
            # print(f.strftime('%B'))# only month print in output
            # for month write %B year %Y,day %d
            df = str(f.strftime('%d'))
            # print(df)
            de = str(c6) + '\n'
            d = df + '\n'
            f11 = open("date.text", "a+").write(d)

            fe1 = open("fees.text", "a+").write(de)

            dfm = str(f.strftime('%B'))
            # print(df)
            dem = str(c6) + '\n'
            dm = dfm + '\n'
            f11m = open("month.text", "a+").write(dm)

            fe1m = open("monthly fees.text", "a+").write(dem)

            # for year report
            dy = str(f.strftime('%y'))
            # print(df)
            dey = str(c6) + '\n'
            dmy = dy + '\n'
            fy1 = open("year.text", "a+").write(dmy)
            fey1 = open("yearly fees.text", "a+").write(dey)

            self.clin.text=""
            self.diag.text=""
            self.inves.text=""
            self.treat.text=""
            self.fud.text=""
            self.fee.text=""
            self.hel.text=""
        f3.close()
class FifthWindow(Screen):
    t = time.asctime()
    def clinical(self):
        df=self.clin.text
        f1 = open("clinical.text", "a+").write(df+'\n')
        # fd=str(self.su)
        toast("Clinical Feature save by the name-:" + df)
        self.clin.text = " "
    def Diagnosis(self):
        df=self.diag.text
        f1 = open("Diagnosis.text", "a+").write(df+'\n')
        # fd=str(self.su)
        toast("Diagnosis save by the name-:" + df)
        self.diag.text = " "

    def Treatment(self):
        df=self.treat.text
        f1 = open("treatment.text", "a+").write(df+'\n')
        # fd=str(self.su)
        toast("Treatment save by the name-:" + df)
        self.treat.text = " "
class SixWindow(Screen):
    t = time.asctime()
    Window.clearcolor=(1,1,1,1)
    ffg=open("monthly fees.text", "a+")
    fm = open("monthly fees.text", "r")
    ffg1 = open("month.text", "a+")
    m = open("month.text", "r")

    ce = fm.readlines()
    cm = m.readlines()

    j = len(cm)

    if '\n' in ce:
        ce.remove("\n")

    else:
        pass
    if j==0:
        g=0
        pass
    else:
        if cm[j - 2] == cm[j - 1]:

            ge = map(int, ce)
            gh = list(ge)
            je = len(gh)
            if gh == []:
                g = 0
            else:
                g = sum(gh)
            # print(g)

        else:
            g = 0
            m = open("month.text", "r+")
            m.truncate()
            m.close()
            fm = open("monthly fees.text", "r+")
            fm.truncate()
            fm.close()
            je = len(ce)
            f11 = open("month.text", "a+").write(cm[j - 1])
            fe1 = open("monthly fees.text", "a+").write(ce[je - 1])
    df = "Monthly Report\n"  + "Total number of patient:-" + str(j)+"\nTotal Income:-"+str(g)

    #Yearly report genrate
    fmg1 = open("yearly fees.text", "a+")
    fm1 = open("yearly fees.text", "r")
    mg1 = open("year.text", "a+")
    m1 = open("year.text", "r")

    ce1 = fm1.readlines()
    cm1 = m1.readlines()

    j1 = len(cm1)

    if '\n' in ce1:
        ce1.remove("\n")

    else:
        pass
    if j1==0:
        g1=0
        pass
    else:
        if cm1[j1 - 2] == cm1[j1 - 1]:

            ge1 = map(int, ce1)
            gh1 = list(ge1)
            je1 = len(gh1)
            if gh1 == []:
                g1 = 0
            else:
                g1 = sum(gh1)
            # print(g)

        else:
            g1 = 0
            m1 = open("year.text", "r+")
            m1.truncate()
            m1.close()
            fm1 = open("yearly fees.text", "r+")
            fm1.truncate()
            fm1.close()
            je1 = len(ce1)
            f111 = open("year.text", "a+").write(cm1[j1 - 1])
            fe11 = open("yearly fees.text", "a+").write(ce1[je1 - 1])
    df1 = "Yearly Report\n" + "Total number of patient:-" + str(j1) + "\nTotal Income:-" + str(g1)

class SevenWindow(Screen):
    t = time.asctime()


    def callback_for_menu_items(self, *args):
        self.searc.text=args[0]
        toast(f"You Selcted -:{args[0]}")

    def show_example_list_bottom_sheet(self):
        f = self.searc.text

        ff = open("Operated patient list.text")
        sd = []
        for g in ff:

            sd.append(g.strip())
        #f1 = ['achin', 'sachin', 'niki','zh']
        jj=sd
        if f == " ":
            d = jj
        else:
            d = []
            for i in jj:
                if f.lower() in i.lower():
                    d.append(i)
        bottom_sheet_menu = MDListBottomSheet()
        for j in d:
            bottom_sheet_menu.add_item(
                f"{j}",
                lambda x, y=j: self.callback_for_menu_items(
                    y

                ),

            )
        bottom_sheet_menu.open()

    def Auto(self):
        f = self.searc.text

        ff = open("Operated patient list.text")
        sd = []
        for g in ff:

            sd.append(g.strip())
        jj=sd

        if f == " ":
            d = jj
        else:
            d = []
            for i in jj:
                if f.lower() in i.lower():
                    d.append(i)
    def hell(self):
        f1 = self.searc.text
        if f1=="":
            toast("Write patient name in search box ")
        else:

            ff = open("Operated search.text", "w+")
            ff.truncate(0)
            ff.write(f1)
            ff.close()
            self.searc.text=""

    def callback_for_menu_items1(self, *args):
        self.searc1.text=args[0]
        toast(f"You Selcted -:{args[0]}")

    def show_example_list_bottom_sheet1(self):
        f = self.searc1.text

        ff = open("Non-Operated patient list.text")
        sd = []
        for g in ff:

            sd.append(g.strip())
        #f1 = ['achin', 'sachin', 'niki','zh']
        jj=sd
        if f == " ":
            d = jj
        else:
            d = []
            for i in jj:
                if f.lower() in i.lower():
                    d.append(i)
        bottom_sheet_menu = MDListBottomSheet()
        for j in d:
            bottom_sheet_menu.add_item(
                f"{j}",
                lambda x, y=j: self.callback_for_menu_items1(
                    y

                ),

            )
        bottom_sheet_menu.open()

    def Auto1(self):
        f = self.searc1.text

        ff = open("Non-Operated patient list.text")
        sd = []
        for g in ff:

            sd.append(g.strip())
        jj=sd
        #f1 = ['achin', 'sachin', 'niki']
        if f == " ":
            d = jj
        else:
            d = []
            for i in jj:
                if f.lower() in i.lower():
                    d.append(i)
    screenmanager=ObjectProperty()
    def hell1(self,*args):
        f1 = self.searc1.text
        if f1=="":
            toast("Write patient name in search box ")
        else:

            ff = open("Non-Operated search.text", "w+")
            ff.truncate(0)
            ff.write(f1)
            ff.close()
            self.searc1.text=""


    pass
class EightWindow(Screen):
    t = time.asctime()

    # autocomplete box for dignosis
    def dignosis(self):
        f = self.diag.text

        ff = open("diagnosis1.text", "r")
        sd = []
        for g in ff:
            sd.append(g.strip())
        # f1 = ['achin', 'sachin', 'niki','zh']
        jj = sd
        if f == " ":

            d = jj



        else:
            d = []
            gf = len(f)

            if gf==0:

                self.diag.text=""
            else:
                for i in jj:
                    if f[(gf - 1)].lower() in i.lower():
                        d.append(i)

        bottom_sheet_menu = MDListBottomSheet()
        for j in d:
            bottom_sheet_menu.add_item(
                f"{j}",
                lambda x, y=j: self.callback_for_diagnosis(
                    y

                ),

            )
        bottom_sheet_menu.open()

    fwd = []

    def callback_for_diagnosis(self, *args):
        self.fwd.append(args[0] + ",")
        fg = ''
        self.diag.text = fg.join(self.fwd)
        toast(f"You are Selected -:{args[0]}")

    def submit(self):
        t = time.asctime()
        su=self.pn.text
        #su1 = self.tt.text
        #su2 = self.pat.text
        su3 = self.gen.text
        su4 = self.mn.text
        su5 = self.add.text
        su6 = self.birt.text
        su7 = self.ag.text
        su8 = self.com.text


        su10 = self.diag.text

        su13 = self.datt.text
        su14 = self.fee.text



        #self.su = self.lp.hint_text
        #print(self.su)
        savetemp1 ="Date & Time -:"+t+"\nPatient Name -:"+su+"\nMobile Number-:"+su4+"      "+"Gender -:"+su3+"\nAddress -:"+su5+"\nBirthday -:"+su6+"      "+"Age :-"+su7
        savetemp2 = "\nDiagnosis -:"+su10+"\nComment -:"+su8+"\nFollow up to Date -:"+su13+"       "+"Fees -:"+su14
        savetemp3 ="\n===================================================================================================================================="
        file=savetemp1+savetemp2+savetemp3
        if su=="" or su3=="" or su4==""or su5=="" or su6=="" or su7=="" or su8=="" or su10=="" or su13=="" or su14=="":
            toast("you miss somthing to write above box")
        else:
            dw=str(su) + '.text'
            f=open(dw,"a+").write(file)
            df=su+"\n"
            f1=open("Operated patient list.text","a+").write(df)
            #fd=str(self.su)
            toast("File is being save by the name-:"+ dw)
            dfe=su+" -: "+su14
            fe = open("Operated patient name & fees.text", "a+").write(dfe)
            f = datetime.now()
            # print(f.strftime('%B'))# only month print in output
            # for month write %B year %Y,day %d
            df = str(f.strftime('%d'))
            # print(df)
            de = str(su14) + '\n'
            d = df + '\n'
            f11 = open("Operated date.text", "a+").write(d)
            fe1 = open("Operated fees.text", "a+").write(de)
            dfm = str(f.strftime('%B'))
            # print(df)
            dem = str(su14) + '\n'
            dm = dfm + '\n'
            f11m = open("Operated month.text", "a+").write(dm)
            fe1m = open("Operated monthly fees.text", "a+").write(dem)
            # for year report
            dy = str(f.strftime('%y'))
            # print(df)
            dey = str(su14) + '\n'
            dmy = dy + '\n'
            fy1 = open("Operated year.text", "a+").write(dmy)
            fey1 = open("Operated yearly fees.text", "a+").write(dey)
            self.pn.text=""

            self.gen.text=""
            self.mn.text=""
            self.add.text=""
            self.birt.text=""
            self.ag.text=""
            self.com.text=""

            self.diag.text=""

            self.datt.text=""
            self.fee.text=""
    pass

class NineWindow(Screen):
    t = time.asctime()

    # autocomplete box for dignosis
    def dignosis(self):
        f = self.diag.text

        ff = open("diagnosis1.text", "r")
        sd = []
        for g in ff:
            sd.append(g.strip())
        # f1 = ['achin', 'sachin', 'niki','zh']
        jj = sd
        if f == " ":

            d = jj



        else:
            d = []
            gf = len(f)
            if gf == 0:

                self.diag.text = ""
            else:
                for i in jj:
                    if f[(gf - 1)].lower() in i.lower():
                        d.append(i)

        bottom_sheet_menu = MDListBottomSheet()
        for j in d:
            bottom_sheet_menu.add_item(
                f"{j}",
                lambda x, y=j: self.callback_for_diagnosis(
                    y

                ),

            )
        bottom_sheet_menu.open()

    fwd = []

    def callback_for_diagnosis(self, *args):
        self.fwd.append(args[0] + ",")
        fg = ''
        self.diag.text = fg.join(self.fwd)
        toast(f"You are Selected -:{args[0]}")

    def submit(self):
        t = time.asctime()
        su=self.pn.text
        #su1 = self.tt.text
        #su2 = self.pat.text
        su3 = self.gen.text
        su4 = self.mn.text
        su5 = self.add.text
        su6 = self.birt.text
        su7 = self.ag.text
        su8 = self.com.text

        su10 = self.diag.text
        su13 = self.datt.text


        #self.su = self.lp.hint_text
        #print(self.su)
        savetemp1 ="Date & Time -:"+t+"\nPatient Name -:"+su+"\nMobile Number-:"+su4+"      "+"Gender -:"+su3+"\nAddress -:"+su5+"\nBirthday -:"+su6+"      "+"Age :-"+su7
        savetemp2 = "\nDiagnosis -:"+su10+"\nComment -:"+su8+"\nFollow up to Date -:"+su13
        savetemp3 ="\n===================================================================================================================================="
        file=savetemp1+savetemp2+savetemp3
        if su=="" or su3=="" or su4==""or su5=="" or su6=="" or su7=="" or su8==""  or su10=="" or su13=="" :
            toast("you miss somthing to write above box")
        else:
            dw=str(su) + '.text'
            f=open(dw,"a+").write(file)
            df=su+"\n"
            f1=open("Non-Operated patient list.text","a+").write(df)
            #fd=str(self.su)
            toast("File is being save by the name-:"+ dw)

            f = datetime.now()
            # print(f.strftime('%B'))# only month print in output
            # for month write %B year %Y,day %d
            df = str(f.strftime('%d'))
            # print(df)

            d = df + '\n'
            f11 = open("Non-Operated date.text", "a+").write(d)

            dfm = str(f.strftime('%B'))
            # print(df)

            dm = dfm + '\n'
            f11m = open("Non-Operated month.text", "a+").write(dm)

            # for year report
            dy = str(f.strftime('%y'))
            # print(df)

            dmy = dy + '\n'
            fy1 = open("Non-Operated year.text", "a+").write(dmy)
            self.pn.text = ""

            self.gen.text = ""
            self.mn.text = ""
            self.add.text = ""
            self.birt.text = ""
            self.ag.text = ""
            self.com.text = ""

            self.diag.text = ""

            self.datt.text = ""


class TenWindow(Screen):
    t = time.asctime()

    def old(self):
        f3 = open("Operated search.text", "r")
        for f1 in f3:
            if f1=="":
                toast("First write patient name in search box")
            else:
                sdf = str(f1) + ".text"
                f2 = open(sdf).read()

        # os.startfile()
                self.hel.text = f2
    def dignosis(self):
        f = self.diag.text

        ff = open("diagnosis1.text", "r")
        sd = []
        for g in ff:
            sd.append(g.strip())
        # f1 = ['achin', 'sachin', 'niki','zh']
        jj = sd
        if f == " ":

            d = jj



        else:
            d = []
            gf = len(f)
            for i in jj:
                if f[(gf - 1)].lower() in i.lower():
                    d.append(i)

        bottom_sheet_menu = MDListBottomSheet()
        for j in d:
            bottom_sheet_menu.add_item(
                f"{j}",
                lambda x, y=j: self.callback_for_diagnosis(
                    y

                ),

            )
        bottom_sheet_menu.open()

    fwd = []

    def callback_for_diagnosis(self, *args):
        self.fwd.append(args[0] + ",")
        fg = ''
        self.diag.text = fg.join(self.fwd)
        toast(f"You are Selected -:{args[0]}")

    def add(self):

        c2 = self.diag.text
        c3 = self.com.text

        c5 = self.fud.text
        c6 = self.fee.text
        f3 = open("Operated search.text", "r")
        for f1 in f3:
            sdf = str(f1) + ".text"
        savetemp2 = "----------Patient next Treatment---------" + "\nDiagnosis -:" + c2 + "\nComment -:" + c3  + "\nFollow up to Date -:" + c5 + "    " + "Fees -:" + c6
        savetemp3 = "\n===================================================================================================================================="
        file = savetemp2 + savetemp3
        if c2=="" or c3=="" or c5=="" or c6=="":
            toast("you miss somthing to write above box")
        else:
            f2 = open(sdf, "a+").write(file)
            f = datetime.now()
            # print(f.strftime('%B'))# only month print in output
            # for month write %B year %Y,day %d
            df = str(f.strftime('%d'))
            # print(df)
            de = str(c6) + '\n'
            d = df + '\n'
            f11 = open("Operated date.text", "a+").write(d)
            fe1 = open("Operated fees.text", "a+").write(de)
            dfm = str(f.strftime('%B'))
            # print(df)
            dem = str(c6) + '\n'
            dm = dfm + '\n'
            f11m = open("Operated month.text", "a+").write(dm)
            fe1m = open("Operated monthly fees.text", "a+").write(dem)
            # for year report
            dy = str(f.strftime('%y'))
            # print(df)
            dey = str(c6) + '\n'
            dmy = dy + '\n'
            fy1 = open("Operated year.text", "a+").write(dmy)
            fey1 = open("Operated yearly fees.text", "a+").write(dey)
            self.diag.text=""
            self.com.text=""

            self.fud.text=""
            self.fee.text=""
            self.hel.text=""
class ElevenWindow(Screen):
    t = time.asctime()

    def old(self):
        f3 = open("Non-Operated search.text", "r")
        for f1 in f3:
            if f1=="":
                toast("First write patient name in search box")
            else:
                sdf = str(f1) + ".text"
                f2 = open(sdf).read()

        # os.startfile()
                self.hel.text = f2
    def dignosis(self):
        f = self.diag.text

        ff = open("diagnosis1.text", "r")
        sd = []
        for g in ff:
            sd.append(g.strip())
        # f1 = ['achin', 'sachin', 'niki','zh']
        jj = sd
        if f == " ":

            d = jj



        else:
            d = []
            gf = len(f)
            for i in jj:
                if f[(gf - 1)].lower() in i.lower():
                    d.append(i)

        bottom_sheet_menu = MDListBottomSheet()
        for j in d:
            bottom_sheet_menu.add_item(
                f"{j}",
                lambda x, y=j: self.callback_for_diagnosis(
                    y

                ),

            )
        bottom_sheet_menu.open()

    fwd = []

    def callback_for_diagnosis(self, *args):
        self.fwd.append(args[0] + ",")
        fg = ''
        self.diag.text = fg.join(self.fwd)
        toast(f"You are Selected -:{args[0]}")

    def add(self):

        c2 = self.diag.text
        c3 = self.com.text

        c5 = self.fud.text

        f3 = open("Non-Operated search.text", "r")
        for f1 in f3:
            sdf = str(f1) + ".text"
        savetemp2 = "----------Patient next Treatment---------" + "\nDiagnosis -:" + c2 + "\nComment -:" + c3 + "\nFollow up to Date -:" + c5
        savetemp3 = "\n===================================================================================================================================="
        file = savetemp2 + savetemp3
        if c2=="" or c3=="" or c5=="" :
            toast("you miss somthing to write above box")
        else:
            f2 = open(sdf, "a+").write(file)
            f = datetime.now()
            # print(f.strftime('%B'))# only month print in output
            # for month write %B year %Y,day %d
            df = str(f.strftime('%d'))
            # print(df)

            d = df + '\n'
            f11 = open("Non-Operated date.text", "a+").write(d)

            dfm = str(f.strftime('%B'))
            # print(df)

            dm = dfm + '\n'
            f11m = open("Non-Operated month.text", "a+").write(dm)

            # for year report
            dy = str(f.strftime('%y'))
            # print(df)

            dmy = dy + '\n'
            fy1 = open("Non-Operated year.text", "a+").write(dmy)
            self.diag.text = ""
            self.com.text = ""

            self.fud.text = ""
            self.hel.text = ""
class TwelveWindow(Screen):
    t = time.asctime()
    def add(self):
        df = self.diag.text
        f1 = open("Diagnosis1.text", "a+").write(df + '\n')
        # fd=str(self.su)
        toast("Diagnosis save by the name-:" + df)
        self.diag.text = " "

class hos(MDApp):

    dialog=None
    t=time.asctime()
    x="hi"
    gf=str(t)
    #def time(self):
     #   self.root.ids.time.text = f'{str(time.asctime())}'

    def build(self):
        #kivy icon change
        self.icon="dig.png"

        sm=ScreenManager()
        sm.add_widget(ZeroWindow(name='zero'))
        sm.add_widget(FirstWindow(name='first'))
        sm.add_widget(SecondWindow(name="second"))
        sm.add_widget(ThirdWindow(name="third"))
        sm.add_widget(FourthWindow(name="fourth"))
        sm.add_widget(FifthWindow(name="fifth"))
        sm.add_widget(SixWindow(name="six"))
        sm.add_widget(SevenWindow(name="seven"))
        sm.add_widget(EightWindow(name="eight"))
        sm.add_widget(NineWindow(name="nine"))
        sm.add_widget(TenWindow(name="ten"))
        sm.add_widget(ElevenWindow(name="eleven"))
        sm.add_widget(TwelveWindow(name="twelve"))
        return sm

    custom_sheet = None

    def show_example_custom_bottom_sheet(self):
        self.custom_sheet = MDCustomBottomSheet(screen=Factory.ContentCustomSheet())
        self.custom_sheet.open()
    dialog = None
    # daily report code
    strp = []
    fgm = open("Operated fees.text", "a+")
    fm = open("Operated fees.text", "r")
    ce = fm.readlines()
    gm = open("Operated date.text", "a+")
    m = open("Operated date.text", "r")
    cm = m.readlines()


    jxa = len(cm)
    if '\n' in ce:
        ce.remove("\n")
    else:
        pass

    if jxa==0:
        gxa=0
    else:
        if cm[jxa - 2] == cm[jxa - 1]:

            ge = map(int, ce)
            # print(strp)
            gh = list(ge)
            je=len(gh)
            if gh == []:
                gxa = 0
            else:
                gxa = sum(gh)
            # print(g)

        else:
            gxa=0
            m = open("Operated date.text", "r+")
            m.truncate()
            m.close()
            fm = open("Operated fees.text", "r+")
            fm.truncate()
            fm.close()
            je=len(ce)
            f11 = open("Operated date.text", "a+").write(cm[jxa - 1])
            fe1 = open("Operated fees.text", "a+").write(ce[je - 1])

    # monthly report code
    fgm1 = open("Operated monthly fees.text", "a+")
    fm1 = open("Operated monthly fees.text", "r")
    ce1 = fm1.readlines()
    gm1 = open("Operated month.text", "a+")
    m1 = open("Operated month.text", "r")
    cm1 = m1.readlines()


    jxa1 = len(cm1)
    if '\n' in ce1:
        ce1.remove("\n")

    else:
        pass
    if jxa1==0:
        gxa1=0
    else:
        if cm1[jxa1 - 2] == cm1[jxa1 - 1]:

            ge1 = map(int, ce1)
            # print(strp)
            gh1 = list(ge1)
            je1=len(gh1)
            if gh1 == []:
                gxa1 = 0
            else:
                gxa1 = sum(gh1)
            # print(g)

        else:
            gxa1=0
            m1 = open("Operated month.text", "r+")
            m1.truncate()
            m1.close()
            fm1 = open("Operated monthly fees.text", "r+")
            fm1.truncate()
            fm1.close()
            je1=len(ce1)
            f111 = open("Operated month.text", "a+").write(cm1[jxa1 - 1])
            fe11 = open("Operated monthly fees.text", "a+").write(ce1[je1 - 1])

    # Yearly report code
    fgm2 = open("Operated yearly fees.text", "a+")
    fm2 = open("Operated yearly fees.text", "r")
    ce2 = fm2.readlines()
    gm2 = open("Operated year.text", "a+")
    m2 = open("Operated year.text", "r")
    cm2 = m2.readlines()

    if '\n' in ce2:
        ce2.remove("\n")

    else:
        pass
    jxa2 = len(cm2)
    if jxa2==0:
        gxa2=0
    else:
        if cm2[jxa2 - 2] == cm2[jxa2 - 1]:

            ge2 = map(int, ce2)
            # print(strp)
            gh2 = list(ge2)
            je2=len(gh2)
            if gh2 == []:
                gxa2 = 0
            else:
                gxa2 = sum(gh2)
            # print(g)

        else:
            gxa=0
            m2 = open("Operated year.text", "r+")
            m2.truncate()
            m2.close()
            fm2 = open("Operated yearly fees.text", "r+")
            fm2.truncate()
            fm2.close()
            je2=len(ce2)
            f112 = open("Operated year.text", "a+").write(cm2[jxa2 - 1])
            fe12 = open("Operated yearly fees.text", "a+").write(ce2[je2 - 1])

    def Daily(self):

        if not self.dialog:
            self.dialog = MDDialog(
                title="Daily Report",
                text="Daily Report" + "\nToday Total Number Patient:-  " + str(
                    self.jxa) + "\nToday Total Income:-" + str(self.gxa),
                buttons=[
                    MDRaisedButton(
                        text="CANCEL", on_release=self.close_dialog
                    ),

                ],
            )
        self.dialog.open()
    log=None
    def Yearly(self):

        if not self.log:
            self.log = MDDialog(
                title="Yearly Report",
                text="Yearly Report" + "\nToday Total Number Patient:-  " + str(
                    self.jxa2) + "\nToday Total Income:-" + str(self.gxa2),
                buttons=[
                    MDRaisedButton(
                        text="CANCEL", on_release=self.close_log
                    ),

                ],
            )
        self.log.open()
    dial=None
    def Monthly(self):

        if not self.dial:
            self.dial = MDDialog(
                title="Monthly Report",
                text="Monthly Report" + "\nToday Total Number Patient:-  " + str(
                    self.jxa1) + "\nToday Total Income:-" + str(self.gxa1),
                buttons=[
                    MDRaisedButton(
                        text="CANCEL", on_release=self.close_dial
                    ),

                ],
            )
        self.dial.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()
    def close_log(self, obj):
        self.log.dismiss()
    def close_dial(self, obj):
        self.dial.dismiss()

if __name__ == '__main__':
    hos().run()