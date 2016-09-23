require_relative 'bst'

class RedBlackTree < BinarySearchTree
	def RBAddNode(node)
		addNode(node)
		checkRBState(node)
	end
	def checkRBState(node)
		# Check if the root node is black
		# puts "checking "+node.value.to_s


		if node.parent == nil
			# puts "head"
			node.color = 'black'
		else

			if node.parent.color == 'red' && node.parent.getSibling != nil && node.parent.getSibling.color == 'red'
				# puts "uncle red for: "+node.value.to_s
				node.parent.parent.color = 'red'
				node.parent.color = 'black'
				node.parent.getSibling.color = 'black'
			elsif node.color == 'red' && node.parent.color == 'red' && ((node.parent.getSibling != nil && node.parent.getSibling.color == 'black') || node.parent.getSibling == nil)
				# puts "uncle black for: "+node.value.to_s
				# puts node.parent.color
				if node.value < node.parent.value && node.parent.parent != nil && node.parent.value < node.parent.parent.value
					# puts "left of a left"
					greatgrandparent = node.parent.parent.parent
					grandparent = node.parent.parent
					parent = node.parent
					parentRight = node.parent.right

					grandparent.left = parentRight
					if parentRight != nil
						parentRight.parent = grandparent
					end

					if greatgrandparent != nil
						if parent.value < greatgrandparent.value
							greatgrandparent.left = parent
						else
							greatgrandparent.right = parent
						end
						parent.parent = greatgrandparent
					else
						@head = parent
						parent.parent = nil
					end

					parent.right = grandparent
					grandparent.parent = parent

					grandparent.color = 'red'
					parent.color = 'black'



				elsif node.value > node.parent.value && node.parent.parent != nil && node.parent.value < node.parent.parent.value
					# puts "right of a left"
					grandparent = node.parent.parent
					parent = node.parent
					leftChild = node.left

					parent.right = leftChild
					if leftChild != nil
						leftChild.parent = parent
					end

					node.left = parent
					parent.parent = node

					grandparent.left = node
					node.parent = grandparent
					# puts "checking on node.left: "+node.left.value.to_s
					checkRBState(node.left)



				elsif node.value < node.parent.value && node.parent.parent != nil && node.parent.value > node.parent.parent.value
					# puts "left of a right"
					grandparent = node.parent.parent
					parent = node.parent
					rightChild = node.right

					parent.left = rightChild
					if rightChild != nil
						rightChild.parent = parent
					end

					node.right = parent
					parent.parent = node

					grandparent.right = node
					node.parent = grandparent
					# puts "checking on node.right: "+node.right.value.to_s
					checkRBState(node.right)

				elsif node.value > node.parent.value && node.parent.parent != nil && node.parent.value > node.parent.parent.value
					# puts "right of a right"

					parent = node.parent
					grandparent = parent.parent
					# puts parent.value
					greatgrandparent = grandparent.parent
					parentLeft = node.parent.left

					grandparent.right = parentLeft
					if parentLeft != nil
						parentLeft.parent = grandparent
					end

					if greatgrandparent != nil
						if parent.value < greatgrandparent.value
							greatgrandparent.left = parent
						else
							greatgrandparent.right = parent
						end
						parent.parent = greatgrandparent
					else
						@head = parent
						parent.parent = nil
					end

					parent.left = grandparent
					grandparent.parent = parent

					grandparent.color = 'red'
					parent.color = 'black'
				else
					# puts "poo"
				end

			end
			#among other things...
			if node.parent != nil
				# puts "checking on node.parent: "+node.parent.value.to_s+" from: "+node.value.to_s
				checkRBState(node.parent)
			end
		end

	end
	def printAsColorTree
		curNode = @head

		activeQ = PJQueue.new
		activeQ.enqueue(@head)
		nextQ = PJQueue.new
		printLists = [[]]
		validValueAdded = true
		while validValueAdded || !activeQ.empty?
			# puts printLists

			if activeQ.empty?

				validValueAdded = false
				activeQ = nextQ
				nextQ = PJQueue.new
				printLists << []
			end
			curNode = activeQ.dequeue.value
			if curNode.value != " "
				printLists[-1] << (curNode.color == 'red' ? 'r' : 'b')
			else
				printLists[-1] << " "
			end
			# printLists[-1] << curNode.color == 'red' ? 'r' : 'b'



			if curNode.left != nil
				nextQ.enqueue(curNode.left)
				validValueAdded = true
			else
				nextQ.enqueue(RBTNode.new(' '))
			end
			if curNode.right != nil
				nextQ.enqueue(curNode.right)
				validValueAdded = true
			else
				nextQ.enqueue(RBTNode.new(' '))
			end

		end
		i = 1
		curNode = @head
		while curNode.right != nil
			curNode = curNode.right
		end
		spaceLengthConst = 1

		printLists.each do |list|
			leadSpaces = 2**(printLists.length-i)-1
			innerSpaces = 2**(printLists.length-i+1)-1
			line = " "*leadSpaces*spaceLengthConst
			list.each do |item|
				line += item.to_s
				if item.to_s.length < spaceLengthConst
					line += " "*(spaceLengthConst-item.to_s.length)
				end
				line += " "*innerSpaces*spaceLengthConst
			end
			i += 1
			puts line
		end


	end
