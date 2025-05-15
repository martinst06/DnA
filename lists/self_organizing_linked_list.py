from linkedlist import LinkedListElement, LinkedList

gg = [4, 5, 10, 11, 13, 20, 19, 22, 7]
gs  = [13, 20, 13, 19,8, 5, 4]

ll = LinkedList()

for n in reversed(gg):
    element = LinkedListElement(n)
    ll.insert(element, 0)

ll.__getitem__(0)
ll.__getitem__(1)
ll.__getitem__(2)
ll.__getitem__(3)
ll.__getitem__(4)

# for n in gs:
#     el = LinkedListElement(n)
#     print(el.value)
#     if ll.find(el):
#         # el.previous.previous.next = el.next

