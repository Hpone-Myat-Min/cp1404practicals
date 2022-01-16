from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label
from kivy.app import StringProperty


class OneDirection(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Louie Tomlinson", "Harry Styles", "Nial Horan", "Liam Payne"]

    def build(self):
        self.title = "One Direction"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        for name in self.names:
            name_label = Label(text=name)
            self.root.ids.main.add_widget(name_label)


if __name__ == '__main__':
    my_app = OneDirection()
    my_app.run()
