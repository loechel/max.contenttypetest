# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import max.contenttypetest


class MaxContenttypetestLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=max.contenttypetest)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'max.contenttypetest:default')


MAX_CONTENTTYPETEST_FIXTURE = MaxContenttypetestLayer()


MAX_CONTENTTYPETEST_INTEGRATION_TESTING = IntegrationTesting(
    bases=(MAX_CONTENTTYPETEST_FIXTURE,),
    name='MaxContenttypetestLayer:IntegrationTesting'
)


MAX_CONTENTTYPETEST_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(MAX_CONTENTTYPETEST_FIXTURE,),
    name='MaxContenttypetestLayer:FunctionalTesting'
)


MAX_CONTENTTYPETEST_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        MAX_CONTENTTYPETEST_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='MaxContenttypetestLayer:AcceptanceTesting'
)
