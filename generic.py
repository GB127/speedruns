from tools import command_select, run_time

class entry:

    def __init__(self):
        raise BaseException("You cannot create an entry class this way")

    def __str__(self):
        pass

    def change_sort(self):
        for no, one in enumerate(list(self.__dict__)):
            print(no + 1, one)
        self.__class__.sorter = command_select(list(self.__dict__))

    def __lt__(self, other):
        if self.__dict__[self.sorter] != other.__dict__[self.sorter]:
            return self.__dict__[self.sorter] < other.__dict__[self.sorter]
        return self.category < other.category

class table:
    def __call__(self):
        def table():
            header = " no |"
            for no, size in enumerate(self.data[0].table_size):
                header += f' {self.get_header()[no]}' + " "*size + "|"
            print(header)
            print("-" * len(header))
            for no, entry in enumerate(self):
                print(f'{no+1:^3} | {entry}')
            print("-" * len(header))

        while True:
            table()
            command = input("What do you want to do? [sort, end]")
            if command == "end": break
            elif command == "sort":
                self.data[0].change_sort()
                self.data.sort()

    def __getitem__(self, argument):
        return self.data[argument]
    def __iter__(self):
        return iter(self.data)        
    def __len__(self):
        return len(self.data)


    def get_header(self):
        types = list(self.data[0].__dict__.keys())
        return types



    def total_time(self):
        return sum([x.time for x in self.data])

    def mean_time(self):
        return run_time(self.total_time() / self.__len__())

