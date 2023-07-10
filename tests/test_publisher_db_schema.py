# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from sweetrpg_catalog_objects.model.publisher import Publisher
from sweetrpg_catalog_objects.db.publisher.schema import PublisherSchema
import json
from datetime import datetime


publisher_json = """
{
    "_id": "this-is-ignored",
    "name": "Joe Bob",
    "created_at": "2021-09-15T21:51:00.001",
    "created_by": "test",
    "updated_at": "2021-09-15T21:51:00.001",
    "updated_by": "test",
    "tags": [{"name": "tag", "value": "tag"}]
}
"""
publisher_datetime = datetime(2021, 9, 15, 21, 51, 0, 1000)
publisher_dict = {
    "_id": "another-id",
    "name": "Billy",
    "created_at": datetime(2021, 9, 15, 7, 35, 0, 2000),
    "created_by": "test",
    "updated_at": datetime(2021, 9, 15, 7, 35, 0, 2001),
    "updated_by": "test",
    "deleted_at": datetime(2021, 9, 15, 7, 35, 0, 2002),
    "deleted_by": "test",
    "tags": [{"name": "tag", "value": "tag"}],
}


# # def test_publisher_repr():
# #     a = Publisher(name="This guy")
# #     assert isinstance(a, Publisher)
# #     s = f"{a!r}"
# #     assert "name=This guy" in s


def test_load_publisher_from_json():
    j = json.loads(publisher_json)
    schema = PublisherSchema()
    p = schema.load(j)
    assert p is not None
    assert isinstance(p, Publisher)
    assert p.id == "this-is-ignored"
    assert p.name == "Joe Bob"
    assert len(p.tags) == 1
    t = p.tags[0]
    assert t["name"] == "tag"
    assert t["value"] == "tag"
    assert p.created_at == publisher_datetime
    assert p.created_by == "test"
    assert p.updated_at == publisher_datetime
    assert p.updated_by == "test"
    assert p.deleted_at is None
    assert p.deleted_by is None


def test_load_publisher_from_dict():
    schema = PublisherSchema()
    p = schema.load(publisher_dict)
    assert p is not None
    assert isinstance(p, Publisher)
    assert p.id == "another-id"
    assert p.name == "Billy"
    assert len(p.tags) == 1
    t = p.tags[0]
    assert t["name"] == "tag"
    assert t["value"] == "tag"
    assert p.created_at == datetime(2021, 9, 15, 7, 35, 0, 2000)
    assert p.created_by == "test"
    assert p.updated_at == datetime(2021, 9, 15, 7, 35, 0, 2001)
    assert p.updated_by == "test"
    assert p.deleted_at == datetime(2021, 9, 15, 7, 35, 0, 2002)
    assert p.deleted_by == "test"
