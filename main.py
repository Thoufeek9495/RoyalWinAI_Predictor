from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from predictor import PredictorPro  # this is your AI engine (to be written next)


class PredictorUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', spacing=10, padding=20, **kwargs)

        self.engine = PredictorPro()
        self.history = []  # All submitted results go here

        self.input_field = TextInput(
            hint_text="Enter Result (3–18)", multiline=False,
            input_filter='int', font_size=24
        )
        self.predict_btn = Button(
            text="🔮 Predict Next", font_size=20, on_press=self.use_history_prediction
        )
        self.submit_btn = Button(
            text="✅ Submit Result", font_size=20, on_press=self.submit_result
        )
        self.feedback = Label(text="Awaiting result input...", font_size=18)

        self.add_widget(self.input_field)
        self.add_widget(self.predict_btn)
        self.add_widget(self.submit_btn)
        self.add_widget(self.feedback)

    def use_history_prediction(self, instance):
        if len(self.history) < 5:
            self.feedback.text = "❗ Need at least 5 results to make a prediction."
            return

        prediction, confidence, details = self.engine.predict_from_history(self.history)
        self.feedback.text = f"🤖 Prediction: {prediction} | Confidence: {confidence}%\n{details}"

    def submit_result(self, instance):
        try:
            val = int(self.input_field.text)
            if val < 3 or val > 18:
                raise ValueError

            self.history.append(val)
            self.engine.learn(val)
            self.feedback.text = f"✅ Result {val} added. History length: {len(self.history)}"

            self.input_field.text = ""

        except:
            self.feedback.text = "❌ Please enter a valid number between 3 and 18."


class PredictorApp(App):
    def build(self):
        return PredictorUI()


if __name__ == '__main__':
    PredictorApp().run()
