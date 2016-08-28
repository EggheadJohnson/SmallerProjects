require_relative 'node'

class LinkedList
	attr_reader :head
	def initialize
		@head = nil
	end
	public
	def addNode(value)
		if @head == nil
			@head = LLNode.new(value)
		else
			curNode = @head
			while curNode.next != nil
				curNode = curNode.next
			end
			curNode.next = LLNode.new(value)
		end
	end
	def sortedAdd(value)
		if @head == nil
			@head = LLNode.new(value)
		elsif value < @head.value
			addNode = LLNode.new(value)
			addNode.next = @head
			@head = addNode
		else
			curNode = @head
			while curNode.next != nil && value >= curNode.next.value
				curNode = curNode.next
			end
			addNode = LLNode.new(value)
			addNode.next = curNode.next
			curNode.next = addNode
		end
	end
	public
	def empty?
		return @head==nil
	end

	public
	def each
		curNode = @head
		while curNode != nil
			yield(curNode.value)
			curNode = curNode.next
		end
	end

	public
	def map
		returnLL = LinkedList.new
		curNode = @head
		while curNode != nil
			returnLL.addNode(yield(curNode.value))
			curNode = curNode.next
		end
		return returnLL
	end

	public
	def map!
		curNode = @head
		while curNode != nil
			curNode.value = yield(curNode.value)
			curNode = curNode.next
		end
	end

end

class LLNode < Node
	attr_accessor :next
	def initialize(value)
		super(value)
		@next = nil
	end
end

# myLL = LinkedList.new
# 10.times do
# 	n = Random.rand(50)
# 	myLL.addNode(n)
# end
# myLL.each {|v| puts v}
# newLL = myLL.map {|v| v*2}
# newLL.each {|v| puts v}
# myLL.map! {|v| v**3}
# myLL.each {|v| puts v}
