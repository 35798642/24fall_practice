# @Version  : 1.0
# @Author   : shyboy
# @File     : Table.py.py
# @Time     : 2024/8/27 9:54
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QWidget, QHBoxLayout, QHeaderView
from qfluentwidgets import TableWidget, PushButton, HyperlinkButton


class Table(QWidget):
    """ 演示窗口类 """
    def __init__(self):
        super().__init__()
        # 创建水平布局器
        self.hBoxLayout = QHBoxLayout(self)
        # 创建表格视图组件
        self.tableView = TableWidget(self)

        # 显示表格边框
        self.tableView.setBorderVisible(True)
        # 设置表格的圆角边框半径
        self.tableView.setBorderRadius(8)

        # 禁用自动换行
        self.tableView.setWordWrap(False)
        # 设置表格的行数为60
        self.tableView.setRowCount(50)
        # 设置表格的列数为8
        self.tableView.setColumnCount(7)

        # 初始化包含5条信息的列表，每条信息为一个子列表
        # caseInfos = [
        #     ['（2021）闽刑终306号', '盗窃', '张三', '25', '北京', '本科', '否', '2024-08-26'],
        #     ['（2021）闽刑终307号', '抢劫', '李四', '30', '上海', '硕士', '是', '2024-08-20'],
        #     ['（2021）闽刑终308号', '诈骗', '王五', '28', '广州', '高中', '否', '2024-07-15'],
        #     ['（2021）闽刑终309号', '贩毒', '赵六', '35', '深圳', '本科', '是', '2024-06-30'],
        #     ['（2021）闽刑终310号', '敲诈勒索', '孙七', '40', '成都', '大专', '否', '2024-05-10']
        #
        caseInfos = []
        for i, caseInfo in enumerate(caseInfos):
            for j, item in enumerate(caseInfo):
                table_item = QTableWidgetItem(item)
                table_item.setTextAlignment(Qt.AlignCenter)  # 设置文本居中
                self.tableView.setItem(i, j, table_item)
            #     # 创建超链接按钮
            # detail_button = HyperlinkButton("https://baidu.com",'查看详情')
            # # detail_button.setStyleSheet("color: blue; text-decoration: underline; background: none; border: none;")
            # # # 为每个按钮传递不同的链接
            # # detail_button.clicked.connect(lambda checked, url=caseInfo[-1]: self.open_link(url))
            # # detail_button.setUrl("https://baidu.com")
            # self.tableView.setCellWidget(i, 8, detail_button)  # 在第9列设置按钮

        # 隐藏垂直表头
        self.tableView.verticalHeader().hide()
        # 设置水平表头标签
        self.tableView.setHorizontalHeaderLabels(
            ['案件编号', '案由', '法院', '原告', '被告', '审判员', '判决时间'])
        
       
        # 根据内容调整列宽
        self.tableView.resizeColumnsToContents()
        # 设置列宽自适应填充模式
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        # 启用表格的排序功能
        self.tableView.setSortingEnabled(True)

        # 设置整体窗口的背景颜色为白色
        self.setStyleSheet("Demo{background: rgb(255, 255, 255)} ")
        # 设置布局器的边距
        self.hBoxLayout.setContentsMargins(50, 30, 50, 30)
        # 将表格视图添加到布局器中
        self.hBoxLayout.addWidget(self.tableView)
        # 调整窗口大小
        self.resize(850, 600)
        # self.tableView.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    def display_results(self, ie_results):
        self.tableView.setRowCount(0)  # 清空表格
        print(ie_results)

        # 设置固定表头
        headers = ['案件编号','案由','法院', '原告', '被告','审判员','判决时间']
        self.tableView.setColumnCount(len(headers))
        self.tableView.setHorizontalHeaderLabels(headers)

        # 设置字体
        font = QFont()
        font.setFamily("Times")
        font.setPointSize(12)
        
        # 填充表格
        for item in ie_results:
            row_position = self.tableView.rowCount()
            self.tableView.insertRow(row_position)
            for i, header in enumerate(headers):
                if header in item:
                    max_probability = -1
                    max_text = None
                    for value_dict in item[header]:
                        if 'probability' in value_dict and value_dict['probability'] > max_probability:
                            max_probability = value_dict['probability']
                            max_text = value_dict['text']
                    if max_text is not None:
                        table_item = QTableWidgetItem(max_text)
                        table_item.setFont(font)  # 设置字体
                        self.tableView.setItem(row_position, i, table_item)
                        
                else:
                   # 如果某个键在 ie_results 中不存在，则对应的表格列为空
                    table_item = QTableWidgetItem("")
                    table_item.setFont(font)  # 设置字体
                    self.tableView.setItem(row_position, i, table_item)
    
    def display_batch_results(self, extracted_results):
        self.tableView.setRowCount(0)  # 清空表格
        print(extracted_results)

        # 设置固定表头
        headers = ['裁定', '一案', '法院', '原告', '被告', '审判员', '判决时间']
        self.tableView.setColumnCount(len(headers))
        self.tableView.setHorizontalHeaderLabels(headers)

        # 设置字体
        font = QFont()
        font.setFamily("Times")
        font.setPointSize(12)

        # 填充表格
        for file_name, content, ie_results in extracted_results:
            row_position = self.tableView.rowCount()
            self.tableView.insertRow(row_position)
            for i, header in enumerate(headers):
                if header in ie_results[0]:
                    max_probability = -1
                    max_text = None
                    for value_dict in ie_results[0][header]:
                        if 'probability' in value_dict and value_dict['probability'] > max_probability:
                            max_probability = value_dict['probability']
                            max_text = value_dict['text']
                    if max_text is not None:
                        table_item = QTableWidgetItem(max_text)
                        table_item.setFont(font)  # 设置字体
                        self.tableView.setItem(row_position, i, table_item)
                else:
                    # 如果某个键在 ie_results 中不存在，则对应的表格列为空
                    table_item = QTableWidgetItem("")
                    table_item.setFont(font)  # 设置字体
                    self.tableView.setItem(row_position, i, table_item)
        # 设置固定表头
        headers = ['案件编号', '案由', '法院', '原告', '被告', '审判员', '判决时间']
        self.tableView.setColumnCount(len(headers))
        self.tableView.setHorizontalHeaderLabels(headers)
    
    # 清空表格内容
    def clear(self):
        self.tableView.clearContents()
        self.tableView.setHorizontalHeaderLabels(['案件编号','案由','法院', '原告', '被告','审判员','判决时间'])
    # 获取表格数据
    def get_table_data(self):
        data = []
        for row in range(self.tableView.rowCount()):
            row_data = []
            for column in range(self.tableView.columnCount()):
                item = self.tableView.item(row, column)
                if item is not None:  # 确保单元格中有数据
                    row_data.append(item.text())
                else:
                    row_data.append('')
            data.append(row_data)
        return data
    
        

if __name__ == "__main__":
    # 启用高DPI缩放比例的处理策略
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    # 启用高DPI缩放支持
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    # 启用高DPI图像支持
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    # 创建应用程序对象
    app = QApplication(sys.argv)
    # 创建演示窗口对象
    w = Table()
    # 显示窗口
    w.show()
    # 进入应用程序的主循环
    sys.exit(app.exec())
