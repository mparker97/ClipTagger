from PyQt6.QtWidgets import QApplication, QWidget

app = QApplication([])

window = QWidget()
window.setWindowTitle('Clip Tagger')
window.setGeometry(100, 100, 1000, 600)
window.show()

app.exec()
