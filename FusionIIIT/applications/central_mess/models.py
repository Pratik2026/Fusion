import datetime
from django.db import models
from applications.academic_information.models import (Student, Holiday)

# Create your models here.
LEAVE_TYPE = (
    ('casual', 'Casual'),
    ('vacation', 'Vacation')
)

SPECIAL_FOOD = (
    ('dal_chawal', 'Dal Chawal'),
    ('khicdi', 'Khicdi'),
    ('tomato_soup','Tomato Soup')
)

MEAL_TIME = (
    ('breakfast', 'Breakfast'),
    ('lunch', 'Lunch'),
    ('dinner','Dinner')
)

MEAL = (
    ('MB', 'Monday Breakfast'),
    ('ML', 'Monday Lunch'),
    ('MD', 'Monday Dinner'),
    ('TB', 'Tuesday Breakfast'),
    ('TL', 'Tuesday Lunch'),
    ('TD', 'Tuesday Dinner'),
    ('WB', 'Wednesday Breakfast'),
    ('WL', 'Wednesday Lunch'),
    ('WD', 'Wednesday Dinner'),
    ('THB', 'Thursday Breakfast'),
    ('THL', 'Thursday Lunch'),
    ('THD', 'Thursday Dinner'),
    ('FB', 'Friday Breakfast'),
    ('FL', 'Friday Lunch'),
    ('FD', 'Friday Dinner'),
    ('SB', 'Saturday Breakfast'),
    ('SL', 'Saturday Lunch'),
    ('SD', 'Saturday Dinner'),
    ('SUB', 'Sunday Breakfast'),
    ('SUL', 'Sunday Lunch'),
    ('SUD', 'Sunday Dinner')
)

STATUS = (
    ('0', 'rejected'),
    ('1', 'pending'),
    ('2', 'accepted')
)

TIME = (
    ('10', '10 a.m.'),
    ('11', '11 a.m.'),
    ('12', '12 p.m.'),
    ('13', '1 p.m.'),
    ('14', '2 p.m.'),
    ('15', '3 p.m.'),
    ('16', '4 p.m.'),
    ('17', '5 p.m.'),
    ('18', '6 p.m.'),
    ('19', '7 p.m.'),
    ('20', '8 p.m.'),
    ('21', '9 p.m.')
)

FEEDBACK_TYPE = (
    ('maintenance', 'Maintenance'),
    ('food', 'Food'),
    ('cleanliness', 'Cleanliness & Hygiene'),
    ('others', 'Others')
)

MONTHS = (
    ('Jan', 'January'),
    ('Feb', 'February'),
    ('Mar', 'March'),
    ('Apr', 'April'),
    ('May', 'May'),
    ('Jun', 'June'),
    ('Jul', 'July'),
    ('Aug', 'August'),
    ('Sep', 'September'),
    ('Oct', 'October'),
    ('Nov', 'November'),
    ('Dec', 'December')

)

INTERVAL = (
    ('Breakfast', 'Breakfast'),
    ('Lunch', 'Lunch'),
    ('Dinner', 'Dinner')
)

MESS_OPTION = (
    ('mess1', 'Mess1'),
    ('mess2', 'Mess2')
)


class Messinfo(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    mess_option = models.CharField(max_length=20, choices=MESS_OPTION,
                                   default='mess2')

    class Meta:
        unique_together = (('student_id', 'mess_option'),)

    def __str__(self):
        return '{} - {}'.format(self.student_id.id, self.mess_option)


class Mess_reg(models.Model):
    sem = models.IntegerField(default='1')
    start_reg = models.DateField(default=datetime.date.today)
    end_reg = models.DateField(default=datetime.date.today)


class MessBillBase(models.Model):
    bill_amount = models.PositiveIntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)


def current_month():
    return datetime.datetime.now().strftime("%B")


def current_year():
    return datetime.datetime.now().strftime("%Y")


