from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import re


class MainApp(App):
    clear_label = "C"
    decimal_delimiter = "."
    operators = ["/", "*", "+", "-"]

    def build(self):
        self.current_text = ""

        main_layout = BoxLayout(orientation="vertical")

        self.history = TextInput(
            multiline=False, readonly=True, halign="right", font_size=55
        )
        main_layout.add_widget(self.history)

        self.solution = TextInput(
            multiline=False, readonly=True, halign="right", font_size=55
        )
        main_layout.add_widget(self.solution)
        self.set_to_text_bar(self.solution, "")

        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [MainApp.decimal_delimiter, "0", MainApp.clear_label, "+"],
        ]
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text=label,
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )
                if label in [str(i) for i in range(10)]:
                    button.bind(on_press=self.on_number_button_press)
                elif label == MainApp.decimal_delimiter:
                    button.bind(on_press=self.on_dot_button_press)
                elif label == MainApp.clear_label:
                    button.bind(on_press=self.on_clear_button_press)
                elif label in MainApp.operators:
                    button.bind(on_press=self.on_operator_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        equals_button = Button(
            text="=", pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        equals_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equals_button)

        return main_layout

    def on_operator_button_press(self, instance):
        button_text = instance.text
        last_button = self.get_last_button()
        last_was_operator = self.is_last_char_operator()

        if last_was_operator:
            # Не добавляйте два оператора подряд, рядом друг с другом
            return
        elif self.current_text == "":
            # Первый символ не может быть оператором
            return
        elif last_button == MainApp.decimal_delimiter:
            # Unable to print operator after dot
            return

        self.pritn_to_text_bar(self.solution, button_text)

    def on_number_button_press(self, instance):
        button_text = instance.text

        if self.get_current_number() == "0":
            # leading zero forbidden
            return

        self.pritn_to_text_bar(self.solution, button_text)

    def on_dot_button_press(self, instance):
        button_text = instance.text

        if self.is_current_number_has_dot():
            # double dot forbidden
            return
        if self.get_current_number() == "":
            # leading dot forbidden
            return

        self.pritn_to_text_bar(self.solution, button_text)

    def on_clear_button_press(self, instance):
        self.set_to_text_bar(self.solution, "")

    def on_solution(self, instance):
        try:
            last_was_operator = self.is_last_char_operator()

            if last_was_operator:
                return
            text = self.solution.text
            if text:
                solution = str(eval(self.current_text))
                self.history.text = self.solution.text
                self.set_to_text_bar(self.solution, solution)
        except ZeroDivisionError:
            self.set_to_text_bar(self.solution, "")
            self.set_fake_text_to_bar(self.solution, "Error")

    def set_to_text_bar(self, text_bar, text):
        self.current_text = text

        if text:
            text_bar.text = text
        else:
            text_bar.text = "0"

    def pritn_to_text_bar(self, text_bar, text):
        self.current_text += text
        self.set_to_text_bar(self.solution, self.current_text)

    def set_fake_text_to_bar(self, text_bar, fake_text):
        text_bar.text = fake_text

    def get_last_button(self):
        if len(self.current_text) == 0:
            return ""
        return self.current_text[-1]

    def is_last_char_operator(self):
        return self.get_last_button() in MainApp.operators

    def is_current_number_has_dot(self):
        return MainApp.decimal_delimiter in self.get_current_number()

    def get_current_number(self):
        search = re.search(r'[\d\.]+$', self.current_text)
        if search:
            return search.group()
        else:
            return ""

if __name__ == "__main__":
    app = MainApp()
    app.run()
