import XCTest
import Algorithms

final class AlgorithmTests: XCTestCase {

    func testBinarySearch() {
        let array = [1, 3, 5, 7, 9]
        XCTAssertEqual(binarySearch(array, target: 5), 2)
        XCTAssertNil(binarySearch(array, target: 10))
    }

    func testQuickSort() {
        let array = [5, 3, 8, 1]
        XCTAssertEqual(quickSort(array), [1, 3, 5, 8])
    }

    func testMergeSort() {
        let array = [5, 3, 8, 1]
        XCTAssertEqual(mergeSort(array), [1, 3, 5, 8])
    }

    func testBFS() {
        let graph = [1: [2, 3], 2: [4], 3: [], 4: []]
        XCTAssertEqual(bfs(graph: graph, start: 1), [1, 2, 3, 4])
    }

    func testDFS() {
        let graph = [1: [2, 3], 2: [4], 3: [], 4: []]
        XCTAssertEqual(dfs(graph: graph, start: 1), [1, 2, 4, 3])
    }
}
