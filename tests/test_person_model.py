# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from sweetrpg_catalog_objects.model.person import Person
import json
from datetime import datetime

author_json = """
{
    "_id": "this-is-ignored",
    "name": "Joe Bob",
    "created_at": "2021-09-13T07:55:00.001",
    "created_by": "test",
    "updated_at": "2021-09-13T07:55:00.001",
    "updated_by": "test",
    "tags": [
        {"name": "tag", "value": "tag"}
    ],
    "properties": [
        {"name": "property", "kind": "property", "value": "property"}
    ]
}
"""
author_datetime = datetime(2021, 9, 13, 7, 55, 0, 1000)


def test_author_from_json():
    j = json.loads(author_json)
    p = Person(**j)
    assert isinstance(p, Person)
    assert p.name == "Joe Bob"
    assert p.id == "this-is-ignored"
    assert p.created_at == author_datetime
    assert p.created_by == "test"
    assert p.updated_at == author_datetime
    assert p.updated_by == "test"
    assert not hasattr(p, "deleted_at") or p.deleted_at is None
    assert not hasattr(p, "deleted_by") or p.deleted_by is None
    assert len(p.tags) == 1
    t = p.tags[0]
    assert t["name"] == "tag"
    assert t["value"] == "tag"
    assert len(p.properties) == 1
    p = p.properties[0]
    assert p["name"] == "property"
    assert p["kind"] == "property"
    assert p["value"] == "property"
