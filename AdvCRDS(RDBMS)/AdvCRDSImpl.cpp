#include "AdvCRDS.h"
#include <sqlite3.h>
#include <stdexcept>
#include <iostream>

// Include the necessary header files for ColumnDefinition and ColumnValue
#include "ColumnDefinition.h"
#include "ColumnValue.h"

AdvCRDS::AdvCRDS(const std::string& db_name) {
  int rc = sqlite3_open(db_name.c_str(), &db_);
  if (rc != SQLITE_OK) {
    throw std::runtime_error("Failed to open database: " + std::string(sqlite3_errmsg(db_)));
  }
}

AdvCRDS::~AdvCRDS() {
  sqlite3_close(db_);
}

bool AdvCRDS::CreateDatabase(const std::string& db_name) {
  int rc = sqlite3_open(db_name.c_str(), &db_);
  if (rc != SQLITE_OK) {
    return false;
  }
  sqlite3_close(db_);
  return true;
}

bool AdvCRDS::DropDatabase(const std::string& db_name) {
  int rc = sqlite3_open(db_name.c_str(), &db_);
  if (rc != SQLITE_OK) {
    return false;
  }
  sqlite3_close(db_);
  return true;
}

bool AdvCRDS::UseDatabase(const std::string& db_name) {
  int rc = sqlite3_open(db_name.c_str(), &db_);
  if (rc != SQLITE_OK) {
    return false;
  }
  sqlite3_close(db_);
  return true;
}

bool AdvCRDS::CreateTable(const std::string& table_name, const std::vector<ColumnDefinition>& columns) {
  std::string sql = "CREATE TABLE " + table_name + " (";

  for (const auto& column : columns) {
    sql += column.name + " ";
    switch (column.type) {
      case ColumnType::INTEGER:
        sql += "INTEGER";
        break;
      case ColumnType::STRING:
        sql += "TEXT";
        break;
    }

    if (column.isPrimary) {
      sql += " PRIMARY KEY";
    }
    sql += ",";
  }

  sql.pop_back();
  sql += ")";
  char* errmsg = nullptr;
  int rc = sqlite3_exec(db_, sql.c_str(), nullptr, nullptr, &errmsg);
  if (rc != SQLITE_OK) {
    sqlite3_free(errmsg);
    return false;
  }
  return true;
}

bool AdvCRDS::DropTable(const std::string& table_name) {
  std::string sql = "DROP TABLE " + table_name;
  char* errmsg = nullptr;
  int rc = sqlite3_exec(db_, sql.c_str(), nullptr, nullptr, &errmsg);
  if (rc != SQLITE_OK) {
    sqlite3_free(errmsg);
    return false;
  }
  return true;
}

bool AdvCRDS::Select(const std::string& table_name, const std::vector<std::string>& columns, const std::string& where_clause) {
  std::string sql = "SELECT ";
  for (const auto& column : columns) {
    sql += column + ",";
  }
  sql.pop_back();
  sql += " FROM " + table_name;

  if (!where_clause.empty()) {
    sql += " WHERE " + where_clause;
  }

  sqlite3_stmt* stmt = nullptr;
  int rc = sqlite3_prepare_v2(db_, sql.c_str(), -1, &stmt, nullptr);
  if (rc != SQLITE_OK) {
    return false;
  }

  while ((rc = sqlite3_step(stmt)) == SQLITE_ROW) {
    for (int i = 0; i < sqlite3_column_count(stmt); i++) {
      switch (sqlite3_column_type(stmt, i)) {
        case SQLITE_INTEGER:
          std::cout << sqlite3_column_int(stmt, i) << " ";
          break;
        case SQLITE_TEXT:
          std::cout << sqlite3_column_text(stmt, i) << " ";
          break;
      }
    }
    std::cout << std::endl;
  }
  sqlite3_finalize(stmt);
  return true;
}

bool AdvCRDS::Insert(const std::string& table_name, const std::vector<ColumnValue>& values) {
  std::string sql = "INSERT INTO " + table_name + " VALUES (";
  for (const auto& value : values) {
    if (value.GetType() == ColumnType::INTEGER) {
      sql += value.ToString() + ",";
    } else if (value.GetType() == ColumnType::STRING) {
      sql += "'" + value.ToString() + "',";
    }
  }
  sql.pop_back();
  sql += ")";
  char* errmsg = nullptr;
  int rc = sqlite3_exec(db_, sql.c_str(), nullptr, nullptr, &errmsg);
  if (rc != SQLITE_OK) {
    sqlite3_free(errmsg);
    return false;
  }
  return true;
}

bool AdvCRDS::Update(const std::string& table_name, const std::vector<ColumnValue>& values, const std::string& where_clause) {
  std::string sql = "UPDATE " + table_name + " SET ";
  for (const auto& value : values) {
    sql += value.GetName() + " = " + value.ToString() + ",";
  }

  sql.pop_back();

  if (!where_clause.empty()) {
    sql += " WHERE " + where_clause;
  }

  char* errmsg = nullptr;
  int rc = sqlite3_exec(db_, sql.c_str(), nullptr, nullptr, &errmsg);
  if (rc != SQLITE_OK) {
    sqlite3_free(errmsg);
    return false;
  }
  return true;
}
