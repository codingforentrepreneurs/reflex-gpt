import reflex as rx

class ChatState(rx.State):

    def handle_submit(self, form_data:dict):
        print('here is our form data', form_data)