# @Version  : 1.0
# @Author   : shyboy
# @File     : Button.py
# @Time     : 2024/8/27 10:45
# # coding=utf-8


import csv
import pandas as pd
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QWidget, QHBoxLayout,QFileDialog,QTableWidgetItem
from qfluentwidgets import Action, PushButton, RoundMenu, TransparentDropDownPushButton
from PyQt5.QtCore import pyqtSignal


class ButtonView(QWidget):

    def __init__(self):
        super().__init__()
        self.setStyleSheet("ButtonView{background: rgb(255,255,255)}")

class WhiteButton(ButtonView):
    def __init__(self):
        super().__init__()
        self.pushButton = PushButton()
        self.pushButton.setStyleSheet("background: transparent;")
        # 创建水平布局器，并将按钮对齐到右边
        layout = QHBoxLayout()
        layout.addWidget(self.pushButton)
        self.setLayout(layout)
        self.setMinimumHeight(50)
        self.setMaximumWidth(130)

class SubmitButton(ButtonView):
    clicked = pyqtSignal()  # 定义 clicked 信号
    
    def __init__(self):
        super().__init__()
        self.pushButton = PushButton(QIcon("img/提交.png"), '开始提取')
        layout = QHBoxLayout()
        layout.addWidget(self.pushButton)
        self.setLayout(layout)
        self.setMinimumHeight(50)
        self.setMaximumWidth(130)
        # 连接 pushButton 的 clicked 信号到 SubmitButton 的 clicked 信号
        self.pushButton.clicked.connect(self.emit_clicked_signal)
    
    def emit_clicked_signal(self):
        self.clicked.emit()

class ClearButton(ButtonView):
    clicked = pyqtSignal()  # 定义 clicked 信号
    
    def __init__(self):
        super().__init__()
        self.pushButton = PushButton(QIcon("img/清空.png"), '清空')
        layout = QHBoxLayout()
        layout.addWidget(self.pushButton)
        self.setLayout(layout)
        self.setMinimumHeight(50)
        self.setMaximumWidth(130)
        # 连接 pushButton 的 clicked 信号到 SubmitButton 的 clicked 信号
        self.pushButton.clicked.connect(self.emit_clicked_signal)
    
    def emit_clicked_signal(self):
        self.clicked.emit()


class ImportButton(ButtonView):
    def __init__(self, table):
        super().__init__()
        self.table = table  # 传入 Table 类的实例

        self.menu = RoundMenu(parent=self)
        action_csv = Action(QIcon("img/CSV图标.png"), 'csv 格式')
        action_excel = Action(QIcon("img/Excel图标.png"), 'excel 格式')
        self.menu.addAction(action_csv)
        self.menu.addAction(action_excel)
        self.transparentDropDownPushButton = TransparentDropDownPushButton(QIcon("img/导入.png"), '导入')

        self.transparentDropDownPushButton.setMenu(self.menu)

        layout = QHBoxLayout()
        layout.addWidget(self.transparentDropDownPushButton)
        self.setLayout(layout)

        action_csv.triggered.connect(self.import_csv)
        action_excel.triggered.connect(self.import_excel)

    def import_csv(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "打开 CSV", "", "CSV 文件 (*.csv)")
        if file_name:
            self.load_csv(file_name)

    def import_excel(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "打开 Excel 文件", "", "Excel 文件 (*.xls *.xlsx)")
        if file_name:
            self.load_excel(file_name)

    def load_csv(self, file_name):
        df = pd.read_csv(file_name)
        self.append_data_to_table(df)

    def load_excel(self, file_name):
        df = pd.read_excel(file_name)
        self.append_data_to_table(df)

    def append_data_to_table(self, df):
         # 设置字体
        font = QFont()
        font.setFamily("Times")
        font.setPointSize(12)
        for i, row in df.iterrows():
            self.table.tableView.insertRow(0)  # 在表格最上方插入新行
            for j, value in enumerate(row):
                if pd.notna(value):
                    table_item = QTableWidgetItem(str(value))
                    table_item.setFont(font)  # 设置字体
                    self.table.tableView.setItem(0, j, table_item)  # 插入数据到新的最上方行


class ExportButton(ButtonView):
    def __init__(self, table):
        super().__init__()  # 调用父类构造函数
        self.table = table  # 保存表格引用

        self.menu = RoundMenu(parent=self)
        action_csv = Action(QIcon("img/CSV图标.png"), 'csv 格式')
        action_excel = Action(QIcon("img/Excel图标.png"), 'excel 格式')
        self.menu.addAction(action_csv)
        self.menu.addAction(action_excel)
        self.transparentDropDownPushButton = TransparentDropDownPushButton(QIcon("img/导出.png"), '导出')
        
        self.transparentDropDownPushButton.setMenu(self.menu)

        # 创建布局，并将按钮添加到布局中
        layout = QHBoxLayout()
        layout.addWidget(self.transparentDropDownPushButton)
        self.setLayout(layout)

        # 连接导出动作
        action_csv.triggered.connect(self.export_csv)
        action_excel.triggered.connect(self.export_excel)

    def export_csv(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save CSV", "", "CSV Files (*.csv)")
        if path:
            data = self.table.get_table_data()  # 获取数据
            headers = ['案件编号', '案由', '法院', '原告', '被告', '审判员', '判决时间']  # 假设这是你的列名
            with open(path, 'w', newline='', encoding='utf-8-sig') as file:  # 注意这里使用 utf-8-sig
                writer = csv.writer(file)
                writer.writerow(headers)  # 首先写入表头
                for row_data in data:
                    writer.writerow(row_data)  # 写入数据

    def export_excel(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save Excel", "", "Excel Files (*.xlsx)")
        if path:
            data = self.table.get_table_data()  # 获取数据
            headers = ['案件编号', '案由', '法院', '原告', '被告', '审判员', '判决时间']  # 假设这是你的列名
            df = pd.DataFrame(data, columns=headers)  # 创建 DataFrame 并指定列名
            df.to_excel(path, index=False)  # 保存到 Excel，不包含索引