class Monthly_bill(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    month = models.CharField(max_length=20, default=current_month)
    year = models.IntegerField(default=current_year)
    amount = models.IntegerField(default=0)
    rebate_count = models.IntegerField(default=0)
    rebate_amount = models.IntegerField(default=0)
    # nonveg_total_bill = models.IntegerField(default=0)
    total_bill = models.IntegerField(default=0)
    paid = models.BooleanField(default=False)

    class Meta:
        unique_together = (('student_id', 'month', 'year'),)

    def __str__(self):
        return '{} - {} - {}'.format(self.student_id.id, self.month, self.year)


class Payments(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount_paid = models.IntegerField(default=0)
    payment_month = models.CharField(max_length=20, default=current_month)
    payment_year = models.IntegerField(default = current_year)
    payment_date = models.DateField(default= datetime.date.today)

    # class Meta:
    #     unique_together = (('student_id',  'payment_date'))

    def __str__(self):
        return '{}'.format(self.student_id.id)


class Menu(models.Model):
    mess_option = models.CharField(max_length=20, choices=MESS_OPTION,
                                   default='mess2')
    meal_time = models.CharField(max_length=20, choices=MEAL)
    dish = models.CharField(max_length=200)

    def __str__(self):
        return '{} - {} - {}'.format(self.mess_option,
                                     self.meal_time, self.dish)


class Rebate(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(default=datetime.date.today)
    purpose = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS, default='1')
    app_date = models.DateField(default=datetime.date.today)
    # TODO = remove leave type
    leave_type = models.CharField(choices=LEAVE_TYPE, max_length=20, default="casual")
    # leave_document = models.FileField(upload_to='central_mess/')
    rebate_remark = models.CharField(max_length=50,default='NA')
    def __str__(self):
        return str(self.student_id.id)


class Vacation_food(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(default=datetime.date.today)
    purpose = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS, default='1')
    app_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return str(self.student_id.id)


# class Nonveg_menu(models.Model):
#     dish = models.CharField(max_length=20)
#     price = models.IntegerField()
#     order_interval = models.CharField(max_length=20, choices=INTERVAL,
#                                       default='Breakfast')

#     def __str__(self):
#         return '{} - {}'.format(self.dish, self.price)


# class Nonveg_data(models.Model):
#     student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
#     order_date = models.DateField(default=datetime.date.today)
#     order_interval = models.CharField(max_length=20, choices=INTERVAL,
#                                       default='Breakfast')
#     dish = models.ForeignKey(Nonveg_menu, on_delete=models.CASCADE)
#     app_date = models.DateField(default=datetime.date.today)

#     def __str__(self):
#         return str(self.student_id.id)


class Special_request(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(default=datetime.date.today)
    request = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS, default='1')
    item1 = models.CharField(choices = SPECIAL_FOOD, max_length=50, default ='dal_chawal')
    item2 = models.CharField(choices = MEAL_TIME, max_length=50, default ='breakfast')
    app_date = models.DateField(default=datetime.date.today)
    # special_food = models.CharField(choices = SPECIAL_FOOD, max_length = 50)

    def __str__(self):
        return str(self.student_id.id)


class Mess_meeting(models.Model):
    meet_date = models.DateField()
    agenda = models.TextField()
    venue = models.TextField()
    meeting_time = models.CharField(max_length=20, choices=TIME)

    def __str__(self):
        return '{} - {}'.format(self.meet_date, self.agenda)


class Mess_minutes(models.Model):
    meeting_date = models.OneToOneField(Mess_meeting, on_delete=models.CASCADE)
    mess_minutes = models.FileField(upload_to='central_mess/')

    def __str__(self):
        return '{} - {}'.format(self.meeting_date.meet_date, self.mess_minutes)


class Menu_change_request(models.Model):
    dish = models.ForeignKey(Menu, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    reason = models.TextField()
    request = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS, default='1')
    app_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return '{} - {} - {} - {}'.format(self.id, self.dish, self.request, self.status)


class Feedback(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    mess = models.CharField(max_length=10, choices=MESS_OPTION, default='mess1')
    mess_rating = models.PositiveSmallIntegerField(default='5')
    fdate = models.DateField(default=datetime.date.today)
    description = models.TextField()
    feedback_type = models.CharField(max_length=20, choices=FEEDBACK_TYPE)
    feedback_remark = models.CharField(max_length=50, default ="NA")
    def __str__(self):
        return str(self.student_id.id)


class Registration_Request(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    Txn_no =models.CharField(max_length=20)
    img = models.ImageField(upload_to='mess/images/registration_request/%Y/%m/%d/',default=None)
    amount=models.IntegerField(default=0)
    status=models.CharField(max_length=10,default='pending')
    registration_remark=models.CharField(max_length=50,default='NA')
    start_date=models.DateField(default=None, null=True)
    # end_date=models.DateField(default=None, null=True)
    payment_date= models.DateField(default=None, null=True)
    def __str__(self):
        return str(self.student_id.id)        

class Reg_main(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    program = models.CharField(max_length=10)
    current_mess_status = models.CharField(max_length=20,default='Deregistered') 
    balance = models.IntegerField(default=0)
    mess_option = models.CharField(max_length=20,default='mess2')
    def __str__(self):
        return str(self.student_id.id)
class Reg_records(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(default=None, null=True)
    def __str__(self):
        return str(self.student_id.id)
    
class Deregistration_Request(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    status=models.CharField(max_length=10,default='pending')
    deregistration_remark=models.CharField(max_length=50,default='NA')
    end_date = models.DateField(default=None, null=True)
    def __str__(self):
        return str(self.student_id.id) 

class Semdates(models.Model):
    start_date = models.DateField(blank=False,default=datetime.date.today)
    end_date = models.DateField(blank=False,default=datetime.date.today)
    class Meta:
        unique_together = (('start_date', 'end_date'),)


class Update_Payment(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    Txn_no =models.CharField(max_length=20)
    img = models.ImageField(upload_to='images/',default=None)
    amount=models.IntegerField(default=0)
    status=models.CharField(max_length=10,default='pending')
    update_remark=models.CharField(max_length=50,default='NA')
    payment_date= models.DateField(default=None, null=True)
    def __str__(self):
        return str(self.student_id.id)
    