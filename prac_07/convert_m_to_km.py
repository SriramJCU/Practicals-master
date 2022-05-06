from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

MILES_TO_KM = 1.6

class ConvertDistanceApp(App):
    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (500, 200)
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_m_to_km.kv')
        return self.root


    def handle_calculate(self):
        """Convert Miles to Kilometers (With Validation)"""
        miles = float(self.root.ids.input_miles.text)
        kilometers = miles * MILES_TO_KM
        try:
            self.root.ids.output_kilometers.text = str(round(kilometers, 3))
        except ValueError:
            self.root.ids.output_kilometers.text = '0.0'


    def handle_increment(self, value):
        """Increase or Decrease Miles by 1 (With Validation)"""
        value = int(value)
        try:
            Input = int(self.root.ids.input_miles.text)
        except ValueError:
            Input = 0
        increment = Input + value
        self.root.ids.input_miles.text = str(increment)

ConvertDistanceApp().run()