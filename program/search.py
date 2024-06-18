import flet as ft

class Search(ft.Column):
    def __init__(self, file_picker):
        super().__init__()
        self.header = ft.Text(value="Total Transport Logistics - Decoder",
                              size=30,
                              expand=True)
        self.path = ft.Text(expand=True)
        self.width = 600
        self.file_picker = file_picker

        # Text update value
        self.path_text()

        # Controls
        self.controls = [ft.Row(controls=[
            self.header
        ]),
        ft.Row(controls=[
            ft.Icon(name=ft.icons.FOLDER_COPY_OUTLINED, color=ft.colors.BLACK),
            self.path,
            ft.ElevatedButton(  'Choose files...',
                                on_click=lambda _: self.file_picker.pick_files())
        ])]

    def path_text(self, path=None):
        self.path.value = path if path else 'Path...'