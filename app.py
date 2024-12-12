import importlib.util
import os
import subprocess
import sys

import pandas as pd
import wmi
from PySide6.QtCore import QSettings, QUrl, QPropertyAnimation, QEasingCurve, QRect, QSize, QCoreApplication, Qt
from PySide6.QtGui import QDesktopServices, QIcon, QFont
from PySide6.QtWidgets import QFileDialog, QTableWidgetItem, QMessageBox, QMainWindow, QApplication, QWidget, QFrame, \
    QVBoxLayout, QPushButton, QSpacerItem, QSizePolicy, QListWidgetItem, QLabel, QHBoxLayout

from ui_form import Ui_MainWindow
from functools import partial
import resources_rc

def check_and_install_dependencies(libraries):
    """检查并安装缺少的依赖库"""
    for library in libraries:
        try:
            __import__(library)
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", library])


def get_windows_system_info():
    info_str = ""
    try:
        c = wmi.WMI()

        # 获取操作系统基本信息
        os_info = c.Win32_OperatingSystem()[0]
        info_str += f"操作系统名称: {os_info.Name}\n"
        info_str += f"操作系统版本: {os_info.Version}\n"
        info_str += f"操作系统制造商: {os_info.Manufacturer}\n"
        info_str += f"操作系统安装日期: {os_info.InstallDate}\n"

        # 获取计算机系统信息
        computer_system = c.Win32_ComputerSystem()[0]
        info_str += f"计算机名称: {computer_system.Name}\n"
        info_str += f"计算机制造商: {computer_system.Manufacturer}\n"
        info_str += f"计算机型号: {computer_system.Model}\n"

        # 获取CPU信息
        for cpu in c.Win32_Processor():
            info_str += f"CPU名称: {cpu.Name}\n"
            info_str += f"CPU核心数: {cpu.NumberOfCores}\n"
            info_str += f"CPU线程数: {cpu.ThreadCount}\n"

        # 获取内存信息
        total_memory = 0
        for memory in c.Win32_PhysicalMemory():
            total_memory += int(memory.Capacity)
        info_str += f"总内存容量: {total_memory / 1024 / 1024 / 1024}GB\n"

        # 获取磁盘信息
        disk_info = ""
        for disk in c.Win32_DiskDrive():
            disk_info += f"磁盘型号: {disk.Model}\n"
            disk_info += f"磁盘容量: {int(disk.Size) / 1024 / 1024 / 1024}GB\n"
        info_str += f"磁盘信息:\n{disk_info}"

    except Exception as e:
        info_str += f"获取系统信息时出现错误: {e}"
    info_str = "\n\n".join(info_str.split('\n'))
    return info_str

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 启用拖放操作
        self.setAcceptDrops(True)

        # 连接按钮事件
        self.ui.action.triggered.connect(self.open_file)
        self.ui.action_2.triggered.connect(self.export_file)
        self.ui.action_process.triggered.connect(self.process_selected_data)  # 处理选中数据的按钮

        # 连接复选框事件
        self.ui.checkBox.stateChanged.connect(self.update_mode)  # 处理按选中单元格处理数据
        self.ui.checkBox_2.stateChanged.connect(self.update_mode)  # 处理按选中单元格一次性传递数据
        self.ui.pushButton.clicked.connect(self.load_last_opened_file)  # 处理选中数据的按钮

        # 初始化处理模式为按选中单元格处理数据
        self.process_mode = "selected_cell"  # 默认按单元格逐一处理数据

        # 读取历史记录
        self.load_last_opened_file()

        # 连接菜单事件
        self.ui.action_3.triggered.connect(self.tutorial)
        self.ui.action_4.triggered.connect(self.plug_in)
        self.ui.action_5.triggered.connect(self.open_group_chat)
        self.ui.action_6.triggered.connect(self.open_last_download)


        # 绑定功能菜单按钮
        # self.list_windows = MyWidget()
        # self.ui.pushButton_2.clicked.connect(self.list_windows.show)

        # 绑定按钮和事件
        # self.list_windows.ui.pushButton_1.clicked.connect(partial(self.apply_function_from_file,"1.py"))
        # self.list_windows.ui.pushButton_2.clicked.connect(partial(self.apply_function_from_file,"2.py"))
        # self.list_windows.ui.pushButton_3.clicked.connect(partial(self.apply_function_from_file,"3.py"))
        # self.list_windows.ui.pushButton_4.clicked.connect(partial(self.apply_function_from_file,"4.py"))
        # self.list_windows.ui.pushButton_5.clicked.connect(partial(self.apply_function_from_file,"5.py"))
        # self.list_windows.ui.pushButton_6.clicked.connect(partial(self.apply_function_from_file,"6.py"))

        # self.list_windows.ui.pushButton_1.clicked.connect(self.list_windows.hide)
        # self.list_windows.ui.pushButton_2.clicked.connect(self.list_windows.hide)
        # self.list_windows.ui.pushButton_3.clicked.connect(self.list_windows.hide)
        # self.list_windows.ui.pushButton_4.clicked.connect(self.list_windows.hide)
        # self.list_windows.ui.pushButton_5.clicked.connect(self.list_windows.hide)
        # self.list_windows.ui.pushButton_6.clicked.connect(self.list_windows.hide)

        # 绑定界面切换事件
        self.ui.pushButton_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.pushButton_4.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.pushButton_5.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.pushButton_6.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(3))



        # 获取系统信息
        sys_info = get_windows_system_info()
        self.ui.label.setText(sys_info)
        self.ui.pushButton_7.clicked.connect(self.copy_sys_info)

        # ------------------ 新增抽屉式侧边栏部分 ---------------------
        # 创建抽屉式侧边栏
        self.drawer = QFrame(self)
        self.drawer.setStyleSheet("background-color: #DCDCDC;")
        self.drawer.setGeometry(-200, 0, 200, self.height())  # 初始位置在视图外面
        self.drawer_layout = QVBoxLayout(self.drawer)

        # 向侧边栏添加内容（按钮等）
        # self.drawer_layout.addWidget(QPushButton("Home"))
        # self.drawer_layout.addWidget(QPushButton("Settings"))
        # self.drawer_layout.addWidget(QPushButton("About"))

        self.drawer_layout.addWidget(self.ui.pushButton_3)
        self.drawer_layout.addWidget(self.ui.pushButton_4)
        self.drawer_layout.addWidget(self.ui.pushButton_5)
        self.drawer_layout.addWidget(self.ui.pushButton_6)


        # 创建一个垂直方向起间隔作用的QWidget（本质利用其空白占位达到间隔效果）
        verticalSpacerWidget = QWidget()
        verticalSpacerWidget.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.drawer_layout.addWidget(verticalSpacerWidget)



        # 创建一个按钮，用于切换侧边栏
        self.toggle_button = QPushButton("", self)
        self.toggle_button.setGeometry(730, 0, 50, 50)  # 按钮的位置
        self.toggle_button.setStyleSheet("""
            QPushButton {
                border: none;  /* 去掉边框 */
                background: transparent;  /* 背景透明 */
                background-position: center;  /* 图标居中显示 */
            }
            QPushButton:hover {
                background-color: #E0E0E0;  /* 鼠标悬停时背景颜色 */
            }
            QPushButton:pressed {
                background-color: #C0C0C0;  /* 鼠标按下时背景颜色 */
            }
        """)
        self.toggle_button.setIconSize(QSize(32, 32))
        self.toggle_button.setIcon(QIcon(":/icons/images/菜单.png"))
        self.toggle_button.clicked.connect(self.toggle_drawer)

        # 创建动画效果
        self.animation = QPropertyAnimation(self.drawer, b"geometry")
        self.animation.setDuration(300)
        self.animation.setEasingCurve(QEasingCurve.InOutQuad)

        # 绑定收起事件
        self.ui.pushButton_3.clicked.connect(self.toggle_drawer)
        self.ui.pushButton_4.clicked.connect(self.toggle_drawer)
        self.ui.pushButton_5.clicked.connect(self.toggle_drawer)
        self.ui.pushButton_6.clicked.connect(self.toggle_drawer)

        # 连接信号和槽
        self.ui.checkBox.stateChanged.connect(self.on_checkBox_stateChanged)
        self.ui.checkBox_2.stateChanged.connect(self.on_checkBox_2_stateChanged)

    def on_checkBox_stateChanged(self, state):
        if state:
            self.ui.checkBox_2.setChecked(False)

    def on_checkBox_2_stateChanged(self, state):
        if state:
            self.ui.checkBox.setChecked(False)

    def toggle_drawer(self):
        """切换侧边栏的展开和收起"""
        current_pos = self.drawer.geometry().x()
        if current_pos < 0:
            # 如果侧边栏在视图外面，展开侧边栏
            self.animation.setStartValue(QRect(-200, 0, 200, self.height()))
            self.animation.setEndValue(QRect(0, 0, 200, self.height()))
        else:
            # 如果侧边栏已经展开，收起侧边栏
            self.animation.setStartValue(QRect(0, 0, 200, self.height()))
            self.animation.setEndValue(QRect(-200, 0, 200, self.height()))

        self.animation.start()

    def copy_sys_info(self):
        clipboard = QApplication.clipboard()
        text_to_copy = self.ui.label.text()
        clipboard.setText(text_to_copy)

    def update_mode(self):
        """根据复选框的选中状态更新处理模式"""
        if self.ui.checkBox.isChecked():
            self.process_mode = "selected_cell"  # 按单元格逐一处理数据
        elif self.ui.checkBox_2.isChecked():
            self.process_mode = "selected_cells_once"  # 按选中单元格一次性处理数据
        else:
            self.process_mode = "selected_cell"  # 默认按单元格逐一处理数据

    def process_selected_data(self):
        """根据复选框的选中状态处理数据"""
        # 获取选中的数据
        selected_indexes = self.ui.tableWidget.selectedIndexes()
        if not selected_indexes:
            QMessageBox.warning(self, "警告", "请先选择一些数据！")
            return

        # 提取选中的数据
        selected_data = {}
        for index in selected_indexes:
            row = index.row()
            col = index.column()
            item = self.ui.tableWidget.item(row, col)
            selected_data[(row, col)] = str(item.text()) if item else ""

        # 弹出文件选择对话框，选择一个 .py 文件
        file_path, _ = QFileDialog.getOpenFileName(
            None, "选择函数文件", "", "Python Files (*.py)"
        )

        if file_path:
            try:
                # 检查并安装所需的依赖库（例如 matplotlib, numpy 等）
                check_and_install_dependencies(['matplotlib', 'numpy'])  # 插件所需库

                # 动态加载用户选择的 Python 文件
                spec = importlib.util.spec_from_file_location("user_module", file_path)
                user_module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(user_module)

                # 确保文件中有一个函数可以处理选中的数据
                if not hasattr(user_module, 'func'):
                    QMessageBox.critical(self, "错误", "选定的 Python 文件中没有 `func` 函数！")
                    return

                # 获取函数
                process_data_function = user_module.func

                if self.process_mode == "selected_cell":
                    # 按单元格逐一处理数据
                    for (row, col), value in selected_data.items():
                        # 将选中的数据作为 x 传递给 func 函数
                        processed_value = process_data_function(value)
                        # 更新处理后的数据到表格
                        self.ui.tableWidget.setItem(row, col, QTableWidgetItem(str(processed_value)))

                elif self.process_mode == "selected_cells_once":
                    # 按选中单元格一次性传递数据
                    # 将所有选中单元格的数据一起传递给 `func` 函数
                    values = list(selected_data.values())
                    processed_values = process_data_function(values)

                    # 更新处理后的数据到表格
                    for i, (row, col) in enumerate(selected_data.keys()):
                        self.ui.tableWidget.setItem(row, col, QTableWidgetItem(str(processed_values[i])))

                QMessageBox.information(self, "成功", "数据处理完成！")
            except Exception as e:
                QMessageBox.critical(self, "错误", f"处理数据时出错: {str(e)}")

    def open_file(self, file_path=None):
        if not file_path:
            file_path, _ = QFileDialog.getOpenFileName(
                None, "选择文件", "", "Excel Files (*.xlsx *.xls)"
            )

        if file_path:
            try:
                df = pd.read_excel(file_path)
                self.display_data(df)

                # 保存最近打开的文件路径
                settings = QSettings("my_company", "my_app")
                settings.setValue("last_opened_file", file_path)
            except Exception as e:
                QMessageBox.critical(None, "错误", f"无法打开文件: {str(e)}")

    def display_data(self, df):
        self.ui.tableWidget.setRowCount(df.shape[0])
        self.ui.tableWidget.setColumnCount(df.shape[1])

        # 设置水平表头标签（使用DataFrame的列名）
        self.ui.tableWidget.setHorizontalHeaderLabels(list(df.columns))

        for row in range(df.shape[0]):
            for col in range(df.shape[1]):
                self.ui.tableWidget.setItem(row, col, QTableWidgetItem(str(df.iloc[row, col])))
        self.ui.tableWidget.resizeColumnsToContents()

    def export_file(self):
        file_path, _ = QFileDialog.getSaveFileName(
            None, "保存文件", "", "Excel Files (*.xlsx)"
        )

        if file_path:
            try:
                row_count = self.ui.tableWidget.rowCount()
                col_count = self.ui.tableWidget.columnCount()
                data = []

                for row in range(row_count):
                    row_data = []
                    for col in range(col_count):
                        item = self.ui.tableWidget.item(row, col)
                        row_data.append(item.text() if item else "")
                    data.append(row_data)

                df = pd.DataFrame(data)
                df.to_excel(file_path, index=False)
                QMessageBox.information(None, "成功", "文件导出成功！")
            except Exception as e:
                QMessageBox.critical(None, "错误", f"导出文件失败: {str(e)}")

    def get_table_data(self):
        # 获取整张表格的数据
        row_count = self.ui.tableWidget.rowCount()
        col_count = self.ui.tableWidget.columnCount()
        table_data = []

        for row in range(row_count):
            row_data = []
            for col in range(col_count):
                item = self.ui.tableWidget.item(row, col)
                row_data.append(str(item.text()) if item else "")
            table_data.append(row_data)

        return table_data

    def dragEnterEvent(self, event):
        # 处理拖放事件：允许拖放 .xlsx/.xls 或 .py 文件
        if event.mimeData().hasUrls():
            file_urls = event.mimeData().urls()
            file_path = file_urls[0].toLocalFile()
            if file_path.endswith('.py') or file_path.endswith('.xlsx') or file_path.endswith('.xls'):
                event.accept()
            else:
                event.ignore()
        else:
            event.ignore()

    def dropEvent(self, event):
        # 处理文件拖放事件
        file_urls = event.mimeData().urls()
        if len(file_urls) == 1:
            file_path = file_urls[0].toLocalFile()
            if file_path.endswith('.py'):
                self.apply_function_from_file(file_path)
            elif file_path.endswith('.xlsx') or file_path.endswith('.xls'):
                self.open_file(file_path)  # 自动打开 Excel 文件

    def apply_function_from_file(self, file_path):
        # 处理选中数据之前，确保有数据被选中
        selected_indexes = self.ui.tableWidget.selectedIndexes()
        if not selected_indexes:
            QMessageBox.warning(self, "警告", "请先选择数据！")
            return

        # 提取选中的数据
        selected_data = {}
        for index in selected_indexes:
            row = index.row()
            col = index.column()
            item = self.ui.tableWidget.item(row, col)
            selected_data[(row, col)] = str(item.text()) if item else ""

        try:
            # 检查并安装所需的依赖库（例如 matplotlib, numpy 等）
            check_and_install_dependencies(['matplotlib', 'numpy'])  # 插件所需库

            # 动态加载用户选择的 Python 文件
            spec = importlib.util.spec_from_file_location("user_module", file_path)
            user_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(user_module)

            # 确保文件中有一个函数可以处理选中的数据
            if not hasattr(user_module, 'func'):
                QMessageBox.critical(self, "错误", "选定的 Python 文件中没有 `func` 函数！")
                return

            # 获取函数
            process_data_function = user_module.func

            if self.process_mode == "selected_cell":
                # 按单元格逐一处理数据
                for (row, col), value in selected_data.items():
                    processed_value = process_data_function(value)
                    self.ui.tableWidget.setItem(row, col, QTableWidgetItem(str(processed_value)))

            elif self.process_mode == "selected_cells_once":
                # 按选中单元格一次性处理数据
                values = list(selected_data.values())
                processed_values = process_data_function(values)

                # 更新处理后的数据到表格
                for i, (row, col) in enumerate(selected_data.keys()):
                    self.ui.tableWidget.setItem(row, col, QTableWidgetItem(str(processed_values[i])))

            QMessageBox.information(self, "成功", "数据处理完成！")
        except Exception as e:
            QMessageBox.critical(self, "错误", f"处理数据时出错: {str(e)}")

    def apply_function_with_callback(self, callback):
        # 处理选中数据之前，确保有数据被选中
        selected_indexes = self.ui.tableWidget.selectedIndexes()
        if not selected_indexes:
            QMessageBox.warning(self, "警告", "请先选择数据！")
            return

        # 提取选中的数据
        selected_data = {}
        for index in selected_indexes:
            row = index.row()
            col = index.column()
            item = self.ui.tableWidget.item(row, col)
            selected_data[(row, col)] = str(item.text()) if item else ""

        try:
            if self.process_mode == "selected_cell":
                # 按单元格逐一处理数据
                for (row, col), value in selected_data.items():
                    processed_value = callback(value)
                    self.ui.tableWidget.setItem(row, col, QTableWidgetItem(str(processed_value)))

            elif self.process_mode == "selected_cells_once":
                # 按选中单元格一次性处理数据
                values = list(selected_data.values())
                processed_values = callback(values)

                # 更新处理后的数据到表格
                for i, (row, col) in enumerate(selected_data.keys()):
                    self.ui.tableWidget.setItem(row, col, QTableWidgetItem(str(processed_values[i])))

            QMessageBox.information(self, "成功", "数据处理完成！")
        except Exception as e:
            QMessageBox.critical(self, "错误", f"处理数据时出错: {str(e)}")



    def load_last_opened_file(self):
        # 加载最后打开的文件路径
        settings = QSettings("my_company", "my_app")
        last_opened_file = settings.value("last_opened_file", "")
        if last_opened_file:
            self.open_file(last_opened_file)

    def open_group_chat(self):
        # 打开交流群网页链接
        url = QUrl(
            "http://qm.qq.com/cgi-bin/qm/qr?_wv=1027&k=2dMalAAHkxATXq_4kjiYVaGsCmUpX41R&authKey=fxzHco4OmBhTuv7U8OkR2shsR1UAHQ8PDLVxq6eevxGRehARVkIC%2BlYKeB1zJgP3&noverify=0&group_code=676860109")
        QDesktopServices.openUrl(url)
        QMessageBox.information(self, "提示", "如果跳转失败，请手动加入，QQ群号：676860109")

    def open_last_download(self):
        # 打开下载链接
        url = QUrl("https://wwpq.lanzouq.com/b004i14qgb")
        QDesktopServices.openUrl(url)
        QMessageBox.information(self, "提示", "密码：666")

    def tutorial(self):
        # 打开教程链接
        url = QUrl("https://www.yuque.com/u26095674/yf6ir9/pym6rvoing10uqz2")
        QDesktopServices.openUrl(url)

    def plug_in(self):
        # 打开插件链接
        url = QUrl("https://www.yuque.com/u26095674/yf6ir9/ma481knf1kwmf920?singleDoc")
        QDesktopServices.openUrl(url)



