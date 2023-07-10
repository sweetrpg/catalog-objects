# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from sweetrpg_catalog_objects.db.contribution.document import ContributionDocument
from datetime import datetime


def test_contribution_document_setup():
    c = ContributionDocument(person_id="1", volume_id="1", roles=["developer"])
    assert c is not None
    assert c.person_id == "1"
    assert c.volume_id == "1"
    assert len(c.roles) == 1
    assert isinstance(c.created_at, datetime)
    assert c.created_by == "system"
    assert isinstance(c.updated_at, datetime)
    assert c.updated_by == "system"
    assert c.deleted_at is None
    assert c.deleted_by is None
