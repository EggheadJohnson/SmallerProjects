require_relative 'node'
require_relative 'queue'

class BinarySearchTree
	def initialize
		@head = nil
	end
	public
	def addNode(value)
		if @head == nil
			@head = BSTNode.new(value)
		else
			nodeToAdd = BSTNode.new(value)
			curNode = @head
			spot = value > curNode.value ? curNode.right : curNode.left
			while spot != nil
				curNode = spot
				spot = value > curNode.value ? curNode.right : curNode.left
			end
			if value > curNode.value
				curNode.right = nodeToAdd
			else
				curNode.left = nodeToAdd
			end
		end

	end
	def removeNode(value)
		curNode = @head
		while curNode != nil && curNode.value != value
			parentNode = curNode
			if curNode.value > value
				curNode = curNode.left
			else
				curNode = curNode.right
			end
		end
		if curNode == nil
			return nil
		elsif curNode.equal? @head
			if curNode.left != nil && curNode.right != nil
				@head = curNode.left
				rightNode = @head
				while rightNode.right != nil
					rightNode = rightNode.right
				end
				rightNode.right = curNode.right
			elsif curNode.left != nil
				@head = curNode.left

			elsif curNode.right != nil
				@head = curNode.right

			else
				@head = nil
			end
			return curNode
		end
		if curNode.right != nil && curNode.left != nil
			if parentNode.left.equal? curNode
				parentNode.left = curNode.left
				rightNode = parentNode.left

			elsif parentNode.right.equal? curNode
				parentNode.right = curNode.left
				rightNode = parentNode.right
			end
			while rightNode.right != nil
				rightNode = rightNode.right
			end
			rightNode.right = curNode.right
		elsif curNode.right != nil
			if parentNode.left.equal? curNode
				parentNode.left = curNode.right
			else
				parentNode.right = curNode.right
			end
		elsif curNode.left != nil
			if parentNode.left.equal? curNode
				parentNode.left = curNode.left
			else
				parentNode.right = curNode.left
			end
		else
			if parentNode.left.equal? curNode
				parentNode.left = nil
			else
				parentNode.right = nil
			end
		end

		return curNode
	end
	public
	def inOrder
		inOrderPrivate(@head)
	end
	private
	def inOrderPrivate(node)
		if node != nil
			inOrderPrivate(node.left)
			node.printMe
			inOrderPrivate(node.right)
		end
	end
	public
	def breadthFirst
		breadthFirstPrivate(@head)
	end
	private
	def breadthFirstPrivate(node)
		if node != nil
			bfsQueue = PJQueue.new
			bfsQueue.enqueue(node)
			while !bfsQueue.empty?
				curNode = bfsQueue.dequeue.value
				puts curNode.value
				if curNode.left != nil
					bfsQueue.enqueue(curNode.left)
				end
				if curNode.right != nil
					bfsQueue.enqueue(curNode.right)
				end
			end
		end
	end
	private
	def checkForValidNodes(head, value)
		value = value == nil ? ' ' : value
		cur = head
		while cur != nil
			if cur.value.value != value
				return true
			end
		end
		return false
	end
	# Note on printAsTree: it does it's best to spread everything out so it lines up nicely.  The problem being, on narrow windows, the line of text will wrap and it might look... funny
	public
	def printAsTree
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
			printLists[-1] << curNode.value



			if curNode.left != nil
				nextQ.enqueue(curNode.left)
				validValueAdded = true
			else
				nextQ.enqueue(BSTNode.new(' '))
			end
			if curNode.right != nil
				nextQ.enqueue(curNode.right)
				validValueAdded = true
			else
				nextQ.enqueue(BSTNode.new(' '))
			end

		end
		i = 1
		curNode = @head
		while curNode.right != nil
			curNode = curNode.right
		end
		spaceLengthConst = curNode.value.to_s.length

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

class BSTNode < Node
	attr_accessor :left, :right
	def initialize(value)
		super(value)
		@left = nil
		@right = nil
	end
end


# myBST = BinarySearchTree.new
# 10.times do
# 	n = Random.rand(200)
# 	# puts n
# 	myBST.addNode(n)
# end
# # [8,4,12,2,6,10,14,1,3,5,7,9,11,13,15].each {|n| myBST.addNode(n)}
# myBST.printAsTree