# from ui_list import Ui_Form
#
# class MyWidget(QWidget):
#     def __init__(self, function_module_path=None):
#         super().__init__()
#         self.ui = Ui_Form()
#         self.ui.setupUi(self)
#
#         self.function_module_path = function_module_path or os.path.join(os.getcwd(), "function_module.py")
#         self.function_items = self.load_function_items()  # 加载函数相关信息列表
#         self.update_ui()  # 根据加载的信息更新界面
#
#     def load_function_items(self):
#         functions_module = self.load_functions_module()
#         if functions_module:
#             return getattr(functions_module, "function_list", [])  # 获取函数信息列表
#         return []
#
#     def load_functions_module(self):
#         module_name = "function_module"
#         spec = importlib.util.spec_from_file_location(module_name, self.function_module_path)
#         if spec is None:
#             return None
#         try:
#             module = importlib.util.module_from_spec(spec)
#             spec.loader.exec_module(module)
#             return module
#         except FileNotFoundError:
#             print(f"函数模块文件 {self.function_module_path} 不存在，请检查路径！")
#             return None
#         except Exception as e:
#             print(f"加载函数模块时出现错误: {e}")
#             return None
#
#     def update_ui(self):
#         self.ui.listWidget.clear()
#         for function_item in self.function_items:
#             custom_item = CustomListWidgetItem(function_item)
#             self.ui.listWidget.addItem(custom_item)
#             self.ui.listWidget.setItemWidget(custom_item, custom_item.widget)
#
#
# class CustomListWidgetItem(QListWidgetItem):
#     def __init__(self, function_item):
#         super().__init__()
#         self.function_item = function_item
#         self.text_label = QLabel(self.function_item.description)
#         font = QFont()
#         font.setPointSize(12)
#         self.text_label.setFont(font)
#         self.text_label.setAlignment(Qt.AlignVCenter)
#         self.button = QPushButton("应用")
#         self.button.setFont(font)
#
#         self.widget = QWidget()
#         main_layout = QVBoxLayout(self.widget)
#         main_layout.setContentsMargins(0, 0, 0, 0)
#         main_layout.setSpacing(0)
#
#         inner_layout = QHBoxLayout()
#         inner_layout.addWidget(self.text_label)
#         inner_layout.addWidget(self.button)
#
#         main_layout.addLayout(inner_layout)
#
#         self.button.setFixedHeight(30)
#         self.button.setMaximumWidth(100)
#         self.text_label.setFixedHeight(30)
#
#         self.button.clicked.connect(self.function_item.func)  # 绑定按钮点击事件到对应的函数
#
#         self.setSizeHint(self.widget.sizeHint())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec())
