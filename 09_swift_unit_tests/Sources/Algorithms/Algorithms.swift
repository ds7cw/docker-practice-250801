public func binarySearch<T: Comparable>(_ array: [T], target: T) -> Int? {
    var low = 0, high = array.count - 1
    while low <= high {
        let mid = (low + high) / 2
        if array[mid] == target {
            return mid
        } else if array[mid] < target {
            low = mid + 1
        } else {
            high = mid - 1
        }
    }
    return nil
}


public func quickSort<T: Comparable>(_ array: [T]) -> [T] {
    guard array.count > 1 else { return array }
    let pivot = array[array.count / 2]
    let less = array.filter { $0 < pivot }
    let equal = array.filter { $0 == pivot }
    let greater = array.filter { $0 > pivot }
    return quickSort(less) + equal + quickSort(greater)
}


public func mergeSort<T: Comparable>(_ array: [T]) -> [T] {
    guard array.count > 1 else { return array }
    let mid = array.count / 2
    let left = mergeSort(Array(array[..<mid]))
    let right = mergeSort(Array(array[mid...]))
    return merge(left, right)
}


public func merge<T: Comparable>(_ left: [T], _ right: [T]) -> [T] {
    var result: [T] = []
    var i = 0, j = 0
    while i < left.count && j < right.count {
        if left[i] < right[j] {
            result.append(left[i])
            i += 1
        } else {
            result.append(right[j])
            j += 1
        }
    }
    result += left[i...] + right[j...]
    return result
}



// Breadth-First Search
public func bfs(graph: [Int: [Int]], start: Int) -> [Int] {
    var visited: Set<Int> = []
    var queue: [Int] = [start]
    var result: [Int] = []

    while !queue.isEmpty {
        let node = queue.removeFirst()
        if !visited.contains(node) {
            visited.insert(node)
            result.append(node)
            queue += graph[node] ?? []
        }
    }
    return result
}
