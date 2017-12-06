from ftw.footer.testing import FTW_FOOTER_FUNCTIONAL_TESTING
from ftw.testbrowser import browsing
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from unittest import TestCase
import transaction


class TestFooterFunctional(TestCase):

    layer = FTW_FOOTER_FUNCTIONAL_TESTING

    def setUp(self):
        super(TestFooterFunctional, self).setUp()
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        transaction.commit()

        self.add_portlet_url = '{0}/++contextportlets++ftw.footer.column1/+/' \
                               'plone.portlet.static.Static'.format(self.portal.absolute_url())

    @browsing
    def test_footer_on_contentish_object(self, browser):
        """
        The footer must be rendered on contentish views.
        """
        browser.login()

        # Add a footer portlet.
        browser.open(self.add_portlet_url)
        browser.fill({
            'Text The text to render': 'My Portlet Text',
        }).save()

        # The footer portlet is shown on the Plone Site.
        browser.open(self.portal)
        self.assertEqual(
            'My Portlet Text',
            browser.css('#footer-column-1').first.text
        )

        # The footer portlet is shown on the control panel, which is a view
        # on a contentish object (Plone Site).
        browser.open(self.portal.absolute_url() + '/@@overview-controlpanel')
        self.assertEqual(
            'My Portlet Text',
            browser.css('#footer-column-1').first.text
        )

        # The footer portlet is shown when managing the footer.
        browser.find('Manage Footer').click()
        self.assertEqual(
            'My Portlet Text',
            browser.css('#footer-column-1').first.text
        )

    @browsing
    def test_footer_on_non_contentish_object(self, browser):
        """
        The footer must be rendered on non-contentish views too, e.g.
        on a portlet context.
        """
        browser.login()

        # Add a footer portlet.
        browser.open(self.add_portlet_url)
        browser.fill({
            'Text The text to render': 'My Portlet Text',
        }).save()

        # The footer portlet is shown on a portlet context.
        browser.open(self.portal.absolute_url() + '/++contextportlets++ftw.footer.column1/portlet_static/edit')
        self.assertEqual(
            'My Portlet Text',
            browser.css('#footer-column-1').first.text
        )
