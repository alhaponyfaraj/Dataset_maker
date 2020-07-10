import ntpath

import psycopg2 as psycopg2
from kivy.app import App
from kivy.base import runTouchApp
from kivy.core.window import Window
from kivy.uix import dropdown
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty

from kivy.uix.recycleview import RecycleView
from kivy.uix.popup import Popup
from kivy.uix.progressbar import ProgressBar
import os
from os.path import join
import webbrowser
import subprocess
from kivy.uix.scrollview import ScrollView

class DownloadListButton(RecycleView):
    pb = ProgressBar(max=1000)

    # this will update the graphics automatically (75% done)
    pb.value = 750
    pass

class CustomPopup1(Popup):
    pass

class CustomPopup2(Popup):
    pass

class CustomPopup3(Popup):
    def open_developer_page(self):
        new = 1;
        dev_url = "http://www.TNL.com"
        webbrowser.open(dev_url,new=new)
    pass

class SearchListButton(RecycleView):
    pass

class DM(BoxLayout):
    url_text_input = ObjectProperty()
    mylabel = ObjectProperty()
    button = ObjectProperty()
    search_list = ObjectProperty()

#each popup need method
    #Validation for Text input
    def open_popup1(self):
        the_popup1 = CustomPopup1()

        the_popup1.open()

    #About Developer and some details
    def open_popup2(self):
        the_popup2 = CustomPopup2()
        the_popup2.open()


    #Developer webpage redirect
    def open_popup3(self):
        the_popup3 = CustomPopup3()
        the_popup3.open()

    def aboutus(self):
        self.open_popup2()

    def Insert(self):
        conn = psycopg2.connect("dbname=Dataset user=Alhapony password=fgfg1995")
        cursor = conn.cursor()
        # Define the fields with the input values
        sentence = str(self.ids.sentence.text)
        reply = str(self.ids.reply.text)
        query = "INSERT INTO sentence_reply (sentence, reply) VALUES (%s, %s);"
        data = (sentence, reply)

        cursor.execute(query, data)
        conn.commit()



