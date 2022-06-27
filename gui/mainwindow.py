from PyQt6.QtWidgets import *


# ui는 두 개의 버튼만 가지고 있다
# 1. 문제 풀기: 현재 페이지의 문제 번호를 받아온 후, 그에 맞는 파일을 생성한 후 노트패드++를 실행시킨다.
# 2. 코드 실행: 작성한 코드를 cmd에서 실행시킨다.
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.solve_btn = QPushButton('문제 풀기', self)
        self.run_btn = QPushButton('코드 실행', self)
        self.setup()
        self.init_window()
        self.init_ui()

    def init_window(self):
        self.setWindowTitle('백준 헬퍼')
        self.setFixedSize(300, 120)

    def init_ui(self):
        _widget = QWidget()
        _layout = QVBoxLayout()
        _layout.setContentsMargins(15, 10, 15, 10)
        _layout.addWidget(self.solve_btn)
        _layout.addWidget(self.run_btn)
        _widget.setLayout(_layout)
        self.setCentralWidget(_widget)

    # 버튼 콜백 삽입
    def setup(self):
        self.solve_btn.setFixedHeight(30)
        self.run_btn.setFixedHeight(30)


def execute():
    import sys
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    execute()
