require 'date'
testArray = [87, 96, 2, 40, 6, 89, 39, 91,96,  31, 57]

def genArray(size, max)
	output = []
	size.times { output.push(Random.rand(max)) }
	return output
end

def arrPri(arr)
	out = arr[0].to_s
	arr.slice(1, arr.length).each do |c|
		out += ", "+c.to_s
	end
	puts out
end

def selectionSort(inpArr)
	sortArr = inpArr.slice(0, inpArr.length)

	(0...sortArr.length).each do |i|
		min = sortArr.max
		swap = i
		(i...sortArr.length).each do |j|
			# puts j, sortArr[j]
			if sortArr[j] < min
				swap = j
				min = sortArr[j]
			end
		end
		tmp = sortArr[i]
		sortArr[i] = sortArr[swap]
		sortArr[swap] = tmp

	end
	return sortArr

end

def sift(inpArr, start, count)
	root = start
	while root * 2 + 1 < count
		child = root * 2 + 1
		if child < count-1 && inpArr[child] < inpArr[child+1]
			child += 1
		end
		if inpArr[child] > inpArr[root]
			inpArr[child], inpArr[root] = inpArr[root], inpArr[child]
			root = child
		else
			return
		end
	end

end

def heapsort(inpArr)
	sortArr = inpArr.slice(0, inpArr.length)
	start = sortArr.length / 2 - 1
	last = sortArr.length - 1
	while start >= 0
		sift(sortArr, start, sortArr.length)
		start -= 1
	end
	while last > 0
		sortArr[0], sortArr[last] = sortArr[last], sortArr[0]
		sift(sortArr, 0, last)
		last -= 1
	end
	return sortArr
end

def quicksort(inpArr)
	sortArr = inpArr.slice(0, inpArr.length)
	if sortArr.length == 1
		return sortArr
	end
	pivot = sortArr[sortArr.length - 1]
	smaller = []
	larger = []
	sortArr.each do |x|
		if x < pivot
			smaller.push(x)
		else
			larger.push(x)
		end
	end
	larger[0], larger[larger.length - 1] = larger[larger.length - 1], larger[0]
	return quicksort(smaller)+quicksort(larger)
end

def insertionSort(inpArr)
	sortArr = inpArr.slice(0, inpArr.length)
	if sortArr.length == 1
		return sortArr
	end
	i = 1
	while i < sortArr.length
		x = i
		while x > 0 && sortArr[x] < sortArr[x-1]
			sortArr[x],sortArr[x-1] = sortArr[x-1],sortArr[x]
			x = x - 1
		end
		i = i + 1
	end
	return sortArr
end

def mergeSort(inpArr)
	sortArr = inpArr.slice(0, inpArr.length)
	if sortArr.length == 1
		return sortArr
	end
	left = sortArr.slice(0, sortArr.length/2)
	right = sortArr.slice(sortArr.length/2, sortArr.length)
	left = mergeSort(left)
	right = mergeSort(right)
	leftCounter = rightCounter = 0
	ans = []
	while leftCounter < left.length || rightCounter < right.length

		if leftCounter < left.length && rightCounter < right.length
			if left[leftCounter] < right[rightCounter]
				ans = ans.push(left[leftCounter])
				leftCounter = leftCounter + 1
			elsif leftCounter != left.length
				ans = ans.push(right[rightCounter])
				rightCounter = rightCounter + 1
			end
		elsif leftCounter < left.length
			left.slice(leftCounter, left.length).each do |x|
				ans.push(x)
			end
			leftCounter = left.length
		elsif rightCounter < right.length
			right.slice(rightCounter, right.length).each do |x|
				ans.push(x)
			end
			rightCounter = right.length
		end



	end
	return ans
end


def timeIt(testArray)
	start = DateTime.now.strftime('%Q').to_i
	selectionSort(testArray)
	stop = DateTime.now.strftime('%Q').to_i
	puts "Selection Sort took: "+(stop-start).to_s
	start = DateTime.now.strftime('%Q').to_i
	heapsort(testArray)
	stop = DateTime.now.strftime('%Q').to_i
	puts "Heap Sort took: "+(stop-start).to_s
	# start = DateTime.now.strftime('%Q').to_i
	# quicksort(testArray)
	# stop = DateTime.now.strftime('%Q').to_i
	# puts "Quick Sort took: "+(stop-start).to_s
	start = DateTime.now.strftime('%Q').to_i
	insertionSort(testArray)
	stop = DateTime.now.strftime('%Q').to_i
	puts "Insertion Sort took: "+(stop-start).to_s
	start = DateTime.now.strftime('%Q').to_i
	mergeSort(testArray)
	stop = DateTime.now.strftime('%Q').to_i
	puts "Merge Sort took: "+(stop-start).to_s
end

# testArray = genArray(20000, 10000)
# timeIt(testArray)


# arrPri(testArray)
# puts
# arrPri(selectionSort(testArray))
# puts
# arrPri(heapsort(testArray))
# puts
# arrPri(quicksort(testArray))
# puts
# arrPri(insertionSort(testArray))
# puts
# arrPri(mergeSort(testArray))
