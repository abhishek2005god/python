import sys #System module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__() #super means go to the parent class and call its __init__ method. In this case, it calls the __init__ method of QMainWindow.
        self.setWindowTitle("My First GUI")
        self.setGeometry(100, 100, 400, 300) #setGeometry(x, y, width, height) sets the position and size of the window. The first two parameters are the x and y coordinates of the top-left corner of the window, and the last two parameters are the width and height of the window.
        self.setWindowIcon(QIcon("123.png")) #setWindowIcon() sets the window icon. QIcon() is used to create an icon from an image file. In this case, it uses 'icon.png' as the icon for the window.

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()