class Node
	attr_accessor :value
	def initialize(value)
		@value = value
	end
	public
	def printMe
		puts @value
	end
end

# puts Node.new(10).value
