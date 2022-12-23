class Tree:
    def __init__(self, parent=None):
        self.parent = parent
        self.children = {}
        self.size = 0

    def add_dir(self, name):
        self.children[name] = Tree(self)

    def get_size(self):
        self.size += sum([child.get_size() for child in self.children.values()])
        return self.size

    def bounded_size(self, bound=1_000_000_000):
        return (self.size if self.size<=bound else 0) + sum([child.bounded_size(bound) for child in self.children.values()])


root = Tree()
curr = root
with open("in1", "r") as f:
    for ln in f.read().split('\n'):
        match ln.strip().split():
            case ['$', 'cd', '/']:
                curr = root
            case ['$', 'cd', '..']:
                curr = curr.parent
            case ['$', 'cd', name]:
                curr = curr.children[name]
            case ['$', 'ls']:
                pass
            case ['dir', name]:
                curr.add_dir(name)
            case [sz, name]:
                curr.size += int(sz)

root.get_size()
print(root.bounded_size(100_000))