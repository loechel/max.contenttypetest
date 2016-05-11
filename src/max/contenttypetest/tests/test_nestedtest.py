# -*- coding: utf-8 -*-
from plone.app.testing import TEST_USER_ID
from zope.component import queryUtility
from zope.component import createObject
from plone.app.testing import setRoles
from plone.dexterity.interfaces import IDexterityFTI
from plone import api

from max.contenttypetest.testing import MAX_CONTENTTYPETEST_INTEGRATION_TESTING  # noqa
from max.contenttypetest.interfaces import INestedTest

import unittest2 as unittest


class NestedTestIntegrationTest(unittest.TestCase):

    layer = MAX_CONTENTTYPETEST_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='NestedTest')
        schema = fti.lookupSchema()
        self.assertEqual(INestedTest, schema)

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='NestedTest')
        self.assertTrue(fti)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='NestedTest')
        factory = fti.factory
        obj = createObject(factory)
        self.assertTrue(INestedTest.providedBy(obj))

    def test_adding(self):
        self.portal.invokeFactory('NestedTest', 'NestedTest')
        self.assertTrue(
            INestedTest.providedBy(self.portal['NestedTest'])
        )
