import flet as ft


def main(page: ft.Page):
    file_picker = ft.FilePicker()
    page.overlay.append(file_picker)
    page.update()

ft.app(target=main, view=ft.WEB_BROWSER)