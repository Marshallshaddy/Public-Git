import sqlite3

class AdvPyRDS:
    def __init__(self, db_name):
        self.db = sqlite3.connect(db_name)

    def create_database(self, db_name):
        self.db = sqlite3.connect(db_name)

    def drop_database(self, db_name):
        self.db.close()

    def use_database(self, db_name):
        self.db.close()
        self.db = sqlite3.connect(db_name)

    def create_table(self, table_name, columns):
        cursor = self.db.cursor()
        sql = f"CREATE TABLE {table_name} ("

        for column in columns:
            sql += f"{column.name} "
            if column.type == ColumnType.INTEGER:
                sql += "INTEGER"
            elif column.type == ColumnType.STRING:
                sql += "TEXT"

            if column.isPrimary:
                sql += " PRIMARY KEY"
            sql += ","

        sql = sql[:-1]  # Remove the trailing comma
        sql += ")"
        cursor.execute(sql)
        self.db.commit()

    def drop_table(self, table_name):
        cursor = self.db.cursor()
        sql = f"DROP TABLE {table_name}"
        cursor.execute(sql)
        self.db.commit()

    def select(self, table_name, columns, where_clause):
        cursor = self.db.cursor()
        sql = f"SELECT "

        for column in columns:
            sql += f"{column},"
        sql = sql[:-1]  # Remove the trailing comma
        sql += f" FROM {table_name}"

        if where_clause:
            sql += f" WHERE {where_clause}"

        cursor.execute(sql)
        results = cursor.fetchall()

        for row in results:
            for value in row:
                print(value, end=" ")
            print()

    def insert(self, table_name, values):
        cursor = self.db.cursor()
        sql = f"INSERT INTO {table_name} VALUES ("

        for value in values:
            if isinstance(value, int):
                sql += f"{value},"
            elif isinstance(value, str):
                sql += f"'{value}',"
        sql = sql[:-1]  # Remove the trailing comma
        sql += ")"
        cursor.execute(sql)
        self.db.commit()

    def update(self, table_name, values, where_clause):
        cursor = self.db.cursor()
        sql = f"UPDATE {table_name} SET "

        for value in values:
            sql += f"{value.name} = {value.to_string()},"

        sql = sql[:-1]  # Remove the trailing comma

        if where_clause:
            sql += f" WHERE {where_clause}"

        cursor.execute(sql)
        self.db.commit()


class ColumnType:
    INTEGER = 1
    STRING = 2