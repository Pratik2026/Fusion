from audioop import reverse
import json

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from django.conf import settings
from django.utils import timezone
from PIL import Image

from applications.academic_information.models import Student
from applications.globals.forms import IssueForm, WebFeedbackForm
from applications.globals.models import (ExtraInfo, Feedback, HoldsDesignation,
                                         Issue, IssueImage, DepartmentInfo,ModuleAccess)
from applications.gymkhana.views import coordinator_club
from applications.placement_cell.forms import (AddAchievement, AddCourse,
                                               AddEducation, AddExperience,
                                               AddPatent, AddProfile,
                                               AddProject, AddPublication,
                                               AddSkill)
from applications.placement_cell.models import (Achievement, Course, Education,
                                                Experience, Has, Patent,
                                                Project, Publication, Skill, PlacementStatus)
from Fusion.settings.common import LOGIN_URL
from notifications.models import Notification
from .models import *
from applications.hostel_management.models import (HallCaretaker,HallWarden)
from notification.views import announcement_list

def index(request):
    context = {}
    if(str(request.user)!="AnonymousUser"):
        return HttpResponseRedirect('/dashboard/')
    else:
        return render(request, "globals/index1.html", context)

# Reset all passwords to 'user@123' in DEV environment
def reset_all_pass(request):
    if settings.ALLOW_PASS_RESET:
        UserMod = get_user_model()
        arr = UserMod.objects.all()
        for e in arr:
            print(e.username)
            u = User.objects.get(username=e.username)
            u.set_password('user@123')
            u.save()
        context = {"done": len(arr)}
        return HttpResponse(json.dumps(context), "application/json")
    else:
        return HttpResponseNotFound("Not allowed")


