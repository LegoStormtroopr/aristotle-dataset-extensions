from django.test import TestCase

import aristotle_mdr.models as MDR
from django.core.urlresolvers import reverse
from aristotle_mdr.tests.utils import ManagedObjectVisibility
from aristotle_mdr.tests.test_html_pages import LoggedInViewConceptPages
from aristotle_mdr.tests.test_admin_pages import AdminPageForConcept

from django.test.utils import setup_test_environment
setup_test_environment()

from aristotle_dse import models

class LoggedInViewDSSConceptPages(LoggedInViewConceptPages):
    def get_help_page(self):
        return reverse('aristotle_dse:about',args=[self.item1._meta.model_name])

class DataSetSpecificationVisibility(TestCase,ManagedObjectVisibility):
    def setUp(self):
        super(DataSetSpecificationVisibility, self).setUp()
        self.wg = MDR.Workgroup.objects.create(name="Setup WG")
        self.item = models.DataSetSpecification.objects.create(name="Test DSS",
            workgroup=self.wg,
            )

class DataSetSpecificationAdmin(AdminPageForConcept,TestCase):
    itemType=models.DataSetSpecification
    form_defaults={
        'dataElements-TOTAL_FORMS':0,
        'dataElements-INITIAL_FORMS':0,
        'dataElements-MAX_NUM_FORMS':1,
        }

class DataSetSpecificationViewPage(LoggedInViewDSSConceptPages,TestCase):
    url_name='datasetspecification'
    itemType=models.DataSetSpecification
    def get_help_page(self):
        return reverse('aristotle_dse:about',args=[self.item1._meta.model_name])
    def test_help_page_exists(self):
        self.logout()
        response = self.client.get(self.get_help_page())
        self.assertEqual(response.status_code,200)