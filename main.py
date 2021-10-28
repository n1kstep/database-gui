import sys

from PyQt5 import QtWidgets
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery
from PyQt5.QtWidgets import QMessageBox

from dbgui import Ui_MainWindow


# SELECT * FROM contacts
class DBInterface(QtWidgets.QMainWindow):
    def __init__(self):
        super(DBInterface, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.show_table)

    def show_table(self):
        con = QSqlDatabase.addDatabase("QSQLITE")
        db_path = "contacts.sqlite"
        con.setDatabaseName(db_path)

        model = QSqlTableModel()

        query = QSqlQuery(con)
        query.prepare(self.ui.lineEdit.text())
        query.exec()

        model.setQuery(query)

        self.ui.tableView.setModel(model)
        self.ui.tableView.resizeColumnsToContents()
        self.ui.tableView.horizontalHeader().setStretchLastSection(True)
        self.ui.tableView.verticalHeader().setStretchLastSection(True)


def createConnection():
    con = QSqlDatabase.addDatabase("QSQLITE")
    con.setDatabaseName("contacts.sqlite")
    if not con.open():
        QMessageBox.critical(
            None,
            "QTableView Example - Error!",
            "Database Error: %s" % con.lastError().databaseText(),
        )
        return False
    return True


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    if not createConnection():
        sys.exit(1)

    window = DBInterface()
    window.show()
    sys.exit(app.exec_())