@login_required(login_url=LOGIN_URL)
def about(request):
    teams = {
        'uiTeam': {
            'teamId': "uiTeam",
            'teamName': "Frontend Team",
        },

        'qaTeam': {
            'teamId': "qaTeam",
            'teamName': "Quality Analysis Team",
        },

        'academics_a_Team': {
            'teamId': "academics_a_Team",
            'teamName': "Academics (A) Module Team",
        },

        'academics_b_Team': {
            'teamId': "academics_b_Team",
            'teamName': "Academics (B) Module Team",
        },

        'spacsTeam': {
            'teamId': "spacsTeam",
            'teamName': "Awards & Scholarship Module Team",
        },

        'messTeam': {
            'teamId': "messTeam",
            'teamName': "Central Mess Module Team",
        },

        'complaintTeam': {
            'teamId': "complaintTeam",
            'teamName': "Complaint Module Team",
        },

        'eisTeam': {
            'teamId': "eisTeam",
            'teamName': "EIS Module Team",
        },

        'filetrackingTeam': {
            'teamId': "filetrackingTeam",
            'teamName': "File Tracking Module Team",
        },

        'gymkhanaTeam': {
            'teamId': "gymkhanaTeam",
            'teamName': "Gymkhana Module Team",
        },

        'leaveTeam': {
            'teamId': "leaveTeam",
            'teamName': "Leave Module Team",
        },

        'phcTeam': {
            'teamId': "phcTeam",
            'teamName': "Primary Health Center Module Team",
        },

        'placementTeam': {
            'teamId': "placementTeam",
            'teamName': "Placement Module Team",
        },

        'vhTeam': {
            'teamId': "vhTeam",
            'teamName': "Visitors Hostel Module Team",
        },
    }

    context = {'teams': teams,
               'psgTeam': {
                   'dev1': {'devName': 'Anuraag Singh',
                            'devImage': 'team/2015043.jpeg',
                            'devTitle': 'Developer'
                            },

                   'dev2': {'devName': 'Kanishka Munshi',
                            'devImage': 'team/2015121.jpg',
                            'devTitle': 'Head UI Developer'
                            },

                   'dev3': {'devName': 'M. Arshad Siddiqui',
                            'devImage': 'team/2015153.jpg',
                            'devTitle': 'Database Designer'
                            },

                   'dev4': {'devName': 'Pranjul Shukla',
                            'devImage': 'team/2015325.jpg',
                            'devTitle': 'Developer'
                            },

                   'dev5': {'devName': 'Saket Patel',
                            'devImage': 'team/2015329.jpg',
                            'devTitle': 'Head Developer'
                            },
               },

               'uiTeam': {
                   'dev1': {'devName': 'Kanishka Munshi',
                            'devImage': 'team/2015121.jpg',
                            'devTitle': 'Head UI Developer'
                            },

                   'dev2': {'devName': 'Ravuri Abhignya',
                            'devImage': 'zlatan.jpg',
                            'devTitle': 'Developer'
                            },
               },

               'qaTeam': {
                   'dev1': {'devName': 'Anuj Upadhaya',
                            'devImage': 'zlatan.jpg',
                            'devTitle': 'Member'
                            },

                   'dev2': {'devName': 'Avinash Kumar',
                            'devImage': 'team/2015058.jpg',
                            'devTitle': 'Head'
                            },

                   'dev3': {'devName': 'G. Vijay Ram',
                            'devImage': 'team/2015095.jpg',
                            'devTitle': 'Member'
                            },
               },

               'academics_a_Team': {
                   'dev1': {'devName': 'Anuraag Singh',
                            'devImage': 'team/2015043.jpeg',
                            'devTitle': '2015043'
                            },

                   'dev2': {'devName': 'Achint Mistry',
                            'devImage': 'zlatan.jpg',
                            'devTitle': '2015009'
                            },

                   'dev3': {'devName': 'Harshit Choubey',
                            'devImage': 'team/2015103.jpeg',
                            'devTitle': '2015103'
                            },

                   'dev4': {'devName': '',
                            'devImage': 'zlatan.jpg',
                            'devTitle': 'Rollnum'
                            },
               },

               'academics_b_Team': {
                   'dev1': {'devName': 'Mayank Saurabh',
                            'devImage': 'team/2015153.jpg',
                            'devTitle': 'UI Developer'
                            },

                   'dev2': {'devName': 'Narosenla Longkumer',
                            'devImage': 'team/2015165.jpg',
                            'devTitle': '2015165'
                            },

                   'dev3': {'devName': 'Rambha Sirisha',
                            'devImage': 'team/2015203.jpg',
                            'devTitle': '2015203'
                            },

                   'dev4': {'devName': '',
                            'devImage': 'zlatan.jpg',
                            'devTitle': '2015'
                            },

                   'dev5': {'devName': '',
                            'devImage': 'zlatan.jpg',
                            'devTitle': '2015'
                            },
               },


               'complaintTeam': {
                   'dev1': {'devName': 'Kanishka Munshi',
                            'devImage': 'team/2015121.jpg',
                            'devTitle': 'UI/UX Developer'
                            },

                   'dev2': {'devName': 'Amresh Kumar Verma',
                            'devImage': 'zlatan.jpg',
                            'devTitle': '2015027'
                            },

                   'dev3': {'devName': 'Rishti Gupta',
                            'devImage': 'zlatan.jpg',
                            'devTitle': '2015209'
                            },

                   'dev4': {'devName': 'Shubham Yadav',
                            'devImage': 'team/2015248.jpg',
                            'devTitle': '2015248'
                            },

                   'dev5': {'devName': '',
                            'devImage': 'zlatan.jpg',
                            'devTitle': ''
                            },
               },

               'eisTeam': {
                   'dev1': {'devName': 'Kanishka Munshi',
                            'devImage': 'team/2015121.jpg',
                            'devTitle': 'UI/UX Developer'
                            },

                   'dev2': {'devName': 'Mayank Saurabh',
                            'devImage': 'team/2015147.jpg',
                            'devTitle': 'UI Developer'
                            },

                   'dev3': {'devName': 'M. Arshad Siddiqui',
                            'devImage': 'team/2015153.jpg',
                            'devTitle': 'Backend Developer'
                            },
               },

               'filetrackingTeam': {
                   'dev1': {'devName': 'Mayank Saurabh',
                            'devImage': 'team/2015147.jpg',
                            'devTitle': 'UI/UX Developer'
                            },

                   'dev2': {'devName': 'Deepak Chhipa',
                            'devImage': 'team/2015076.jpg',
                            'devTitle': '2015076'
                            },

                   'dev3': {'devName': '',
                            'devImage': 'zlatan.jpg',
                            'devTitle': '2015'
                            },

                   'dev4': {'devName': '',
                            'devImage': 'zlatan.jpg',
                            'devTitle': '2015'
                            },

                   'dev5': {'devName': '',
                            'devImage': 'zlatan.jpg',
                            'devTitle': '2015'
                            },
               },

               'gymkhanaTeam': {
                   'dev1': {'devName': 'Kanishka Munshi',
                            'devImage': 'team/2015121.jpg',
                            'devTitle': 'UI/UX Developer'
                            },
               },


               'leaveTeam': {
                   'dev1': {'devName': 'Kanishka Munshi',
                            'devImage': 'team/2015121.jpg',
                            'devTitle': 'UI/UX Developer'
                            },

                   'dev2': {'devName': 'Saket Patel',
                            'devImage': 'team/2015329.jpg',
                            'devTitle': 'Backend Developer'
                            },
               },

               'messTeam': {
                   'dev1': {'devName': 'Kanishka Munshi',
                            'devImage': 'team/2015121.jpg',
                            'devTitle': 'UI/UX Developer'
                            },

                   'dev2': {'devName': 'Ankita Makker',
                            'devImage': 'team/2015034.jpg',
                            'devTitle': '2015034'
                            },

                   'dev3': {'devName': 'K. Venkateshwar Reddy',
                            'devImage': 'team/2015117.jpg',
                            'devTitle': '2015117'
                            },

                   'dev4': {'devName': 'Pratibha Singh',
                            'devImage': 'team/2015189.jpg',
                            'devTitle': '2015189'
                            },

                   'dev5': {'devName': 'Varnika Jain',
                            'devImage': 'team/2015268.jpg',
                            'devTitle': '2015268'
                            },
               },

               'phcTeam': {
                   'dev1': {'devName': 'Ravuri Abhignya',
                            'devImage': 'zlatan.jpg',
                            'devTitle': 'UI/UX Developer'
                            },

                   'dev2': {'devName': 'B. Krishnanjali',
                            'devImage': 'team/2015061.jpeg',
                            'devTitle': '2015061'
                            },

                   'dev3': {'devName': 'K. Jahnavi',
                            'devImage': 'team/2015120.jpeg',
                            'devTitle': '2015120'
                            },

                   'dev4': {'devName': 'K. Sai Srikar',
                            'devImage': 'team/2015127.jpg',
                            'devTitle': '2015127'
                            },

                   'dev5': {'devName': 'Priyanka Agarwal',
                            'devImage': 'team/2015192.jpg',
                            'devTitle': '2015192'
                            },
               },


               'placementTeam': {
                   'dev1': {'devName': 'Kanishka Munshi',
                            'devImage': 'team/2015121.jpg',
                            'devTitle': 'UI/UX Developer'
                            },

                   'dev2': {'devName': 'Avinash Kumar',
                            'devImage': 'team/2015058.jpg',
                            'devTitle': '2015058'
                            },

                   'dev3': {'devName': 'Arpit Jain',
                            'devImage': 'team/2015047.jpg',
                            'devTitle': '2015047'
                            },

                   'dev4': {'devName': 'Gautam Yadav',
                            'devImage': 'zlatan.jpg',
                            'devTitle': '2015093'
                            },

                   'dev5': {'devName': '',
                            'devImage': 'zlatan.jpg',
                            'devTitle': '2015'
                            },
               },

               'spacsTeam': {
                   'dev1': {'devName': 'Ravuri Abhignya',
                            'devImage': 'zlatan.jpg',
                            'devTitle': 'UI/UX Developer'
                            },

                   'dev2': {'devName': 'Atla Shashidhar Reddy',
                            'devImage': 'team/2015056.jpeg',
                            'devTitle': '2015056'
                            },

                   'dev3': {'devName': 'Gopisetti Pramod Kumar',
                            'devImage': 'team/2015314.jpg',
                            'devTitle': '2015314'
                            },

                   'dev4': {'devName': 'Segu Balaji',
                            'devImage': 'team/2015335.png',
                            'devTitle': '2015335'
                            },

                   'dev5': {'devName': '',
                            'devImage': 'zlatan.jpg',
                            'devTitle': ''
                            },
               },

               'vhTeam': {
                   'dev1': {'devName': 'Ravuri Abhignya',
                            'devImage': 'zlatan.jpg',
                            'devTitle': 'UI/UX Developer'
                            },

                   'dev2': {'devName': 'Imdad Ali',
                            'devImage': 'zlatan.jpg',
                            'devTitle': '2015'
                            },

                   'dev3': {'devName': 'Prashant Shivam',
                            'devImage': 'zlatan.jpg',
                            'devTitle': '2015'
                            },

                   'dev4': {'devName': 'Riya Goyal',
                            'devImage': 'team/2015210.png',
                            'devTitle': '2015210'
                            },

                   'dev5': {'devName': 'Anuj Upadhyay',
                            'devImage': 'zlatan.jpg',
                            'devTitle': '2015'
                            },
               },
               }
    return render(request, "globals/about.html", context)

