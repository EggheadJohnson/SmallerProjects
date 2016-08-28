require_relative 'll'

class PJQueue < LinkedList
	def initialize
		super
	end
	public
	def dequeue
		returnNode = @head
		@head = @head.next
		if @head == nil
			@isEmpty = true
		end
		return returnNode
	end
	public
	def enqueue(value)
		@isEmpty = false
		addNode(value)
	end
end


# myQ = PJQueue.new
# puts myQ.empty?
# 10.times do
# 	2.times {myQ.enqueue(Random.rand(30))}
# 	printLine = ""
# 	myQ.each do |v|
# 		printLine += v.to_s + ", "
# 	end
# 	puts printLine.chop.chop
# 	1.times {puts myQ.dequeue.value}
# end
# puts myQ.empty?
