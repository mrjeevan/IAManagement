from django.urls import path,include
from .views import *
from . import views
import re
app_name = 'management'

urlpatterns = [
    path('',views.home, name='home'),
    path("addstudent/",AddStudent.as_view(),name='addstudent' ),
    path("student/",StudentView.as_view(),name="students"),
    path('student/<pk>/delete/', DeleteStudent.as_view()), 
    path('student/<pk>/update/', UpdateStudent.as_view()), 
#############################################################
    path("addsemsec/",AddSemsec.as_view(),name="addsemsec"),
    path("semsec/",SemsecView.as_view(),name="semsec"),
    path('semsec/<pk>/delete/', DeleteSemsec.as_view()), 
    path('semsec/<pk>/update/', UpdateSemsec.as_view()),
#############################################################
    path("addsubject/",AddSubject.as_view(),name="addsubject"),
    path("subject/",SubjectView.as_view(),name = "subject"),
    path('subject/<pk>/delete/', DeleteSubject.as_view()), 
    path('subject/<pk>/update/', UpdateSubject.as_view()),
#############################################################
    path("addmarks/",Addmarks.as_view(),name = "addmarks"),
    path("marks/",MarksView.as_view(),name = "marks"),
    path('marks/<str:pk>/', views.marksubview),
    path('marks/<pk>/delete/', DeleteMarks.as_view()), 
    path('marks/<pk>/update/', UpdateMarks.as_view()),
#############################################################
    path("addfaculty/",AddFaculty.as_view(),name="addfaculty"),
    path("faculty/",FacultyView.as_view(),name = "faculty"),
    path('faculty/<pk>/delete/', DeleteFaculty.as_view()), 
    path('faculty/<pk>/update/', UpdateFaculty.as_view()),
#############################################################
    path("addincharge/",AddIncharge.as_view(),name="addincharge"),
    path("incharge/",InchargeView.as_view(),name = "incharge"),
    path('incharge/<pk>/delete/', DeleteIncharge.as_view()), 
    path('incharge/<pk>/update/', UpdateIncharge.as_view()),
###################################  EXTRA  #################
    path('Outstanding',views.Outstanding, name='Outstanding'),
    path('Execelent',views.Execelent, name='Execelent'),
    path('Average',views.Average, name='Average'),
    path('Improve',views.Improve, name='Improve'),
#####################
    path('Upgrade',views.Upgrade, name='Upgrade'), 
####################
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'), 
]