def login(request):
    context = {}
    return render(request, "globals/login.html", context)

def about(request):

    teams = {


        'uiTeam': {
            'teamId': "uiTeam",
            'teamName': "UI/UX",
        },

        'AcademicsTeam': {
            'teamId': "AcademicsTeam",
            'teamName': "Academics Module",
        },

        'eisTeam': {
            'teamId': "eisTeam",
            'teamName': "EIS Module",
        },

        'leaveTeam': {
            'teamId': "leaveTeam",
            'teamName': "Leave Module",
        },

        'CourseManagementTeam': {
            'teamId': "CourseManagementTeam",
            'teamName': "Course Management Module",
        },

        'complaintTeam': {
            'teamId': "complaintTeam",
            'teamName': "Complaint Module",
        },

        'CentralMessTeam': {
            'teamId': "CentralMessTeam",
            'teamName': "Mess Module",
        },

        'PlacementTeam': {
            'teamId': "PlacementTeam",
            'teamName': "Placement Module",
        },

        'ScholarshipTeam': {
            'teamId': "ScholarshipTeam",
            'teamName': "Awards and Scholarship Module",
        },
    }

    context = {'teams': teams,
               'psgTeam': {
                   'dev1': {'devName': 'Anuraag Singh',
                            'devImage': 'zlatan.jpg',
                            'devTitle': 'Developer'
                            },

                   'dev2': {'devName': 'Kanishka Munshi',
                            'devImage': 'zlatan.jpg',
                            'devTitle': 'UI/UX Developer'
                            },

                   'dev3': {'devName': 'M. Arshad Siddiqui',
                            'devImage': 'zlatan.jpg',
                            'devTitle': 'Database Designer'
                            },

                   'dev4': {'devName': 'Pranjul Shukla',
                            'devImage': 'zlatan.jpg',
                            'devTitle': 'Developer'
                            },

                   'dev5': {'devName': 'Saket Patel',
                            'devImage': 'zlatan.jpg',
                            'devTitle': 'Developer'
                            },
               },
               'AcademicsTeam': {
                   'dev1': {'devName': 'Anuraag Singh',
                            'devImage': 'zlatan.jpg',
                            'devTitle': 'Steering Group'
                            },

                   'dev2': {'devName': 'Achint Mistri',
                            'devImage': 'zlatan.jpg',
                            'devTitle': 'Developer'
                            },

                   'dev3': {'devName': 'Harshit Choubey',
                            'devImage': 'zlatan.jpg',
                            'devTitle': 'Developer'
                            },

                   'dev4': {'devName': 'Narosena Longkumar',
                            'devImage': 'zlatan.jpg',
                            'devTitle': 'Developer'
                            },
               },
               'uiTeam': {
                   'dev1': {'devName': 'Kanishka Munshi',
                            'devImage': 'zlatan.jpg',
                            'devTitle': 'Head UI Developer'
                            },

                   'dev2': {'devName': 'Mayank Saurabh',
                            'devImage': 'zlatan.jpg',
                            'devTitle': 'UI Developer'
                            },

                   'dev3': {'devName': 'Ravuri Abhignya',
                            'devImage': 'zlatan.jpg',
                            'devTitle': 'UI Developer'
                            },
               },

               'complaintTeam': {
                   'dev1': {'devName': 'Saksham Agarwal',
                            'devImage': 'zlatan.jpg',
                            'devTitle': 'Developer'
                            },

                   'dev2': {'devName': 'Rishti Gupta',
                            'devImage': 'zlatan.jpg',
                            'devTitle': 'Developer'
                            },

                   'dev3': {'devName': 'Shubham Yadav',
                            'devImage': 'zlatan.jpg',
                            'devTitle': 'Developer'
                            },

                   'dev4': {'devName': 'Amresh Kumar Verma',
                            'devImage': 'zlatan.jpg',
                            'devTitle': 'Developer'
                            },
               },
               'eisTeam': {

                   'dev1': {'devName': 'M. Arshad Siddiqui',
                            'devImage': 'zlatan.jpg',
                            'devTitle': 'Developer'
                            },
               },

               'leaveTeam': {
                   'dev1': {'devName': 'Pranjul Shukla',
                            'devImage': 'zlatan.jpg',
                            'devTitle': 'Developer'
                            },

                   'dev2': {'devName': 'Saket Patel',
                            'devImage': 'zlatan.jpg',
                            'devTitle': 'Developer'
                            },
               },

               'CentralMessTeam': {
                   'dev1': {'devName': 'Ankita Makker',
                            'devImage': 'zlatan.jpg',
                            'devTitle': 'Developer'
                            },

                   'dev2': {'devName': 'Vernika Jain',
                            'devImage': 'zlatan.jpg',
                            'devTitle': 'Developer'
                            },
               },

               'PlacementTeam': {
                   'dev1': {'devName': 'Arpit Jain',
                            'devImage': 'zlatan.jpg',
                            'devTitle': 'Developer'
                            },

                   'dev2': {'devName': 'Gautam Yadav',
                            'devImage': 'zlatan.jpg',
                            'devTitle': 'Developer'
                            },
               },

               'ComplaintTeam': {
                   'dev1': {'devName': 'Srigari Avilash Kumar',
                            'devImage': 'zlatan.jpg',
                            'devTitle': 'Developer'
                            },

                   'dev2': {'devName': 'NakulArya',
                            'devImage': 'zlatan.jpg',
                            'devTitle': 'Developer'
                            },
               },

               'ScholarshipTeam': {
                   'dev1': {'devName': 'Segu Balaji',
                            'devImage': 'zlatan.jpg',
                            'devTitle': 'Developer'
                            },

                   'dev2': {'devName': 'M. Shrisha',
                            'devImage': 'zlatan.jpg',
                            'devTitle': 'Developer'
                            },

                   'dev3': {'devName': 'Atla Shashidar Reddy',
                            'devImage': 'zlatan.jpg',
                            'devTitle': 'Developer'
                            },
               },

               'CourseManagementTeam': {
                   'dev1': {'devName': 'Animesh Pandey',
                            'devImage': 'zlatan.jpg',
                            'devTitle': 'Developer'
                            },

                   'dev2': {'devName': 'Paras Rastogi',
                            'devImage': 'zlatan.jpg',
                            'devTitle': 'Developer'
                            },
               },
               }
    return render(request, "globals/about.html", context)

