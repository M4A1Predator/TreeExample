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

NODE_HEIGHT = 40

game_data = [
    ('Game', None),
    ('CSGO', 'FPS'),
    ('MOBA', 'Game'),
    ('FPS', 'Game'),
    ('BF', 'FPS'),
    ('COD', 'FPS'),
    ('DOTA2', 'MOBA'),
]

game_data = sorted(game_data, key=lambda tup:tup[0])

class MyNode(BoxLayout, TreeViewNode):
    def __init__(self, image, text, **kwargs):
        BoxLayout.__init__(self, **kwargs)
        self.text = text
        self.height = NODE_HEIGHT
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

    def on_touch_up(self, t):
        print('release', self.category_name.text)

    def cb(self, e):
        print(e)


class MainWindow(BoxLayout):
    def __init__(self, **kwargs):
        BoxLayout.__init__(self, **kwargs)

        self.nodes = []
        self.tree = TreeView(hide_root=True)

        #   Create UI
        self.add_node()
        self.add_widget(self.tree)

    def add_node(self):
        parent_nodes = []
        remove_list = []
        parent_texts = []
        add_list = []
        add_nodes = []

        # Add root node
        for g in game_data:
            if not g[1]:
                node = self.get_node(g[0])
                node.is_open = True
                self.tree.add_node(node)
                parent_nodes.append(node)
                remove_list.append(g)
                parent_texts.append(g[0])

        # Remove parents level 1
        for rm in remove_list:
            print('remove ', rm[0])
            game_data.remove(rm)
        remove_list = []

        c = 0
        while game_data and c < 5:
            print('data is ', game_data)
            for index, g in enumerate(game_data):
                if g[1] in parent_texts:
                    print(g[0], ' is child of ', parent_texts)
                    add_list.append(g)

            parent_texts = []

            for p in parent_nodes:
                for g in add_list:
                    if g[1] == p.text:
                        node = self.get_node(g[0])
                        self.tree.add_node(node, parent=p)
                        add_nodes.append(node)
                        parent_texts.append(g[0])
                        remove_list.append(g)

            # Clear list
            parent_nodes = add_nodes
            add_nodes = []
            print(parent_nodes)

            # Remove
            for rm in remove_list:
                game_data.remove(rm)
                remove_list = []

            c += 1

    @staticmethod
    def get_node(text):
        img = Image(source='C:\\Users\\PredatorPy\\Pictures\\Wallpaper\\eun-jin-dia.jpg', size_hint_x=0.1)
        node = None
        if text:
            node = MyNode(img, text)
        return node

    def cb(self, e, e2, e3):
        print('cb', e, e2, e3)

    def state(self, e):
        print(e)

    def on_touch_up(self, t):
        pass


class MainApp(App):
    def build(self):
        return MainWindow(orientation="vertical")

MainApp().run()
