class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
        
    def get_level(self):
        level = 0
        par = self.parent
        while par:
            par = par.parent
            level += 1
        
        return level
            
            
        
    def print_tree(self):
        prefix = ' ' * self.get_level() * 3
        print(prefix+ self.data)
        if self.children:
            for child in self.children:
                child.print_tree()
                


def build_product_tree():
    root = Node("Electronics")

    laptop = Node("Laptop")
    laptop.add_child(Node("Mac"))
    laptop.add_child(Node("Surface"))
    laptop.add_child(Node("Thinkpad"))

    cellphone = Node("Cell Phone")
    cellphone.add_child(Node("iPhone"))
    cellphone.add_child(Node("Google Pixel"))
    cellphone.add_child(Node("Vivo"))

    tv = Node("TV")
    tv.add_child(Node("Samsung"))
    tv.add_child(Node("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    root.print_tree()

if __name__ == '__main__':
    build_product_tree()
    
        