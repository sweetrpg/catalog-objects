// swift-tools-version: 6.0
// The swift-tools-version declares the minimum version of Swift required to build this package.

import PackageDescription

let package = Package(
    name: "CatalogObjects",
    platforms: [
       .macOS(.v13),
    ],
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
            dependencies: [.product(name: "ModelCore", package: "model-core")],
            swiftSettings: swiftSettings),
        .testTarget(
            name: "CatalogObjectsTests",
            dependencies: ["CatalogObjects"],
            swiftSettings: swiftSettings),
    ],
    swiftLanguageModes: [.v5]
)

var swiftSettings: [SwiftSetting] { [
    .enableUpcomingFeature("DisableOutwardActorInference"),
    .enableExperimentalFeature("StrictConcurrency"),
] }
