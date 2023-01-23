import flet as ft

def main(page: ft.Page):
    t = ft.Text(value="Hello, world!")
    page.add(t)

ft.app(target=main, view=ft.WEB_BROWSER)
