from django import forms
import datetime

class DonationReceiptForm(forms.Form):
    fullName = forms.CharField(label="Full Name", max_length=100)
    email = forms.CharField(label="Email", max_length=100)
    mobile = forms.CharField(label="Mobile", max_length=15)
    date = forms.DateField(label="Date", initial=datetime.date.today)
    channel = forms.CharField(label="Channel", max_length=100)
    amount = forms.CharField(label = "Amount")



