'''使用栈实现队列的下列操作：

push(x) -- 将一个元素放入队列的尾部。
pop() -- 从队列首部移除元素。
peek() -- 返回队列首部的元素。
empty() -- 返回队列是否为空。
示例:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);
queue.peek();  // 返回 1
queue.pop();   // 返回 1
queue.empty(); // 返回 false
说明:

你只能使用标准的栈操作 -- 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）。'''


class MyQueue(object):

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#
#     def push(self, x):
#         """
#         Push element x to the back of queue.
#         :type x: int
#         :rtype: void
#         """
#
#     def pop(self):
#         """
#         Removes the element from in front of queue and returns that element.
#         :rtype: int
#         """
#
#     def peek(self):
#         """
#         Get the front element.
#         :rtype: int
#         """
#
#     def empty(self):
#         """
#         Returns whether the queue is empty.
#         :rtype: bool
#         """
#
# # Your MyQueue object will be instantiated and called as such:
# # obj = MyQueue()
# # obj.push(x)
# # param_2 = obj.pop()
# # param_3 = obj.peek()
# # param_4 = obj.empty()
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stact = []
        self.queue = []
        self.len = 0


    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stact.append(x)
        self.len += 1


    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        while len(self.stact) != 0:
            self.queue.append(self.stact.pop())

        x = self.queue.pop()

        while len(self.queue) != 0:
            self.stact.append(self.queue.pop())

        self.len -= 1
        return x


    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        while len(self.stact) != 0:
            self.queue.append(self.stact.pop())

        x = self.queue.pop()
        self.queue.append(x)

        while len(self.queue) != 0:
            self.stact.append(self.queue.pop())

        return x


    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        # print(self.len)

        if self.len:
            return False
        else:
            return True


if __name__ == '__main__':
    a = MyQueue()
    x=3
    y=4
    z=5
    a.push(x)
    a.push(y)
    a.push(z)
    print(a.pop())
    print(a.empty())
    print(a.pop())
    #print(a.push())
    print(a.peek())
    print(a.empty())
    print(a.pop())
    print(a.empty())