from ftw.footer.interfaces import IFtwFooterLayer
from ftw.footer.testing import FTW_FOOTER_INTEGRATION_TESTING
from plone.app.testing import login
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.app.testing import TEST_USER_NAME
from Products.Five.browser import BrowserView
from unittest2 import TestCase
from zope.component import queryMultiAdapter
from zope.interface import alsoProvides
from zope.viewlet.interfaces import IViewletManager


class TestFooter(TestCase):

    layer = FTW_FOOTER_INTEGRATION_TESTING

    def setUp(self):
        super(TestFooter, self).setUp()
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        login(self.portal, TEST_USER_NAME)

    def get_viewet(self, context):
        alsoProvides(context.REQUEST, IFtwFooterLayer)
        view = BrowserView(context, context.REQUEST)
        manager_name = 'plone.portalfooter'

        manager = queryMultiAdapter(
            (context, context.REQUEST, view),
            IViewletManager,
            manager_name)
        self.failUnless(manager)

        # Set up viewlets
        manager.update()
        name = 'ftw.footer.viewlet'
        viewlets = [v for v in manager.viewlets if v.__name__ == name]

        if len(viewlets) == 1:
            return viewlets[0]
        return None

    def test_viewlet_registered_plone_root(self):
        viewlet = self.get_viewet(self.portal)

        self.assertTrue(viewlet, 'Viewlet is not available on portal root')
