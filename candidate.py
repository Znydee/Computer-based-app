import random
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen,ScreenManager,SlideTransition
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.dialog import MDDialog
from kivy.clock import Clock
from kivymd.uix.button import MDRaisedButton
import json
from kivymd.uix.card import MDCard
from kivy.uix.button import Button
from kivy.uix.button import ButtonBehavior
from kivymd.uix.label import MDLabel
import socket
import time
import threading
kkk='''
#: import ew kivy.uix.effectwidget
<Screen1>:       
    name:'screen1'
    # Image:
    #     source:'9.png'
    #     size_hint:(1,1)
    #     allow_stretch:True
    #     keep_ratio:True
    MDLabel:
        text:'Znydee'
        bold:True
        halign:'right'
        valign:'bottom'
        font_size:150
        underline:True
        
    # MDCard:
    #     pos_hint:{'center_x':0.5,'center_y':0.5}
    #     FitImage:
    #         source:'1.jpg'   
    # MDRaisedButton:
    #     text:'click me'
    #     pos_hint:{'center_x':0.5,'center_y':0.3} 
    # MDLabel:
<Screen2>:       
    name:'screen2'
    # MDCard:
    #     id:mdd
    #     elevation:0
    #     orientation:'vertical'
    #     pos_hint:{'center_x':0.84,'center_y':0.85}
    #     size_hint:(.3,.2)
    #     MDLabel:
    #         id:mdd1
    #         text:'Notice!!!'
    #         halign:'center'
    #         bold:True
    #         underline:True
    #     MDLabel:
    #         id:mdd2
    #         bold:True
    #         halign:'center'
    #         text:'please, ensure to make your one-time payment into the account...Thanks'
    #     MDLabel:
    #         id:mdd3
    #         bold:True
    #         halign:'center'
    #         text:'uba, 2079108043, Yusuf Farouk '
            
    MDLabel:
        text:'Developed by Znydee.....+2347034599042,farouz98@gmail.com'
        font_size:20
        halign:'center'
        pos_hint:{'center_y':0.03}
    BoxLayout:
        size_hint:(.7,.5)
        pos_hint:{'center_x':0.5,'center_y':0.5}
        spacing:20
        MDCard:
            size_hint_x:.5
            FitImage:
               # pos_hint:{'center_x':0.5,'center_y':0.5}
                source:'10.png'
        BoxLayout:    
            id:bx1
            orientation:'vertical'
            spacing:10
            MDLabel:
                text:'Username'
                halign:'left'
                bold:True
                font_size:30
                color:(0,0,0,1)
            TextInput:
                id:l0
                multi_line:False
                text:''
                background_active:self.background_normal
            MDLabel:
                text:'Exam title'
                halign:'left'
                bold:True
                font_size:30
                color:(0,0,0,1)
            TextInput:
                id:l1
                multi_line:False
                text:''
                background_active:self.background_normal
            MDLabel:
                halign:'left'
                text:'Host'
                color:(0,0,0,1)
                bold:True
                font_size:30
            TextInput:
                id:host
                multi_line:False
                text:''
                background_active:self.background_normal
            MDRaisedButton:
                id:mll
                theme_text_color:'Custom'
                md_bg_color:(0,0,0,1)
                text:'Establish connection'
                on_press:app.beginn_test()
            # MDRaisedButton:
            #     theme_text_color:'Custom'
            #     md_bg_color:(0,0,0,1)
            #     text:'Enter'
            #     on_press:app.begin_test()
            # MDLabel:
            #     id:progress
            #     text:''
            #     halign:'left'
            #     bold:True
            #     font_size:30
            #     color:(0,0,0,1)
<Screen3>:    
    name:'screen3'   
    BoxLayout:
        orientation:'vertical'
        GridLayout:
            cols:2
            MDLabel:
                text:'Instructions'
                bold:True
                font_size:100 
                underline:True 
            MDLabel:
                id:z1
                text:'Do not start until you are told to do so'
                bold:True
                font_size:50  
        GridLayout:
            cols:2
            MDLabel:
                text:'Total number of questions :'
                bold:True
                font_size:50 
            MDLabel:
                id:z2
                text:''
                bold:True
                font_size:50 
        GridLayout:
            cols:2
            MDLabel:
                text:'Total time(min) :'
                bold:True
                font_size:50 
            MDLabel:
                id:z3
                text:''
                bold:True
                font_size:50     
        MDRaisedButton:
            text:'START'
            bold:True
            font_size:60 
            pos_hint:{'center_x':0.5}
            md_bg_color:(0,0,0,1)
            on_press:
                root.manager.current='screen4'
            
        Widget:
            size_hint:(1,None)
            height:10
<Screen4>:    
    name:'screen4'   
    GridLayout:
        cols:2
        spacing:15
        BoxLayout:
            orientation:'vertical'
            ScrollView:
                bar_width:0
                BoxLayout:
                    orientation:'vertical'
                    size_hint:(1,None)
                    height:self.minimum_height+500
                    spacing:45
                    MDLabel:
                        id:wx
                        text:'1'
                        bold:True
                        font_size:70
                        halign:'center'
                        size_hint:(1,None)
                        height:self.texture_size[1]
                    MDLabel:
                        id:wq
                        text:''
                        bold:True
                        font_size:70
                        halign:'left'
                        size_hint:(1,None)
                        height:self.texture_size[1]
                    GridLayout:
                        cols:2
                        MDLabel:
                            text:'A :'
                            bold:True
                            font_size:30
                            halign:'left'
                            valign:'top'
                            size_hint:(None,None)
                            width:50
                            height:self.texture_size[1]
                        MDLabelll:
                            id:wa
                            text:''
                            bold:True
                            font_size:30
                            halign:'left'
                            valign:'center'
                            size_hint_y:None
                            height:self.texture_size[1]
                            on_press:app.show_chosen1()
                        MDLabel:
                            text:'B :'
                            bold:True
                            font_size:30
                            halign:'left'
                            size_hint:(None,None)
                            width:50
                            height:self.texture_size[1]
                        MDLabelll:
                            id:wb
                            text:''
                            bold:True
                            font_size:30
                            halign:'left'
                            valign:'center'
                            size_hint_y:None
                            height:self.texture_size[1]
                            on_press:app.show_chosen2()                            
                        MDLabel:
                            text:'C :'
                            bold:True
                            font_size:30
                            halign:'left'
                            size_hint:(None,None)
                            width:50
                            height:self.texture_size[1]
                        MDLabelll:
                            id:wc
                            text:''
                            bold:True
                            font_size:30
                            halign:'left'
                            valign:'center'
                            size_hint_y:None
                            height:self.texture_size[1]
                            on_press:app.show_chosen3()
                        MDLabel:
                            text:'D :'
                            bold:True
                            font_size:30
                            halign:'left'
                            size_hint:(None,None)
                            width:50
                            height:self.texture_size[1]
                        MDLabelll:
                            id:wd
                            text:''
                            bold:True
                            font_size:30
                            halign:'left'
                            valign:'center'
                            size_hint_y:None
                            height:self.texture_size[1]
                            on_press:app.show_chosen4()
            MDCard:
                size_hint_y:None 
                height:60    
                Button:
                    text:'Previous'
                    size_hint_x:1 
                    bold:True
                    on_press:app.previous_question()
                Button:
                    size_hint_x:1 
                    text:'Next'
                    bold:True
                    on_press:app.next_question()
        MDCard:
            size_hint:(.4,1)
            BoxLayout:
                orientation:'vertical'
                MDLabel:
                    id:p1
                    text:''
                    bold:True
                    font_size:100 
                    halign:'center'

                ScrollView:
                    bar_width:0
                    size_hint:(1,1)
                    GridLayout:
                        id:lll
                        cols:7
                        size_hint:(1,None)
                        height:self.minimum_height+500
                        spacing:10            
                Widget:
                    size_hint:(1,None)
                    height:10
                MDRaisedButton:
                    id:submit
                    text:'Submit'
                    bold:True
                    font_size:60 
                    pos_hint:{'center_x':0.5}
                    md_bg_color:(0,0,0,1)      
                    on_press:app.dial() 
<Screen2b>:       
    name:'screen2b'
    BoxLayout:
        size_hint:(.7,.5)
        pos_hint:{'center_x':0.5,'center_y':0.7}
        orientation:'vertical'
        spacing:20
        MDLabel:
            text:'You have successfully completed your exam'
            bold:True
            font_size:45
            halign:'center'
            size_hint_y:None
            heght:self.texture_size[1]
        MDRaisedButton:
            text:'close'
            bold:True
            font_size:30
            pos_hint:{'center_x':0.5}
            md_bg_color:(0,0,0,1)  
            on_press:app.stop()
    
<Content>:
	size_hint_y:None
	spacing:20
	height:150
	MDLabel:
        text:'Are you sure you want to submit'
        bold:True
        font_size:45
        halign:'center'           
        '''
