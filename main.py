import sys, os
from PySide6 import QtWidgets, QtSql
from PySide6.QtCore import QEvent
from PySide6.QtWidgets import QApplication, QMainWindow
from login import Ui_MainWindow
from apple_launcher import Ui_AppleLauncher
from connection import Data
from datetime import date


class Launcher(QMainWindow):
    def __init__(self):
        super(Launcher, self).__init__()
        self.ui = Ui_AppleLauncher()
        self.ui.setupUi(self)
        self.conn = Data()

        self.model = QtSql.QSqlTableModel()

        self.model.setTable("Users")
        self.model.select()
        self.view_users()

        self.ui.btn_main.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.btn_manual.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.btn_exit.clicked.connect(self.exit_launcher)
        self.ui.btn_start.clicked.connect(self.open_game)
        self.ui.btn_delete_user.clicked.connect(self.delete_user)

        self.ui.btn_ln.clicked.connect(lambda: self.view_users("u.last_name"))
        self.ui.btn_fn.clicked.connect(lambda: self.view_users("u.first_name"))
        self.ui.btn_acr.clicked.connect(lambda: self.view_users("u.surname"))
        self.ui.btn_age.clicked.connect(lambda: self.view_users("u.date"))

        self.ui.btn_score.clicked.connect(lambda: self.view_users_results("r.score"))
        self.ui.btn_ftime.clicked.connect(lambda: self.view_users_results("r.ftime"))
        self.ui.btn_mtime.clicked.connect(lambda: self.view_users_results("r.mtime"))
        self.ui.btn_data_score.clicked.connect(lambda: self.view_users_results("r.data"))

        self.ui.search_fio.textChanged.connect(lambda: self.view_users("u.last_name"))

    # /==============================Table `Users` views==============================/
    def view_users(self, order_now="u.last_name"):
        self.refresh_users()
        self.ui.stackedWidget.setCurrentIndex(0)

        query = self.conn.execute_query_with_params(f'''
        SELECT u.last_name, u.first_name, u.surname, u.date, u.id FROM Users AS u
        WHERE u.last_name LIKE '{self.ui.search_fio.text()}%' OR u.first_name LIKE '{self.ui.search_fio.text()}%' OR u.surname LIKE '{self.ui.search_fio.text()}%'
        ORDER BY {order_now} DESC
        ''')

        while query.next():
            rows, label_last_name, label_first_name, label_acronim, label_age, label_id = self.ui.create_table_users()
            rows.installEventFilter(self)
            age = self.calculate_age(query.value(3).split("."))

            label_last_name.setText(query.value(0))
            label_first_name.setText(query.value(1))
            label_acronim.setText(query.value(2))
            label_age.setText(str(age))
            label_id.setText(str(query.value(4)))

            rows.mousePressEvent = self.user_profile
            self.ui.verticalLayout_9.insertWidget(0, rows)

    def refresh_users(self):
        widgets = self.ui.scrollAreaWidgetContents_2.layout().count()
        if widgets > 1:
            for i in range(widgets - 1):
                checkWidget = self.ui.scrollAreaWidgetContents_2.layout().itemAt(0).widget()
                self.ui.scrollAreaWidgetContents_2.layout().removeWidget(checkWidget)
                checkWidget.close()
                del checkWidget
    # /===============================================================================/

    # /==============================Table `Results` views==============================/
    def view_users_results(self, order_now="r.score"):
        self.refresh_user_resutlts()
        self.best_Score = 0
        query = self.conn.execute_query_with_params(f'''
            SELECT r.score, r.ftime, r.mtime, r.data FROM Results AS r
            WHERE r.user_id == {self.data['id']}
            ORDER BY {order_now} ASC
        ''')

        while query.next():
            rows, label_score, label_ftime, label_mtime, label_data_result = self.ui.create_table_results()
            rows.installEventFilter(self)

            label_score.setText(str(query.value(0)))
            label_ftime.setText(str(query.value(1)))
            label_mtime.setText(str(query.value(2)))
            label_data_result.setText(str(query.value(3)))

            if int(query.value(0)) > self.best_Score:
                self.best_Score = query.value(0)

            self.ui.verticalLayout_6.insertWidget(0, rows)

    def refresh_user_resutlts(self):
        widgets = self.ui.scrollAreaWidgetContents.layout().count()
        if widgets > 1:
            for i in range(widgets - 1):
                checkWidget = self.ui.scrollAreaWidgetContents.layout().itemAt(0).widget()
                self.ui.scrollAreaWidgetContents.layout().removeWidget(checkWidget)
                checkWidget.close()
                del checkWidget

    # /===============================================================================/

    def delete_user(self):

        btn = QtWidgets.QMessageBox.question(None, "Подтвердите действие", "Вы уверены, что хотите удалить аккаунт?")

        if btn == QtWidgets.QMessageBox.Yes:
            self.conn.delete_transaction_query(self.data["id"])
            self.view_users()
            self.ui.stackedWidget.setCurrentIndex(0)

    def calculate_age(self, born):
        today = date.today()
        return today.year - int(born[2]) - ((today.month, today.day) < (int(born[1]), int(born[0])))

    def user_profile(self, event):
        data = self.data
        self.ui.label_info_ln.setText(data["first_name"])
        self.ui.label_info_fn.setText(data["last_name"])
        self.ui.label_info_acr.setText(data["surname"])
        self.ui.label_info_age.setText(f'Возраст: {data["age"]}')
        self.view_users_results()
        self.ui.label_info_bs.setText(f'Рекорд: {self.best_Score}')

        self.ui.stackedWidget.setCurrentIndex(1)

    def open_game(self):
        with open('settings.txt', 'w') as f:
            f.write(self.ui.lineEdit.text() + '\n')
            f.write(self.data['id'] + '\n')
            f.write(str(int(self.ui.lineEdit_2.text()) * 100))

        os.startfile('apple.lnk')

    def eventFilter(self, obj, event):
        if obj in self.ui.scrollAreaWidgetContents_2.children() and event.type() == QEvent.Type.MouseButtonPress:
            self.data = {
                'first_name': obj.layout().itemAt(0).widget().text(),
                'last_name': obj.layout().itemAt(1).widget().text(),
                'surname': obj.layout().itemAt(2).widget().text(),
                'age': obj.layout().itemAt(3).widget().text(),
                'id': obj.layout().itemAt(4).widget().text()
            }
        return super().eventFilter(obj, event)

    def exit_launcher(self):
        self.login_launcher = LoginApple()
        self.login_launcher.show()
        self.close()

    # def set_user_view(self):
    #     self.ui.label_3.setText(self.user_info[0])
    #     self.ui.label_4.setText(self.user_info[1])
    #     self.ui.label_5.setText(self.user_info[2])


