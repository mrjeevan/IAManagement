from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from django.urls import reverse_lazy
# Create your views here.
from django.contrib.auth import authenticate, login


def home(request):

    context = {
        'outstanding' : IAmark.objects.filter(average_marks = 30).count(),
        'execelent' : IAmark.objects.filter(average_marks__gte=20, average_marks__lte = 29).count(),
        'average' : IAmark.objects.filter(average_marks__gte=14,average_marks__lt=20).count(),
        'improve' : IAmark.objects.filter(average_marks__gte=0,average_marks__lt=14).count()
    }
    return render(request,'home.html',context)
############

class AddStudent(CreateView):
    model = Student
    template_name = "addstudent.html"
    form_class = AddStudentForm
    success_url = reverse_lazy('management:students')
    
class StudentView(ListView):
    model = Student
    template_name = "student.html"

class DeleteStudent(DeleteView):
    model = Student
    success_url =reverse_lazy('management:students')
    template_name = "delete.html"

class UpdateStudent(UpdateView):
    model = Student
    fields = '__all__'
    success_url =reverse_lazy('management:students')
    template_name = "update.html"
#####################
class AddSemsec(CreateView):
    model = SemSec
    template_name = "addsemsec.html"
    form_class = AddSemsecForm
    success_url = reverse_lazy('management:semsec')

class SemsecView(ListView):
    model = SemSec
    template_name = "semsec.html"

class DeleteSemsec(DeleteView):
    model = SemSec
    success_url = reverse_lazy('management:semsec')
    template_name = "delete.html"

class UpdateSemsec(UpdateView):
    model = SemSec
    fields = '__all__'
    success_url = reverse_lazy('management:semsec')
    template_name = "update.html"
########################
class AddSubject(CreateView):
    model = Subject
    template_name = "addsubject.html"
    form_class = AddSubjectForm
    success_url = reverse_lazy('management:subject')

class SubjectView(ListView):
    model = Subject
    template_name = "subject.html"


class DeleteSubject(DeleteView):
    model = Subject
    success_url = reverse_lazy('management:subject')
    template_name = "delete.html"

class UpdateSubject(UpdateView):
    model = Subject
    fields = '__all__'
    success_url = reverse_lazy('management:subject')
    template_name = "update.html"
#####################
class Addmarks(CreateView):
    model = IAmark
    template_name = "addmarks.html"
    form_class = AddmarksForm
    success_url = reverse_lazy('management:marks')

class MarksView(ListView):
    model = IAmark
    template_name = "marks.html"
    
    var1 = Subject.objects.all()
    var2 = IAmark.objects.all()
    def get(self, request, *args, **kwargs):
        context = {
        'var1' : self.var1,
        'var2' : self.var2
        }
        return render(request,self.template_name, context)

class DeleteMarks(DeleteView):
    model = IAmark
    success_url = reverse_lazy('management:marks')
    template_name = "delete.html"

class UpdateMarks(UpdateView):
    model = IAmark
    fields = '__all__'
    success_url = reverse_lazy('management:marks')
    template_name = "update.html"
##################
class AddFaculty(CreateView):
    model = Faculty
    template_name = "addfaculty.html"
    form_class = AddFacultyForm
    success_url = reverse_lazy('management:faculty')

class FacultyView(ListView):
    model = Faculty
    template_name = "faculty.html"

class DeleteFaculty(DeleteView):
    model = Faculty
    success_url =reverse_lazy('management:faculty')
    template_name = "delete.html"

class UpdateFaculty(UpdateView):
    model = Faculty
    fields = '__all__'
    success_url =reverse_lazy('management:faculty')
    template_name = "update.html"
#################
class AddIncharge(CreateView):
    model = Incharge
    template_name = "addincharge.html"
    form_class = AddInchargeForm
    success_url = reverse_lazy('management:incharge')

class InchargeView(ListView):
    model = Incharge
    template_name = "incharge.html"

class DeleteIncharge(DeleteView):
    model = Incharge
    success_url = reverse_lazy('management:incharge')
    template_name = "delete.html"

class UpdateIncharge(UpdateView):
    model = Incharge
    fields = '__all__'
    success_url =reverse_lazy('management:incharge')
    template_name = "update.html"
####################
def Outstanding(request):
    context = {
        'object_list' : IAmark.objects.filter(average_marks = 30),
    }
    return render(request,'outstanding.html',context)
####################
def Execelent(request):
    context = {
        'object_list' : IAmark.objects.filter(average_marks__gte=20, average_marks__lte = 29)
    }
    return render(request,'execelent.html',context)
####################
def Average(request):
    context = {
        'object_list' : IAmark.objects.filter(average_marks__gte=14,average_marks__lt=20)
    }
    return render(request,'average.html',context)
####################
def Improve(request):
    context = {
        'object_list' : IAmark.objects.filter(average_marks__gte=0,average_marks__lt=14)
    }
    return render(request,'improve.html',context)
################### Extra
def Upgrade(request):
    ERROR = 0
    SEM = SemSec.objects.all()
    Sub = Subject.objects.all()
    Stu = Student.objects.all()
    INTER = ['IA1','IA2','IA3']
    for Sem in SEM:
        for sub in Sub:
            for stu in Stu:
                for ia in INTER:
                    print(Sem.sem,sub.subcode,stu.usn,ia)
                    x = IAmark()
                    x.usn = stu
                    x.sub_code = sub
                    x.sem = Sem
                    x.internals = ia
                    try:
                        x.save()
                    except :
                        ERROR +=1
                        pass
    return HttpResponse(f'Automated update Success [{ERROR}]')


def marksubview(request,pk):
   
    context = {
        'var2' : IAmark.objects.filter(sub_code = pk),
        
    }
    return render(request,'marks.html',context)