class MDLabelll(ButtonBehavior,MDLabel):
    pass
class Screen1(Screen):
    pass
class Screen2(Screen):
    def on_enter(self):
        mw=[1,2,3,4,5]
        mww = random.choice(mw)
        if mww == 3 :
            mdd=MDCard(orientation='vertical',pos_hint={'center_x':0.84,'center_y':0.85},size_hint=(.3,.2))
            mdd.add_widget(MDLabel(text= 'Notice!!!',halign= 'center',bold= True,underline=True))
            mdd.add_widget(MDLabel(text='please, ensure to make your one-time payment into the account...Thanks', halign='center', bold=True))
            mdd.add_widget(MDLabel(text='uba, 2079108043, Yusuf Farouk ', halign='center', bold=True))
            sm.get_screen("screen2").add_widget(mdd)
        else:
            pass
class Screen2b(Screen):
    pass
class Screen3(Screen):
    pass
class Content(BoxLayout):
	pass
class Screen4(Screen):
    def on_enter(self):
        self.ids.p1.text =str(eee)+':00'
        th2.start()
        Clock.schedule_interval(self.calc_time, 1)
        global dial_open
        dial_open=False
        print(dial_open)
    def calc_time(self,obj):

        #self.ids.p1.text=str(int(self.ids.p1.text)-0.02)
        if self.ids.p1.text != '0:0':
            kh=self.ids.p1.text
            ad=kh.split(':')
            ad[1]=float(ad[1])/60
            am=float(ad[0])+float(ad[1])
           # add=('.').join(ad)
            mr=float(am)-(1/60)
            mr=round(mr,2)
            mr=str(mr)
            ad = mr.split('.')
            ad[1]='.'+ad[1]
            ad[1]=str(round(float(ad[1])*60))
            ad= (':').join(ad)
            self.ids.p1.text=ad
            kt=self.ids.p1.text
            ktt=kt.split(':')
            kttt = ('.').join(ktt)
            if float(kttt)<10 and float(kttt)>=0:
                self.ids.p1.color = (1, 0, 0, 1)
                if float(kttt)==0:
                    print(student_answers)
                    ffo = json.dumps(student_answers)
                    s.send(str.encode(ffo))
                    if dial_open == True:
                        MainApp.dialog.dismiss()
                    else:
                        pass
                else:
                    pass
            else:
                pass
        else:
            pass



