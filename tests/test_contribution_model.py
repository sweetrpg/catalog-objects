# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from sweetrpg_catalog_objects.model.contribution import Contribution
import json
from datetime import datetime

contribution_json = """
{
    "_id": "this-is-ignored",
    "person_id": "1",
    "volume_id": "1",
    "roles": ["developer"],
    "created_at": "2021-09-13T07:55:00.001",
    "created_by": "test",
    "updated_at": "2021-09-13T07:55:00.001",
    "updated_by": "test"
}
"""
contribution_datetime = datetime(2021, 9, 13, 7, 55, 0, 1000)


def test_contribution_from_json():
    j = json.loads(contribution_json)
    a = Contribution(**j)
    assert isinstance(a, Contribution)
    assert a.person_id == "1"
    assert a.volume_id == "1"
    assert len(a.roles) == 1
    assert a.id == "this-is-ignored"
    assert a.created_at == contribution_datetime
    assert a.created_by == "test"
    assert a.updated_at == contribution_datetime
    assert a.updated_by == "test"
    assert not hasattr(a, "deleted_at") or a.deleted_at is None
    assert not hasattr(a, "deleted_by") or a.deleted_by is None
