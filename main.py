from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class CounterApp(App):
    def build(self):
        self.counter = 0

        # Main layout
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Counter display
        self.label = Label(text=str(self.counter), font_size='40sp')

        # Buttons for incrementing, decrementing, and resetting the counter
        increment_button = Button(text='Increase', on_press=self.increment)
        decrement_button = Button(text='Decrease', on_press=self.decrement)
        reset_button = Button(text='Reset', on_press=self.reset)

        # Adding widgets to the layout
        self.layout.add_widget(self.label)
        self.layout.add_widget(increment_button)
        self.layout.add_widget(decrement_button)
        self.layout.add_widget(reset_button)

        return self.layout

    def increment(self, instance):
        self.counter += 1
        self.update_label()

    def decrement(self, instance):
        self.counter -= 1
        self.update_label()

    def reset(self, instance):
        self.counter = 0
        self.update_label()

    def update_label(self):
        self.label.text = str(self.counter)

if __name__ == '__main__':
    CounterApp().run()
