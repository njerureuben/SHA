from django import forms
from .models import Appointment, Contact


class AppointmentForm(forms.ModelForm):
    DEPARTMENT_CHOICES = [
        ('Cardiology Department', 'Cardiology'),
        ('Pediatrics Department', 'Pediatrics'),
        ('Orthopedics Department', 'Orthopedics'),
    ]

    DOCTOR_CHOICES = [
        ('Dr. Wanjiru Kamau', 'Dr. Wanjiru Kamau'),
        ('Dr. Otieno Onyango', 'Dr. Otieno Onyango'),
        ('Dr. Achieng Oduor', 'Dr. Achieng Oduor'),
    ]

    department = forms.ChoiceField(
        choices=DEPARTMENT_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
    doctor = forms.ChoiceField(
        choices=DOCTOR_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = Appointment
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'description':forms.Textarea(attrs={'class': 'form-control','placeholder': 'Message (Optional)'}),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'contactName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'contactEmail': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'contactSubject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}),
            'contactMessage':forms.Textarea(attrs={'class': 'form-control','placeholder': 'Message (Optional)'}),
        }
