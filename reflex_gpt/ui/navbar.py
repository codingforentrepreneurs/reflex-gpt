import reflex as rx

def base_navbar(child, *args, **kwargs) -> rx.Component:
    return rx.heading(child, *args, **kwargs)