@login_required(login_url=LOGIN_URL)
def dashboard(request):
    # cse_faculty = ExtraInfo.objects.filter(user_type = 'faculty', department = DepartmentInfo.objects.get(name = 'CSE'))
    # ece_faculty = ExtraInfo.objects.filter(user_type = 'faculty', department = DepartmentInfo.objects.get(name = 'ECE'))
    # me_faculty = ExtraInfo.objects.filter(user_type = 'faculty', department = DepartmentInfo.objects.get(name = 'ME'))
    # des_faculty = ExtraInfo.objects.filter(user_type = 'faculty', department = DepartmentInfo.objects.get(name = 'Design'))
    # ns_faculty = ExtraInfo.objects.filter(user_type = 'faculty', department = DepartmentInfo.objects.get(name = 'Natural Science'))
    # cse_students = ExtraInfo.objects.filter(user_type = 'student', department = DepartmentInfo.objects.get(name = 'CSE'))
    # ece_students = ExtraInfo.objects.filter(user_type = 'student', department = DepartmentInfo.objects.get(name = 'ECE'))
    # me_students = ExtraInfo.objects.filter(user_type = 'student', department = DepartmentInfo.objects.get(name = 'ME'))
    # des_students = ExtraInfo.objects.filter(user_type = 'student', department = DepartmentInfo.objects.get(name = 'Design'))
    # ns_students = ExtraInfo.objects.filter(user_type = 'student', department = DepartmentInfo.objects.get(name = 'Natural Science'))
    # students_2017 = Student.objects.filter(batch = 2017)
    # students_2016 = Student.objects.filter(batch = 2016)
    # students_2015 = Student.objects.filter(batch = 2015)
    # students_2019 = Student.objects.filter(batch = 2019)
    # students_2018 = Student.objects.filter(batch = 2018)
    # data = {'cse': cse_faculty,
    #         'ece': ece_faculty,
    #         'me': me_faculty,
    #         'des': des_faculty,
    #         'ns': ns_faculty,
    #         'students_2019': students_2019,
    #         'students_2018': students_2018,
    #         'students_2017': students_2017,
    #         'students_2016': students_2016,
    #         'students_2015': students_2015}
    user=request.user
    notifs=request.user.notifications.all()
    name = request.user.first_name +"_"+ request.user.last_name
    desig = list(HoldsDesignation.objects.select_related('user','working','designation').all().filter(working = request.user).values_list('designation'))
    b = [i for sub in desig for i in sub]
    design = HoldsDesignation.objects.select_related('user','designation').filter(working=request.user)

    designation=[]
    for i in design:
        designation.append(str(i.designation))

    roll_ = []
    for i in b :
        name_ = get_object_or_404(Designation, id = i)
        roll_.append(str(name_.name))

    hall_caretakers = HallCaretaker.objects.all().select_related()
    hall_wardens = HallWarden.objects.all().select_related()

    hall_caretaker_user = []
    for caretaker in hall_caretakers:
        hall_caretaker_user.append(caretaker.staff.id.user)

    hall_warden_user = []
    for warden in hall_wardens:
        hall_warden_user.append(warden.faculty.id.user)
    print("modules are")
    print(request.session.get('moduleAccessRights'))
    context={
        'notifications':notifs,
        'Curr_desig' : roll_,
        'club_details' : coordinator_club(request),
        'designation' : designation,
        'hall_caretaker': hall_caretaker_user,
        'hall_warden': hall_warden_user,
        'announcements': announcement_list(request)['announcements']
        
    }
    # a=HoldsDesignation.objects.select_related('user','working','designation').filter(designation = user)
    print(context)
    print(type(user.extrainfo.user_type))
    print(announcement_list(request))
    if(request.user.get_username() == 'director'):
        return render(request, "dashboard/director_dashboard2.html", {})
    elif( "dean_rspc" in designation):
        return render(request, "dashboard/dashboard.html", context)
    elif user.extrainfo.user_type != "student":
        print ("inside")
        designat = HoldsDesignation.objects.select_related().filter(user=user)
        response = {'designat':designat}
        context.update(response)
        return render(request, "dashboard/dashboard.html", context)
    else:
        print ("inside2")
        
        return render(request, "dashboard/dashboard.html", context)


