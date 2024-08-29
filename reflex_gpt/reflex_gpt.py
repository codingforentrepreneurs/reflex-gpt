"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from . import chat, pages, navigation

app = rx.App()
app.add_page(pages.home_page, route=navigation.routes.HOME_ROUTE)
app.add_page(pages.about_us_page, route=navigation.routes.ABOUT_US_ROUTE)
app.add_page(
    chat.chat_page, 
    route=f"{navigation.routes.CHAT_ROUTE}/[session_id]",
    on_load=chat.state.ChatState.on_detail_load
)

app.add_page(
    chat.chat_page, 
    route=navigation.routes.CHAT_ROUTE,
    on_load=chat.state.ChatState.on_load
)

