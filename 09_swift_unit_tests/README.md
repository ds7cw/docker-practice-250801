# Set up a container to run Swift (iOS) unit tests

### File structure
```bash
09_swift_unit_tests/
├── Sources/
│   └── Algorithms/
│       └── Algorithms.swift
├── Tests/
│   └── AlgorithmsTests/
│       └── AlgorithmsTests.swift
├── Dockerfile
└── README.md
```

### Dependencies/imports
The project uses the following imports:
```
PackageDescription
XCTest
```

### Build the image and run the container
Build the image before starting the container
```bash
cd 09_swift_unit_tests
docker build -t swift-algorithms .
```

Run the container
```bash
cd 09_swift_unit_tests
docker run --rm swift-algorithms
```

### Expected output after the Docker Container starts running
```bash
Build complete! (7.27s)
Test Suite 'All tests' started at 14:46:38.447
Test Suite 'debug.xctest' started at 14:46:38.470
Test Suite 'AlgorithmTests' started at 14:46:38.470
Test Case 'AlgorithmTests.testBFS' started at 14:46:38.470
Test Case 'AlgorithmTests.testBFS' passed (0.001 seconds)
Test Case 'AlgorithmTests.testBinarySearch' started at 14:46:38.471
Test Case 'AlgorithmTests.testBinarySearch' passed (0.101 seconds)
Test Case 'AlgorithmTests.testDFS' started at 14:46:38.572
Test Case 'AlgorithmTests.testDFS' passed (0.0 seconds)
Test Case 'AlgorithmTests.testMergeSort' started at 14:46:38.573
Test Case 'AlgorithmTests.testMergeSort' passed (0.001 seconds)
Test Case 'AlgorithmTests.testQuickSort' started at 14:46:38.573
Test Case 'AlgorithmTests.testQuickSort' passed (0.0 seconds)
Test Suite 'AlgorithmTests' passed at 14:46:38.573
         Executed 5 tests, with 0 failures (0 unexpected) in 0.103 (0.103) seconds
Test Suite 'debug.xctest' passed at 14:46:38.574
         Executed 5 tests, with 0 failures (0 unexpected) in 0.103 (0.103) seconds
Test Suite 'All tests' passed at 14:46:38.574
         Executed 5 tests, with 0 failures (0 unexpected) in 0.103 (0.103) seconds
◇ Test run started.
↳ Testing Library Version: 6.1.3 ()
↳ Target Platform: x86_64-unknown-linux-gnu
✔ Test run with 0 tests passed after 0.001 seconds.
```
