# Lists and Trees
## node.rb
Contains a generic node that must be extended by a list or a tree for use.
## ll.rb
A generic linked list that allows you to add, sortedAdd, or remove nodes.  Also implements .each, .map, .map!, .empty? methods.  Contains LLNode which extends node.rb.
## queue.rb
Extends ll.rb with enqueue and dequeue methods which behave as LIFO.  Since the Ruby class Queue exists, this implementation is named PJQueue.  Caution!  Does not override any ll.rb methods.
## stack.rb
Extends ll.rb with push and pop methods which behave as LILO.  Caution!  Does not override any ll.rb methods.
## bst.rb
An implementation of binary search tree that includes add, remove, in-order, level-order, and tree-like printing.  Also contains a BSTNode which extends node.rb
