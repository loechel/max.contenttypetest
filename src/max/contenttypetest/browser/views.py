# -*- coding: utf-8 -*-

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class NestedTestView(BrowserView):

    template = ViewPageTemplateFile('templates/nestedtest.pt')

    def __init__(self, context, request):
        super(NestedTestView, self).__init__(context, request)

    def __call__(self):
        return self.template()


class TableView(BrowserView):

    template = ViewPageTemplateFile('templates/table.pt')

    def __init__(self, context, request):
        super(TableView, self).__init__(context, request)

    def __call__(self):
        return self.template()


class RowView(BrowserView):

    template = ViewPageTemplateFile('templates/row.pt')

    def __init__(self, context, request):
        super(RowView, self).__init__(context, request)

    def __call__(self):
        return self.template()
