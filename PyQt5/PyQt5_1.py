import sys
from PyQt5.QtWidgets import QApplication, QWidget

# 1. Create the application instance
app = QApplication(sys.argv)

# 2. Create a basic desktop window
window = QWidget()
window.resize(400, 200)
window.setWindowTitle('PyQt5 is Working!')
window.show()

# 3. Cleanly close the app when you exit
sys.exit(app.exec_())