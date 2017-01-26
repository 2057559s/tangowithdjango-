from django.test import *
from rango.forms import *

# Create your tests here.


class TestCategoryForm(TestCase):
    

    def test_Category_name(self):
        form = CategoryForm(name="Nick", views=0)
        self.assertEqual(self.form.name, "Nick")

