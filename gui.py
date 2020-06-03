import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QPushButton, QWidget
from PyQt5 import QtGui


class Gui(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        self.initUI()
        self.__createFileMenu()
        self.__createEditeMenu()
        self.__createHelpMenu()


    def initUI(self):
        self.statusBar().showMessage('Ready')

        #Taille de la fenêtre au lancement et position
        self.setGeometry(300, 300, 1280, 720)

        # Taille minimum de la fenêtre
        self.setMinimumSize(1280, 720)

        # Titre de la fenêtre
        self.setWindowTitle('Jeu de la vie')

        #Monter la fenêtre
        self.show()

        #Changer l'icône de l'interface
        self.setWindowIcon(QtGui.QIcon('python.png'))


    def __createFileMenu(self):

        actOpen = QAction(QIcon("icons/open.png"), "&Ouvrir", self)
        actOpen.setShortcut("Ctrl+O")
        actOpen.setStatusTip("Ouvrir le fichier")

        actSave = QAction(QIcon("icons/save.png"), "&Sauvegarder", self)
        actSave.setShortcut("Ctrl+S")
        actSave.setStatusTip("Sauegarder le fichier")

        actExit = QAction(QIcon("icons/exit.png"), "&Sortir", self)
        actExit.setShortcut("Ctrl+Q")
        actExit.setStatusTip("Sortir de l'application")
        actExit.triggered.connect(self.close)

        menuBar = self.menuBar()
        Fichier = menuBar.addMenu("&Fichier")
        Fichier.addAction(actOpen)
        Fichier.addAction(actSave)
        Fichier.addSeparator()
        Fichier.addAction(actExit)

    def __createEditeMenu(self):

        actCopy = QAction(QIcon("icons/copy.png"), "&Copy", self)
        actCopy.setStatusTip("Copy")

        actCut = QAction(QIcon("icons/cut.png"), "&Cut", self)
        actCut.setStatusTip("Cut")

        actPaste = QAction(QIcon("icons/paste.png"), "&Paste", self)
        actPaste.setStatusTip("Paste")

        menuBar = self.menuBar()
        edit = menuBar.addMenu("&Edit")
        edit.addAction(actCopy)
        edit.addAction(actCut)
        edit.addSeparator()
        edit.addAction(actPaste)

    def __createHelpMenu(self):
        actAbout = QAction("&About", self)
        actAbout.setStatusTip("About...")

        menuBar = self.menuBar()
        helpMenu = menuBar.addMenu("&Help")
        helpMenu.addAction(actAbout)
        helpMenu.addSeparator()


























