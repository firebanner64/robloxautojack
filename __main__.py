import config
import generate
import gui
import sys

from PyQt5 import QtWidgets

class Control:

    def __init__(self):
        self.t = None
        self.config = config.Config().default_configuration() # generate default config instance

        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.ui = gui.Ui_MainWindow() # instantiate the user created ui
        self.ui.setupUi(MainWindow)
        print('before')
        self.ui.startButton.clicked.connect(self.start)
        self.ui.stopButton.clicked.connect(self.stop)
        print("after")
        MainWindow.show()
        sys.exit(app.exec_())
    
    def start(self):
        self.stop()

        self.config.mode = self.ui.modeComboBox.currentIndex() + 1
        self.config.cap_mode = self.ui.capitalizationComboBox.currentIndex() + 1
        self.config.punctuation = self.ui.punctuationTextBox.toPlainText()
        self.config.start = self.ui.beginAtSpinBox.value()
        self.config.end = self.ui.endAtSpinBox.value()

        if self.config.mode == 1:
            self.t = generate.GenerateThread(target = generate.jj, args=(self.config,))
        if self.config.mode == 2:
            self.t = generate.GenerateThread(target = generate.hj, args=(self.config,))
        if self.config.mode == 3:
            self.t = generate.GenerateThread(target = generate.dj, args=(self.config,))
        if self.config.mode == 4:
            self.t = generate.GenerateThread(target = generate.cj, args=(self.config,))
        
        self.t.start()

        
    
    def stop(self):
        if isinstance(self.t, generate.GenerateThread):
            self.t.raise_exception()
            self.t = None

Control()



'''
if __name__ == "__main__":
    #config_instance = config.Config().prompt_console_configuration()

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = gui.Ui_MainWindow() # instantiate the user created ui
    ui.setupUi(MainWindow)
    # ui modifications
    

    # 
    MainWindow.show()
    sys.exit(app.exec_())

    if config_instance.mode == 1:
        generate.jj(config_instance)
    if config_instance.mode == 2:
        generate.hj(config_instance)
    if config_instance.mode == 3:
        generate.dj(config_instance)
    if config_instance.mode == 4:
        generate.cj(config_instance)
'''