@login_required(login_url=LOGIN_URL)
def   profile(request, username=None):
    """
    Generic endpoint for views.
    If it's a faculty, redirects to /eis/profile/*
    If it's a student, displays the profile.
    If the department is 'department: Academics:, redirects to /aims/
    Otherwise, redirects to root

    Args:
        username: Username of the user. If None,
            displays the profile of currently logged-in user
    """



    user = get_object_or_404(User, Q(username=username)) if username else request.user
    editable = request.user == user
    print("editable",editable)
    profile = get_object_or_404(ExtraInfo, Q(user=user))
    print("profile",profile)
    if(str(user.extrainfo.user_type)=='faculty'):
        print("profile")
        return HttpResponseRedirect('/eis/profile/' + (username if username else ''))
    if(str(user.extrainfo.department)=='department: Academics'):
        print("profile2")
        return HttpResponseRedirect('/aims')
    
    array = [
     "student",
    "CC convenor",
    "Mechatronic convenor",
    "mess_committee",
    "mess_convener",
    "alumini",
    "Electrical_AE",
    "Electrical_JE",
    "Civil_AE",
    "Civil_JE",
    "co-ordinator",
    "co co-ordinator",
    "Convenor",
    "Convener",
    "cc1convener",
    "CC2 convener",
    "mess_convener_mess2",
    "mess_committee_mess2"
]

    # queryset = HoldsDesignation.objects.select_related('user','working','designation').filter(Q(working=user))

    # for obj in queryset:
    #     designation_name = obj.designation.name
    #     print("designation_name",designation_name)
        
    # design = False
    # if designation_name in array:
    #     design = True
    #     print("design",design)
    #     print("designation_name",designation_name)
    # if design:
    #     current = HoldsDesignation.objects.select_relapted('user','working','designation').filter(Q(working=user, designation__name=designation_name))
    #     for obj in current:
    #         obj.designation.name = obj.designation.name.replace(designation_name, 'student')
    
    designation_name = ""
    design = False

    current = HoldsDesignation.objects.select_related('user', 'working', 'designation').filter(Q(working=user))

    for obj in current:
        designation_name = obj.designation.name
        if designation_name in array:
            design = True
            break

    if design:
        current = HoldsDesignation.objects.filter(working=user, designation__name=designation_name)
        for obj in current:
            obj.designation.name = obj.designation.name.replace(designation_name, 'student')
    
    print(user.extrainfo.user_type)
    print("current",current)
    if current:
        print("profile3")
        student = get_object_or_404(Student, Q(id=profile.id))
        print("student",student)
        if editable and request.method == 'POST':
            if 'studentapprovesubmit' in request.POST:
                status = PlacementStatus.objects.select_related('notify_id','unique_id__id__user','unique_id__id__department').filter(pk=request.POST['studentapprovesubmit']).update(invitation='ACCEPTED', timestamp=timezone.now())
            if 'studentdeclinesubmit' in request.POST:
                status = PlacementStatus.objects.select_related('notify_id','unique_id__id__user','unique_id__id__department').filter(Q(pk=request.POST['studentdeclinesubmit'])).update(invitation='REJECTED', timestamp=timezone.now())
            if 'educationsubmit' in request.POST:
                form = AddEducation(request.POST)
                if form.is_valid():
                    institute = form.cleaned_data['institute']
                    degree = form.cleaned_data['degree']
                    grade = form.cleaned_data['grade']
                    stream = form.cleaned_data['stream']
                    sdate = form.cleaned_data['sdate']
                    edate = form.cleaned_data['edate']
                    education_obj = Education.objects.create(unique_id=student, degree=degree,
                                                             grade=grade, institute=institute,
                                                             stream=stream, sdate=sdate, edate=edate)
                    education_obj.save()
            if 'profilesubmit' in request.POST:
                about_me = request.POST.get('about')
                age = request.POST.get('age')
                address = request.POST.get('address')
                contact = request.POST.get('contact')
                extrainfo_obj = ExtraInfo.objects.select_related('user','department').get(user=user)
                extrainfo_obj.about_me = about_me
                extrainfo_obj.date_of_birth = age
                extrainfo_obj.address = address
                extrainfo_obj.phone_no = contact
                extrainfo_obj.save()
                profile = get_object_or_404(ExtraInfo, Q(user=user))
            if 'picsubmit' in request.POST:
                form = AddProfile(request.POST, request.FILES)
                extrainfo_obj = ExtraInfo.objects.select_related('user','department').get(user=user)
                extrainfo_obj.profile_picture = form.cleaned_data["pic"]
                extrainfo_obj.save()
            if 'skillsubmit' in request.POST:
                form = AddSkill(request.POST)
                if form.is_valid():
                    skill = form.cleaned_data['skill']
                    skill_rating = form.cleaned_data['skill_rating']
                    try:
                        skill_id = Skill.objects.get(skill=skill)
                    except Exception as e:
                        skill_id = Skill.objects.create(skill=skill)
                        skill_id.save()
                    has_obj = Has.objects.create(unique_id=student,
                                                 skill_id=skill_id,
                                                 skill_rating = skill_rating)
                    has_obj.save()
            if 'achievementsubmit' in request.POST:
                form = AddAchievement(request.POST)
                if form.is_valid():
                    achievement = form.cleaned_data['achievement']
                    achievement_type = form.cleaned_data['achievement_type']
                    description = form.cleaned_data['description']
                    issuer = form.cleaned_data['issuer']
                    date_earned = form.cleaned_data['date_earned']
                    achievement_obj = Achievement.objects.create(unique_id=student,
                                                                 achievement=achievement,
                                                                 achievement_type=achievement_type,
                                                                 description=description,
                                                                 issuer=issuer,
                                                                 date_earned=date_earned)
                    achievement_obj.save()
            if 'publicationsubmit' in request.POST:
                form = AddPublication(request.POST)
                if form.is_valid():
                    publication_title = form.cleaned_data['publication_title']
                    description = form.cleaned_data['description']
                    publisher = form.cleaned_data['publisher']
                    publication_date = form.cleaned_data['publication_date']
                    publication_obj = Publication.objects.create(unique_id=student,
                                                                 publication_title=
                                                                 publication_title,
                                                                 publisher=publisher,
                                                                 description=description,
                                                                 publication_date=publication_date)
                    publication_obj.save()
            if 'patentsubmit' in request.POST:
                form = AddPatent(request.POST)
                if form.is_valid():
                    patent_name = form.cleaned_data['patent_name']
                    description = form.cleaned_data['description']
                    patent_office = form.cleaned_data['patent_office']
                    patent_date = form.cleaned_data['patent_date']
                    patent_obj = Patent.objects.create(unique_id=student, patent_name=patent_name,
                                                       patent_office=patent_office,
                                                       description=description,
                                                       patent_date=patent_date)
                    patent_obj.save()
            if 'coursesubmit' in request.POST:
                form = AddCourse(request.POST)
                if form.is_valid():
                    course_name = form.cleaned_data['course_name']
                    description = form.cleaned_data['description']
                    license_no = form.cleaned_data['license_no']
                    sdate = form.cleaned_data['sdate']
                    edate = form.cleaned_data['edate']
                    course_obj = Course.objects.create(unique_id=student, course_name=course_name,
                                                       license_no=license_no,
                                                       description=description,
                                                       sdate=sdate, edate=edate)
                    course_obj.save()
            if 'projectsubmit' in request.POST:
                form = AddProject(request.POST)
                if form.is_valid():
                    project_name = form.cleaned_data['project_name']
                    project_status = form.cleaned_data['project_status']
                    summary = form.cleaned_data['summary']
                    project_link = form.cleaned_data['project_link']
                    sdate = form.cleaned_data['sdate']
                    edate = form.cleaned_data['edate']
                    project_obj = Project.objects.create(unique_id=student, summary=summary,
                                                         project_name=project_name,
                                                         project_status=project_status,
                                                         project_link=project_link,
                                                         sdate=sdate, edate=edate)
                    project_obj.save()
            if 'experiencesubmit' in request.POST:
                form = AddExperience(request.POST)
                if form.is_valid():
                    title = form.cleaned_data['title']
                    status = form.cleaned_data['status']
                    company = form.cleaned_data['company']
                    location = form.cleaned_data['location']
                    description = form.cleaned_data['description']
                    sdate = form.cleaned_data['sdate']
                    edate = form.cleaned_data['edate']
                    experience_obj = Experience.objects.create(unique_id=student, title=title,
                                                               company=company, location=location,
                                                               status=status,
                                                               description=description,
                                                               sdate=sdate, edate=edate)
                    experience_obj.save()
            if 'deleteskill' in request.POST:
                hid = request.POST['deleteskill']
                hs = Has.objects.select_related('skill_id','unique_id__id__user','unique_id__id__department').get(Q(pk=hid))
                hs.delete()
            if 'deleteedu' in request.POST:
                hid = request.POST['deleteedu']
                hs = Education.objects.select_related('unique_id__id__user','unique_id__id__department').get(Q(pk=hid))
                hs.delete()
            if 'deletecourse' in request.POST:
                hid = request.POST['deletecourse']
                hs = Course.objects.select_related('unique_id__id__user','unique_id__id__department').get(Q(pk=hid))
                hs.delete()
            if 'deleteexp' in request.POST:
                hid = request.POST['deleteexp']
                hs = Experience.objects.select_related('unique_id__id__user','unique_id__id__department').get(Q(pk=hid))
                hs.delete()
            if 'deletepro' in request.POST:
                hid = request.POST['deletepro']
                hs = Project.objects.select_related('unique_id__id__user','unique_id__id__department').get(Q(pk=hid))
                hs.delete()
            if 'deleteach' in request.POST:
                hid = request.POST['deleteach']
                hs = Achievement.objects.select_related('unique_id__id__user','unique_id__id__department').get(Q(pk=hid))
                hs.delete()
            if 'deletepub' in request.POST:
                hid = request.POST['deletepub']
                hs = Publication.objects.select_related('unique_id__id__user','unique_id__id__department').get(Q(pk=hid))
                hs.delete()
            if 'deletepat' in request.POST:
                hid = request.POST['deletepat']
                hs = Patent.objects.select_related('unique_id__id__user','unique_id__id__department').get(Q(pk=hid))
                hs.delete()

        form = AddEducation(initial={})
        form1 = AddProfile(initial={})
        form10 = AddSkill(initial={})
        form11 = AddCourse(initial={})
        form12 = AddAchievement(initial={})
        form5 = AddPublication(initial={})
        form6 = AddProject(initial={})
        form7 = AddPatent(initial={})
        form8 = AddExperience(initial={})
        form14 = AddProfile()
        skills = Has.objects.select_related('skill_id','unique_id__id__user','unique_id__id__department').filter(Q(unique_id=student))
        education = Education.objects.select_related('unique_id__id__user','unique_id__id__department').filter(Q(unique_id=student))
        course = Course.objects.select_related('unique_id__id__user','unique_id__id__department').filter(Q(unique_id=student))
        experience = Experience.objects.select_related('unique_id__id__user','unique_id__id__department').filter(Q(unique_id=student))
        project = Project.objects.select_related('unique_id__id__user','unique_id__id__department').filter(Q(unique_id=student))
        achievement = Achievement.objects.select_related('unique_id__id__user','unique_id__id__department').filter(Q(unique_id=student))
        publication = Publication.objects.select_related('unique_id__id__user','unique_id__id__department').filter(Q(unique_id=student))
        patent = Patent.objects.select_related('unique_id__id__user','unique_id__id__department').filter(Q(unique_id=student))
        context = {'user': user, 'profile': profile, 'skills': skills,
                   'educations': education, 'courses': course, 'experiences': experience,
                   'projects': project, 'achievements': achievement, 'publications': publication,
                   'patent': patent, 'form': form, 'form1': form1, 'form14': form14,
                   'form5': form5, 'form6': form6, 'form7': form7, 'form8': form8,
                   'form10':form10, 'form11':form11, 'form12':form12, 'current':current,
                   'editable': editable
                   }
        if 'skillsubmit' in request.POST or 'deleteskill' in request.POST:
            return render(request, "globals/student_profile2.html", context)
        if 'coursesubmit' in request.POST or 'educationsubmit' in request.POST or 'deleteedu' in request.POST or 'deletecourse' in request.POST:
            return render(request, "globals/student_profile3.html", context)
        if 'experiencesubmit' in request.POST or 'projectsubmit' in request.POST or 'deleteexp' in request.POST or 'deletepro' in request.POST:
            return render(request, "globals/student_profile4.html", context)
        if 'achievementsubmit' in request.POST or 'deleteach' in request.POST:
            return render(request, "globals/student_profile5.html", context)
        # print("context",context)
        return render(request, "globals/student_profile.html", context)
    else:
        return redirect("/")

