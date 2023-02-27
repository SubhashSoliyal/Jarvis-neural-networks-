from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from transformers import AutoModelWithLMHead, AutoTokenizer

class ChatGPTApp(App):
    # Load the model and tokenizer
    model = AutoModelWithLMHead.from_pretrained("microsoft/DialoGPT-medium")
    tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")

    def build(self):
        # Load the model and tokenizer
        model = AutoModelWithLMHead.from_pretrained("microsoft/DialoGPT-medium")
        tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")

        # Create a layout to hold the input and output widgets
        layout = BoxLayout(orientation='vertical')

        # Create a text input widget for the user's message
        self.input_text = TextInput(hint_text="Type your message here...")
        self.input_text.bind(on_text_validate=self.generate_response)
        layout.add_widget(self.input_text)

        # Create a label to display the response from ChatGPT
        self.output_label = Label(text="")
        layout.add_widget(self.output_label)

        return layout

    def generate_response(self, instance):
        # Get the user's message
        message = self.input_text.text

        # Generate a response using ChatGPT
        response = self.model.generate(
            input_ids=self.tokenizer.encode(message, return_tensors="pt"),
            max_length=100,
            top_p=0.9,
            top_k=20,
            do_sample=True
        )

        # Decode the response from the tokenizer
        response_text = self.tokenizer.decode(response[0], skip_special_tokens=True)

        # Update the output label with the response text
        self.output_label.text = response_text

if __name__ == '__main__':
    ChatGPTApp().run()
