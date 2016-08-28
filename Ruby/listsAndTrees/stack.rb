require_relative 'll'

class Stack < LinkedList
	def initialize
		super
	end
	public
	def push(value)
		nodeToPush = LLNode.new(value)
		nodeToPush.next = @head
		@head = nodeToPush
	end
	def pop
		nodeToReturn = @head
		@head = @head.next
		return nodeToReturn
	end
end

# myStack = Stack.new
# puts myStack.empty?
# 10.times do
# 	2.times {myStack.push(Random.rand(30))}
# 	printList = ""
# 	myStack.each do |v|
# 		printList += v.to_s + ", "
# 	end
# 	# puts printList.chop.chop
# 	1.times {puts myStack.pop.value}
# end
# puts myStack.empty?

# printList = ""
# myStack.each do |v|
# 	printList += v.to_s + ", "
# end
# puts printList.chop.chop
# myStack.map! {|v| v-10}
# printList = ""
# myStack.each do |v|
# 	printList += v.to_s + ", "
# end
# puts printList.chop.chop
# 3.times {myStack.pop}
# printList = ""
# myStack.each do |v|
# 	printList += v.to_s + ", "
# end
# puts printList.chop.chop
