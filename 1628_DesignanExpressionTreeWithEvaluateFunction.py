import abc 
from abc import ABC, abstractmethod 
"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""

class Node(ABC):
    @abstractmethod
    # define your fields here
    def evaluate(self) -> int:
        pass

class NumNode(Node):
    def __init__(self, _val):
        self.val = _val
    def evaluate(self) -> int:
        return self.val
    
class OpNode(Node):
    def __init__(self, _op, _left, _right):
        self.op = _op
        self.left = _left
        self.right = _right
    def evaluate(self) -> int:
        if self.op == '+':
            return self.left.evaluate() + self.right.evaluate()
        if self.op == '-':
            return self.left.evaluate() - self.right.evaluate()
        if self.op == '*':
            return int(self.left.evaluate() * self.right.evaluate())
        if self.op == '/':
            return int(self.left.evaluate() / self.right.evaluate())
        return 0
"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""

class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        stack = []
        for token in postfix:
            if str.isalnum(token):
                stack.append(NumNode(int(token)))
            else:
                right = stack.pop()
                left = stack.pop()
                stack.append(OpNode(token, left, right))
        return stack[-1]
		
"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
