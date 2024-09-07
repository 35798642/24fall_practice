# @Version  : 1.0
# @Author   : shyboy
# @File     : Left.py
# @Time     : 2024/8/26 22:18

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QTextEdit
from PyQt5.QtGui import QTextCharFormat, QColor, QFont
from PyQt5.QtCore import Qt
from Button import SubmitButton,ClearButton
from Table import Table
from pprint import pprint
import paddle
import paddlehub as hub
from paddlenlp import Taskflow
import erniebot


class InputText(QWidget):
    def __init__(self,table):
        super().__init__()

        self.textEdit = QTextEdit(self)
        self.textEdit.setPlaceholderText("请在此处输入案卷文本")
        self.textEdit.setStyleSheet("color: black; background: transparent")
        self.textEdit.setFont(QFont("Times",13))

        self.table=table
        
        self.submit_button = SubmitButton()
        self.submit_button.clicked.connect(self.submit)
        
        self.clear_button = ClearButton()
        self.clear_button.clicked.connect(self.clear)
        
        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)

        # 创建水平布局，将按钮放在水平居中位置
        button_layout = QHBoxLayout()
        button_layout.addStretch()  # 添加左侧弹性空间
        button_layout.addWidget(self.submit_button)  # 添加按钮
        button_layout.addWidget(self.clear_button)
        button_layout.addStretch()  # 添加右侧弹性空间

        layout.addLayout(button_layout)  # 将水平布局添加到主布局中
        self.setLayout(layout)
    
    def submit(self):
        text = self.textEdit.toPlainText()
        # print(text)
        schema = ['案件编号','法院', {'原告': '委托代理人'}, {'被告': '委托代理人'},'时间','一案','裁定','案情','案由','罪','判决结果']  # Define the schema for entity extraction
        ie = Taskflow('information_extraction', schema=schema, model='uie-m-base')
        ie.set_schema(schema)
        ie_results = ie(text)
        pprint(ie_results)
        self.display_ie_results(ie_results)
        self.display_extracted_results(ie_results)
        # erniebot.api_type = 'aistudio'
        # erniebot.access_token = '3f080f245967c292ea4d0fe159854a364cdb7e59'

        # response = erniebot.ChatCompletion.create(
        # model='ernie-3.5',
        # messages=[{
        # 'role': 'user',
        # 'content': text+"对于上述法律文书，我需要提取案件编号、案由、法院、原告或者公诉方、被告、审判员、审判时间、裁定、罪名等信息。返回格式为字典类型,要求"
        # }])

        # print(response.get_result())

        
    def display_ie_results(self, ie_results):
        cursor = self.textEdit.textCursor()
        # 设置特定文本的颜色和字体
        format = QTextCharFormat()
        format.setForeground(QColor("red"))
        format.setFont(QFont("Times", 13, QFont.Bold))
        for item in ie_results:
            for key, value_list in item.items():
                #self.resultEdit.append(f"{key}")
                max_probability = -1
                max_text = None
                start_pos=0
                end_pos=0
                # 不用找到概率最大的文本
                for value_dict in value_list:
                    if 'text' in value_dict:
                        max_text=value_dict['text']
                        start_pos=value_dict['start']
                        end_pos=value_dict['end']
                        cursor.setPosition(start_pos)  # 设置光标位置到特定文本的起始位置
                        cursor.setPosition(end_pos, cursor.MoveMode.KeepAnchor)  # 选择特定文本
                        cursor.setCharFormat(format)
                # 找到概率最大的文本
                # for value_dict in value_list:
                #     if 'text' in value_dict and 'probability' in value_dict:
                #         probability = value_dict['probability']
                #         if probability > max_probability:
                #             max_probability = probability
                #             max_text = value_dict['text']
                #             start_pos=value_dict['start']
                #             end_pos=value_dict['end']
    
                # if max_text is not None:
                #     cursor.setPosition(start_pos)  # 设置光标位置到特定文本的起始位置
                #     cursor.setPosition(end_pos, cursor.MoveMode.KeepAnchor)  # 选择特定文本
                #     cursor.setCharFormat(format)
    def display_extracted_results(self, ie_results):
        # 假设有一个 Table 类的实例 self.table
        self.table.display_results(ie_results)
    
    def clear(self):
        self.textEdit.clear()
        self.table.clear()
                
                    
import os
from PyQt5.QtWidgets import QWidget, QFileDialog, QVBoxLayout, QHBoxLayout, QListWidgetItem, QLabel, QSizePolicy, QTextEdit
from qfluentwidgets import PlainTextEdit, PushButton, ListWidget
import textract
import fitz  # PyMuPDF

