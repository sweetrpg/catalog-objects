// swift-tools-version: 5.7
// The swift-tools-version declares the minimum version of Swift required to build this package.

import PackageDescription

let package = Package(
    name: "CatalogObjects",
    products: [
        .library(
            name: "CatalogObjects",
            targets: ["CatalogObjects"]),
    ],
    dependencies: [
        .package(url: "https://github.com/sweetrpg/model-core.git", branch: "feature/swift"),
        .package(url: "https://github.com/apple/swift-docc-plugin", from: "1.0.0"),
    ],
    targets: [
        .target(
            name: "CatalogObjects",
            dependencies: [.product(name: "ModelCore", package: "model-core")]),
        .testTarget(
            name: "CatalogObjectsTests",
            dependencies: ["CatalogObjects"]
        ),
    ]
)