class LoginApple(QMainWindow):
    def __init__(self):
        super(LoginApple, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.conn = Data()

        self.ui.btn_login.clicked.connect(self.login)
        self.ui.btn_create.clicked.connect(self.create_new_user)
        self.ui.btn_login_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.btn_cancel.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))

    def login(self):
        self.launcher = Launcher()
        self.launcher.show()
        self.close()

    def create_new_user(self):
        labels = [
            self.ui.last_name.text(),
            self.ui.first_name.text(),
            self.ui.acronim.text(),
            self.ui.date.text()
        ]

        if self.checked_input(labels):
            self.conn.add_new_transaction_query(
                last_name=self.ui.last_name.text(),
                first_name=self.ui.first_name.text(),
                surname=self.ui.acronim.text(),
                date=self.ui.date.text(),
            )
            self.login()

    def checked_input(self, labels: list):
        for i in labels:
            if i.isdigit():
                QtWidgets.QMessageBox.critical(None, 'Ошибка ввода!', 'Можно вводить только буквы.',
                                               QtWidgets.QMessageBox.Ok)
                return False

            elif i == '':
                QtWidgets.QMessageBox.critical(None, 'Ошибка ввода!', 'Заполните все поля ввода.',
                                               QtWidgets.QMessageBox.Ok)
                return False

        return True


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginApple()
    window.show()
    sys.exit(app.exec())
