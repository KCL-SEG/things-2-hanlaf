from django.test import TestCase
from things.forms import ThingForm

# Create your tests here.

class ThingFormTestCase(TestCase):
    def setUp(self):
        self.form_input = {
            "name" : "Thing",
            "description" : "This is a thing",
            "quantity" : 1,
        }

    # Form accepts valid input
    def test_form_accepts_valid_input(self):
        form = ThingForm(data=self.form_input)
        self.assertTrue(form)

    # Form refuses form with empty name
    def test_form_refuses_empty_name(self):
        self.form_input['name'] = ""
        form = ThingForm(data=self.form_input)
        self.assertFalse(form.is_valid())
    
    # Form refuses form with empty quantity
    def test_form_refuses_empty_quantity(self):
        form_input = {
            "name" : "Thing",
            "description" : "This is a thing"
            }
        form = ThingForm(data=form_input)
        self.assertFalse(form.is_valid())

    # Form refuses form with quantity below 0
    def test_form_refuses_quantity_below_zero(self):
        self.form_input['quantity'] = -1
        form = ThingForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    # Form accepts form with quantity 0 and above
    def test_form_accepts_quantity_zero_or_above(self):
        self.form_input['quantity'] = 0
        form = ThingForm(data=self.form_input)
        self.assertTrue(form.is_valid())

    # Form has correct fields
    def test_form_has_correct_fields(self):
        form = ThingForm()
        self.assertIn('name', form.fields)
        self.assertIn('quantity', form.fields)