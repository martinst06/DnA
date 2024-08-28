class LinkedList:
    def __init__(self):
        """
            Create a new LinkedList
        """
        self.head = None


    def insert(self, element, pos):
        """
            Insert an element into this list

            element: The element to insert
            pos: The position to insert (0 being the start)

            return: The modified LinkedList
            raise: IndexError if pos is outside of the list
        """
        if pos == 0 and self.head == None:
            self.head = element
        elif pos == 0 and self.head != None:
            self.head.previous = element
            element.next = self.head
            self.head = element
        else:
            counter = 0
            testElement = self.head
            
            while counter < pos:
                if testElement.next == None:
                    raise IndexError("IndexError")
                testElement = testElement.next
                counter += 1
            self.insert(element)
        print("insert", element.value)


    def remove(self, pos):
        """
            Remove an element from this list
            pos: The position of the element to remove
            returns: The modified LinkedList
            raise: IndexError if pos is outside of the list
        """
        counter = 0
        element = self.head

        if pos == 0:
            element.next.previous = None
            self.head = element.next
        else:
            while counter < pos:
                if element.next == None:
                    raise IndexError("IndexError")
                element = element.next
                counter += 1
            print("remove", element.value)
            self.remove()

    def find(self, value):
        """
            Find an element in this list

            value: The value of the element to find
            returns: The position of the first occurrence of such an element or -1 if not found
        """
        element = self.head
        counter = 0

        while element != None:
            if element.value != value:
                element = element.next
                counter += 1
            else:
                print("find", element.value)
                return counter

            return -1


    def __getitem__(self, pos):
        """
            Return an element at a specific position in the list

            pos: The position of the element to return (0 being the first)
            return: The element 
            raise: IndexError if pos is outside of the list
        """

        element =  self.head
        counter = 0
        while counter < pos:
            if element.next == None:
                    raise IndexError("IndexError")
            element = element.next
            counter += 1

        return element


class LinkedListElement:
    next = None
    previous = None

    def __init__(self, value):
        self.value = value

    def remove(self):
        """
            Remove this item from a LinkedList
        """
        if self.previous:
            self.previous.next = self.next

        if self.next:
            self.next.previous = self.previous

        self.previous = None
        self.next = None

    def insert(self, element):
        """
            Insert an element after this element

            element: The element to insert
        """
        element.previous.next = element
        element.previous = element.previous
        element.next = element
        element.previous = element



if __name__ == "__main__":
    # Create a new LinkedList
    l = LinkedList()

    # Create a new LinkedListElement
    e1 = LinkedListElement(23)
    assert e1.value == 23, "LinkedListElement e1 does have the wrong value."

    # Insert LinkedListElement to beginning of l
    l.insert(e1, 0)
    assert l.find(23) >= 0, "Cannot find element with value '23' in l"
    assert l[0] == e1, "Element l[0] is not e1"

    # Insert another LinkedListElement at the start
    e2 = LinkedListElement(42)
    e3 = LinkedListElement(40)
    l.insert(e2, 0)
    assert l.find(42) >= 0, "Cannot find element with value '42' in l"
    assert l[0] == e2, "Element l[0] is not e2"
    assert l[1] == e1, "Element l[1] is not e1"


    # Remove e1 from LinkedList
    e1.remove()
    assert l.find(42) >= 0, "Cannot find element with value '42' in l"
    assert l.find(23) < 0, "Element with value '23' is still in l"
    assert l[0] == e2, "Element l[0] is not e2"
    try:
        assert l[1] == e1
    except IndexError:
        pass
    else:
        raise RuntimeError("Reading out of bounds should raise IndexError!")
