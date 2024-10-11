/**
 */

import Foundation
import ModelCore

/**
 */
public struct Contribution : Auditable {
    public var personId : URL
    public var volumeId : URL
    public var roles : [String]

    public var createdAt : Date
    public var createdBy : URL
    public var updatedAt : Date
    public var updatedBy : URL
    public var deletedAt : Date?
    public var deletedBy : URL?
}
