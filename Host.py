import os
import random
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen,ScreenManager,SlideTransition
import socket
import json
from kivymd.uix.button import MDRaisedButton
import threading
from kivymd.uix.dialog import MDDialog
from kivy.uix.boxlayout import BoxLayout
import time
kk='''
<Screen1>:
    name:'screen1'
    MDLabel:
        text:'Developed by Znydee.....+2347034599042,Znydee01@gmail.com'
        font_size:20
        halign:'center'
        pos_hint:{'center_y':0.03}
    BoxLayout:
        orientation:'vertical'
        size_hint:(.7,.7)
        pos_hint:{'center_x':0.5,'center_y':0.7}
        spacing:100
        BoxLayout:
            spacing:20
            MDTextField:
                id:fil
                background_active:self.background_normal
            MDRaisedButton:
                theme_text_color:'Custom'
                bold:True
                font_size:30 
                md_bg_color:(0,0,0,1)
                text:'Choose file'
                on_press:app.choosefile()
        MDRaisedButton:
            text:'Create Server'
            bold:True
            font_size:60 
            pos_hint:{'center_x':0.5}
            md_bg_color:(0,0,0,1)  
            on_press:
                root.manager.current = "screen1b"
    
<Screen1b>:
	name:"screen1b"
	BoxLayout:
        orientation:'vertical'
        size_hint:(.7,.7)
        pos_hint:{'center_x':0.5,'center_y':0.7}
        spacing:100
        BoxLayout:
            spacing:20
            MDLabel:
                text:'Number of candidates'
                size_hint_y:None
                height:self.texture_size[1]
                font_size:30
                bold:True
            MDTextField:
                id:fila
                background_active:self.background_normal
        MDRaisedButton:
            text:'continue'
            bold:True
            font_size:60 
            pos_hint:{'center_x':0.5}
            md_bg_color:(0,0,0,1)  
            on_press:app.kkl()
<Screen1c>:
	name:"screen1c"
    GridLayout:
        pos_hint:{'center_x':0.6}
	    padding:20
	    spacing:5
	    cols:2
	    MDLabel:
	        text:'Scripts recieved'
	        font_size:30
	        bold:True
	    MDLabel:
	        id:filaa
	        text:''
	        font_size:30
	        bold:True
	    Widget:
	MDLabel:
        id:fi
        text:''
        halign:'center'
        pos_hint:{'center_y':0.6}
        font_size:30
        bold:True
    MDBoxLayout:
        id:mdt
        size_hint:(.25,.1)
        pos_hint:{'center_x':.5,'center_y':0.3}
        MDRaisedButton:
            id:mr
            text:'Save scripts'
            font_size:20
            bold:True
            md_bg_color:(0, 0, 0, 1)
            on_press:app.dial()
        
<Screen2>:
	name:"screen2"
	FileChooserIconView:
    	id:filechooser
    	on_selection:app.selected(filechooser.selection) 
    	
<Screen3>:   
	name:"screen3"
	GridLayout:
	    padding:20
	    spacing:5
	    cols:2
	    MDLabel:
	        text:'Hostname'
	        font_size:30
	        bold:True
	    MDLabel:
	        id:hos
	        text:''
	        font_size:30
	        bold:True
	    MDLabel:
	        text:'State'
	        font_size:30
	        bold:True
	    MDLabel:
	        id:ins
	        halign:'left'
	        text:'Accepting connections...please, do not press any key on the keyboard'
	        font_size:30
	        bold:True
	    MDLabel:
	        id:inss
	        text:'Connected'
	        font_size:30
	        bold:True
	    MDLabel:
	        id:inss
	        text:''
	        font_size:30
	        bold:True
	    Widget:	
    MDRaisedButton:
        size_hint:(.25,.1)
        pos_hint:{'center_x':.5,'center_y':0.1}
        text:'Begin Exam >>>'
        font_size:20
        bold:True
        md_bg_color:(0, 0, 0, 1)
        on_press:app.ppk()
<Content>:
	size_hint_y:None
	spacing:20
	height:150
	MDTextField:
		id:ss1
		text:''
		background_active:self.background_normal       
'''
class Screen1(Screen):
    pass
class Screen1b(Screen):
    pass
class Screen1c(Screen):
    def on_enter(self):
        th2.start()
class Screen2(Screen):
    pass
class Screen3(Screen):
    def on_enter(self):
        sm.get_screen("screen3").ids.inss.text = f'0 of {int(sm.get_screen("screen1b").ids.fila.text)}'