@login_required(login_url=LOGIN_URL)
def logout_view(request):
    logout(request)
    return redirect("/")


""" Views for Feedback and Issue reports """


@login_required(login_url=LOGIN_URL)
def feedback(request):
    feeds = Feedback.objects.select_related('user').all().order_by("rating").exclude(user=request.user)
    if feeds.count() > 5:
        feeds = feeds[:5]
    rated = []
    for feed in feeds:
        rated.append(range(feed.rating))
    feeds = zip(feeds, rated)
    if request.method == "POST":
        try:
            feedback = Feedback.objects.select_related('user').get(user=request.user)
        except Exception as e:
            feedback = None
        if feedback:
            form = WebFeedbackForm(request.POST or None, instance=feedback)
        else:
            form = WebFeedbackForm(request.POST or None)
        feedback = form.save(commit=False)
        user_rating = request.POST.get("rating")
        feedback.user = request.user
        if int(user_rating) > 0 and int(user_rating) < 6:
            feedback.rating = user_rating
            feedback.save()
        form = WebFeedbackForm(instance=feedback)
        stars = []
        for i in range(0, int(feedback.rating)):
            stars.append(1)
        rating = 0
        for feed in Feedback.objects.all():
            rating = rating + feed.rating
        if Feedback.objects.all().count() > 0:
            rating = round(rating/Feedback.objects.all().count(),1)
        context = {
            'form': form,
            "feedback": feedback,
            'rating': rating,
            "stars": stars,
            "reviewed": True,
            "feeds": feeds
        }
        return render(request, "globals/feedback.html", context)
    rating = 0
    for feed in Feedback.objects.all():
        rating = rating + feed.rating
    if Feedback.objects.all().count() > 0:
        rating = round(rating/Feedback.objects.all().count(),1)
    try:
        feedback = Feedback.objects.select_related('user').get(user=request.user)
        form = WebFeedbackForm(instance=feedback)
    except Exception as e:
        form = WebFeedbackForm()
        context = {"form": form, "rating": rating, "feeds": feeds}
        return render(request, "globals/feedback.html", context)
    stars = []
    for i in range(0, int(feedback.rating)):
        stars.append(1)
    context = {
        "rating": rating,
        "feedback": feedback,
        "stars": stars,
        "form": form,
        "reviewed": True,
        "feeds": feeds
    }
    return render(request, "globals/feedback.html", context)


