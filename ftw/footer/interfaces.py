from zope.interface import Interface
from zope import schema


class IFooterSettings(Interface):

    columns_count = schema.Choice(title=u"Footer Columns count",
                                  description=u"Defines how many Columns \
                                  there are in the Footer",
                                  values=[1, 2, 4],
                                  default=4
                                  )


class IFtwFooterLayer(Interface):
    """Request marker interface"""