class InputFile(QWidget):
    def __init__(self,table):
        super().__init__()
        self.table = table
        self.extracted = False  # 标志变量，标记是否已经提取过关键词
        self.extracted_texts = []  # 存储提取后的文本
        # 创建布局
        self.layout = QVBoxLayout(self)

        # 文件选择按钮
        self.select_button = PushButton("选择文件", self)
        self.select_button.clicked.connect(self.open_file_dialog)
        self.select_button.setFixedWidth(150)
        # self.select_button.setFixedWidth(120)

        # 将选择文件按钮添加到布局中，并使其靠左
        self.layout.addWidget(self.select_button)

        # 创建水平布局，左侧是较窄的ListWidget，右侧是较宽的PlainTextEdit
        self.horizontal_layout = QHBoxLayout()

        # 左侧较窄的ListWidget，用于显示文件名和删除按钮
        self.file_list_widget = ListWidget(self)
        self.file_list_widget.setStyleSheet("color: black; background: transparent;border: 1px solid #b0b0b0;")
        self.file_list_widget.setMinimumWidth(150)
        self.file_list_widget.setMaximumWidth(150)
        self.file_list_widget.itemClicked.connect(self.display_file_content)

        # 右侧较宽的PlainTextEdit，用于显示文件内容
        self.content_text_edit = QTextEdit(self)
        self.content_text_edit.setStyleSheet("color: black; background: transparent; border: 1px solid #b0b0b0;")
        self.content_text_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.content_text_edit.setReadOnly(True)
        # self.content_text_edit.setLineWrapMode(PlainTextEdit.WidgetWidth)
        self.content_text_edit.setFont(QFont("Times",13))
        # 将两个控件添加到水平布局中
        self.horizontal_layout.addWidget(self.file_list_widget)
        self.horizontal_layout.addWidget(self.content_text_edit)

        # 将水平布局添加到主布局中
        self.layout.addLayout(self.horizontal_layout)

        # 开始提取按钮
        self.start_extract_button = SubmitButton()
        self.start_extract_button.pushButton.setText("批量提取")
        self.start_extract_button.clicked.connect(self.extract_file_content)
        self.clear_button = ClearButton()
        self.clear_button.clicked.connect(self.clear)
        
        # 创建水平布局，将按钮放在水平居中位置
        button_layout = QHBoxLayout()
        button_layout.addStretch()  # 添加左侧弹性空间
        button_layout.addWidget(self.start_extract_button)  # 添加按钮
        button_layout.addWidget(self.clear_button)
        button_layout.addStretch()  # 添加右侧弹性空间

        self.layout.addLayout(button_layout)  # 将水平布局添加到主布局中

        # 设置默认路径
        self.default_path = os.path.join("txt")

    def open_file_dialog(self):
        self.extracted = False  # 重置标志变量
        # 弹出文件选择器，默认路径在桌面，允许多选文件
        files, _ = QFileDialog.getOpenFileNames(
            self, "选择文件", self.default_path,
            "All Supported Files (*.txt *.docx *.doc *.pdf);;Text Files (*.txt);;Word Files (*.docx *.doc);;PDF Files (*.pdf)",
            options=QFileDialog.Options()
        )

        # 限制最多选择50个文件
        if len(files) > 50:
            files = files[:50]

        # 清空列表
        self.file_list_widget.clear()

        # 将选择的文件名添加到列表中，并添加删除按钮
        for file in files:
            self.add_file_item(file)

    def add_file_item(self, file_path):
        # 创建一个 QWidget 用于包含文件名和删除按钮
        item_widget = QWidget()
        item_layout = QHBoxLayout(item_widget)

        # 显示文件名的标签
        file_name = os.path.basename(file_path)
        file_label = QLabel(file_name)
        file_label.setStyleSheet("font-size:12px;font-family: 'Microsoft YaHei UI';color: black;")

        # 删除按钮
        remove_button = PushButton("删除")
        remove_button.setStyleSheet("""
                    QPushButton {
                        font-size:13px;
                        font-family: 'Microsoft YaHei UI';
                        color: black;
                        border-radius: 2px;  /* 较小的圆角 */
                        border: 1px solid #b0b0b0;  /* 边框为稍深的灰色 */
                    }
                    QPushButton:hover {
                        background-color: #e0e0e0;  /* 悬停时稍微变深 */
                    }
                    QPushButton:pressed {
                        background-color: #d0d0d0;  /* 点击时变为更深的灰色 */
                    }
                """)
        remove_button.setFixedWidth(45)
        remove_button.clicked.connect(lambda: self.remove_file_item(item_widget))

        # 将标签和按钮添加到布局中
        item_layout.addWidget(file_label)
        item_layout.addWidget(remove_button)
        item_layout.setContentsMargins(0, 0, 0, 0)

        # 创建 QListWidgetItem 并将 QWidget 作为其内容
        list_item = QListWidgetItem(self.file_list_widget)
        list_item.setSizeHint(item_widget.sizeHint())

        # 将 QWidget 作为 QListWidgetItem 的子项添加到 QListWidget 中
        self.file_list_widget.addItem(list_item)
        self.file_list_widget.setItemWidget(list_item, item_widget)

    def remove_file_item(self, item_widget):
        # 查找对应的 QListWidgetItem 并移除
        for i in range(self.file_list_widget.count()):
            list_item = self.file_list_widget.item(i)
            if self.file_list_widget.itemWidget(list_item) == item_widget:
                self.file_list_widget.takeItem(i)
                break

    def display_file_content(self, item):
        # 获取点击的文件路径
        item_widget = self.file_list_widget.itemWidget(item)
        file_label = item_widget.findChild(QLabel)
        file_path = os.path.join(self.default_path, file_label.text())

        # 读取文件内容并显示在右侧的PlainTextEdit中
        if self.extracted:
            # 如果已经提取过关键词，显示标红后的文本
            self.content_text_edit.clear()
            for file_name, content, ie_results in self.extracted_texts:
                if file_name == file_label.text():
                    self.content_text_edit.setPlainText(content)
                    self.display_ie_results(ie_results)
                    break
        else:
            # 否则显示原始文本
            if file_path.endswith('.txt'):
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
            elif file_path.endswith('.docx') or file_path.endswith('.doc'):
                content = textract.process(file_path).decode('utf-8')
            elif file_path.endswith('.pdf'):
                with fitz.open(file_path) as pdf_document:
                    content = ""
                    for page_num in range(len(pdf_document)):
                        page = pdf_document.load_page(page_num)
                        content += page.get_text()
            self.content_text_edit.setPlainText(content)
    
    def extract_file_content(self):
        extracted_results = []
        self.extracted_texts.clear() # 清空之前提取的文本
        
        for i in range(self.file_list_widget.count()):
            item = self.file_list_widget.item(i)
            item_widget = self.file_list_widget.itemWidget(item)
            file_label = item_widget.findChild(QLabel)
            file_path = os.path.join(self.default_path, file_label.text())

            # 读取文件内容
            if file_path.endswith('.txt'):
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
            elif file_path.endswith('.docx') or file_path.endswith('.doc'):
                content = textract.process(file_path).decode('utf-8')
            elif file_path.endswith('.pdf'):
                with fitz.open(file_path) as pdf_document:
                    content = ""
                    for page_num in range(len(pdf_document)):
                        page = pdf_document.load_page(page_num)
                        content += page.get_text()

            # 提取信息
            schema = ['案件编号', '案情','罪名','法院', {'原告': '委托代理人'}, {'被告': '委托代理人'}, '审判员','时间', '裁定']
            ie = Taskflow('information_extraction', schema=schema, model='uie-m-base')
            ie.set_schema(schema)
            ie_results = ie(content)
            extracted_results.append((file_label.text(), content, ie_results))
            self.extracted_texts.append((file_label.text(), content, ie_results))
            
        # 将提取结果传递给表格
        self.display_extracted_results(extracted_results)
        self.extracted = True  # 更新标志变量
    
    def display_extracted_results(self, extracted_results):
        self.table.display_batch_results(extracted_results)
    
    def display_ie_results(self, ie_results):
        cursor = self.content_text_edit.textCursor()
        # 设置特定文本的颜色和字体
        format = QTextCharFormat()
        format.setForeground(QColor("red"))
        format.setFont(QFont("Times", 13, QFont.Bold))
        for item in ie_results:
            for key, value_list in item.items():
                max_probability = -1
                max_text = None
                start_pos=0
                end_pos=0
                # 不用找到概率最大的文本
                for value_dict in value_list:
                    if 'text' in value_dict:
                        max_text=value_dict['text']
                        start_pos=value_dict['start']
                        end_pos=value_dict['end']
                        cursor.setPosition(start_pos)
                        cursor.setPosition(end_pos, cursor.MoveMode.KeepAnchor)
                        cursor.setCharFormat(format)
    
    def clear(self):
        self.file_list_widget.clear()
        self.content_text_edit.clear()
        self.table.clear()
        self.extracted = False
        self.extracted_texts.clear()
            

    