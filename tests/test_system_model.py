# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from sweetrpg_catalog_objects.model.system import System
import json
from datetime import datetime

system_json = """
{
    "_id": "this-is-ignored",
    "game_system": "dnd",
    "title": "Dungeons and Dragons",
    "created_at": "2021-09-13T07:55:00.001",
    "created_by": "test",
    "updated_at": "2021-09-13T07:55:00.001",
    "updated_by": "test",
    "tags": [
        {"name": "tag", "value": "tag"}
    ]
}
"""
system_datetime = datetime(2021, 9, 13, 7, 55, 0, 1000)


def test_system_from_json():
    j = json.loads(system_json)
    s = System(**j)
    assert isinstance(s, System)
    assert s.id == "this-is-ignored"
    assert s.game_system == "dnd"
    assert s.title == "Dungeons and Dragons"
    assert s.created_at == system_datetime
    assert s.created_by == "test"
    assert s.updated_at == system_datetime
    assert s.updated_by == "test"
    assert not hasattr(s, "deleted_at") or s.deleted_at is None
    assert not hasattr(s, "deleted_by") or s.deleted_by is None
    assert len(s.tags) == 1
    t = s.tags[0]
    assert t["name"] == "tag"
    assert t["value"] == "tag"
