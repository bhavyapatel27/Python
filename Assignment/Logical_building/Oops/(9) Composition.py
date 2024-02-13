""" When we want to use some responsibilities of one class to another class,
then we use composition instead of inherit the whole class """


class Engine:
    def __init__(self, key, status):
        self.key = key
        self.status = status

    def start(self):
        return self.key + self.status


class Car:
    def __init__(self, name, color, key, status):
        self.name = name
        self.color = color
        self.obj_engine = Engine(key, status)

    def end(self):
        return self.name + self.color

    def final_condition(self):
        return (self.obj_engine.start() + self.end())


obj = Car('Innova', 'Gray', 'Yes', 'On')
print(obj.final_condition())
