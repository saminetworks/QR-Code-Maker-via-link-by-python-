
"""QRコード作成アプリ"""

import io
import qrcode  # QRコード使用
import FreeSimpleGUI as sg

# グローバル変数の初期定義
IMAGE = None

# アプリの色合いを決める
sg.theme("DarkBrown3")

# URLとURL入力エリア、QRコード作成ボタン、
# QRコード作成ボタン、ファイル保存ボタンとテキストエリア
# QRコード表示エリア
layout = [
    [
        sg.Text("URL"),
        sg.InputText(key="in1"),
    ],
    [
        sg.Button(
            "QRコード作成",
            key="btn1",
        ),
    ],
    [
        sg.Button(
            "ファイルを保存",
            key="btn2",
        ),
        sg.Text(key="txt"),
    ],
    [
        sg.Image(key="img"),
    ],
]

# アプリのウインドウ全体作成(resizable=Trueで可変にする)
window = sg.Window("QRコード作成", layout, size=(320, 400), resizable=True)


def execute():
    """QRコードを生成"""
    global IMAGE  # pylint: disable=global-statement
    if not values["in1"]:
        sg.PopupTimed("URLを入力してください。")
        return
    IMAGE = qrcode.make(values["in1"])  # QRコード画像を生成
    IMAGE.thumbnail((300, 300))
    bio = io.BytesIO()
    IMAGE.save(bio, format="PNG")
    window["img"].update(data=bio.getvalue())


while True:
    event, values = window.read()
    if event == "btn1":  # QRコード作成ボタン
        execute()
    if event is None:
        break
window.close()
