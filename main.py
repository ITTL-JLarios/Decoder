import flet as ft
from datetime import datetime

from program.search import Search
from program.decoder import Decoder


def main(page: ft.Page):
    def on_dialog_result(e: ft.FilePickerResultEvent):
        print('path: ', e.files[0].path)
        main_page.path_text(e.files[0].path)
        decoder_page.set_path(e.files[0].path)
        page.update()

    def change_date_start(e):
        print(f"Start Date picker changed, value is {date_picker_start.value}")
        decoder_page.set_start_date(date_picker_start.value)
        page.update()

    def change_date_end(e):
        print(f"End Date picker changed, value is {date_picker_start.value}")
        decoder_page.set_end_date(date_picker_end.value)
        page.update()

    page.title = 'TTL - Decoder'
    page.scroll = ft.ScrollMode.AUTO
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    # File Picker
    file_picker = ft.FilePicker(on_result=on_dialog_result)
    page.overlay.append(file_picker)
    # Date Picker
    date_picker_start = ft.DatePicker(
            on_change=change_date_start,
            last_date=datetime.now()
        )
    date_picker_end = ft.DatePicker(
            on_change=change_date_end,
            last_date=datetime.now()
        )
    page.overlay.append(date_picker_start)
    page.overlay.append(date_picker_end)
    page.update()

    # craete application instance
    main_page = Search(file_picker)
    decoder_page = Decoder(date_picker_start, date_picker_end)
    page.add(main_page)
    page.add(decoder_page)
    

ft.app(target=main)