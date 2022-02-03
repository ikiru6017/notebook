import json
import os
from datetime import datetime, date, timedelta
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont, QKeySequence, QRegExpValidator
from PyQt5.QtWidgets import QAction, QLineEdit, QFileDialog, QMainWindow, QPushButton, \
                            QShortcut, QAbstractItemView, QSizePolicy, QCheckBox, QTableWidgetItem, \
                            QDialogButtonBox, QFormLayout, QItemDelegate, QStyledItemDelegate
from PyQt5.QtCore import Qt, QSettings, QRegExp
from functools import partial
from plyer import notification


if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)



class Ui_MainWindow(object):
    
    def setup_ui(self, MainWindow):
        """
            Initialize interface
        """
        self.MW = MainWindow
        path = os.path.dirname(os.path.abspath(__file__))
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 400)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setStyleSheet("QMainWindow{background-color:#ffffff;}")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setObjectName("centralwidget")
        self.grid_layout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.grid_layout_2.setContentsMargins(9, 9, -1, -1)
        self.grid_layout_2.setObjectName("grid_layout_2")
        self.grid_layout = QtWidgets.QGridLayout()
        self.grid_layout.setContentsMargins(0, -1, -1, -1)
        self.grid_layout.setObjectName("grid_layout")
        self.grid_layout_2.addLayout(self.grid_layout, 0, 0, 1, 1)

        MainWindow.setWindowIcon(QtGui.QIcon(os.path.join(path, r"icons\notebook.png")))

        # fonts
        font1 = QtGui.QFont('Montserrat')
        font1.setPointSize(15)
        font = QtGui.QFont('Retro Gaming')
        font.setPointSize(11)
        font2 = QtGui.QFont('Retro Gaming')
        font2.setPointSize(7)
        fonttb = QtGui.QFont('Montserrat Medium')
        fonttb.setPointSize(8)
        fontbtn = QtGui.QFont('Montserrat')
        fontbtn.setPointSize(8)
        fontlam = QtGui.QFont('Montserrat')
        fontlam.setPointSize(8)
        
        # lbl
        self.lbl = QtWidgets.QLabel("Записная книжка")
        self.lbl.setFont(font1)
        self.lbl.setAlignment(Qt.AlignCenter)
        self.grid_layout.addWidget(self.lbl, 1, 0)

        #search field
        self.search = QLineEdit()
        self.grid_layout.addWidget(self.search, 3, 0)
        self.search.setFont(fonttb)
        self.search.setPlaceholderText("Поиск..")
        self.search.setStyleSheet("QLineEdit {background-color:#ffffff}")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menu_bar = QtWidgets.QMenuBar(MainWindow)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 288, 21))
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.menu_bar.sizePolicy().hasHeightForWidth())
        self.menu_bar.setSizePolicy(size_policy)
        self.menu_bar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menu_bar.setDefaultUp(False)
        self.menu_bar.setNativeMenuBar(True)
        self.menu_bar.setObjectName("menu_bar")
        self.menu_file = QtWidgets.QMenu(self.menu_bar)
        self.menu_file.setFont(font)
        self.menu_file.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menu_file.setToolTipsVisible(True)
        self.menu_file.setObjectName("menu_file")
        self.menu_edit = QtWidgets.QMenu(self.menu_bar)
        self.menu_edit.setFont(font)
        self.menu_edit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menu_edit.setToolTipsVisible(True)
        self.menu_edit.setObjectName("menu_edit")
        MainWindow.setMenuBar(self.menu_bar)
        self.tool_bar = QtWidgets.QToolBar(MainWindow)
        self.tool_bar.setEnabled(True)
        self.tool_bar.setSizePolicy(size_policy)
        self.tool_bar.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.tool_bar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tool_bar.setMovable(True)
        self.tool_bar.setAllowedAreas(QtCore.Qt.AllToolBarAreas)
        self.tool_bar.setOrientation(QtCore.Qt.Vertical)
        self.tool_bar.setIconSize(QtCore.QSize(20, 24))
        self.tool_bar.setFloatable(True)
        self.tool_bar.setObjectName("tool_bar")

        self.notebook_tbl = QtWidgets.QTableWidget(self.centralwidget)
        self.notebook_tbl.setColumnCount(3)
        self.notebook_tbl.setHorizontalHeaderLabels(['ФИО', '№ телефона', 'Дата рождения'])
        notebook_tbl_header = self.notebook_tbl.horizontalHeader()
        notebook_tbl_header.setFont(fonttb)
        self.notebook_tbl.setFont(fonttb)
        notebook_tbl_header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        notebook_tbl_header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        notebook_tbl_header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.notebook_tbl.horizontalHeaderItem(0).setTextAlignment(Qt.AlignCenter)
        self.notebook_tbl.horizontalHeaderItem(1).setTextAlignment(Qt.AlignCenter)
        self.notebook_tbl.horizontalHeaderItem(2).setTextAlignment(Qt.AlignCenter)

        self.notebook_tbl.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.notebook_tbl.setAutoFillBackground(False)
        self.notebook_tbl.setStyleSheet("QWidget{background-color: #ffffff;}")
        self.notebook_tbl.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.notebook_tbl.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.notebook_tbl.setLineWidth(1)
        self.notebook_tbl.setObjectName("notebook_tbl")
        self.grid_layout.addWidget(self.notebook_tbl, 2, 0, 1, 1)
        self.notebook_tbl.setSelectionMode(1)
        self.notebook_tbl.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.notebook_tbl.setItemDelegate(HexDelegate())

        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.tool_bar)
        self.action_add = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(r"icons\plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_add.setIcon(icon)
        self.action_add.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.action_add.setAutoRepeat(True)
        self.action_add.setVisible(True)
        self.action_add.setMenuRole(QtWidgets.QAction.TextHeuristicRole)
        self.action_add.setIconVisibleInMenu(True)
        self.action_add.setShortcutVisibleInContextMenu(False)
        self.action_add.setObjectName("action_add")

        self.action_remove = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(r"icons\minus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_remove.setIcon(icon1)
        self.action_remove.setAutoRepeat(True)
        self.action_remove.setVisible(True)
        self.action_remove.setIconVisibleInMenu(True)
        self.action_remove.setShortcutVisibleInContextMenu(False)
        self.action_remove.setObjectName("action_remove")
        self.action_remove.setShortcut(QKeySequence("Del"))

        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(r"icons\save1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_save = QtWidgets.QAction(MainWindow)
        self.action_save.setIcon(icon7)
        self.action_save.setAutoRepeat(True)
        self.action_save.setVisible(True)
        self.action_save.setIconVisibleInMenu(True)
        self.action_save.setShortcutVisibleInContextMenu(False)
        self.action_save.setObjectName("action_save")

        self.action_sort = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(r"icons\sort.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_sort.setIcon(icon4)
        self.action_sort.setAutoRepeat(True)
        self.action_sort.setVisible(True)
        self.action_sort.setIconVisibleInMenu(True)
        self.action_sort.setShortcutVisibleInContextMenu(False)
        self.action_sort.setObjectName("action_sort")

        self.actionRename = QtWidgets.QAction(MainWindow)

        self.change_cbox = QtWidgets.QCheckBox("Changed")
        self.change_cbox.setChecked(False)
        self.change_cbox.hide()
        
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(r"icons\recent1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        self.menu_file.addAction(self.action_save)
        self.openThemes = self.menu_file.addMenu("Themes")
        self.openThemes.setFont(font)
        self.menu_edit.addAction(self.action_add)
        self.menu_edit.addAction(self.action_remove)
        self.menu_edit.addAction(self.action_sort)

        self.menu_bar.addAction(self.menu_file.menuAction())
        self.menu_bar.addAction(self.menu_edit.menuAction())
        self.tool_bar.addAction(self.action_add)
        self.tool_bar.addAction(self.action_remove)
        self.tool_bar.addAction(self.action_sort)
        self.tool_bar.addWidget(self.change_cbox)

        self.contextmenu = self.centralwidget.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.centralwidget.addAction(self.actionRename)

        # self.action_add.triggered.connect(self.add_new_task)
        self.action_add.triggered.connect(self.add_new_task)
        self.action_remove.triggered.connect(self.remove_task)
        self.action_sort.triggered.connect(self.sort_task)

        self.search.textChanged.connect(self.find_name)
        
        self.retranslate_ui(MainWindow)
        
        
    def retranslate_ui(self, MainWindow):
        """
            Menu naming
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Notebook"))
        self.menu_file.setTitle(_translate("MainWindow", "File"))
        self.menu_edit.setTitle(_translate("MainWindow", "Edit"))
        self.tool_bar.setWindowTitle(_translate("MainWindow", "tool_bar"))
        self.action_save.setText(_translate("MainWindow", "Save      Ctrl+S"))
        self.action_add.setText(_translate("MainWindow", "Add"))
        self.action_remove.setText(_translate("MainWindow", "Remove"))
        self.action_sort.setText(_translate("MainWindow", "Sort"))


    def add_new_task(self):
        """
            Add new task (in 1st column by default)
        """
        row = self.notebook_tbl.rowCount()
        self.notebook_tbl.insertRow(row)

        self.was_changed()

    
    def find_name(self):
        """
            Search by name
        """
        name = self.search.text().lower()
        for row in range(self.notebook_tbl.rowCount()):
            item = self.notebook_tbl.item(row, 0)
            self.notebook_tbl.setRowHidden(row, name not in item.text().lower())
            

    def remove_task(self):
        """
            Delete selected task
        """
        row = self.notebook_tbl.currentRow()
        self.notebook_tbl.removeRow(row)

        self.was_changed()


    def sort_task(self):
        """
            Sorting tasks by abc
        """
        self.notebook_tbl.sortItems(0, QtCore.Qt.AscendingOrder)
        self.was_changed()


    def was_changed(self):
        """
            Hidden checkbox for asking about saving file if something was changed
        """
        self.change_cbox.setChecked(True)



class HexDelegate(QStyledItemDelegate):
    """
        Provide formatting to columns through RegExp
    """
    def createEditor(self, parent, option, index):

        if index.column() == 0:
            name_regexed = QLineEdit(parent)
            regex0 = QRegExp("^[A-Za-z А-Яа-я]*$")
            name_regexed.setValidator(QRegExpValidator(regex0, self))
            return name_regexed
        elif index.column() == 1:
            number_regexed = QLineEdit(parent)
            regex1 = QRegExp("^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$")
            number_regexed.setValidator(QRegExpValidator(regex1, self))
            return number_regexed
        elif index.column() == 2:    
            birthday_regexed = QLineEdit(parent)
            regex2 = QRegExp("^([1-9]|0[1-9]|[12][0-9]|3[01])[-\.](0[1-9]|1[012])[-\.](19[4-9][0-9]|20[0][0-9]|20[1][0-5])$")
            birthday_regexed.setValidator(QRegExpValidator(regex2, self))
            return birthday_regexed



class MyMainWindow(QtWidgets.QMainWindow):
    
    def __init__(self, *args, **kwargs):
        """
            Initialize settings file, save file, theme from settings
        """
        path = os.path.dirname(os.path.abspath(__file__))
        super().__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setup_ui(self)
        # Create file for storing settings 
        self.settings = QSettings("pyqt_settings.ini", QSettings.IniFormat)
        # Initialize save file from settings
        self.save_file = self.settings.value("LastFile")
        # Initialize theme from settings
        self.theme = self.settings.value("Theme")
        # Create new save file if it doesn't exist
        if not self.save_file:
            self.save_file = os.path.join(path, 'saves1.json')
        self.read_from_file(self.save_file)
        
        self.change_theme(self.theme)
        # Initialize hotkey for saving
        action_save = self.ui.action_save
        action_save.triggered.connect(lambda: self.write_to_file(self.save_file))
        self.shortcut = QShortcut(QKeySequence("Ctrl+S"), self)
        self.shortcut.activated.connect(lambda: self.write_to_file(self.save_file))
        
        openThemes = self.ui.openThemes
        openThemes.aboutToShow.connect(self.add_themes_to_menu)

        change_cbox = self.ui.change_cbox
        change_cbox.setChecked(False)
    

    def add_themes_to_menu(self):
        """
            Add themes to menu
        """
        openThemes = self.ui.openThemes
        openThemes.clear()

        act_type_themes_list = []
        acts = ['light', 'dark']
        
        for theme in acts:
            action = QAction(theme, self)
            action.triggered.connect(partial(self.change_theme, theme))
            act_type_themes_list.append(action)

        openThemes.addActions(act_type_themes_list)


    def change_theme(self, theme):
        """
            Change theme (dark by default)
        """
        centralwidget = self.ui.centralwidget
        lbl = self.ui.lbl
        menu_bar = self.ui.menu_bar
        menu_file = self.ui.menu_file
        menu_edit = self.ui.menu_edit
        tool_bar = self.ui.tool_bar

        if theme == 'light':
            centralwidget.setStyleSheet("QWidget{background-color: qlineargradient( x2:2 y2:2, x1:2 y1:0, stop:0 #d1d1d1, stop:1 #dbdbdb);}")
            lbl.setStyleSheet("color: #000000; background: None")
            
            menu_bar.setStyleSheet("QMenuBar{background-color: qlineargradient( x2:2 y2:2, x1:0 y1:2, stop:0 #ffffff, stop:1 #ededed);\n"
                                "color:#000000}")
            menu_file.setStyleSheet("QMenu {background-color:#798d9c;\n"
                                    "color:#FFFFFF;} QMenu:selected {background-color: #5b6a75;}")
            menu_edit.setStyleSheet("QMenu {background-color:#798d9c;\n"
                                    "color:#FFFFFF;} QMenu:selected {background-color: #5b6a75;}")
            tool_bar.setStyleSheet("QToolBar{background-color: qlineargradient( x2:2 y2:2, x1:2 y1:0, stop:0 #ffffff, stop:1 #ededed);\n"
                                "border:#e41234;\n"
                                "padding:2px;\n"
                                "color:#e41234;}")
        elif theme == 'dark':
            centralwidget.setStyleSheet("QWidget{background-color: qlineargradient( x2:2 y2:2, x1:2 y1:0, stop:0 #303030, stop:1 #383838)} QMenu{color: #ffffff};")
            # centralwidget.setStyleSheet("QMenu{color: #ffffff}")
            lbl.setStyleSheet("color: #ffffff; background: None")
            
            menu_bar.setStyleSheet("QMenuBar{background-color: qlineargradient( x2:2 y2:2, x1:0 y1:2, stop:0 #404040, stop:1 #424242);\n"
                                "color:#ffffff}")
            menu_file.setStyleSheet("QMenu {background-color:#C3083F;\n"
                                    "color:#FFFFFF;} QMenu:selected {background-color: #85052b;}")
            menu_edit.setStyleSheet("QMenu {background-color:#C3083F;\n"
                                    "color:#FFFFFF;} QMenu:selected {background-color: #85052b;}")
            tool_bar.setStyleSheet("QToolBar{background-color: qlineargradient( x2:2 y2:2, x1:2 y1:0, stop:0 #404040, stop:1 #424242);\n"
                                "border:#e41234;\n"
                                "padding:2px;\n"
                                "color:#e41234;}")
        else:
            theme = 'dark'
            
        self.settings.setValue("Theme", theme)
        
        
    def write_to_file(self, file):
        """
            Saving file and if it`s name 'saves1' then you can edit name whatever you want
        """
        change_cbox = self.ui.change_cbox
        self.notebook_tbl = self.ui.notebook_tbl

        path = os.path.dirname(os.path.abspath(__file__))
        # Rename save file after 1st saving
        if self.save_file == os.path.join(path, 'saves1.json'):
            file, _ = QFileDialog.getSaveFileName(self, "Save As..", "", "JSON Files (JSON);;Json Files (*.json)")
            if file:
                self.save_file = os.path.join(path, file)
            os.remove("saves1.json")

        try:
            data = []
            row = 0
            # Fill list of table values
            for _ in range(self.notebook_tbl.rowCount()):
                data.append({
                    "name": self.notebook_tbl.item(row, 0).text(),
                    "number": self.notebook_tbl.item(row, 1).text(),
                    "birthday": self.notebook_tbl.item(row, 2).text()
                })
                row += 1

            with open(file, 'w', encoding='utf-8') as outfile:
                json.dump(data, outfile, indent=4)
            change_cbox.setChecked(False)

        except OSError as err:
            print(f"file {file} could not be written")
        
        self.settings.setValue("LastFile", file)


    def reminder(self, message):
        """
            Using plyer library for birthday reminder
        """
        notification.notify(message=message, title="FeelsBirthdayMan", timeout=5, app_icon=r"icons\birthday2.ico")


    def read_from_file(self, file):
        """
            Read data from json file
        """
        self.notebook_tbl = self.ui.notebook_tbl

        try:
            readfile = open(file, 'r', encoding='utf-8')
            obj = json.load(readfile)

            for person in obj:
                row = self.notebook_tbl.rowCount()
                self.notebook_tbl.insertRow(row)
                # Get current day and month in str format for compare
                current_date_day = '{:02d}'.format(datetime.now().day)
                current_date_month = '{:02d}'.format(datetime.now().month)
                # Get day and month from table in str format for compare
                tbl_date_month = (datetime.strptime(person["birthday"], "%d.%m.%Y")).strftime("%m")
                tbl_date_day = (datetime.strptime(person["birthday"], "%d.%m.%Y")).strftime("%d")
                # Get day and month plus 1/7 days for different notifications
                deltaplus7 = datetime.strptime(person["birthday"], "%d.%m.%Y") + timedelta(days=-7)
                deltaplus1 = datetime.strptime(person["birthday"], "%d.%m.%Y") + timedelta(days=-1)
                
                if deltaplus7.strftime("%m") == current_date_month:
                    if deltaplus7.strftime("%d") == current_date_day:
                        self.reminder(message="SEVEN DAYS LEFT: " + person["name"])
                if deltaplus1.strftime("%m") == current_date_month:
                    if deltaplus1.strftime("%d") == current_date_day:
                        self.reminder(message="ONE DAY LEFT: " + person["name"])
                if current_date_month == tbl_date_month:
                    if current_date_day == tbl_date_day:
                        self.reminder(message="HAPPY BIRTHDAY, " + person["name"] + "!!!")

                # Fill table by reading save file
                self.notebook_tbl.setItem(row, 0, QTableWidgetItem(person["name"]))
                self.notebook_tbl.setItem(row, 1, QTableWidgetItem(person["number"]))
                self.notebook_tbl.setItem(row, 2, QTableWidgetItem(person["birthday"]))            

            readfile.close()

        except OSError as err:
            with open(file, 'w'):
                pass
        
        self.settings.setValue("LastFile", file)

    
    def closeEvent(self, event):
        """
            Saving message when exit
        """
        change_cbox = self.ui.change_cbox
        if change_cbox.isChecked():
            should_save = QtWidgets.QMessageBox.question(self, "Save data", 
                                                        "Should the data be saved?",
                                                        defaultButton = QtWidgets.QMessageBox.Yes)
            if should_save == QtWidgets.QMessageBox.Yes:
                self.write_to_file(self.save_file)
            return super().closeEvent(event)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MyMainWindow()
    MainWindow.show()
    sys.exit(app.exec_())