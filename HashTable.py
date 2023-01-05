class HashTable:
    def __init__(self,size=7):
        self.data_map = [None]*size

    def __Hash(self,key):
        my_hash = 0
        for item in key:
            my_hash = (my_hash + ord(item) * 23)%len(self.data_map)
        return my_hash

    def print_table(self):
        for key,val in enumerate(self.data_map):
            print(key,':',val)

    def set_value(self,key,value):
        index = self.__Hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key,value])

    def get_value(self,key):
        index = self.__Hash(key)
        item = self.data_map[index]
        if item is not None:
            for k,v in item:
                if key == k:
                    return v
        return item

    def get_keys(self):
        keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in self.data_map[i]:
                    keys.append(j[0])
        return keys



my_table = HashTable()
my_table.set_value('nuts', 120)
my_table.set_value('screws', 345)
my_table.set_value('bolts', 1201)
my_table.set_value('washers', 1206)
print(my_table.get_keys())
my_table.print_table()