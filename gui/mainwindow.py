from PyQt6.QtWidgets import *
from config import config
from notepp import manager


# ui는 한 개의 입력과 두 개의 버튼만 가지고 있다
# 1. 문제 풀기: 현재 페이지의 문제 번호를 받아온 후, 그에 맞는 파일을 생성한 후 노트패드++를 실행시킨다.
# 2. 코드 실행: 작성한 코드를 cmd에서 실행시킨다.
# 3. 문제 코드: 문제의 번호를 입력한다.
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.problem_input = QLineEdit(self)
        self.solve_btn = QPushButton('문제 풀기', self)
        self.run_btn = QPushButton('코드 실행', self)
        self.setup()
        self.init_window()
        self.init_ui()

    def init_window(self):
        self.setWindowTitle('백준 헬퍼')
        self.setFixedSize(300, 160)

    def init_ui(self):
        _widget = QWidget()
        _layout = QVBoxLayout()
        _layout.setContentsMargins(15, 10, 15, 10)
        _layout.addWidget(self.problem_input)
        _layout.addWidget(self.solve_btn)
        _layout.addWidget(self.run_btn)
        _widget.setLayout(_layout)
        self.setCentralWidget(_widget)

    # 위젯 설정
    def setup(self):
        self.problem_input.setPlaceholderText('문제 번호')
        self.solve_btn.setFixedHeight(30)
        self.run_btn.setFixedHeight(30)
        # 콜백 설정
        self.solve_btn.clicked.connect(self._on_solve_click)
        self.run_btn.clicked.connect(self._on_run_click)

    def get_current_number(self):
        return self.problem_input.text()

    def _on_solve_click(self):
        current_num = self.get_current_number()
        if not current_num:
            self.alert('알림', '문제 번호를 입력해주세요')
            return
        if manager.exists(current_num, config.FILE_NAME):
            result = self.show_dialog('알림', '이미 존재하는 파일이 있습니다. 덮어씌웁니까?')
            if result == QMessageBox.StandardButton.No:
                return
        manager.save_file(current_num, config.FILE_NAME)
        manager.open_as_np(current_num, config.FILE_NAME)

    def _on_run_click(self):
        current_num = self.get_current_number()
        if not current_num:
            self.alert('알림', '문제 번호를 입력해주세요')
            return
        if not manager.exists(current_num, config.FILE_NAME):
            self.alert('알림', '파일이 존재하지 않습니다.')
            return
        manager.run_code(current_num, config.FILE_NAME)

    def alert(self, title, message):
        msgbox = QMessageBox()
        msgbox.setIcon(QMessageBox.Icon.Warning)
        msgbox.setWindowTitle(title)
        msgbox.setText(message)
        msgbox.setStandardButtons(QMessageBox.StandardButton.Ok)
        msgbox.exec()

    def show_dialog(self, title, message):
        msgbox = QMessageBox()
        msgbox.setIcon(QMessageBox.Icon.Information)
        msgbox.setWindowTitle(title)
        msgbox.setText(message)
        msgbox.setStandardButtons(QMessageBox.StandardButton.No | QMessageBox.StandardButton.Yes)
        return msgbox.exec()


def execute():
    import sys
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    execute()
