def repeater(func):
    def wrapper(*args, **kwargs):
        for i in range(1, 4):
            print("number of iteration:", i)
            print(func(args, kwargs))
    return wrapper


@repeater
def sum_square(*args, **kwargs):
    result = 0
    all_numbers = []
    for i in args:
        if type(i) == tuple:
            for g in i:
                all_numbers.append(g)
        elif type(i) == dict:
            for g in i.values():
                all_numbers.append(g)

    for i in kwargs.values():
        all_numbers.append(i)

    for num in all_numbers:
        num = int(num)            #тут же можно не использовать try?
        result += pow(num, 2)

    return result


class Item:
    def __init__(self, name, due_date, priority):
        self.name = name
        self.due_date = due_date
        self.priority = priority

    def set_name(self, new_name):
        self.name = new_name

    def set_due_date(self, new_due_date):
        self.due_date = new_due_date

    def set_priority(self, new_priority):
        self.priority = new_priority

    def info(self):
        print(f"{self.name}: due date - {self.due_date}, priority - {self.priority}")


class ItemList:
    def __init__(self, items):
        self.items = items

    def get_items(self):
        return self.items

    def get_items_by_date(self, search_date):
        result = []
        for item in self.items:
            if item.due_date == search_date:
                result.append(item)
        return result

    def get_important_items(self):
        result = []
        for item in self.items:
            if item.priority == 'important' or item.priority == 'very important':
                result.append(item)
        return result

    def create_new_item(self, new_item):
        self.items.append(new_item)

    def delete_item(self, deleted_item):
        self.items.remove(deleted_item)

    def set_attribute_item(self, item, attribute, new_value):
        if item in self.items:
            if attribute == 'name':
                item.name = new_value

            elif attribute == 'due_date':
                item.due_date = new_value

            elif attribute == 'priority':
                item.priority = new_value
