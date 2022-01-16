from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty


class MilesToKm(App):

    MILES_TO_KM = 1.609344
    output_result = StringProperty()

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("convert_miles_km_2.kv")
        return self.root

    def handle_increment(self, num, value):
        try:
            new_value = int(num) + value
            self.root.ids.input_num.text = str(new_value)
        except:
            new_value = int(0) + value
            self.root.ids.input_num.text = str(new_value)

    def convert_to_km(self):
        try:
            kilometres = int(self.root.ids.input_num.text) * MilesToKm.MILES_TO_KM
            self.output_result = str(kilometres)
        except:
            self.output_result = str(0)


if __name__ == '__main__':
    my_app = MilesToKm()
    my_app.run()
