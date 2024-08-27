import reflex as rx

class ChatState(rx.State):
    did_submit: bool = False

    @rx.var
    def user_did_submit(self) -> bool:
        return self.did_submit

    def handle_submit(self, form_data:dict):
        print('here is our form data', form_data)
        self.did_submit = True