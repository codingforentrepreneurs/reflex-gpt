"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config

from reflex_gpt import ui

def home_page() -> rx.Component:
    # Welcome Page (Index)
    return ui.base_layout(
        rx.vstack(
            rx.heading("Welcome to Reflex GPT!", size="9"),
            rx.text(
                "Get started by editing something like ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )
