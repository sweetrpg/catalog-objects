# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from sweetrpg_catalog_objects.model.studio import Studio
from sweetrpg_catalog_objects.db.studio.schema import StudioSchema
import json
from datetime import datetime


studio_json = """
{
    "_id": "this-is-ignored",
    "name": "Joe Bob",
    "created_at": "2021-09-13T07:55:00.001",
    "created_by": "test",
    "updated_at": "2021-09-13T07:55:00.001",
    "updated_by": "test",
    "tags": [{"name": "tag", "value": "tag"}]
}
"""
studio_datetime = datetime(2021, 9, 13, 7, 55, 0, 1000)
studio_dict = {
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


def test_load_studio_from_json():
    j = json.loads(studio_json)
    schema = StudioSchema()
    t = schema.load(j)
    assert t is not None
    assert isinstance(t, Studio)
    assert t.id == "this-is-ignored"
    assert t.name == "Joe Bob"
    tag = t.tags[0]
    assert tag["name"] == "tag"
    assert tag["value"] == "tag"
    assert t.created_at == studio_datetime
    assert t.created_by == "test"
    assert t.updated_at == studio_datetime
    assert t.updated_by == "test"
    assert t.deleted_at is None
    assert t.deleted_by is None


def test_load_studio_from_dict():
    schema = StudioSchema()
    t = schema.load(studio_dict)
    assert t is not None
    assert isinstance(t, Studio)
    assert t.id == "another-id"
    assert t.name == "Billy"
    tag = t.tags[0]
    assert tag["name"] == "tag"
    assert tag["value"] == "tag"
    assert t.created_at == datetime(2021, 9, 15, 7, 35, 0, 2000)
    assert t.created_by == "test"
    assert t.updated_at == datetime(2021, 9, 15, 7, 35, 0, 2001)
    assert t.updated_by == "test"
    assert t.deleted_at == datetime(2021, 9, 15, 7, 35, 0, 2002)
    assert t.deleted_by == "test"
