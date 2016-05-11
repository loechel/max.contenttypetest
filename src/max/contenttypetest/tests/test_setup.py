# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from max.contenttypetest.testing import MAX_CONTENTTYPETEST_INTEGRATION_TESTING  # noqa
from plone import api

import unittest2 as unittest


class TestSetup(unittest.TestCase):
    """Test that max.contenttypetest is properly installed."""

    layer = MAX_CONTENTTYPETEST_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if max.contenttypetest is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('max.contenttypetest'))

    def test_browserlayer(self):
        """Test that IMaxContenttypetestLayer is registered."""
        from max.contenttypetest.interfaces import IMaxContenttypetestLayer
        from plone.browserlayer import utils
        self.assertIn(IMaxContenttypetestLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = MAX_CONTENTTYPETEST_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['max.contenttypetest'])

    def test_product_uninstalled(self):
        """Test if max.contenttypetest is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled('max.contenttypetest'))

    def test_browserlayer_removed(self):
        """Test that IMaxContenttypetestLayer is removed."""
        from max.contenttypetest.interfaces import IMaxContenttypetestLayer
        from plone.browserlayer import utils
        self.assertNotIn(IMaxContenttypetestLayer, utils.registered_layers())
