"""シンプルな電卓を表示するモジュール."""
from tkinter import *
from tkinter import ttk


# 2次元配列のとおりに、gridでレイアウトを作成する
LAYOUT = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', 'C', '=', '+'],
]

# 記号をまとめた定数. if char in CALC_SYMBOLS:... のように使うために定義
CALC_SYMBOLS = ('+', '-', '*', '/', '**', '//')


class CalcApp(ttk.Frame):
    """電卓アプリ."""

    def __init__(self, master=None):
        super().__init__(master)
        # 現在の式を格納するリスト。['1', '+', '100', '*', '1'] のようになる
        self.exp_list = ['0']
        self.create_style()
        self.create_widgets()

    def create_style(self):
        """ボタン、ラベルのスタイルを変更."""
        style = ttk.Style()

        # ラベルのスタイルを上書き
        style.configure(
            'TLabel', font=('Helvetica', 20),
            background='black', foreground='white',
        )
        # ボタンのスタイルを上書き
        style.configure('TButton', font=('Helvetica', 20))

    def create_widgets(self):
        """ウィジェットの作成."""
        # 1 + 2 * 3 // 4 のようなpythonの式が文字列で入る
        self.expression_var = StringVar()
        self.expression_var.set('0')  # 初期値

        # 計算結果の表示ラベル
        dispay_label = ttk.Label(
            self, textvariable=self.expression_var)
        dispay_label.grid(
            column=0, row=0, columnspan=4, sticky=(N, S, E, W))

        # レイアウトの作成
        for y, row in enumerate(LAYOUT, 1):
            for x, char in enumerate(row):
                button = ttk.Button(self, text=char)
                button.grid(column=x, row=y, sticky=(N, S, E, W))
                button.bind('<Button-1>', self.calc)

        # 横の引き伸ばし設定。全て等分に引き伸ばす
        self.grid(column=0, row=0, sticky=(N, S, E, W))
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)

        # 縦の引き伸ばし設定。0番目の結果表示欄だけ、元の大きさのまま
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)

        # ウィンドウ自体の引き伸ばし設定
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

    def calc(self, event):
        """全てのボタンは、押すとここが呼ばれる."""
        # 押されたボタンのテキストを取得
        char = event.widget['text']

        # 最後に押したボタンの内容
        last = self.exp_list[-1]

        # =ボタン(現在の式の評価)の場合
        if char == '=':
            if last in CALC_SYMBOLS:
                self.exp_list.pop()
            exp = eval(''.join(self.exp_list))
            self.exp_list = [str(exp)]

        # Cボタン、内容クリア
        elif char == 'C':
            self.exp_list = ['0']

        # +,-,*,/,等の記号を押した場合
        elif char in CALC_SYMBOLS:
            if last == char == '/':
                self.exp_list[-1] += '/'
            elif last == char == '*':
                self.exp_list[-1] += '*'
            elif last in CALC_SYMBOLS:
                self.exp_list[-1] = char
            else:
                self.exp_list.append(char)

        # それ以外、数字を押した場合
        else:
            if last == '0':
                self.exp_list[-1] = char
            elif last in CALC_SYMBOLS:
                self.exp_list.append(char)
            else:
                self.exp_list[-1] += char

        # リストに格納している式を文字列にし、画面に反映
        self.expression_var.set(
            ' '.join(self.exp_list)
        )


def main():
    root = Tk()
    root.title('簡単電卓')
    app = CalcApp(root)
    root.mainloop()


if __name__ == '__main__':
    main()
