import reflex as rx


from .state import ChatState
from .state import ChatState

def chat_form() -> ChatState:
    return rx.form(
        rx.vstack(
            rx.text_area(
                name='message',
                placeholder='Ketik disini teman...',
                required=True,
                width='100%'
            ),
            rx.hstack(
                rx.button('Submit', type='submit'),
                rx.cond(
                    ChatState.did_submit,
                    rx.text("Sumitted"),
                    rx.fragment(),
                )
                
            )
        ),
        on_submit=ChatState.handle_submit,
        reset_on_submit=True
        
    )