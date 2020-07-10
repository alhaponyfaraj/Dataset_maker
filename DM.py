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