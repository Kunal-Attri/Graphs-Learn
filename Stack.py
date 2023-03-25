from abc import ABC


class Node(ABC):
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, first=None):
        self.__head = Node("head")
        self.__size = 0
        if first is not None:
            self.push(first)

    def getSize(self):
        return self.__size

    def empty(self):
        self.__head.next = None
        self.__size = 0

    def isEmpty(self):
        return self.__size == 0

    def peek(self):
        return self.__head.next.value

    def push(self, obj):
        node = Node(obj)
        node.next = self.__head.next
        self.__head.next = node
        self.__size += 1

    def pop(self):
        if self.isEmpty():
            print("Stack already empty!\n")
            return
        remove = self.__head.next
        self.__head.next = self.__head.next.next
        self.__size -= 1
        return remove.value

    def __str__(self):
        current = self.__head.next
        output = ""
        while current:
            output += str(current.value) + " -> "
            current = current.next
        return output[:-4]
