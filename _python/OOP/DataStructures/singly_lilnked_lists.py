class SList:
    def __init__(self):
        self.head = None

    def add_to_front(self,val):
        new_node = SLNode(val)
        new_node.next = self.head
        self.head = new_node
        return self
    
    def print_values(self):
        print("-"*30,"My List Values","-"*30)
        runner = self.head
        while(runner != None):
            print(runner.value)
            runner = runner.next
        print("\n")
        return self
    
    def add_to_back(self,val):
        if self.head == None:
            self.add_to_front(val)
            return self
        
        new_node = SLNode(val)
        runner = self.head
        while(runner.next != None):
            runner = runner.next
        runner.next = new_node
        return self
    

    def insert_at(self,val,n):
        if n > self.list_length():
            print("index out of range")
            return self
        if(n == 0):
            self.add_to_front(val)
            return self
        if(n == self.list_length()):
            self.add_to_back(val)
            return self
        
        new_node = SLNode(val)
        runner = self.head
        for i in range(1, n):
            runner = runner.next

        new_node.next = runner.next
        runner.next = new_node
        return self
    

    def list_length(self):
        runner = self.head
        counter = 0
        while(runner != None):
            runner = runner.next
            counter += 1
        return counter
    
    def remove_from_front(self):
        removed_val = self.head.value
        self.head = self.head.next
        return  self, removed_val
    
    def remove_from_back(self):
        runner = self.head
        prev_runner = None
        while(runner.next != None):
            prev_runner = runner
            runner = runner.next
        prev_runner.next = None
        return self, runner.value
    
    def remove_val(self,val):
        if(val == self.head.value):
            return self, self.remove_from_front()[1]
        
        runner = self.head.next
        prev_runner = None

        while(val != runner.value):
            prev_runner = runner
            runner = runner.next
        prev_runner.next = runner.next
        return self, runner.value


class SLNode:
    def __init__(self,val):
        self.value = val
        self.next = None



my_list = SList()
my_list.add_to_front(1).add_to_front(3).add_to_front(4).add_to_back(0).add_to_back(6).add_to_front(10).add_to_front(47).add_to_back(99).print_values()

print("\nTesting removal")
print("Removed Value from front:" , my_list.remove_from_front()[1])
print("Removed Value from back:" , my_list.remove_from_back()[1])
my_list.print_values()

print("\nTesting Remving a specific Value")
print("Removing a vlue found in the front:", my_list.remove_val(10)[1])
print("Removing a vlue found in the middle:", my_list.remove_val(0)[1])
print("Removing a vlue found at the end:", my_list.remove_val(6)[1])
my_list.print_values()


my_list.insert_at(10,2)
my_list.print_values()

