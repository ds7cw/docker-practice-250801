// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Algorithms",
    products: [
        .library(name: "Algorithms", targets: ["Algorithms"]),
    ],
    targets: [
        .target(name: "Algorithms"),
        .testTarget(name: "AlgorithmsTests", dependencies: ["Algorithms"]),
    ],
)
