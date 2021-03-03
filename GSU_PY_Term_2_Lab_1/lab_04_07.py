class Row:
    def __init__(self, id, collection, value):
        self.id = id
        self.collection = collection
        self.value = value

    def display(self):
        print("{}\t{}|\t{}".format(self.id, "".join("{}\t".format(self.collection[i]) for i in range(len(self.collection))),
                                    self.value))

    def get_argument_name(self, i):
        if i > len(self.collection):
            return "x"
        return "x{}".format(i)


class Table:
    table_head = "id\t{}\tf({})"
    argument = "x{}"
    result_separator = "|"

    def __init__(self, rows_num):
        self.rows = []
        self.rows_num = rows_num

    def add_row(self, row):
        self.rows.append(row)

    def set_row(self, row):
        if self.rows[row.id]:
            self.rows[row.id] = row

    def get_row(self, row_id):
        return self.rows[rowId]

    def display(self):
        print(self.__getTableHead__())
        for row in self.rows:
            row.display()

    def __getTableHead__(self):
        arguments_line = "".join("x{}\t".format(i) for i in range(len(self.rows[0].collection)))
        func_arguments_line = ("".join("x{},".format(i) for i in range(len(self.rows[0].collection))))[0:-1]
        return "id\t{}\tf({})".format(arguments_line, func_arguments_line)


class LogicFunction:
    def __init__(self, variables_num, table):
        self.variables_num = variables_num
        self.table = table

    def get_expression(self):
        result = "y = "
        expression = ""
        for row in table.rows:
            if row.value == 1:
                if expression != "":
                    expression += "|| "
                expression += "&& ".join("x{} ".format(i) for i in range(len(row.collection)))
        if expression == "":
            expression = "0"
        return result + expression

    def get_table(self):
        return self.table

    def printTable(self):
        self.table.display()


table = Table(3)
table.add_row(Row(0, [0, 0], 0))
table.add_row(Row(1, [0, 1], 0))
table.add_row(Row(2, [1, 0], 0))
table.add_row(Row(3, [1, 1], 0))

func = LogicFunction(2, table)
func.printTable()
print(func.get_expression())