@login_required(login_url=LOGIN_URL)
def issue(request):
    if request.method == "POST":
        form = IssueForm(request.POST or None)
        if form.is_valid():
            issue = form.save(commit=False)
            issue.user = request.user
            issue.save()
            for image in request.FILES.getlist('images'):
                try:
                    Image.open(image)
                    image = IssueImage.objects.create(image=image, user=request.user)
                    issue.images.add(image)
                except Exception as e:
                    pass
            issue.save()
            openissue = Issue.objects.select_related('user').prefetch_related('images','support').filter(closed=False)
            closedissue = Issue.objects.select_related('user').prefetch_related('images','support').filter(closed=True)
            form = IssueForm()
            context = {"form": form, "openissue": openissue, "closedissue": closedissue, }
            return render(request, "globals/issue.html", context)
        openissue = Issue.objects.select_related('user').prefetch_related('images','support').filter(closed=False)
        closedissue = Issue.objects.select_related('user').prefetch_related('images','support').filter(closed=True)
        form = IssueForm(request.POST)
        context = {"form": form, "openissue": openissue, "closedissue": closedissue, }
        return render(request, "globals/issue.html", context)
    openissue = Issue.objects.select_related('user').prefetch_related('images','support').filter(closed=False)
    closedissue = Issue.objects.select_related('user').prefetch_related('images','support').filter(closed=True)
    form = IssueForm()
    context = {"form": form, "openissue": openissue, "closedissue": closedissue, }
    return render(request, "globals/issue.html", context)


