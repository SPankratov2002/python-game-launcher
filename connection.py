from PySide6 import QtWidgets, QtSql


class Data:
    def __init__(self):
        super(Data, self).__init__()
        self.create_connection()

    def create_connection(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('AppleGraden.db')

        if not (db.open()):
            QtWidgets.QMessageBox.critical(None, 'Cannot open database', 'Click Cancel to exit',
                                           QtWidgets.QMessageBox.Cancel)
            return False

        query = QtSql.QSqlQuery()
        query.exec(
            'CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY AUTOINCREMENT,'
            'first_name TEXT(50),'
            'last_name TEXT(50),'
            'surname TEXT(50),'
            'age INTEGER,'
            'score INTEGER,'
            'date TEXT(8),'
            'midtime REAL(6),'
            'fulltime REAL(6))'
        )

        return True

    def execute_query_with_params(self, sql_query, query_values=None):
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)

        if query_values is not None:
            for query_value in query_values:
                query.addBindValue(query_value)

        query.exec()

        return query

    def add_new_transaction_query(self, last_name, first_name, surname, date):
        sql_query = "INSERT INTO Users (last_name, first_name, surname, date) VALUES (?, ?, ?, ?)"
        self.execute_query_with_params(sql_query, [last_name, first_name, surname, date])

    def update_transaction_query(self, Battletag, Tank, Damage, Support, Mail, password_ow, description, password_mail, ID):
        if password_mail != '':
            password_mail = f"password_mail={password_mail},"
        print(password_mail, "-that")

        sql_query = f"UPDATE accounts SET BattleTag=?, Tank=?, Damage=?, Support=?, Mail=?, password_ow=?, {password_mail} description=? WHERE ID=?"
        self.execute_query_with_params(sql_query, [Battletag, Tank, Damage, Support, Mail, password_ow, description, ID])

    def delete_transaction_query(self, id):
        sql_query = "DELETE FROM Users WHERE id=?"
        self.execute_query_with_params(sql_query, [id])