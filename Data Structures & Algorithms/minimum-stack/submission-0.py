class StackItem:
    def __init__(self, val, lastMin):
        self.val = val
        self.lastMin = lastMin


class MinStack:

    def __init__(self):
        self.stack: list[StackItem] = []
        self.min: StackItem = None 
        

    def push(self, val: int) -> None:
        newItem = StackItem(val=val, lastMin=self.min)
        if not self.min or newItem.val < self.min.val:
            self.min = newItem
        self.stack.append(newItem)
        

    def pop(self) -> None:
        if self.min == self.stack[-1]:
            self.min = self.stack[-1].lastMin
        self.stack = self.stack[:-1]
        

    def top(self) -> int:
        return self.stack[-1].val
        

    def getMin(self) -> int:
        if self.min:
            return self.min.val
        return None
        
