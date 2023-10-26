#pragma once

#include <string>
#include <vector>
#include <exception>

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

  ColumnType GetType() const {
    return isString ? ColumnType::STRING : ColumnType::INTEGER;
  }

  // Add a GetName function to get the name of the value (optional)
  std::string GetName() const {
    return isString ? strData : std::to_string(intData);
  }

private:
  int intData;
  std::string strData;
  bool isString;
};
