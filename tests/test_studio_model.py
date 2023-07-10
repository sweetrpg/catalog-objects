# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from sweetrpg_catalog_objects.model.studio import Studio
import json
from datetime import datetime

studio_json = """
{
    "_id": "this-is-ignored",
    "name": "One Room",
    "created_at": "2021-09-13T07:55:00.001",
    "created_by": "test",
    "updated_at": "2021-09-13T07:55:00.001",
    "updated_by": "test",
     "tags": [
        {"name": "tag", "value": "tag"}
    ]
}
"""
studio_datetime = datetime(2021, 9, 13, 7, 55, 0, 1000)


def test_studio_from_json():
    j = json.loads(studio_json)
    s = Studio(**j)
    assert isinstance(s, Studio)
    assert s.id == "this-is-ignored"
    assert s.name == "One Room"
    assert s.created_at == studio_datetime
    assert s.created_by == "test"
    assert s.updated_at == studio_datetime
    assert s.updated_by == "test"
    assert not hasattr(s, "deleted_at") or s.deleted_at is None
    assert not hasattr(s, "deleted_by") or s.deleted_by is None
    assert len(s.tags) == 1
    t = s.tags[0]
    assert t["name"] == "tag"
    assert t["value"] == "tag"
