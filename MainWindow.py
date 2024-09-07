# -*- coding: utf-8 -*-

from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QGroupBox, QStackedLayout
from Button import ExportButton, ImportButton
from Table import Table
from Left import InputText, InputFile
from SegmentedButton import SegmentedButton


class Ui_MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setUpUi()

    def create_stacked_layout(self):
        self.stack_layout = QStackedLayout()
        win1_input_text = InputText(self.table)
        win2_input_file = InputFile(self.table)
        self.stack_layout.addWidget(win1_input_text)
        self.stack_layout.addWidget(win2_input_file)

    def text_clicked(self):
        self.stack_layout.setCurrentIndex(0)

    def file_clicked(self):
        self.stack_layout.setCurrentIndex(1)

    def paintEvent(self, event):  # set background_img

        painter = QPainter(self)

        painter.drawRect(self.rect())

        pixmap = QPixmap("img\\背景4.png")
        # 设置透明度，0.0 完全透明，1.0 完全不透明
        painter.setOpacity(0.15)  # 将透明度设置为15%
        painter.drawPixmap(self.rect(), pixmap)
        
    # def setUpUi(self):
    #     icon = QtGui.QIcon("img/法律法规.png")
    #     self.setWindowIcon(icon)
    #     self.setWindowTitle("司法文本信息提取")

    #     # 主窗口设置部分
    #     self.setObjectName("MainWindow")
    #     self.move(0, 0)
    #     self.resize(1920, 795)

    #     # 总体布局
    #     container = QHBoxLayout(self)

    #     # 左侧 box和左侧布局器
    #     left_box = QGroupBox(self)
    #     left_layout = QVBoxLayout(left_box)

    #     # 表格
    #     self.table = Table()
        
    #     # 使用 SegmentedButton 类，包含 SegmentedButton 和堆栈布局
    #     segmented_button = SegmentedButton(self.table)
    #     left_layout.addWidget(segmented_button)

    #     # 右侧 box和右侧布局器
    #     right_box = QGroupBox(self)
    #     right_layout = QVBoxLayout(right_box)

    #     # 导入/导出按钮
    #     right_up_layout = QHBoxLayout()
    #     import_button = ImportButton(self.table)
    #     export_button = ExportButton(self.table)
    #     right_up_layout.addWidget(import_button)
    #     right_up_layout.addWidget(export_button)
    #     right_layout.addLayout(right_up_layout)

        
    #     right_layout.addWidget(self.table)

    #     # 添加左右布局到主布局
    #     container.addWidget(left_box, stretch=1)
    #     container.addWidget(right_box, stretch=1)

    #     # 设置左侧 box 的最小宽度
    #     left_box.setMinimumWidth(580)

    #     self.setLayout(container)

    #     # 设置焦点到窗口本身，避免文本框默认获得焦点
    #     self.setFocus()
        
    def setUpUi(self):
        icon = QtGui.QIcon("img/法律法规.png")
        self.setWindowIcon(icon)
        self.setWindowTitle("司法文本信息提取")

        # 主窗口设置部分
        self.setObjectName("MainWindow")
        self.move(0, 0)
        self.resize(1920, 795)

        # 设置窗口的背景颜色
        self.setStyleSheet("""
            background-color: rgba(70,130,180,0.8);  /* 偏蓝色背景 */
        """)

        # 总体布局
        container = QHBoxLayout(self)

        # 左侧 box和左侧布局器
        left_box = QGroupBox(self)
        left_layout = QVBoxLayout(left_box)

        # 表格
        self.table = Table()
        
        # 使用 SegmentedButton 类，包含 SegmentedButton 和堆栈布局
        segmented_button = SegmentedButton(self.table)
        left_layout.addWidget(segmented_button)

        # 右侧 box和右侧布局器
        right_box = QGroupBox(self)
        right_layout = QVBoxLayout(right_box)

        left_box.setStyleSheet("""
                               
            background-color: rgba(248,248,255,0.8);  /* 白色背景 */
            
            border-radius: 15px;  /* 边框圆角 */
            margin-top: 5px;  /* 顶部外边距 */
            padding: 0px;  /* 内边距 */
        """)
        right_box.setStyleSheet("""
            background-color: rgba(248,248,255,0.8);  /* 白色背景 */
            
            border-radius: 15px;  /* 边框圆角 */
            margin-top: 5px;  /* 顶部外边距 */
            padding: 0px;  /* 内边距 */
        """)
        
        # 导入/导出按钮
        right_up_layout = QHBoxLayout()
        import_button = ImportButton(self.table)
        export_button = ExportButton(self.table)
        right_up_layout.addWidget(import_button)
        right_up_layout.addWidget(export_button)
        right_layout.addLayout(right_up_layout)

        right_layout.addWidget(self.table)

        # 添加左右布局到主布局
        container.addWidget(left_box, stretch=1)
        container.addWidget(right_box, stretch=1)

        # 设置左侧 box 的最小宽度
        left_box.setMinimumWidth(580)

        self.setLayout(container)

        # 设置焦点到窗口本身，避免文本框默认获得焦点
        self.setFocus()
