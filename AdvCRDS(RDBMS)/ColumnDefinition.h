#pragma once

#include <string>
#include <vector>
#include <exception>

struct ColumnDefinition;

class ColumnDefinition {
public:
  ColumnDefinition(const std::string& name, ColumnType type, bool isPrimary = false)
    : name(name), type(type), isPrimary(isPrimary) {}

  std::string name;
  ColumnType type;
  bool isPrimary;
};