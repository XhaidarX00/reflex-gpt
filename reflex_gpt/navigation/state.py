import reflex as rx 


from . import routes


class NavState(rx.State):
    def to_home(self):
        """
        on_click event
        """
        return rx.redirect(routes.HOME_ROUTE)
    
    def to_about_us(self):
        """
        on_click event
        """
        return rx.redirect(routes.ABOUT_US_PAGE)
    
    def to_chat(self):
        """
        on_click event
        """
        return rx.redirect(routes.CHAT_ROUTE)