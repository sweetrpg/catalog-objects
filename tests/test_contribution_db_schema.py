# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from sweetrpg_catalog_objects.model.contribution import Contribution
from sweetrpg_catalog_objects.db.contribution.schema import ContributionSchema
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
contribution_dict = {
    "_id": "another-id",
    "person_id": "1",
    "volume_id": "1",
    "roles": ["developer"],
    "created_at": datetime(2021, 9, 15, 7, 35, 0, 2000),
    "created_by": "test",
    "updated_at": datetime(2021, 9, 15, 7, 35, 0, 2001),
    "updated_by": "test",
    "deleted_at": datetime(2021, 9, 15, 7, 35, 0, 2001),
    "deleted_by": "test",
}


def test_load_contribution_from_json():
    j = json.loads(contribution_json)
    schema = ContributionSchema()
    a = schema.load(j)
    assert a is not None
    assert isinstance(a, Contribution)
    assert a.id == "this-is-ignored"
    assert a.person_id == "1"
    assert a.volume_id == "1"
    assert len(a.roles) == 1
    assert a.created_at == contribution_datetime
    assert a.created_by == "test"
    assert a.created_at == contribution_datetime
    assert a.updated_by == "test"
    assert a.deleted_at is None
    assert a.deleted_by is None


def test_load_contribution_from_dict():
    schema = ContributionSchema()
    a = schema.load(contribution_dict)
    assert a is not None
    assert isinstance(a, Contribution)
    assert a.id == "another-id"
    assert a.person_id == "1"
    assert a.volume_id == "1"
    assert len(a.roles) == 1
    assert a.created_at == datetime(2021, 9, 15, 7, 35, 0, 2000)
    assert a.created_by == "test"
    assert a.updated_at == datetime(2021, 9, 15, 7, 35, 0, 2001)
    assert a.updated_by == "test"
    assert a.deleted_at == datetime(2021, 9, 15, 7, 35, 0, 2001)
    assert a.deleted_by == "test"
