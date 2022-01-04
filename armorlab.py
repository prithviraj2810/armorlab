from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.label import MDLabel
from kivy.core.text import Label
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.clock import Clock
from kivy.core.window import Window
import plotly.graph_objects as go
import plotly.offline as pyo
import os

Window.size = (500,740)

def createMainRadarPlot(): 
    categories = ['Strength', 'Stamina', 'Agility', 'Control']
    categories = [*categories, categories[0]]

    subject = [8.8, 7.4, 2.0, 4.0]
    average_person = [6.8, 7.5, 6.0, 5.0]
    subject = [*subject, subject[0]]
    average_person = [*average_person, average_person[0]]

    fig = go.Figure(
        data=[
            go.Scatterpolar(r=subject, theta=categories, fill='toself', name='Your Stats'),
            go.Scatterpolar(r=average_person, theta=categories, fill='toself', name='Average Person')
        ],
        layout=go.Layout(
            polar={'radialaxis': {'visible': True}},
            showlegend=True
        )
    )

    if not os.path.exists("graphs"):
        os.mkdir("graphs")

    fig.write_image("graphs/radarPlot.jpeg")

class BaseScreen(Screen):
    createMainRadarPlot()
    def __init__(self, **kw):
        super().__init__(**kw)
        Clock.schedule_once(self.set_toolbar_title_halign)
    def set_toolbar_title_halign(self, *args):
        self.ids.toolbar.ids.label_title.halign = "center"

class GitButtonScreen(Screen):
    pass
    
class MenuToggledScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        Clock.schedule_once(self.set_toolbar_title_halign)
    def set_toolbar_title_halign(self, *args):
        self.ids.toolbar.ids.label_title.halign = "center"

screen_manager = ScreenManager(transition=NoTransition())

class armorlab(MDApp):
    def build(self):
        screen_manager.add_widget(BaseScreen(name="BaseScreen"))
        screen_manager.add_widget(GitButtonScreen(name="GitButtonScreen"))
        screen_manager.add_widget(MenuToggledScreen(name="MenuToggledScreen"))
        return screen_manager
    def menuClicked(self):
        screen_manager.current = 'MenuToggledScreen'
    def menuUnclicked(self):
        screen_manager.current = 'BaseScreen'

if __name__ == '__main__':
    armorlab().run()