from AdvPyRDS import AdvPyRDS, ColumnType
from ColumnDefinition import ColumnDefinition
from ColumnValue import ColumnValue

def main():
    # Create a new AdvCRDS instance
    adv_crds = AdvPyRDS("my_database")

    # Create a new table
    columns = [
        ColumnDefinition("id", ColumnType.INTEGER, True),
        ColumnDefinition("name", ColumnType.STRING),
    ]

    if adv_crds.create_table("users", columns):
        print("Table 'users' created successfully.")

        # Insert a new row into the table
        values = [
            ColumnValue(1),
            ColumnValue("John Doe"),
        ]

        if adv_crds.insert("users", values):
            print("Row inserted successfully.")

            # Select all rows from the table
            select_columns = ["id", "name"]
            results = adv_crds.select("users", select_columns, "")

            if results:
                print("Select results:")
                for row in results: # type: ignore
                    for value in row:
                        print(value.to_string(), end=" ")
                    print()
            else:
                print("Select failed.")
        else:
            print("Insert failed.")
    else:
        print("Table creation failed.")

if __name__ == "__main__":
    main()
