# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from sweetrpg_catalog_objects.model.review import Review
from sweetrpg_catalog_objects.model.volume import Volume
from sweetrpg_catalog_objects.db.review.schema import ReviewSchema
import json
from datetime import datetime


review_json = """
{
    "_id": "this-is-ignored",
    "title": "This sucks",
    "body": "I hate it",
    "language": "en",
    "created_at": "2021-09-13T07:55:00.001",
    "created_by": "test",
    "updated_at": "2021-09-13T07:55:00.001",
    "updated_by": "test",
    "tags": [{"name": "tag", "value": "tag"}]
}
"""
review_datetime = datetime(2021, 9, 13, 7, 55, 0, 1000)
review_dict = {
    "_id": "another-id",
    "title": "This is great",
    "body": "I love it",
    "language": "en_US",
    "created_at": datetime(2021, 9, 15, 7, 35, 0, 2000),
    "created_by": "test",
    "updated_at": datetime(2021, 9, 15, 7, 35, 0, 2001),
    "updated_by": "test",
    "deleted_at": datetime(2021, 9, 15, 7, 35, 0, 2002),
    "deleted_by": "test",
    "tags": [{"name": "tag", "value": "tag"}],
    "volume": "99",
}


def test_load_review_from_json():
    j = json.loads(review_json)
    j["volume"] = "99"  # Volume(id="99", name="Gretsky", slug="wayne", system="la-kings")
    schema = ReviewSchema()
    r = schema.load(j)
    assert r is not None
    assert isinstance(r, Review)
    assert r.id == "this-is-ignored"
    assert r.title == "This sucks"
    assert r.body == "I hate it"
    assert r.language == "en"
    assert r.created_at == review_datetime
    assert r.created_by == "test"
    assert r.updated_at == review_datetime
    assert r.updated_by == "test"


def test_load_review_from_dict():
    schema = ReviewSchema()
    r = schema.load(review_dict)
    assert r is not None
    assert isinstance(r, Review)
    assert r.title == "This is great"
    assert r.body == "I love it"
    assert r.language == "en_US"
    assert r.id == "another-id"
    assert r.created_at == datetime(2021, 9, 15, 7, 35, 0, 2000)
    assert r.created_by == "test"
    assert r.updated_at == datetime(2021, 9, 15, 7, 35, 0, 2001)
    assert r.updated_by == "test"
    assert r.deleted_at == datetime(2021, 9, 15, 7, 35, 0, 2002)
    assert r.deleted_by == "test"
