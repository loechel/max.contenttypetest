# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s max.contenttypetest -t test_nestedtest.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src max.contenttypetest.testing.MAX_CONTENTTYPETEST_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/plonetraining/testing/tests/robot/test_nestedtest.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a NestedTest
  Given a logged-in site administrator
    and an add nestedtest form
   When I type 'My NestedTest' into the title field
    and I submit the form
   Then a nestedtest with the title 'My NestedTest' has been created

Scenario: As a site administrator I can view a NestedTest
  Given a logged-in site administrator
    and a nestedtest 'My NestedTest'
   When I go to the nestedtest view
   Then I can see the nestedtest title 'My NestedTest'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add nestedtest form
  Go To  ${PLONE_URL}/++add++NestedTest

a nestedtest 'My NestedTest'
  Create content  type=NestedTest  id=my-nestedtest  title=My NestedTest


# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.title  ${title}

I submit the form
  Click Button  Save

I go to the nestedtest view
  Go To  ${PLONE_URL}/my-nestedtest
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a nestedtest with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the nestedtest title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
