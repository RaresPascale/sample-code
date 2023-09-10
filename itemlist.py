class ItemList:
    def __init__(self,name):
        self.name = name
        self.description = None
        self.items = list()

    def add_items(self,item):
        self.items.append(item)

    def set_items(self, items):
        self.items = items

    def get_items(self):
        return self.items


class ToDoList(ItemList):
    def __init__(self, name, asignee):
        #Call super constructor(name)
        super().__init__(name)
        self.asignee = asignee

    def __str__(self):
        return "Override 'str' in ToDoList class"

it1 = ItemList("Item1")
it1.add_items("t1")
print(it1.get_items())
td1 = ToDoList("ToDo1", "User1")
print(td1.get_items())
td1.add_items('todo1'); print(td1.get_items())
print(str(td1)); print(str(it1))