@login_required(login_url=LOGIN_URL)
def view_issue(request, id):
    if request.method == "POST":
        issue = get_object_or_404(Issue, id=id, user=request.user)
        form = IssueForm(request.POST or None, instance=issue)
        if form.is_valid():
            issue.save()
            remove = request.POST.get("remove-images")
            if remove:
                for img in issue.images.all():
                    img.delete()
            for image in request.FILES.getlist('images'):
                try:
                    Image.open(image)
                    image = IssueImage.objects.create(image=image, user=request.user)
                    issue.images.add(image)
                except Exception as e:
                    pass
            issue.save()
            form = IssueForm(instance=issue)
            context = {
                "form": form,
                "issue": issue,
            }
            return render(request, "globals/view_issue.html", context)
        form = IssueForm(request.POST or None)
        context = {
            "form": form,
            "issue": issue,
        }
        return render(request, "globals/view_issue.html", context)
    issue = get_object_or_404(Issue, id=id)
    form = None
    if request.user == issue.user:
        form = IssueForm(instance=issue)
    context = {
        "form": form,
        "issue": issue,
    }
    return render(request, "globals/view_issue.html", context)


@login_required(login_url=LOGIN_URL)
def support_issue(request, id):
    issue = get_object_or_404(Issue, id=id)
    supported = True
    if request.user in issue.support.all():
        issue.support.remove(request.user)
        supported = False
    else:
        issue.support.add(request.user)
    support_count = issue.support.all().count()
    context = {
        "supported": supported,
        "support_count": support_count,
    }
    return HttpResponse(json.dumps(context), "application/json")

@login_required(login_url=LOGIN_URL)
def search(request):
    """
    Search endpoint.
    Renders search results populated with results from 'q' GET query.
    If length of the query is less than 3 or no results are found, shows a
    helpful message instead.
    Algorithm: Includes the first 15 users whose first/last name starts with the query words.
               Thus, searching 'Atu Gu' will return 'Atul Gupta' as one result.

               Note: All the words in the query must be matched.
               While, searching 'Atul Kumar', the word 'Kumar' won't match either 'Atul' or 'Gupta'
               and thus it won't be included in the search results.
    """
    key = request.GET['q']
    if len(key) < 3:
        return render(request, "globals/search.html", {'sresults': ()})
    words = (w.strip() for w in key.split())
    name_q = Q()
    for token in words:
        name_q = name_q & (Q(first_name__icontains=token) | Q(last_name__icontains=token))#search constraints
    search_results = User.objects.filter(name_q)[:15]
    if len(search_results) == 0:
        search_results = []
    context = {'sresults':search_results}
    return render(request, "globals/search.html", context),

@login_required(login_url=LOGIN_URL)
def update_global_variable(request):
    if request.method == 'POST':
        selected_option = request.POST.get('dropdown')
        request.session['currentDesignationSelected'] = selected_option
        module_access = ModuleAccess.objects.filter(designation=selected_option).first()
        if module_access:
            access_rights = {}
    
            field_names = [field.name for field in ModuleAccess._meta.get_fields() if field.name not in ['id', 'designation']]
    
            for field_name in field_names:
                access_rights[field_name] = getattr(module_access, field_name)
    
        request.session['moduleAccessRights'] = access_rights      
                
        print(selected_option)
        print(request.session['currentDesignationSelected'])
        return HttpResponseRedirect('/dashboard')
    # Redirect to home if not a POST request or some issue occurs
    return HttpResponseRedirect(reverse('home'))