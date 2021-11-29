from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField

class Clinic(models.Model):
    CANADA = 'CA'
    INDIA = 'IN'
    PHONECODE_CHOICES = [
        (CANADA, '+1'),
        (INDIA, '+91'),
    ]
    # address
    clinic_name = models.CharField(max_length=50)
    address_line_one = models.CharField(max_length=100)
    address_line_two = models.CharField(max_length=100)

    postal_code = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    provinces = models.CharField(max_length=50)

    phone_code = models.CharField(max_length=5, choices=PHONECODE_CHOICES, default=CANADA)
    phone_number = models.CharField(max_length=10)
    # website
    website = models.CharField(max_length=500,  blank=True)
    # opening time 
    opening_time = models.TimeField()
    # closing time
    closing_time = models.TimeField()
    # class Vaccine obj

    def __str__(self):
        return self.clinic_name

class Vaccine(models.Model):
    ModernaVaccine = 'MV'
    PfizerVaccine = 'PV'
    JAJVaccine = 'JV'
    AstrazenecaVaccine = 'AV'
    VACCINE_CHOICES = [
        (ModernaVaccine, 'Moderna vaccine'),
        (PfizerVaccine, 'Pfizer vaccine'),
        (JAJVaccine, 'Johnson and Johnson vaccine'),
        (AstrazenecaVaccine, 'Astrazeneca vaccine'),
    ]
    vaccine_for = models.CharField(max_length=500)
    # vacine name
    vaccine_name = models.CharField(max_length=2, choices=VACCINE_CHOICES)
    # is_avaliable
    is_available = models.BooleanField(default=True)
    # quantity
    quantity = models.PositiveIntegerField()

    clinic = models.ForeignKey('Clinic', on_delete=models.CASCADE)


    def __str__(self):
        # return self.get_vaccine_name_display()
        return self.vaccine_for + " " + self.vaccine_name + " " + str(self.quantity)


class UserAppointBooking(models.Model):
    CANADA = 'CA'
    INDIA = 'IN'
    PHONECODE_CHOICES = [
        (CANADA, '+1'),
        (INDIA, '+91'),
    ]
    ModernaVaccine = 'MV'
    PfizerVaccine = 'PV'
    JAJVaccine = 'JV'
    AstrazenecaVaccine = 'AV'
    VACCINE_CHOICES = [
        (ModernaVaccine, 'Moderna vaccine'),
        (PfizerVaccine, 'Pfizer vaccine'),
        (JAJVaccine, 'Johnson and Johnson vaccine'),
        (AstrazenecaVaccine, 'Astrazeneca vaccine'),
    ]

    FIRST = 'FD'
    SECOND = 'SD'
    DOSE_CHOICES = [
        (FIRST, 'First Dose'),
        (SECOND, 'Second Dose'),
    ]

    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    ]
    # firts_name
    first_name = models.CharField(max_length=50)
    # last_name
    last_name = models.CharField(max_length=50)
    # user_address
    address_line_one = models.CharField(max_length=100)
    address_line_two = models.CharField(max_length=100)

    postal_code = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    provinces = models.CharField(max_length=50)
    # DOB
    DOB = models.DateField()
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1)
    # phone number
    phone_code = models.CharField(max_length=5, choices=PHONECODE_CHOICES, default=CANADA)
    phone_number = models.CharField(max_length=10)
    # Health card (image)
    health_card = models.ImageField(upload_to='images/')
    # which_dose (1st, 2nd)
    which_dose = models.CharField(max_length=2, choices=DOSE_CHOICES)
    # vaccine name
    vaccine_name = models.CharField(choices=VACCINE_CHOICES, max_length=2)

    # date when user will get his/her vaccine
    # time of the day
    choose_date = models.DateTimeField()
    got_dose = models.BooleanField(default=False)
    mossed_dose = models.BooleanField(null=True, blank=True)

    #FOR LANDING PAGE
    # what you must bring alongwith you while visiting pharmacy or vaccine centre (mandatory things 1)

    # Services(2)
    # Doctor information(3) 
    # About pharmacy ambience or environment (4)
    # Donation box(money, blood, clothes and food) (4)






