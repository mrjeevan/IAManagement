from django.contrib.auth.decorators import * 
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import DetailView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin


def home(request):
    context = {
        'outstanding' : IAmark.objects.filter(average_marks = 30).count(),
        'execelent' : IAmark.objects.filter(average_marks__gte=20, average_marks__lte = 29).count(),
        'average' : IAmark.objects.filter(average_marks__gte=14,average_marks__lt=20).count(),
        'improve' : IAmark.objects.filter(average_marks__gte=0,average_marks__lt=14).count()
    }
    return render(request,'home.html',context)
############

class AddStudent(LoginRequiredMixin,CreateView):
    model = Student
    template_name = "addstudent.html"
    form_class = AddStudentForm
    success_url = reverse_lazy('management:students')
    
class StudentView(LoginRequiredMixin,ListView):
    model = Student
    template_name = "student.html"


class DeleteStudent(LoginRequiredMixin,DeleteView):
    
    model = Student
    success_url =reverse_lazy('management:students')
    template_name = "delete.html"

class UpdateStudent(LoginRequiredMixin,UpdateView):
    model = Student
    fields = '__all__'
    success_url =reverse_lazy('management:students')
    template_name = "update.html"
#####################
class AddSemsec(LoginRequiredMixin,CreateView):
    model = SemSec
    template_name = "addsemsec.html"
    form_class = AddSemsecForm
    success_url = reverse_lazy('management:semsec')

class SemsecView(LoginRequiredMixin,ListView):
    model = SemSec
    template_name = "semsec.html"

class DeleteSemsec(LoginRequiredMixin,DeleteView):
    model = SemSec
    success_url = reverse_lazy('management:semsec')
    template_name = "delete.html"

class UpdateSemsec(LoginRequiredMixin,UpdateView):
    model = SemSec
    fields = '__all__'
    success_url = reverse_lazy('management:semsec')
    template_name = "update.html"
########################
class AddSubject(LoginRequiredMixin,CreateView):
    model = Subject
    template_name = "addsubject.html"
    form_class = AddSubjectForm
    success_url = reverse_lazy('management:subject')

class SubjectView(LoginRequiredMixin,ListView):
    model = Subject
    template_name = "subject.html"


class DeleteSubject(LoginRequiredMixin,DeleteView):
    model = Subject
    success_url = reverse_lazy('management:subject')
    template_name = "delete.html"

class UpdateSubject(LoginRequiredMixin,UpdateView):
    model = Subject
    fields = '__all__'
    success_url = reverse_lazy('management:subject')
    template_name = "update.html"
#####################
class Addmarks(LoginRequiredMixin,CreateView):
    model = IAmark
    template_name = "addmarks.html"
    form_class = AddmarksForm
    success_url = reverse_lazy('management:marks')

class MarksView(LoginRequiredMixin,ListView):
    model = IAmark
    template_name = "marks.html"

    # var1 = Subject.objects.filter(usn=users.username) # original
    var1 = Subject.objects.all()
    var2 = IAmark.objects.all()



    def get(self, request, *args, **kwargs):
        context = {
        'var1' : self.var1,
        'var2' : self.var2
        }
        return render(request,self.template_name, context)

class DeleteMarks(LoginRequiredMixin,DeleteView):
    model = IAmark
    success_url = reverse_lazy('management:marks')
    template_name = "delete.html"

class UpdateMarks(LoginRequiredMixin,UpdateView):
    model = IAmark
    fields = '__all__'
    success_url = reverse_lazy('management:marks')
    template_name = "update.html"
##################
class AddFaculty(LoginRequiredMixin,CreateView):
    model = Faculty
    template_name = "addfaculty.html"
    form_class = AddFacultyForm
    success_url = reverse_lazy('management:faculty')

class FacultyView(LoginRequiredMixin,ListView):
    model = Faculty
    template_name = "faculty.html"

class DeleteFaculty(LoginRequiredMixin,DeleteView):
    model = Faculty
    success_url =reverse_lazy('management:faculty')
    template_name = "delete.html"

class UpdateFaculty(LoginRequiredMixin,UpdateView):
    model = Faculty
    fields = '__all__'
    success_url =reverse_lazy('management:faculty')
    template_name = "update.html"
#################
class AddIncharge(LoginRequiredMixin,CreateView):
    model = Incharge
    template_name = "addincharge.html"
    form_class = AddInchargeForm
    success_url = reverse_lazy('management:incharge')

class InchargeView(LoginRequiredMixin,ListView):
    model = Incharge
    template_name = "incharge.html"

class DeleteIncharge(LoginRequiredMixin,DeleteView):
    model = Incharge
    success_url = reverse_lazy('management:incharge')
    template_name = "delete.html"

class UpdateIncharge(LoginRequiredMixin,UpdateView):
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

####### login / logout ##

def login_page(request):
    forms = LoginForm()
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect( 'management:home' )

    context = {'form': forms}
    return render(request, 'users/login.html', context)


def logout_page(request):
    logout(request)
    return redirect('login')

################### Extra

@permission_required('management.Upgrade') 
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