# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from sweetrpg_catalog_objects.db.person.document import PersonDocument
from sweetrpg_catalog_objects.db.embedded.property.document import PropertyDocument
from sweetrpg_catalog_objects.db.embedded.tag.document import TagDocument
from datetime import datetime


def test_author_document_setup():
    t = TagDocument(name="tag", value="value")
    p = PropertyDocument(name="property", kind="kind", value="value")
    a = PersonDocument(name="Bob", properties=[p], tags=[t])
    assert a is not None
    assert a.name == "Bob"
    assert len(a.properties) == 1
    assert len(a.tags) == 1
    assert isinstance(a.created_at, datetime)
    assert a.created_by == "system"
    assert isinstance(a.updated_at, datetime)
    assert a.updated_by == "system"
    assert a.deleted_at is None
    assert a.deleted_by is None
