import pytest
from main import Stack

test_Stack = Stack()

class TestStack:
    def setup(self):
        print("method setup")   
    def teardown(self):
        print("method teardown")  

    def test_isEmpty(self):
        print(test_Stack)
        assert test_Stack.isEmpty()

    def test_push(self):
        test_Stack.push('test_1') 
        last_el = test_Stack.stack[-1]
        del test_Stack.stack[-1]
        assert 'test_1' == last_el
        
    def test_pop(self):
        test_Stack.push('test_1') 
        result = test_Stack.pop()
        assert result == 'test_1' and test_Stack.isEmpty
    
    def test_peek(self):
        test_Stack.push('test_1')
        assert test_Stack.peek() == test_Stack.stack[-1]
        print(test_Stack)
        test_Stack.pop()
        
    def test_size(self):
        test_list = [1, 2, 3]
        for i in test_list:
            test_Stack.push(i)
        assert test_Stack.size() == len(test_list)
        for i in test_list:
            test_Stack.pop()