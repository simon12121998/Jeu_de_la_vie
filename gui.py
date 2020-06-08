import sys
from tkinter import PanedWindow, HORIZONTAL

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QPushButton, QWidget, QTabWidget, QVBoxLayout,QDialog, QDialogButtonBox, QTableWidget, QTableWidgetItem, QFileDialog
from PyQt5 import QtGui, QtCore


class Gui(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.initUI()
        self.CreateFileMenu()
        self.CreateEditeMenu()
        self.CreateHelpMenu()


        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)


    def initUI(self):
        self.statusBar().showMessage('Ready')

        # Taille de la fenêtre au lancement et position
        self.setGeometry(300, 300, 1280, 720)

        # Taille minimum de la fenêtre
        self.setMinimumSize(1280, 720)

        # Titre de la fenêtre
        self.setWindowTitle('Jeu de la vie')

        # Montrer la fenêtre
        self.show()

        # Changer l'icône de l'interface
        self.setWindowIcon(QtGui.QIcon('logo.ico'))




    def CreateFileMenu(self):
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

    def CreateEditeMenu(self):
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

    def CreateHelpMenu(self):
        actAbout = QAction("&About", self)
        actAbout.setStatusTip("About...")

        menuBar = self.menuBar()
        helpMenu = menuBar.addMenu("&Help")
        helpMenu.addAction(actAbout)
        helpMenu.addSeparator()

    def Enregister(self):
        data = self.model.setQuery(self.lineEdit_requeete.text())
        filename = QtGui.QFileDialog().getSaverFileName(self, 'Enregister un fichier')
        self.file = QtCore.QFile(filename + ".dat")
        with open(filename, 'wb') as f:
            writer = csv.writer(f)
            writer.writerow(['Column 1','Column 2'])
            writer.writerows(data)




class MyTableWidget(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        self.creatingTables()

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tabs.resize(300, 200)

        # Add tabs
        self.tabs.addTab(self.tab1, "Nom de l'utilisateur")
        self.tabs.addTab(self.tab2, "Caracteristiques")

        # Create first tab
        self.tab1.layout = QVBoxLayout(self)
        self.pushButton1 = QPushButton("Input File")
        self.pushButton1.setMaximumSize(250, 150)
        self.tab1.layout.addWidget(self.pushButton1)
        self.tab1.layout.addWidget(self.tableWidget)
        self.tab1.setLayout(self.tab1.layout)

        # Create second tab
        self.tab2.layout = QVBoxLayout(self)
        self.tab2.layout.addWidget(self.tableWidget)
        self.tab2.setLayout(self.tab2.layout)

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)



    def creatingTables(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(7)
        self.tableWidget.setColumnCount(2)

        self.tableWidget.setItem(0, 0, QTableWidgetItem(""))
        self.tableWidget.setItem(1, 0, QTableWidgetItem("Nom"))
        self.tableWidget.setItem(2, 0, QTableWidgetItem("Prenom"))
        self.tableWidget.setItem(3, 0, QTableWidgetItem("Date de naissance"))
        self.tableWidget.setItem(4, 0, QTableWidgetItem("Sexe"))
        self.tableWidget.setItem(5, 0, QTableWidgetItem("Taille"))
        self.tableWidget.setItem(6, 0, QTableWidgetItem("Poids"))

        self.tableWidget.setItem(0, 1, QTableWidgetItem("Utilisateur"))
        self.tableWidget.setColumnWidth(0, 250)
        self.tableWidget.setColumnWidth(1, 200)



        self.vBoxLayout = QVBoxLayout()
        self.vBoxLayout.addWidget(self.tableWidget)
        self.setLayout(self.vBoxLayout)


    def  Window1(self):
        myLabel = QLabel("Second Window")
        okButton = QPushButton("&OK")
        cacelButton = QPushButton("Cancel")
        buttonLayout = 


