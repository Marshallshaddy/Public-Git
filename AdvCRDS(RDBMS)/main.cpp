#include "AdvCRDS.h"
#include "ColumnDefinition.h" // Include definition of ColumnDefinition
#include "ColumnValue.h"      // Include definition of ColumnValue
#include <iostream>
#include <vector>

int main() {
    // Create a new AdvCRDS instance
    AdvCRDS adv_crds("my_database");

    // Create a new table
    std::vector<ColumnDefinition> columns = {
        ColumnDefinition("id", ColumnType::INTEGER, true),
        ColumnDefinition("name", ColumnType::STRING),
    };

    if (adv_crds.CreateTable("users", columns)) {
        std::cout << "Table 'users' created successfully.\n";

        // Insert a new row into the table
        std::vector<ColumnValue> values = {
            ColumnValue(1),
            ColumnValue("John Doe"),
        };

        if (adv_crds.Insert("users", values)) {
            std::cout << "Row inserted successfully.\n";

            // Select all rows from the table
            std::vector<std::string> select_columns = {"id", "name"};
            std::vector<std::vector<ColumnValue>> results;

            if (adv_crds.Select("users", select_columns, "")) {
                std::cout << "Select results:\n";
                for (const std::vector<ColumnValue>& row : results) {
                    for (const ColumnValue& value : row) {
                        std::cout << value.ToString() << " ";
                    }
                    std::cout << std::endl;
                }
            } else {
                std::cout << "Select failed.\n";
            }
        } else {
            std::cout << "Insert failed.\n";
        }
    } else {
        std::cout << "Table creation failed.\n";
    }

    return 0;
}
