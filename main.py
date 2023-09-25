#file name:main.py
import pymysql
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget


Screen_helper='''
ScreenManager:
    BoxLayoutExample:  
    BoxLayoutExample2:
    BoxLayoutExample3:   
#---------------------------------screen 1---------------------------------------
<BoxLayoutExample>:
    name: 'login'
    
    FloatLayout:
        
        canvas.before:
            
            Color:
                rgba:1,.1,.1,.1
            Rectangle:
                pos:self.pos
                size:self.size


            Ellipse:

            Ellipse:
                pos:200,200

            Ellipse:
                pos:500,200

            Ellipse:
                pos:400,50

            Ellipse:
                pos:600,400

            Ellipse:
                pos:400,300

            Ellipse:
                pos:200,500

        
        Image:
            source:'image/R15.png'
            color:.5,.5,.5,.5
            size_hint:None,None
            size:800,850
            pos_hint:{'center_x':.5,'center_y':.5}
            
            
        
        FloatLayout:
            
        
            color:.1,1,1,1
        
            pos_hint:{'center_x':.5,'center_y':.5}
            size_hint:None,None
            size:350,450
            border:3
            spacing:50
            
            Image:
                source:'image/login.png'
                size_hint:None,None
                pos_hint:{'center_x':.5,'center_y':.9}
            Label:
                text:'Login'
                font_text: 'Microsoft Yahel Ui Light'
                font_size:50
                size_hint:.5,.5
                pos_hint:{'center_x':.5,'center_y':.75}
    
            ProgressBar:
                size_hint:None,None
                size:'220dp','100dp'
                pos_hint:{'center_x':.5,'center_y':.67}
                background_color:'blue'
                color:1,.1,.2,10
    
    
            TextInput:
                id:email
                hint_text: 'Email'
                size_hint:None,None
                size:'350dp','30dp'
                pos_hint:{'center_x':.5,'center_y':.6}
                color: 'red'
                multiline:False
    
            TextInput:
                id:password
                hint_text:'password'
                password:True
                size_hint:None,None
                size:'350dp','30dp'
                pos_hint:{'center_x':.5,'center_y':.5}
                multiline:False
                cursor_color:rgba(0,0,59,255)
    
            Button:
                text:'Login'
                color: 'white'
                size_hint:None,.07
                pos_hint:{'center_x':.5,'center_y':.4}
                background_color:'blue'
                on_press:root.on_button_Login(email.text,password.text)
                #on_release:app.verify(email.text,password.text)
                #on_release:root.manager.current='signup'
                
    
    
            Label:
    
                text:'--------------------------------OR--------------------------------'
                font_text: 'Microsoft Yahel Ui Light'
                font_size:20
                size_hint:.5,.5
                pos_hint:{'center_x':.5,'center_y':.3}
    
    
            Label:
    
                text:'you dont have an account ?'
                
                font_text: 'Microsoft Yahel Ui Light'
                font_size:15
                size_hint:.5,.5
                pos_hint:{'center_x':.35,'center_y':.2}
                
    
                
            Button:
                id:go_to_signup
                text: 'signup'
                background_color:'red'
                color: 'white'
                size_hint:None, None
                size:50,35
                pos_hint:{'center_x':.7,'center_y':.2}
                on_press:
                    root.manager.current='signup'
                    root.manager.transition.direction='left'
            
#---------------------------------screen 2---------------------------------------
<BoxLayoutExample2>:
    name: 'signup'

    FloatLayout:
        

        canvas.before:
            Color:
                
                rgba:.1,.1,.1,1
            Rectangle:
                #size_hint:None,None
                #size:dp(800),dp(450)
                pos:dp(0),dp(60)
                #pos_hint:{'center_x':.5,'center_y':.5}
                
            #Rectangle:
                #size_hint:None,None
                #size:dp(800),dp(450)
                pos:dp(250),dp(200)
                #pos_hint:{'center_x':.5,'center_y':.5}

            Ellipse:
                #size_hint:.5,.5
                #pos_hint:{'center_x':.2,'center_y':.1}

            Ellipse:
                pos:dp(200),dp(200)

            Ellipse:
                pos:dp(500),dp(200)

            Ellipse:
                pos:dp(400),dp(50)

            Ellipse:
                pos:dp(600),dp(400)

            Ellipse:
                pos:dp(50),dp(400)

            Ellipse:
                pos:dp(600),dp(50)
                
        Image:
            color:1,.1,.2,1
            source:'image/S1.jpg'
            size_hint:None,None
            size:950,600
            pos_hint:{'center_x':.5,'center_y':.45}
    FloatLayout:
        
        pos_hint:{'center_x':.5,'center_y':.5}
        size_hint:None,None
        size:350,450
        border:3
        spacing:50
        Label:
            text: 'Signup'
            font_size:50
            size_hint:.5,.05
            pos_hint:{'center_x':.5,'center_y':.9}


        ProgressBar:
            size_hint:None,None
            size:'220dp','30dp'
            pos_hint:{'center_x':.5,'center_y':.80}


        TextInput:
            id:email
            hint_text: 'Email'
            size_hint:None,None
            size:'350dp','30dp'
            pos_hint:{'center_x':.5,'center_y':.68}
            multiline:False
            #border:'0'
            
        TextInput:
            id:username
            hint_text: 'username'
            size_hint:None,None
            size:'350dp','30dp'
            pos_hint:{'center_x':.5,'center_y':.58}
            multiline:False
            #border:'0'

        TextInput:
            id:password
            hint_text: 'password'
            password:True
            size_hint:None,None
            size:'350dp','30dp'
            pos_hint:{'center_x':.5,'center_y':.48}
            multiline:False
            #border:'0'

        TextInput:
            id:conform_password
            hint_text:'conform password'
            password:True
            size_hint:None,None
            size:'350dp','30dp'
            pos_hint:{'center_x':.5,'center_y':.38}
            multiline:False
            #border:'0'
            
                 
        CheckBox:
            #group:'check'
            id:check_box
            size_hint:None,None
            size:'50dp','50dp'
            pos_hint:{'center_x':.10,'center_y':.28}
            color:.1,.5,1,2
            active:0
        Label:
            text:'I agree to the Terms & condition'
            size_hint:None,None
            size:'150dp','30dp'
            font_size:dp(15)
            pos_hint:{'center_x':.45,'center_y':.28}


        Button:
            text:'Submit'
            size_hint:None,None
            size:'150dp','30dp'
            pos_hint:{'center_x':.5,'center_y':.2}
            background_color:'red'
            on_press:root.empty(email.text,username.text,password.text,conform_password.text,check_box.active)
           
        
        Label:
            text:'------------------------or----------------------'
            size_hint:None,None
            size:'150dp','30dp'
            font_size:dp(25)
            pos_hint:{'center_x':.5,'center_y':.12}
        
        
        Label:
            text:'you have an account !! '
            size_hint:.3,.2
            pos_hint:{'center_x':dp(0.39),'center_y':dp(0.05)}
            
        Button:
            text:'login'
            size_hint:None,None
            size:'50dp','30dp'
            border_hint:0
            #translation:20
            #translation_color:'red'
            transition:.5
            transition_color:'red'
            background_color:'blue'
            pos_hint:{'center_x':dp(.68),'center_y':dp(0.05)}
            on_press:
                root.manager.current='login'
                root.manager.transition.direction='right'
#---------------------------------screen 1---------------------------------------
<BoxLayoutExample3>:
    name:'page1'
    FloatLayout:
    
        canvas.before:
            Color:
                
                rgba:.1,.1,.1,.5
            Rectangle:
                #pos_hint:None,None
                #size_hint:None,None
                size:1000,400
                pos:0,100
                
        Image:
            color:1,.1,.2,.2
            size_hint:None,None
            size:700,850
            pos_hint:{'center_x':.5,'center_y':.5}
            source:'image/1b.png'
            
            
        Label:
            text:'welcome to my application'
            
            
        
                
                
















'''


