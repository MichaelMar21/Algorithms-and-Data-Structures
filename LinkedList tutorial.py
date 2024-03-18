class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        
    def print(self):
        if not self.head:
            print("List is empty")
            return
        node = self.head
        printer = ''
        while node:
            printer += str(node.data) + '--->' if node.next else str(node.data)
            node = node.next
        print(printer)
        
    def get_length(self):
        node = self.head
        counter = 0
        while node:
            counter += 1
            node = node.next
        return counter


    def insert_at_beginning(self, data):
        if not self.head:
            self.head = Node(data, next = None)
            return
        node = Node_exp(data, next = self.head)
        self.head.prev = node
        self.head = node
        

    def insert_at_end(self, data):
        itr = self.head
        if not itr:
            self.head = Node(data, next = None)
            return
        while itr.next:
            itr = itr.next
        itr.next = Node(data, next = None, prev = itr)

    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.insert_at_beginning()
        else:
            itr = self.head
            idx_counter = 0          
        while idx_counter < index - 1:
            itr = itr.next
            idx_counter += 1
        itr.next = Node(data, next = itr.next)
            

    def remove_at(self, index):
        if index<0 or index > self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.head = self.head.next
        else:
            idx_counter = 0
            itr = self.head
            while idx_counter < index - 1:
                itr = itr.next
                idx_counter += 1
            itr.next = itr.next.next

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
            
    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head
        while itr.data != data_after:
            itr = itr.next
        if not itr:
            "Value wasnt found"
            return
        itr.next = Node(data_to_insert, next = itr.next)
        
    def remove_by_value(self, data):
        itr = self.head
        counter = 0
        while itr.data != data:
            itr = itr.next
            counter += 1
            if not itr:
                print("Value wasnt found")
                return
        self.remove_at(counter)
        
class Node_exp(Node):
    def __init__(self, data = None, next = None, prev = None):
        super().__init__(data, next)
        self.prev = prev
        
class DoubleLinkedList(LinkedList):
    def __init__(self):
        super().__init__()
    
    def print_forward(self):
        itr = self.head
        string = ''
        while itr.next:
             string += str(itr.data) + '--->' if itr.next else  str(itr.data)
             itr = itr.next
    
    def print_backward(self):
        itr = self.head
        while itr.next:
            if not itr.next:
                break
            itr = itr.next
        string = ''
        while not itr.prev:
            string += str(itr.data) + '---->' if itr.prev else str(itr.data)
        print(string)
        
        
        
        
            



if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.insert_at(1,"blueberry")
    ll.remove_at(2)
    ll.print()

    ll.insert_values([45,7,12,567,99])
    ll.insert_at_end(67)
    ll.print()
    
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()