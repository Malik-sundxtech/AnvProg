from dataclasses import dataclass


class MyStruct1:
    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __repr__(self):

        return f"MyStruct1(field1={self.field1}, field2={self.field2})"


@dataclass
class MyStruct2:
    # I en dataclass er __repr__ (og en masse andet) automatisk generert
    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2


min_variabel1 = MyStruct1(1, 2)
min_variabel2 = MyStruct2(1234234, 13)
# fields can be anything
min_variabel3 = MyStruct2("Her er text", min_variabel2)


print(min_variabel1)
print(min_variabel2)
print(min_variabel3)
