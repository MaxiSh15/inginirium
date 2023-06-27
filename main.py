from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
 
class MainApp(App):
    def build(self):
        main_layout = BoxLayout(orientation="vertical")
        point = TextInput(multiline=False)
        main_layout.add_widget(point)
        point_2 = TextInput(multiline=False)
        main_layout.add_widget(point_2)
        label_1 = Label()
        main_layout.add_widget(label_1)
        equals_button = Button(text="ckj;bnm")
        equals_button.bind(on_press=lambda instanse: setattr(label_1, "text", str(float(point.text) + float(point_2.text))))
        main_layout.add_widget(equals_button)
     
 
        return main_layout
 
     
if __name__ == "__main__":
    app = MainApp()
    app.run()