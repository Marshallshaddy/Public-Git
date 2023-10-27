import sqlite3

class ColumnType:
    INTEGER = "INTEGER"
    STRING = "STRING"

class AdvPyRDS:
    def __init__(self, db_name):
        self.db = sqlite3.connect(db_name)

    def __del__(self):
        self.db.close()

    def create_database(self, db_name):
        try:
            sqlite3.connect(db_name)
            return True
        except Exception:
            return False

    def drop_database(self, db_name):
        try:
            self.close_connection()
            return True
        except Exception:
            return False

    def use_database(self, db_name):
        try:
            self.close_connection()
            self.db = sqlite3.connect(db_name)
            return True
        except Exception:
            return False

    def create_table(self, table_name, columns):
        try:
            cursor = self.db.cursor()
            sql = "CREATE TABLE " + table_name + " ("
            for column in columns:
                sql += column.name + " "
                if column.type == ColumnType.INTEGER:
                    sql += "INTEGER"
                elif column.type == ColumnType.STRING:
                    sql += "TEXT"
                if column.is_primary:
                    sql += " PRIMARY KEY"
                sql += ","
            sql = sql[:-1]  # Remove the trailing comma
            sql += ")"
            cursor.execute(sql)
            self.db.commit()
            return True
        except Exception:
            return False

    def drop_table(self, table_name):
        try:
            cursor = self.db.cursor()
            sql = "DROP TABLE " + table_name
            cursor.execute(sql)
            self.db.commit()
            return True
        except Exception:
            return False

    def select(self, table_name, columns, where_clause=""):
        try:
            cursor = self.db.cursor()
            sql = "SELECT " + ", ".join(columns) + " FROM " + table_name
            if where_clause:
                sql += " WHERE " + where_clause
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                print(" ".join(map(str, row)))
            return True
        except Exception:
            return False

    def insert(self, table_name, values):
        try:
            cursor = self.db.cursor()
            sql = "INSERT INTO " + table_name + " VALUES ("
            for value in values:
                if value.get_type() == ColumnType.INTEGER:
                    sql += str(value.to_string()) + ","
                elif value.get_type() == ColumnType.STRING:
                    sql += "'" + value.to_string() + "',"
            sql = sql[:-1]  # Remove the trailing comma
            sql += ")"
            cursor.execute(sql)
            self.db.commit()
            return True
        except Exception:
            return False

    def update(self, table_name, values, where_clause=""):
        try:
            cursor = self.db.cursor()
            sql = "UPDATE " + table_name + " SET "
            for value in values:
                sql += value.get_name() + " = " + value.to_string() + ","
            sql = sql[:-1]  # Remove the trailing comma
            if where_clause:
                sql += " WHERE " + where_clause
            cursor.execute(sql)
            self.db.commit()
            return True
        except Exception:
            return False

    def delete(self, table_name, where_clause=""):
        try:
            cursor = self.db.cursor()
            sql = "DELETE FROM " + table_name
            if where_clause:
                sql += " WHERE " + where_clause
            cursor.execute(sql)
            self.db.commit()
            return True
        except Exception:
            return False

    def close_connection(self):
        self.db.close()