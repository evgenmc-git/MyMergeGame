import flet as ft

@ft.control
class ItemButton(ft.Button):
    pass

class MainPage:
    def __init__(self, page: ft.Page):
        self.page = page
        page.add(ft.Row(controls=[
            ft.Container(content=ft.Row(
                controls=[
                    ft.Column(controls=[ItemButton('0')])
                ]
            ))
        ]))

#region Start
def begin(page: ft.Page):
    a = MainPage(page)

ft.run(begin)
#endregion