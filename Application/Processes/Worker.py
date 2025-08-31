from PyQt5.QtCore import QRunnable, QThreadPool, pyqtSlot


# Retrieved from https://stackoverflow.com/a/47561712

class Worker(QRunnable):
    def __init__(self, target, args):
        super().__init__()
        self.function = target
        self.args = args

    def run(self):
        self.function(*self.args)

    def start(self):
        QThreadPool.globalInstance().start(self)
