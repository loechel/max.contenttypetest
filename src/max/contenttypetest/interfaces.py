# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from max.contenttypetest import _
from z3c.form.object import registerFactoryAdapter
from zope import schema
from zope.interface import Interface
from zope.interface import implements
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IMaxContenttypetestLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IRow(Interface):

    course = schema.TextLine(
        title=_(u"Course"),
        required=False,
    )

    ects = schema.Int(
        title=_(u"ECTS"),
        required=False,
    )

    grade = schema.Decimal(
        title=_(u"Grade"),
        description=_(u"The Grade you have become for this Course.")
    )


class Row(object):
    implements(IRow)

    def __init__(self):
        pass


registerFactoryAdapter(IRow, Row)


class ITable(Interface):

    row = schema.List(
        title=_(u"Row"),
        value_type=schema.Object(
            title=_(u"Row Object"),
            schema=IRow,
        ),
        required=False,
    )

    average = schema.Decimal(
        title=_(u"Average"),
        required=False,
    )


class Table(object):
    implements(ITable)

    def __init__(self):
        pass


registerFactoryAdapter(ITable, Table)


class INestedTest(Interface):

    title = schema.TextLine(
        title=_(u"Title"),
        description=_(u"Description"),
        required=True,
    )

    nested = schema.List(
        title=_(u"Nested Objects"),
        value_type=schema.Object(schema=ITable),
        required=False
    )