class MainApp(MDApp):
    global sm,questions_displayed,student_answers,qqa,ost
    sm=ScreenManager(transition=SlideTransition())
    questions_displayed={}
    student_answers={}
    qqa=[]
    ost=[]
  #  def back_image(self):
       # return random.choice(('4.jpg'))
    def on_start(self):
        Clock.schedule_once(self.change_screen,5)
    def dial(self):
        MainApp.dialog = MDDialog(type='custom', content_cls=Content(),auto_dismiss=False,
                               buttons=[MDRaisedButton(text='Yes',theme_text_color='Custom',
                                                       md_bg_color=(0, 0, 0, 1)
                                                       ,on_press=self.submit),
                                        MDRaisedButton(text='No', theme_text_color='Custom',
                                                       md_bg_color=(0, 0, 0, 1),on_press=self.gbac)])
        MainApp.dialog.open()
        global dial_open
        dial_open=True
        print(dial_open)
    def gbac(self,obj):
        MainApp.dialog.dismiss()
    def change_screen(self,obj):
        sm.current='screen2'
    def cc(self):
        MainApp.cc.filess=None
        MainApp.cc.filess = s.recv(1024)
        print(MainApp.cc.filess)
        sm.get_screen("screen2").ids['mz'].text='Start Exam'
    def dd(self):
        mag = s.recv(1024)
        print(mag,'WAS RECIEVED')
        sm.current = 'screen2b'
    def beginn_test(self):
        try:
            global s
            s = socket.socket()
            host = sm.get_screen("screen2").ids.host.text
            port = 8080
            s.connect((host, port))
            print('connected')
            self.root.get_screen("screen2").ids.bx1.remove_widget(self.root.get_screen("screen2").ids.mll)
            mkk = MDRaisedButton(text='Waiting for questions...', theme_text_color='Custom', md_bg_color=(0, 0, 0, 1),
                                 on_press=self.begin_test)
            sm.get_screen("screen2").ids['mz']=mkk
            sm.get_screen("screen2").ids.bx1.add_widget(mkk)
            th1.start()

        except:
            pass
    def begin_test(self,obj):
        if MainApp.cc.filess != None:
            print(MainApp.cc.filess)
            dd =MainApp.cc.filess.decode()
            qq=json.loads(dd)
            print(type(qq))
            print(qq["instructions"])
            print(qq["number of questions"])
            print(qq["time"])
            try:
                candidate=self.root.get_screen("screen2").ids.l0.text
                student_answers['candidte']=candidate
                student_answers['questt'] = {}
                sm.current = 'screen3'
                self.root.get_screen("screen3").ids.z1.text=qq["instructions"]
                self.root.get_screen("screen3").ids.z2.text=str(qq["number of questions"])
                self.root.get_screen("screen3").ids.z3.text=str(qq["time"])
                global eee,ff,wwk
                self.gg=qq["questions"]
                eee=qq["time"]
                ff=qq["number of questions"]
                lmm = random.choice(self.gg)
               # qqa.append(lmm)
                self.root.get_screen("screen4").ids.wq.text = lmm["Q"]
                self.root.get_screen("screen4").ids.wa.text = lmm["Ans"][0]
                self.root.get_screen("screen4").ids.wb.text = lmm["Ans"][1]
                self.root.get_screen("screen4").ids.wc.text = lmm["Ans"][2]
                self.root.get_screen("screen4").ids.wd.text = lmm["Ans"][3]
                for i in range(1,qq["number of questions"]+1):
                    btn=Button(text=f'{i}',on_press=self.tt,size_hint_y=None,height=50)
                    self.root.get_screen("screen4").ids[f'{i}']=btn
                    self.root.get_screen("screen4").ids.lll.add_widget(btn)
            except:
                pass
        else:
            pass
    def tt(self,obj):
        if obj.text in questions_displayed:
            self.root.get_screen("screen4").ids.wx.text=obj.text
            self.root.get_screen("screen4").ids.wq.text = questions_displayed[obj.text]['q']
            self.root.get_screen("screen4").ids.wa.text = questions_displayed[obj.text]['ans'][0]
            self.root.get_screen("screen4").ids.wb.text = questions_displayed[obj.text]['ans'][1]
            self.root.get_screen("screen4").ids.wc.text = questions_displayed[obj.text]['ans'][2]
            self.root.get_screen("screen4").ids.wd.text = questions_displayed[obj.text]['ans'][3]
        else:
            pass
    def next_question(self):
        eap = str(int(self.root.get_screen("screen4").ids.wx.text) + 1)
        print(eap)
        if int(eap) <=ff:
            if eap in questions_displayed :
                self.root.get_screen("screen4").ids.wx.text = eap
                self.root.get_screen("screen4").ids.wq.text = questions_displayed[eap]['q']
                self.root.get_screen("screen4").ids.wa.text= questions_displayed[eap]['ans'][0]
                self.root.get_screen("screen4").ids.wb.text= questions_displayed[eap]['ans'][1]
                self.root.get_screen("screen4").ids.wc.text= questions_displayed[eap]['ans'][2]
                self.root.get_screen("screen4").ids.wd.text= questions_displayed[eap]['ans'][3]
                if eap in student_answers['questt'] :
                    if self.root.get_screen("screen4").ids.wa.text==student_answers['questt'][eap]['ans']:
                        self.root.get_screen("screen4").ids.wa.color = (0, 0.6, 1, 1)
                        self.root.get_screen("screen4").ids.wb.color = (0, 0, 0, .9)
                        self.root.get_screen("screen4").ids.wc.color = (0, 0, 0, .9)
                        self.root.get_screen("screen4").ids.wd.color = (0, 0, 0, .9)
                    elif self.root.get_screen("screen4").ids.wb.text==student_answers['questt'][eap]['ans']:
                        self.root.get_screen("screen4").ids.wb.color = (0, 0.6, 1, 1)
                        self.root.get_screen("screen4").ids.wb.color = (0, 0.6, 1, 1)
                        self.root.get_screen("screen4").ids.wa.color = (0, 0, 0, .9)
                        self.root.get_screen("screen4").ids.wc.color = (0, 0, 0, .9)
                        self.root.get_screen("screen4").ids.wd.color = (0, 0, 0, .9)
                    elif self.root.get_screen("screen4").ids.wc.text==student_answers['questt'][eap]['ans']:
                        self.root.get_screen("screen4").ids.wc.color = (0, 0.6, 1, 1)
                        self.root.get_screen("screen4").ids.wc.color = (0, 0.6, 1, 1)
                        self.root.get_screen("screen4").ids.wa.color = (0, 0, 0, .9)
                        self.root.get_screen("screen4").ids.wb.color = (0, 0, 0, .9)
                        self.root.get_screen("screen4").ids.wd.color = (0, 0, 0, .9)
                    elif self.root.get_screen("screen4").ids.wd.text==student_answers['questt'][eap]['ans']:
                        self.root.get_screen("screen4").ids.wd.color = (0, 0.6, 1, 1)
                        self.root.get_screen("screen4").ids.wd.color = (0, 0.6, 1, 1)
                        self.root.get_screen("screen4").ids.wa.color = (0, 0, 0, .9)
                        self.root.get_screen("screen4").ids.wb.color = (0, 0, 0, .9)
                        self.root.get_screen("screen4").ids.wc.color = (0, 0, 0, .9)
                else:
                    self.root.get_screen("screen4").ids.wd.color = (0, 0, 0, .9)
                    self.root.get_screen("screen4").ids.wa.color = (0, 0, 0, .9)
                    self.root.get_screen("screen4").ids.wb.color = (0, 0, 0, .9)
                    self.root.get_screen("screen4").ids.wc.color = (0, 0, 0, .9)


            else:
                lmmm = random.choice(self.gg)
                # while lmmm in qqa:
                #     lmmm = random.choice(self.gg)
                # qqa.append(lmmm)
                self.root.get_screen("screen4").ids.wa.color = (0, 0, 0, .9)
                self.root.get_screen("screen4").ids.wb.color = (0, 0, 0, .9)
                self.root.get_screen("screen4").ids.wc.color = (0, 0, 0, .9)
                self.root.get_screen("screen4").ids.wd.color = (0, 0, 0, .9)
                questions_displayed[self.root.get_screen("screen4").ids.wx.text] = {'q': self.root.get_screen("screen4").ids.wq.text,
                                              'ans': [self.root.get_screen("screen4").ids.wa.text,
                                                      self.root.get_screen("screen4").ids.wb.text,
                                                      self.root.get_screen("screen4").ids.wc.text,
                                                      self.root.get_screen("screen4").ids.wd.text]}
                self.root.get_screen("screen4").ids.wx.text=str(int(self.root.get_screen("screen4").ids.wx.text)+1)
                self.root.get_screen("screen4").ids.wq.text =lmmm["Q"]
                self.root.get_screen("screen4").ids.wa.text =lmmm["Ans"][0]
                self.root.get_screen("screen4").ids.wb.text =lmmm["Ans"][1]
                self.root.get_screen("screen4").ids.wc.text =lmmm["Ans"][2]
                self.root.get_screen("screen4").ids.wd.text =lmmm["Ans"][3]
                questions_displayed[self.root.get_screen("screen4").ids.wx.text] = {
                    'q': self.root.get_screen("screen4").ids.wq.text,
                    'ans': [self.root.get_screen("screen4").ids.wa.text,
                            self.root.get_screen("screen4").ids.wb.text,
                            self.root.get_screen("screen4").ids.wc.text,
                            self.root.get_screen("screen4").ids.wd.text]}
        elif int(eap) == ff+1:
            if str(int(eap)-1) in student_answers['questt'] :
                pass
            else:
                questions_displayed[self.root.get_screen("screen4").ids.wx.text] = {
                    'q': self.root.get_screen("screen4").ids.wq.text,
                    'ans': [self.root.get_screen("screen4").ids.wa.text,
                            self.root.get_screen("screen4").ids.wb.text,
                            self.root.get_screen("screen4").ids.wc.text,
                            self.root.get_screen("screen4").ids.wd.text]}
        else:
            pass
    def previous_question(self):
        eas=str(int(self.root.get_screen("screen4").ids.wx.text) - 1)
        if int(eas) > 0:
            self.root.get_screen("screen4").ids.wx.text=eas
            self.root.get_screen("screen4").ids.wq.text=questions_displayed[eas]['q']
            self.root.get_screen("screen4").ids.wa.text=questions_displayed[eas]['ans'][0]
            self.root.get_screen("screen4").ids.wb.text= questions_displayed[eas]['ans'][1]
            self.root.get_screen("screen4").ids.wc.text= questions_displayed[eas]['ans'][2]
            self.root.get_screen("screen4").ids.wd.text= questions_displayed[eas]['ans'][3]
            if eas in student_answers['questt']:
                if self.root.get_screen("screen4").ids.wa.text == student_answers['questt'][eas]['ans']:
                    self.root.get_screen("screen4").ids.wa.color = (0, 0.6, 1, 1)
                    self.root.get_screen("screen4").ids.wb.color = (0, 0, 0, .9)
                    self.root.get_screen("screen4").ids.wc.color = (0, 0, 0, .9)
                    self.root.get_screen("screen4").ids.wd.color = (0, 0, 0, .9)
                elif self.root.get_screen("screen4").ids.wb.text == student_answers['questt'][eas]['ans']:
                    self.root.get_screen("screen4").ids.wb.color = (0, 0.6, 1, 1)
                    self.root.get_screen("screen4").ids.wa.color = (0, 0, 0, .9)
                    self.root.get_screen("screen4").ids.wc.color = (0, 0, 0, .9)
                    self.root.get_screen("screen4").ids.wd.color = (0, 0, 0, .9)
                elif self.root.get_screen("screen4").ids.wc.text == student_answers['questt'][eas]['ans']:
                    self.root.get_screen("screen4").ids.wc.color = (0, 0.6, 1, 1)
                    self.root.get_screen("screen4").ids.wa.color = (0, 0, 0, .9)
                    self.root.get_screen("screen4").ids.wb.color = (0, 0, 0, .9)
                    self.root.get_screen("screen4").ids.wd.color = (0, 0, 0, .9)
                elif self.root.get_screen("screen4").ids.wd.text == student_answers['questt'][eas]['ans']:
                    self.root.get_screen("screen4").ids.wd.color = (0, 0.6, 1, 1)
                    self.root.get_screen("screen4").ids.wa.color = (0, 0, 0, .9)
                    self.root.get_screen("screen4").ids.wb.color = (0, 0, 0, .9)
                    self.root.get_screen("screen4").ids.wc.color = (0, 0, 0, .9)
            else:
                self.root.get_screen("screen4").ids.wd.color = (0, 0, 0, .9)
                self.root.get_screen("screen4").ids.wa.color = (0, 0, 0, .9)
                self.root.get_screen("screen4").ids.wb.color = (0, 0, 0, .9)
                self.root.get_screen("screen4").ids.wc.color = (0, 0, 0, .9)
        else:
            pass

    def show_chosen1(self):
        clikk = self.root.get_screen("screen4").ids.wx.text
        self.root.get_screen("screen4").ids[clikk].background_color = (0, 0, 0, 1)
        self.root.get_screen("screen4").ids.wa.color = (0, 0.6, 1, 1)
        self.root.get_screen("screen4").ids.wb.color = (0, 0, 0, .9)
        self.root.get_screen("screen4").ids.wc.color = (0, 0, 0, .9)
        self.root.get_screen("screen4").ids.wd.color = (0, 0, 0, .9)
        student_answers['questt'][clikk]={'q':self.root.get_screen("screen4").ids.wq.text,'ans':self.root.get_screen("screen4").ids.wa.text}

    def show_chosen2(self):
        clikk = self.root.get_screen("screen4").ids.wx.text
        self.root.get_screen("screen4").ids[clikk].background_color = (0, 0, 0, 1)
        self.root.get_screen("screen4").ids.wb.color = (0, 0.6, 1, 1)
        self.root.get_screen("screen4").ids.wa.color = (0, 0, 0, .9)
        self.root.get_screen("screen4").ids.wc.color = (0, 0, 0, .9)
        self.root.get_screen("screen4").ids.wd.color = (0, 0, 0, .9)
        student_answers['questt'][clikk]={'q':self.root.get_screen("screen4").ids.wq.text,'ans':self.root.get_screen("screen4").ids.wb.text}

    def show_chosen3(self):
        clikk = self.root.get_screen("screen4").ids.wx.text
        self.root.get_screen("screen4").ids[clikk].background_color = (0, 0, 0, 1)
        self.root.get_screen("screen4").ids.wc.color = (0, 0.6, 1, 1)
        self.root.get_screen("screen4").ids.wa.color = (0, 0, 0, .9)
        self.root.get_screen("screen4").ids.wb.color = (0, 0, 0, .9)
        self.root.get_screen("screen4").ids.wd.color = (0, 0, 0, .9)
        student_answers['questt'][clikk]={'q':self.root.get_screen("screen4").ids.wq.text,'ans':self.root.get_screen("screen4").ids.wc.text}

    def show_chosen4(self):
        clikk = self.root.get_screen("screen4").ids.wx.text
        self.root.get_screen("screen4").ids[clikk].background_color = (0, 0, 0, 1)
        self.root.get_screen("screen4").ids.wd.color = (0, 0.6, 1, 1)
        self.root.get_screen("screen4").ids.wa.color = (0, 0, 0, .9)
        self.root.get_screen("screen4").ids.wb.color = (0, 0, 0, .9)
        self.root.get_screen("screen4").ids.wc.color = (0, 0, 0, .9)
        student_answers['questt'][clikk]={'q':self.root.get_screen("screen4").ids.wq.text,'ans':self.root.get_screen("screen4").ids.wd.text}
    def submit(self,obj):
        print(student_answers)
        ffo=json.dumps(student_answers)
        s.send(str.encode(ffo))
        #mmd=s.recv(1024)
        print('script has been submitted successfully')
        MainApp.dialog.dismiss()

        #sm.current = 'screen2b'
    def build(self):
      #  self.theme_cls.theme_style='Dark'
        kk=Builder.load_string(kkk)
        sm.add_widget(Screen1(name='screen1'))
        sm.add_widget(Screen2(name='screen2'))
        sm.add_widget(Screen2b(name='screen2b'))
        sm.add_widget(Screen3(name='screen3'))
        sm.add_widget(Screen4(name='screen4'))
        return sm
    # def rand(self):
    #     return random.choice([1,2,3,4,5,6,7])
th1=threading.Thread(target=MainApp.cc, args=(1,))
th2=threading.Thread(target=MainApp.dd, args=(1,))
MainApp().run()