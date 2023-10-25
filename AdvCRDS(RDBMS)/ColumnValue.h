#pragma once

#include <string>
#include <vector>
#include <exception>

struct ColumnValue;

class ColumnValue {
public:
  ColumnValue(int intValue) : intData(intValue), isString(false) {}
  ColumnValue(const std::string& stringValue) : strData(stringValue), isString(true) {}

  std::string ToString() const {
    if (isString) {
      return strData;
    } else {
      return std::to_string(intData);
    }
  }

private:
  int intData;
  std::string strData;
  bool isString;
};