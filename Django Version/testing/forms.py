from django import forms
from django_range_slider.fields import RangeSliderField
from .models import Sliders

class SliderForm(forms.Form):
    slider1 = RangeSliderField(minimum=30,maximum=300,name="TestName")
    class Meta:
        model = Sliders
        fields = ('slider1')
