from PyQt5  import QtWidgets
from urllib import request

class MainDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        layout=QtWidgets.QVBoxLayout()
        self.edit_url=QtWidgets.QLineEdit()
        self.edit_path=QtWidgets.QLineEdit()
        self.browser = QtWidgets.QPushButton("Browse")
        self.progress = QtWidgets.QProgressBar()
        self.progress.setMinimum(0)
        self.progress.setMaximum(100)
        self.progress.setValue(0)

        submit = QtWidgets.QPushButton("Download")

        submit.clicked.connect(self.submit_clicked)
        self.browser.clicked.connect(self.browse)

        layout.addWidget(self.edit_url)
        layout.addWidget(self.edit_path)
        layout.addWidget(self.browser)
        layout.addWidget(self.progress)
        layout.addWidget(submit)

        self.setLayout(layout)

    def submit_clicked(self):
        path = self.edit_path.text()
        url = self.edit_url.text()
        # urlarr = url.split('/')
        # self.filename=urlarr[-1]
        # print(self.filename)
        request.urlretrieve(url, path, self.handle)


        self.progress.setValue(100)

        QtWidgets.QMessageBox.information(self, "Hello", "Downloaded")
        self.edit_url.setText("")
        self.edit_path.setText("")
        self.progress.setValue(0)

    def browse(self):
        path, type = QtWidgets.QFileDialog.getSaveFileName(self,"Browser","File Location to be saved")
        self.edit_path.setText(path)

    def handle(self, index, frame, size):
        percent = 100 * index * frame // size
        self.progress.setValue(percent)
