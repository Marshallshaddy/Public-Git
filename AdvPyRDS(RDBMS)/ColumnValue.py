class ColumnValue:
    def __init__(self, value):
        if isinstance(value, int):
            self.int_data = value
            self.is_string = False
        elif isinstance(value, str):
            self.str_data = value
            self.is_string = True
        else:
            raise ValueError("Unsupported value type")

    def to_string(self):
        if self.is_string:
            return self.str_data
        else:
            return str(self.int_data)

    def get_type(self):
        return ColumnType.STRING if self.is_string else ColumnType.INTEGER

    def get_name(self):
        return self.str_data if self.is_string else str(self.int_data)