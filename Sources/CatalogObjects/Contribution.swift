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
extension Contribution : Auditable {
    public let createdAt : Date
    public let createdBy : String
    public let updatedAt : Date
    public let updatedBy : String
    public let deletedAt : Date?
    public let deletedBy : String?
}
