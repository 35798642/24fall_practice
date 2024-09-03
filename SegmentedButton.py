# @Version  : 1.0
# @Author   : shyboy
# @File     : SegmentedButton.py
# @Time     : 2024/8/30 15:21
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QStackedWidget, QVBoxLayout, QLabel, QSizePolicy, QHBoxLayout

from qfluentwidgets import Pivot, setTheme, Theme, SegmentedWidget, FluentIcon

from Left import InputText, InputFile
from Table import Table

class SegmentedButton(QWidget):
    def __init__(self,table):
        super().__init__()
        self.setStyleSheet("""
            SegmentedButton{background: white}
            QLabel{
                font: 20px 'Segoe UI';
                background: rgb(242,242,242);
                border-radius: 8px;
            }
            /* 设置 SegmentedWidget 的样式，使按钮更窄更高 */
            SegmentedWidget QPushButton {
                max-width: 100px;  /* 按钮的最大宽度 */
                min-height: 25px;  /* 按钮的最小高度 */
                max-height: 25px;  /* 按钮的最大高度 */
                font-size: 16px;  /* 字体大小 */
            }
        """)
        # self.resize(800, 600)  # 调整窗口大小

        # 创建 SegmentedButton
        self.pivot = SegmentedWidget(self)
        self.pivot.setFixedSize(100, 240)

        self.stackedWidget = QStackedWidget(self)

        self.input_text = InputText(table)  # InputText 实例
        self.input_file = InputFile(table)  # InputFile 实例

        # 添加子界面
        self.addSubInterface(self.input_text, 'input_text', '📄 文本输入')
        self.addSubInterface(self.input_file, 'input_file', '📁 文件输入')

        hBoxLayout = QHBoxLayout()
        hBoxLayout.addWidget(self.pivot)
        # 添加组件到布局中
        vBoxLayout = QVBoxLayout(self)
        vBoxLayout.addLayout(hBoxLayout)  # 添加 SegmentedButton
        vBoxLayout.addWidget(self.stackedWidget)  # 添加堆栈布局
        vBoxLayout.setContentsMargins(50, 10, 55, 30)

        self.stackedWidget.setCurrentWidget(self.input_text)
        self.pivot.setCurrentItem(self.input_text.objectName())
        self.pivot.currentItemChanged.connect(
            lambda k: self.stackedWidget.setCurrentWidget(self.findChild(QWidget, k))
        )

    def addSubInterface(self, widget, objectName, text):
        widget.setObjectName(objectName)
        self.stackedWidget.addWidget(widget)
        self.pivot.addItem(routeKey=objectName, text=text)
