class Tree:
    def __init__(self):
        """
        Construct empty Tree
        """
        self.root = None

    def insert(self, k):
        """
        Insert Element with Key `k` into this Tree
        """
        if self.root:
            self.root.insert(k)
        else:
            self.root = Node(k)

    def remove(self, k):
        """
        Remove Element with Key `k` from this Tree
        Raise: IndexError if no such Element is found
        """
        if self.root:
            self.root.remove(k)
        else:
            raise IndexError

    def search(self, k):
        """
        Search Element with Key `k` in this Tree
        Return: Element if found
                None otherwise
        """
        if self.root:
            return self.root.search(k)
        else:
            return None

    def __str__(self):
        """
        Pretty Prints a Tree
        """
        if self.root:
            return self.root.recursive_print(0)
        else:
            return ""








class Node:
    """
    A node of the Tree
    """

    def __init__(self, k):
        self.k = k
        self.parent = None
        self.left = None
        self.right = None

    def insert(self, k):
        if k < self.k:
            if self.left is None:
                self.left = Node(k)
            else:
                self.left.insert(k)

        else:
            if self.right is None:
                self.right = Node(k)
            else:
                self.right.insert(k)

    def remove(self, k):
        if k < self.k:
            if self.left:
                self.left = self.left.remove(k)
            else:
                print("key not found")

        elif k > self.k:
            if self.right:
                self.right = self.right.remove(k)
            else:
                print("key not found")
        else:
            if self.left is None and self.right is None:
                return None

# if node has one child, replace the node with it
        if self.left is None:
            return self.right
        
        if self.right is None:
            return self.left

# if node has two children ?


    def search(self, k):
        if self.k == k:
            return  self
        elif k < self.k and self.left:
            return self.left.search(k)
        elif k > self.k and self.right:
            return self.right.search(k)
        else:
            return None


    def __str__(self):
        return "%d" %(self.k)



    def recursive_print(self, indentation):
        """
        Pretty Prints a Tree with this Node as root
        """
        icon = "(-) " if (self.left == None and self.right == None) else "(+) "
        s = ""
        if self.left:
            s += self.left.recursive_print(indentation+1)
        s += ("\t"*indentation) + icon + str(self) + "\n"
        if self.right:
            s += self.right.recursive_print(indentation+1)
        return s

# Create a Tree
t = Tree()

# Insert some Nodes
for x in [10,15,4,23,17,9,20,22,100]:
    t.insert(x)

# Print the Tree
print(t)

# Find some Nodes
for x in [10,19,1,50,17]:
    print("%d found? %r" %(x, t.search(x)))

# Remove some Nodes:
t.remove(9)
t.remove(15)

# Print the Tree
print(t)