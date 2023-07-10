# -*- coding: utf-8 -*-
__volume__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from sweetrpg_catalog_objects.model.volume import Volume
from sweetrpg_catalog_objects.db.volume.schema import VolumeSchema
import json
from datetime import datetime


volume_json = """
{
    "_id": "this-is-ignored",
    "title": "Bob's Book",
    "description": "The book that Bob worked pretty hard on",
    "system_ids": ["bobo"],
    "created_at": "2021-09-13T07:55:00.001",
    "created_by": "test",
    "updated_at": "2021-09-13T07:55:00.001",
    "updated_by": "test",
    "tags": [{"name":"tag", "value":"tag"}],
    "publisher_ids": ["1"],
    "properties": [
        {"name": "value", "value": "1", "kind": "int"}
    ]
}
"""
volume_datetime = datetime(2021, 9, 13, 7, 55, 0, 1000)
volume_dict = {
    "_id": "another-id",
    "title": "BillyBook",
    "description": "Another work",
    "system_ids": ["yo"],
    "created_at": datetime(2021, 9, 15, 7, 35, 0, 2000),
    "created_by": "test",
    "updated_at": datetime(2021, 9, 15, 7, 35, 0, 2001),
    "updated_by": "test",
    "deleted_at": datetime(2021, 9, 15, 7, 35, 0, 2001),
    "deleted_by": "test",
    "tags": [{"name": "tag", "value": "tag"}],
    "publisher_ids": ["1"],
    "properties": [
        {"name": "value", "value": "1", "kind": "int"},
    ],
}


# # def test_volume_repr():
# #     a = Volume(name="This guy")
# #     assert isinstance(a, Volume)
# #     s = f"{a!r}"
# #     assert "name=This guy" in s


def test_load_volume_from_json():
    j = json.loads(volume_json)
    schema = VolumeSchema()
    v = schema.load(j)
    assert v is not None
    assert isinstance(v, Volume)
    assert v.id == "this-is-ignored"
    assert v.title == "Bob's Book"
    assert v.description == "The book that Bob worked pretty hard on"
    assert "bobo" in v.system_ids
    assert "1" in v.publisher_ids
    assert len(v.tags) == 1
    t = v.tags[0]
    assert t["name"] == "tag"
    assert t["value"] == "tag"
    assert len(v.properties) == 1
    p = v.properties[0]
    assert p["name"] == "value"
    assert p["value"] == "1"
    assert p["kind"] == "int"
    assert v.created_at == volume_datetime
    assert v.created_by == "test"
    assert v.created_at == volume_datetime
    assert v.updated_by == "test"
    assert v.deleted_at is None
    assert v.deleted_by is None


def test_load_volume_from_dict():
    schema = VolumeSchema()
    v = schema.load(volume_dict)
    assert v is not None
    assert isinstance(v, Volume)
    assert v.id == "another-id"
    assert v.title == "BillyBook"
    assert v.description == "Another work"
    assert "yo" in v.system_ids
    assert "1" in v.publisher_ids
    assert len(v.tags) == 1
    t = v.tags[0]
    assert t["name"] == "tag"
    assert t["value"] == "tag"
    assert len(v.properties) == 1
    p = v.properties[0]
    assert p["name"] == "value"
    assert p["value"] == "1"
    assert p["kind"] == "int"
    assert v.created_at == datetime(2021, 9, 15, 7, 35, 0, 2000)
    assert v.created_by == "test"
    assert v.updated_at == datetime(2021, 9, 15, 7, 35, 0, 2001)
    assert v.updated_by == "test"
    assert v.deleted_at == datetime(2021, 9, 15, 7, 35, 0, 2001)
    assert v.deleted_by == "test"
