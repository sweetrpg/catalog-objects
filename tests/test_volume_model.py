# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from sweetrpg_catalog_objects.model.volume import Volume
import json
from datetime import datetime

volume_json = """
{
    "_id": "this-is-ignored",
    "title": "Player's Handbook",
    "description": "Informative",
    "system_ids": ["dnd5"],
    "publisher_ids": ["1"],
    "studio_ids": ["1"],
    "tags": [{"name": "tag", "value": "tag"}],
    "properties": [
        {"name": "value", "value": "1", "kind": "int"}
    ],
    "created_at": "2021-09-13T07:55:00.001",
    "created_by": "test",
    "updated_at": "2021-09-13T07:55:00.001",
    "updated_by": "test"
}
"""
volume_datetime = datetime(2021, 9, 13, 7, 55, 0, 1000)


def test_volume_from_json():
    j = json.loads(volume_json)
    v = Volume(**j)
    assert isinstance(v, Volume)
    assert v.id == "this-is-ignored"
    assert v.title == "Player's Handbook"
    assert v.description == "Informative"
    assert "dnd5" in v.system_ids
    assert "1" in v.publisher_ids
    assert "1" in v.studio_ids
    assert len(v.tags) == 1
    t = v.tags[0]
    assert t["name"] == "tag"
    assert t["value"] == "tag"
    p = v.properties[0]
    assert p["name"] == "value"
    assert p["value"] == "1"
    assert p["kind"] == "int"
    assert v.created_at == volume_datetime
    assert v.created_by == "test"
    assert v.updated_at == volume_datetime
    assert v.updated_by == "test"
    assert not hasattr(v, "deleted_at") or v.deleted_at is None
    assert not hasattr(v, "deleted_by") or v.deleted_by is None
