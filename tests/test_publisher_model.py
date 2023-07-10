# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from sweetrpg_catalog_objects.model.publisher import Publisher
import json
from datetime import datetime

publisher_json = """
{
    "_id": "this-is-ignored",
    "name": "Cheap League",
    "created_at": "2021-09-14T20:05:00.001",
    "created_by": "test",
    "updated_at": "2021-09-14T20:05:00.001",
    "updated_by": "test",
    "tags": [
        {"name": "tag", "value": "tag"}
    ]
}
"""
publisher_datetime = datetime(2021, 9, 14, 20, 5, 0, 1000)


def test_publisher_from_json():
    j = json.loads(publisher_json)
    p = Publisher(**j)
    assert isinstance(p, Publisher)
    assert p.id == "this-is-ignored"
    assert p.name == "Cheap League"
    assert p.created_at == publisher_datetime
    assert p.created_by == "test"
    assert p.updated_at == publisher_datetime
    assert p.updated_by == "test"
    assert not hasattr(p, "deleted_at") or p.deleted_at is None
    assert not hasattr(p, "deleted_by") or p.deleted_by is None
    assert len(p.tags) == 1
    t = p.tags[0]
    assert t["name"] == "tag"
    assert t["value"] == "tag"
