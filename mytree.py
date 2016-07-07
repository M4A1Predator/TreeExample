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
    def __init__(self, image, text, **kwargs):
        BoxLayout.__init__(self, **kwargs)
        self.width = 800
        self.add_widget(image)
        label = Label(text=text, size_hint_x=0.9, text_size=(400, None), halign='left')
        label.width = 700

        self.category_name = label
        self.add_widget(self.category_name)

    def create_components(self):
        pass

    def on_touch_down(self, t):
        print('touch', self.category_name.text)
        # print(type(super(MyNode, self).on_touch_down(t)))
        # print(t.__dict__)

    def on_touch_up(self, t):
        print('release', self.category_name.text)

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

        node3 = MyNode(img, 'CSGO',  orientation="horizontal")
        node3.height = 45
        node3.fbind('on event', self.state)
        node4 = MyNode(Image(), 'COD', orientation="horizontal")

        self.tree.add_node(node1)
        self.tree.add_node(node2)
        self.tree.add_node(node3, parent=node1)
        self.tree.add_node(node4, parent=node1)

    def cb(self, e, e2, e3):
        print('cb', e, e2, e3)

    def state(self, e):
        print(e)

    def on_touch_up(self, t):
        pass
        #print('release window')


class MainApp(App):
    def build(self):
        return MainWindow(orientation="vertical")

MainApp().run()
