import sys
import os
import pandas as pd
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import QFileDialog, QTableWidgetItem, QMessageBox, QMainWindow, QApplication
from PySide6.QtCore import QSettings, Qt, QUrl
import importlib.util

from ui_form import Ui_MainWindow


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

        # 读取历史记录
        self.load_last_opened_file()

        # 连接菜单事件
        self.ui.action_3.triggered.connect(self.tutorial)
        self.ui.action_4.triggered.connect(self.plug_in)
        self.ui.action_5.triggered.connect(self.open_group_chat)
        self.ui.action_6.triggered.connect(self.open_last_download)

    def load_last_opened_file(self):
        settings = QSettings("my_company", "my_app")
        last_file = settings.value("last_opened_file", "")

        if last_file and os.path.exists(last_file):
            self.open_file(last_file)

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

        for row in range(df.shape[0]):
            for col in range(df.shape[1]):
                self.ui.tableWidget.setItem(row, col, QTableWidgetItem(str(df.iloc[row, col])))

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

    def process_selected_data(self):
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
                # 动态加载用户选择的 Python 文件
                spec = importlib.util.spec_from_file_location("user_module", file_path)
                user_module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(user_module)

                # 确保文件中有一个函数可以处理选中的数据
                if not hasattr(user_module, 'func'):
                    QMessageBox.critical(self, "错误", "选定的 Python 文件中没有 `func` 函数！")
                    return

                # 获取函数并应用到选中的数据
                process_data_function = user_module.func
                for (row, col), value in selected_data.items():
                    # 将选中的数据作为 x 传递给 func 函数
                    processed_value = process_data_function(value)
                    # 更新处理后的数据到表格
                    self.ui.tableWidget.setItem(row, col, QTableWidgetItem(str(processed_value)))

                QMessageBox.information(self, "成功", "数据处理完成！")
            except Exception as e:
                QMessageBox.critical(self, "错误", f"处理数据时出错: {str(e)}")

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

        try:
            # 动态加载用户选择的 Python 文件
            spec = importlib.util.spec_from_file_location("user_module", file_path)
            user_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(user_module)

            # 确保文件中有一个函数可以处理选中的数据
            if not hasattr(user_module, 'func'):
                QMessageBox.critical(self, "错误", "选定的 Python 文件中没有 `func` 函数！")
                return

            # 获取函数并应用到选中的数据
            process_data_function = user_module.func
            selected_data = {}
            for index in selected_indexes:
                row = index.row()
                col = index.column()
                item = self.ui.tableWidget.item(row, col)
                selected_data[(row, col)] = str(item.text()) if item else ""

            for (row, col), value in selected_data.items():
                # 将选中的数据作为 x 传递给 func 函数
                processed_value = process_data_function(value)
                # 更新处理后的数据到表格
                self.ui.tableWidget.setItem(row, col, QTableWidgetItem(str(processed_value)))

            QMessageBox.information(self, "成功", "数据处理完成！")
        except Exception as e:
            QMessageBox.critical(self, "错误", f"处理数据时出错: {str(e)}")

    def open_group_chat(self):
        # 打开交流群网页链接
        url = QUrl("http://qm.qq.com/cgi-bin/qm/qr?_wv=1027&k=2dMalAAHkxATXq_4kjiYVaGsCmUpX41R&authKey=fxzHco4OmBhTuv7U8OkR2shsR1UAHQ8PDLVxq6eevxGRehARVkIC%2BlYKeB1zJgP3&noverify=0&group_code=676860109")  # 替换为实际的入门教程链接
        QDesktopServices.openUrl(url)
        QMessageBox.information(self, "提示", "如果跳转失败，请手动加入，QQ群号：676860109")

    def open_last_download(self):
        # 打开交流群网页链接
        url = QUrl("https://wwpq.lanzouq.com/b004i14qgb")  # 替换为实际的入门教程链接
        QDesktopServices.openUrl(url)
        QMessageBox.information(self, "提示", "密码：666")

    def tutorial(self):
        # 打开交流群网页链接
        url = QUrl("https://www.yuque.com/u26095674/yf6ir9/pym6rvoing10uqz2")  # 替换为实际的入门教程链接
        QDesktopServices.openUrl(url)

    def plug_in(self):
        # 打开交流群网页链接
        url = QUrl("https://www.yuque.com/u26095674/yf6ir9/ma481knf1kwmf920?singleDoc")
        QDesktopServices.openUrl(url)

def main():
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
