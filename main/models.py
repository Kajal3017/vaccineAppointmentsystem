from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class BookingFormINFO(models.Model):
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
    phone_number = models.PositiveIntegerField(validators=[MaxValueValidator(10)])
    # website
    website = models.CharField(max_length=500,  blank=True)
    # opening time 
    opening_time = models.TimeField()
    # closing time
    closing_time = models.TimeField()
    # class Vaccine obj
    vaccine = models.ForeignKey('Vaccine', on_delete=models.CASCADE)

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
    # vacine name
    vaccine_name = models.CharField(max_length=2, choices=VACCINE_CHOICES)
    # is_avaliable
    is_available = models.BooleanField(default=True)
    # quantity
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.vaccine_name + " " + str(self.quantity)


# class UserBooking(models.Model):
#     FIRSTDOSE = 'FD'
#     SECOUNDOSE = 'SD'
#     DOSE_CHOICES = [
#         (FIRSTDOSE, 'First Dose'),
#         (SECOUNDOSE, 'Last Dose'),
#     ]
#     year_in_school = models.CharField(
#         max_length=2,
#         choices=YEAR_IN_SCHOOL_CHOICES,
#         default=FRESHMAN,
#     )
#     # firts_name
#     first_name = models.CharField(max_length=50)
#     # last_name
#     last_name = models.CharField(max_length=50)
#     # user_address
#     address = models.CharField(max_length=100)
#     # DOB
#     DOB = models.DateField()
#     # phone number
#     phone_number = models.PositiveIntegerField()
#     # Health card (image)
#     health_card = models.ImageField()
#     # which_dose (1st, 2nd)
#     which_dose = models.CharField(max_length=2, choices=DOSE_CHOICES)
#     # vaccine name
#     vaccine_name = models.CharField()

#     # date when user will get his/her vaccine
#     # time of the day

#     #FOR LANDING PAGE
#     # what you must bring alongwith you while visiting pharmacy or vaccine centre (mandatory things 1)

#     # Services(2)
#     # Doctor information(3) 
#     # About pharmacy ambience or environment (4)
#     # Donation box(money, blood, clothes and food) (4)






