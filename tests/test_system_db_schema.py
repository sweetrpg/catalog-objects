# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from sweetrpg_catalog_objects.model.system import System
from sweetrpg_catalog_objects.db.system.schema import SystemSchema
import json
from datetime import datetime


system_json = """
{
    "_id": "this-is-ignored",
    "game_system": "dnd",
    "name": "Dungeons and Dragons",
    "edition": "5",
    "created_at": "2021-09-13T07:55:00.001",
    "created_by": "test",
    "updated_at": "2021-09-13T07:55:00.001",
    "updated_by": "test",
    "tags": [{"name": "tag", "value": "tag"}]
}
"""
system_datetime = datetime(2021, 9, 13, 7, 55, 0, 1000)
system_dict = {
    "_id": "another-id",
    "game_system": "dnd",
    "name": "Dungeons and Dragons",
    "edition": "5",
    "created_at": datetime(2021, 9, 15, 7, 35, 0, 2000),
    "created_by": "test",
    "updated_at": datetime(2021, 9, 15, 7, 35, 0, 2001),
    "updated_by": "test",
    "deleted_at": datetime(2021, 9, 15, 7, 35, 0, 2002),
    "deleted_by": "test",
    "tags": [{"name": "tag", "value": "tag"}],
}


def test_load_system_from_json():
    j = json.loads(system_json)
    schema = SystemSchema()
    s = schema.load(j)
    assert s is not None
    assert isinstance(s, System)
    assert s.id == "this-is-ignored"
    assert s.game_system == "dnd"
    assert s.name == "Dungeons and Dragons"
    assert s.edition == "5"
    assert s.created_at == system_datetime
    assert s.created_by == "test"
    assert s.updated_at == system_datetime
    assert s.updated_by == "test"
    assert s.deleted_at is None
    assert s.deleted_by is None


def test_load_system_from_dict():
    schema = SystemSchema()
    s = schema.load(system_dict)
    assert s is not None
    assert isinstance(s, System)
    assert s.id == "another-id"
    assert s.game_system == "dnd"
    assert s.name == "Dungeons and Dragons"
    assert s.edition == "5"
    assert s.created_at == datetime(2021, 9, 15, 7, 35, 0, 2000)
    assert s.created_by == "test"
    assert s.updated_at == datetime(2021, 9, 15, 7, 35, 0, 2001)
    assert s.updated_by == "test"
    assert s.deleted_at == datetime(2021, 9, 15, 7, 35, 0, 2002)
    assert s.deleted_by == "test"
