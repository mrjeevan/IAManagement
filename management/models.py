from django.db import models

# Create your models here.

class Student(models.Model):

    usn = models.CharField(max_length=10,null = False,unique=True)
    name = models.CharField( max_length=15,null =False)
    address = models.CharField(max_length=50,null = False)
    phno = models.CharField(max_length=12,null = False)
    GENDER = (
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other'),
    )
    gender = models.CharField(max_length=6,null = False,choices = GENDER)
    class Meta:
        ordering = ["usn"]
    def __str__(self):
        return f'{self.name}'

class SemSec(models.Model):
    SEM = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
    )
    sem = models.CharField(max_length=1,null =False, choices = SEM,unique=True)
    # section = models.CharField(max_length=50,null =False)
    usn = models.ManyToManyField(Student, verbose_name='Students')

    def get_usn_values(self):

        ret = ''

        print(self.usn.all())

        # use models.ManyToMany field's all() method to return all the Department objects that this employee belongs to.
        for usn in self.usn.all():
            ret = ret + usn.usn + ','

        # remove the last ',' and return the value.
        return ret[:-1]

    def __str__(self):
        return f'[{self.sem}]'


class Subject(models.Model):
    SEM = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
    )
    subcode = models.CharField(max_length=10,null=False,unique=True)
    title = models.CharField(max_length=50,null=False)
    sem = models.CharField(max_length=1,null =False, choices = SEM)
    credit = models.PositiveIntegerField(default=20,null = False)

    def __str__(self):
        return f'{self.title}({self.subcode})'



class IAmark(models.Model):
    INTER = (
        ('IA1','IA1'),
        ('IA2','IA2'),
        ('IA3','IA3'),
    )
    ispresent = models.BooleanField(default=True,verbose_name = "Present / Absent")
    usn = models.ForeignKey(Student, on_delete=models.CASCADE,verbose_name = "Student")
    sub_code = models.ForeignKey(Subject, on_delete=models.CASCADE,verbose_name = "Subject code")
    sem = models.ForeignKey(SemSec, verbose_name='Semister', on_delete=models.CASCADE)
    internals = models.CharField(max_length=3,null =False, choices = INTER)
    a1 = models.PositiveIntegerField(verbose_name="1a",default=0)
    a2 = models.PositiveIntegerField(verbose_name="1b",default=0)
    a3 = models.PositiveIntegerField(verbose_name="1c",default=0)
    b1 = models.PositiveIntegerField(verbose_name="2a",default=0)
    b2 = models.PositiveIntegerField(verbose_name="2b",default=0)
    b3 = models.PositiveIntegerField(verbose_name="2c",default=0)
    c1 = models.PositiveIntegerField(verbose_name="3a",default=0)
    c2 = models.PositiveIntegerField(verbose_name="3b",default=0)
    c3 = models.PositiveIntegerField(verbose_name="3c",default=0)
    d1 = models.PositiveIntegerField(verbose_name="4a",default=0)
    d2 = models.PositiveIntegerField(verbose_name="4b",default=0)
    d3 = models.PositiveIntegerField(verbose_name="4c",default=0)
    total_marks = models.PositiveIntegerField(default=0,verbose_name = "Total")
    assignment = models.PositiveIntegerField(default=0,verbose_name = "Assignment")
    average_marks = models.PositiveIntegerField(default=0,verbose_name = "Average")
    finial_marks = models.PositiveIntegerField(default=0,verbose_name = "Finial")
    
    class Meta:
        unique_together = (('usn', 'sub_code','internals'),)

    def save(self):
        self.total_marks = max((self.a1+self.a2+self.a3),(self.b1+self.b2+self.b3))+ max((self.c1+self.c2+self.c3),(self.d1+self.d2+self.d3))
        self.average_marks = self.total_marks/3
        self.finial_marks = self.average_marks + self.assignment
        return super(IAmark, self).save()

    def __str__(self):
        return f'{self.usn}'

class Faculty(models.Model):
    Fid = models.CharField(max_length=10,null =False,verbose_name = "Faculty ID")
    Name = models.CharField( max_length=15,null =False)
    SPEC = (
        ('AI/ML','AI/ML'),
        ('CSE','CSE'),
        ('CyberSecurity','CyberSecurity'),
        ('Networking','Networking'),
        ('Languages','Languages'),
        ('DBMS','DBMS'),
        ('Management','Management'),
        ('Basic Science','Basic Science'),
        ('Physical Edu','Physical Edu'),
        ('Electronics','Electronics'),
        ('Other','Other'),
    )
    specialization = models.CharField( max_length=25,null =False,choices = SPEC,verbose_name = "Specilised in ")
    subject = models.ManyToManyField(Subject, verbose_name="Subject")
    def __str__(self):
        return self.Name
    

class Incharge(models.Model):
    cr1 = models.ForeignKey(Student, on_delete=models.SET_NULL,null =True,related_name='cr1',verbose_name = "CR 1")
    cr2 = models.ForeignKey(Student, on_delete=models.SET_NULL,null =True,related_name='cr2',verbose_name = "CR 2")
    class_cordinator = models.ForeignKey(Faculty,on_delete=models.SET_NULL,null =True,related_name='class_cord')
    sem_cordinator = models.ForeignKey(Faculty,on_delete=models.SET_NULL,null =True,related_name='sem_cord')
    classroom = models.ForeignKey(SemSec,on_delete=models.CASCADE,null =False)
    def __str__(self):
        return f'{self.class_cordinator}'
