/**
 */

import Foundation
import ModelCore

/**
 */
public struct Contribution {
    public let personId : URI
    public let volumeId : URI
    public let roles : [String]
}

/**
 */
extension Contribution : Auditable {}
