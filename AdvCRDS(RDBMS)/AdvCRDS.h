#pragma once

#include <string>
#include <vector>
#include <exception>

struct ColumnDefinition;
struct ColumnValue;

enum class ColumnType {
  INTEGER,
  STRING
};

class AdvCRDS {
public:
  AdvCRDS(const std::string& db_name);
  ~AdvCRDS();
  sqlite3* db_;

  bool CreateDatabase(const std::string& db_name);
  bool DropDatabase(const std::string& db_name);
  bool UseDatabase(const std::string& db_name);

  bool CreateTable(const std::string& table_name, const std::vector<ColumnDefinition>& columns);
  bool DropTable(const std::string& table_name);
  bool Select(const std::string& table_name, const std::vector<std::string>& columns, const std::string& where_clause = "");
  bool Insert(const std::string& table_name, const std::vector<ColumnValue>& values);
  bool Update(const std::string& table_name, const std::vector<ColumnValue>& values, const std::string& where_clause = "");
  bool Delete(const std::string& table_name, const std::string& where_clause = "");

private:
  // Implementation details omitted for brevity
};