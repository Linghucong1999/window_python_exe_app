import tkinter as tk
from tkinter import simpledialog, scrolledtext
from tkinter import ttk
import threading
import time
import requests


class DataCrawlerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("爬虫数据采集器")

        # 创建输入框
        tk.Label(root, text="请输入isp-token：").grid(row=0, column=0)
        self.token_entry = tk.Entry(root)
        self.token_entry.grid(row=0, column=1)

        tk.Label(root, text="请输入Cookie:").grid(row=1, column=0)
        self.cookie_entry = tk.Entry(root)
        self.cookie_entry.grid(row=1, column=1)

        tk.Label(root, text="请输入载荷:").grid(row=2, column=0)
        self.json_text = scrolledtext.ScrolledText(root, height=10, width=50)
        self.json_text.grid(row=2, column=1, rowspan=3)

        # 创建发送按钮
        tk.Button(root, text="发送", command=self.send_data).grid(
            row=5, column=1)

    def send_data(self):
        token = self.token_entry.get()
        cookie = self.cookie_entry.get()
        data_raw = self.json_text.get("1.0", tk.END)
        print(f"isp-token:{token}, Cookie:{cookie}, data:{data_raw}")


if __name__ == "__main__":
    root = tk.Tk()
    app = DataCrawlerApp(root)
    root.mainloop()