end

class RBTNode < BSTNode
	attr_accessor :color
	def initialize(value)
		super(value)
		@color = 'red'
	end
	def getSibling
		if @parent != nil && @value < @parent.value
			return @parent.right
		elsif @parent != nil
			return @parent.left
		end
		return nil
	end
end

# myRBTNode = RBNode.new(10)
# puts myRBNode.value, myRBNode.color
myRBT = RedBlackTree.new

# inputInt = gets.to_i
# while inputInt != -1
# 	myRBT.RBAddNode(RBTNode.new(inputInt))
# 	myRBT.printAsTree
# 	myRBT.printAsColorTree
# 	myRBT.inOrder
#
# 	inputInt = gets.to_i
# end

10.times do
	n = RBTNode.new(Random.rand(200))
	if !myRBT.contains(n.value)
		puts n.value

		myRBT.RBAddNode(n)
	end
end
myRBT.printAsTree
myRBT.printAsColorTree
myRBT.inOrder

# [8,4,12,2,6,10,14,1,3,5,7,9,11,13,15].each do |n|
# 	addN = RBTNode.new(n)
# 	myRBT.RBAddNode(addN)
# end

# (1..10).each do |n|
# 	addN = RBTNode.new(11-n)
# 	myRBT.RBAddNode(addN)
# end


# myRBT.RBAddNode(RBTNode.new(3))
# myRBT.printAsTree
# myRBT.printAsColorTree
# myRBT.RBAddNode(RBTNode.new(1))
# myRBT.printAsTree
# myRBT.printAsColorTree
# myRBT.RBAddNode(RBTNode.new(4))
# myRBT.head.right.color = 'black'
# myRBT.printAsTree
# myRBT.printAsColorTree
# myRBT.RBAddNode(RBTNode.new(2))

# myRBT.RBAddNode(RBTNode.new(2))
# myRBT.printAsTree
# myRBT.printAsColorTree
# myRBT.RBAddNode(RBTNode.new(1))
# myRBT.head.left.color = 'black'
# myRBT.printAsTree
# myRBT.printAsColorTree
# myRBT.RBAddNode(RBTNode.new(4))
# myRBT.printAsTree
# myRBT.printAsColorTree
# myRBT.RBAddNode(RBTNode.new(3))

# puts "printing"
# myRBT.printAsTree
# myRBT.printAsColorTree
# myRBT.inOrder
# puts myRBT.head.color
# puts myRBT.head.right.color
# puts myRBT.head.left.color
# puts myRBT.head.left.right.color

# puts myRBT.head.right.value, myRBT.head.right.left.parent.value, myRBT.head.right.right.parent.value
# puts myRBT.head.right.left.value, myRBT.head.right.left.getSibling.value