class WidgetExample(Widget):
    pass

class BoxLayoutExample(Screen):


    def on_button_Login(self,email,password):
        if email == '' or password == '':
            the_content=Label(text='Error : pleas enter your email \n and your password ')
            the_content.color=(1,1,1,1)
            popup=Popup(title='Error',content=the_content,size_hint=(None,None),size=(350,150))
            popup.open()
        else :
            self.manager.current='page1'






    def main_file(self):
        print('bbb')



class BoxLayoutExample2(Screen):
    def empty(self,email,username,password,conform_password ,check_box):
        if email =='' or username == '' or password == '' or conform_password=='':
            the_content=Label(text='Error :pleas enter full information ')
            the_content.color = (1,1,1,1)
            popup=Popup(title='Error',content=the_content,size_hint=(None,None),size=(350,150))
            popup.open()

        elif check_box == 0 :
            the_content=Label(text="Error : you don't accept the condition\n Info : if you accept please active the checkbox")
            the_content.color=(1,1,1,1)
            popup=Popup(title='Error' ,content= the_content ,size_hint=(None,None),size=(350,150))
            popup.open()

        elif password != conform_password :
            the_content=Label(text='Error : password is incompatible with \nconform password')
            the_content.color=(1,1,1,1)
            popup=Popup(title='Error',content=the_content,size_hint=(None,None),size=(350,150))
            popup.open()
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='raoufdede2016')
                mycursor =con.cursor()

            except:
                the_content=Label(text='Error : database Connectivity Issue , pleas try again ')
                the_content.color=(1,1,1,1)
                popup=Popup(title='Error',content=the_content,pos_hint=(None,None),pos=(350,150))
                popup.open()
                return
            try:
                query='create database userdata'
                mycursor.execute(query)
                query='use userdata'
                mycursor.execute(query)
                query=('create table data(id int auto_increment primary key not null , email varchar(100),username '
                       'varchar(50),password varchar(20))')
                mycursor.execute(query)
            except:
                mycursor.execute('use userdata')


            query='insert into userdata.data(email,username,password)values(%s,%s,%s)'
            mycursor.execute(query,(email,username,password))
            con.commit()
            con.close()
            the_content=Label(text='SUCCESS : Registration is successful')
            the_content.color=(1,1,1,1)
            popup=Popup(title='Info',content=the_content,size_hint=(None,None),size=(350,150))
            popup.open()
            self.manager.current='login'


class BoxLayoutExample3(Screen):
    pass



class windowManager(ScreenManager):
    pass

sm=ScreenManager()
sm.add_widget(BoxLayoutExample(name='login'))
sm.add_widget(BoxLayoutExample2(name='signup'))
sm.add_widget(BoxLayoutExample3(name='page1'))
class MyApplication(App):
    def build(self):

        screen = Builder.load_string(Screen_helper)
        return screen



MyApplication().run()