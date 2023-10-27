class ColumnDefinition:
    def __init__(self, name, column_type, is_primary=False):
        self.name = name
        self.type = column_type
        self.isPrimary = is_primary