class Content(BoxLayout):
	pass
class MainApp(MDApp):
    def choosefile(self):
        sm.current = "screen2"

    def dial(self):
        self.dialog = MDDialog(title='Enter filename', type='custom', content_cls=Content(),
                               buttons=[MDRaisedButton(text='save', on_press=self.ppp)])
        self.dialog.open()

    def ppp(self, obj):
        ww = self.dialog.content_cls.ids.ss1.text
        par=os.getcwd()
        new_d='scripts'
        new_path=os.path.join(par,new_d)
        try:
            os.mkdir(new_path)
            with open(f'{new_path}/{ww}.json', 'w') as file:
                mii=json.dump(client_answers, file)
        except:
            with open(f'{new_path}/{ww}.json', 'w') as file:
                mii=json.dump(client_answers, file)
        self.dialog.dismiss()
        sm.current = "screen1c"
        self.root.get_screen("screen1c").ids.fi.text ='scripts have been saved successfully'
        self.root.get_screen("screen1c").ids.mdt.remove_widget(self.root.get_screen("screen1c").ids.mr)
        btn=MDRaisedButton(text='Close',font_size=20,bold=True,md_bg_color=(0, 0, 0, 1),on_press=self.eer)
        self.root.get_screen("screen1c").ids.mdt.add_widget(btn)
    def eer(self,obj):
        self.stop()
    def ppk(self):
        if len(connected_users)>0:
            for conn in connected_users:
                conn.send(MainApp.selected.dat)
                sm.current = 'screen1c'
                print(MainApp.selected.dat,'has been sent')
        else:
            pass

    def selected(self, filename):
        if ".json" in filename[0]:
            self.root.get_screen("screen1").ids.fil.text=filename[0]
            with open(filename[0],'rb') as file:
                file_data=json.load(file)
                print('0ld file data', file_data)
                for every in file_data["questions"]:
                    random.shuffle(every["Ans"])
                print('new file data', file_data)
                MainApp.selected.dat=str.encode(json.dumps(file_data))
            sm.current="screen1"
        else:
            pass
    def kkl(self):
        global host
        host = socket.gethostname()
        self.root.get_screen("screen3").ids.hos.text = host
        sm.current='screen3'
        th1.start()
    def jj(self):
        pass
    def build(self):
        global sm,connected_users,client_answers
        client_answers=[]
        sm=ScreenManager()
        connected_users=[]
        self.theme_cls.theme_style = "Dark"
        Builder.load_string(kk)
        sm.add_widget(Screen1(name='screen1'))
        sm.add_widget(Screen1b(name='screen1b'))
        sm.add_widget(Screen1c(name='screen1c'))
        sm.add_widget(Screen2(name='screen2'))
        sm.add_widget(Screen3(name='screen3'))
        return sm
    def cc(self):
        global s
        s = socket.socket()

        port = 8080
        s.bind((host, port))
        s.listen(200)

        while len(connected_users) < int(sm.get_screen("screen1b").ids.fila.text):
            conn, addr = s.accept()
            connected_users.append(conn)
            sm.get_screen("screen3").ids.inss.text = f'{len(connected_users)} of {int(sm.get_screen("screen1b").ids.fila.text)}'
            print(addr, 'has connected')
            print(int(sm.get_screen("screen1b").ids.fila.text))
        sm.get_screen("screen3").ids.ins.text = 'All connections has been successfully accepted...you can now proceed'
        sm.get_screen("screen1c").ids.filaa.text = f'0 of {int(sm.get_screen("screen1b").ids.fila.text)} submitted'
    def dd(self):
        while len(client_answers) < int(sm.get_screen("screen1b").ids.fila.text):
            for connn in connected_users:
                mag=connn.recv(1024)
                if mag == None:
                    pass
                else:
                    lii=mag.decode()
                    slii=json.loads(lii)
                    if slii in client_answers:
                        pass
                    else:
                        client_answers.append(slii)
                        print(slii)
                        print(client_answers)
                        connn.send(str.encode('successfully recieved'))
                        print('successfully recieved')
                        sm.get_screen("screen1c").ids.filaa.text = f'{len(client_answers)} of {int(sm.get_screen("screen1b").ids.fila.text)} recieved'
th1=threading.Thread(target=MainApp.cc, args=(1,))
th2=threading.Thread(target=MainApp.dd, args=(1,))
MainApp().run()