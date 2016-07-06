from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.treeview import TreeView, TreeViewNode, TreeViewLabel
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
Config.set('graphics', 'width', 800)
Config.set('graphics', 'height', 600)
from kivy.core.window import Window


class MyNode(BoxLayout, TreeViewNode):
    def __init__(self, image, text, parent=None, **kwargs):
        BoxLayout.__init__(self, **kwargs)
        self.width = 800
        self.parent_node = parent
        self.add_widget(image)
        label = Label(text=text, size_hint_x=0.9, text_size=(400, None), halign='left')
        label.width = 700

        self.category_name = label
        self.add_widget(self.category_name)
        #self.bind(on_motion=self.cb)

    def create_components(self):
        pass

    def cb(self, e):
        print(e)


class MainWindow(BoxLayout):
    def __init__(self, **kwargs):
        BoxLayout.__init__(self, **kwargs)

        self.tree = TreeView(hide_root=True)
        self.add_node()
        self.add_widget(self.tree)

    def add_node(self):
        node1 = TreeViewLabel(text='FPS', is_open=True)
        node2 = TreeViewLabel(text='RTS')

        img = Image(source='C:\\Users\\PredatorPy\\Pictures\\Wallpaper\\7CQ5vyX.jpg', size_hint_x=0.1)

        node3 = MyNode(img, 'CSGO', parent=node1, orientation="horizontal")
        node3.height = 45
        node3.fbind('on event', self.state)
        self.tree.add_node(node1)
        self.tree.add_node(node2)
        self.tree.add_node(node3, parent=node1)
        Window.bind(on_motion=self.cb)

    def cb(self, e, e2, e3):
        print('cb', e, e2, e3)

    def state(self, e):
        print(e)


class MainApp(App):
    def build(self):
        return MainWindow(orientation="vertical")

MainApp().run()
