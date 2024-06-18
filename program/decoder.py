import flet as ft
from cryptography.fernet import Fernet
from datetime import datetime

class Decoder(ft.Column):
    def __init__(self, date_picker_start, date_picker_end):
        super().__init__()
        self.key = b'3lqUcKreSiI3DzVdHHD7VggudxDIcWCp-bONmioaebE='
        self.fernet = Fernet(self.key)
        self.path = None
        self.width = 700

        self.date_picker_start, self.date_picker_end = date_picker_start, date_picker_end

        self.start_date = ft.ElevatedButton(
                        "From: Date",
                        icon=ft.icons.CALENDAR_MONTH,
                        expand= True,
                        on_click=lambda _: self.date_picker_start.pick_date())
        
        self.end_date = ft.ElevatedButton(
                        "To: Date",
                        icon=ft.icons.CALENDAR_MONTH,
                        expand= True,
                        on_click=lambda _: self.date_picker_end.pick_date())

        # Table
        self.headers = [
            ft.DataColumn(ft.Text('DateTime')),
            ft.DataColumn(ft.Text('App')),
            ft.DataColumn(ft.Text('Title Window'))
        ]
        self.rows = []

        self.controls = [
            ft.Row(
                controls=[
                    self.start_date,
                    ft.Text(value='To'),
                    self.end_date
                ]
            ),
            ft.Row(
                controls=[
                    ft.ElevatedButton(text='Decode File',
                                  icon='Decode',
                                  expand=True,
                                  on_click=self.decode,
                                  bgcolor=ft.colors.BLUE,
                                  color=ft.colors.WHITE,
                                  width=600
                                  )
                ]
            ),
            ft.DataTable(
                columns=self.headers,
                rows=self.rows,
                expand=True
            )
        ]

    def decode(self, e):
        dlg = ft.AlertDialog(
            title=ft.Text('PLease seclect a File to Decode'),
            on_dismiss=lambda e: print('dismissed'))
        if self.path:
            print('decoding...')
            with open(self.path, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    row = line.split(',')

                    time_stamp = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S.%f')

                    if type(self.start_date.text) == str or self.start_date.text > time_stamp:
                        if type(self.end_date.text) == str or self.end_date.text < time_stamp:
                    
                            decrypt_app = self.fernet.decrypt(row[1]).decode()
                            decrypt_title = self.fernet.decrypt(row[2]).decode()
                            self.rows.append(
                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(ft.Text(str(row[0]))),
                                        ft.DataCell(ft.Text(decrypt_app)),
                                        ft.DataCell(ft.Text(decrypt_title)),
                                    ]
                                )
                            )
            self.update()
        else:
            dlg.open = True

    def set_path(self, path:str):
        self.path = path

    def set_start_date(self, date):
        self.start_date.text = date

    def set_end_date(self, date):
        self.end_date.text = date