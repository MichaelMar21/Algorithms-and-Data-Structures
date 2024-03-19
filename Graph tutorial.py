class Node:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
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
            
            
        
    def print_tree(self, command, level_range):
        
        prefix = ' ' * self.get_level() * 3
        if command == "name":
            print(prefix + self.name)
        elif command == 'designation':
            print(prefix + self.designation)
        elif command == 'both':
            print(prefix + self.name + '(' + self.designation + ')')
        if self.children and self.get_level() < level_range:
            for child in self.children:
                child.print_tree(command, level_range)
                


def build_management_tree():
    # CTO Hierarchy
    infra_head = Node("Vishwa","Infrastructure Head")
    infra_head.add_child(Node("Dhaval","Cloud Manager"))
    infra_head.add_child(Node("Abhijit", "App Manager"))

    cto = Node("Chinmay", "CTO")
    cto.add_child(infra_head)
    cto.add_child(Node("Aamir", "Application Head"))

    # HR hierarchy
    hr_head = Node("Gels","HR Head")

    hr_head.add_child(Node("Peter","Recruitment Manager"))
    hr_head.add_child(Node("Waqas", "Policy Manager"))

    ceo = Node("Nilupul", "CEO")
    ceo.add_child(cto)
    ceo.add_child(hr_head)

    return ceo

if __name__ == '__main__':
    root = build_management_tree()
    root.print_tree("name", 10)
    root.print_tree("name", 2)
    """
    root.print_tree("designation")
    root.print_tree("both")
    """

        