from attr import fields
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from applications.gymkhana.models import Club_info,Session_info,Event_info
from applications.gymkhana.models import Club_member,Club_budget,Club_report,Fest_budget,Fest,Registration_form,Budget,Budget_Comments,Event_Comments,Achievements,ClubPosition, EventInput, EventReport

# class Voting_choicesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Voting_choices
#         fields = ['poll_event', 'title', 'description', 'votes']


class Club_infoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Club_info
        fields = ['club_name', 'category', 'co_ordinator', 'co_coordinator', 'faculty_incharge', 'club_file', 'activity_calender', 'description', 'alloted_budget', 'spent_budget', 'avail_budget', 'status', 'head_changed_on', 'created_on']



class EmptySerializer(serializers.Serializer):
    pass

class Club_memberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club_member
        fields = ['member','club','description', 'status','remarks','id']
    

# class Core_teamSerializer(serializers.ModelSerializer):

#     class Meta:
#         model=Core_team
#         fields=('all')

class Club_DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Club_info
        fields=['club_name',"co_ordinator","co_coordinator","activity_calender","category",'faculty_incharge',"club_file", "status" ,"description"]

class Session_infoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session_info
        fields = [ 'venue', 'date', 'start_time', 'end_time', 'details','status','session_poster','id', 'club']



class event_infoserializer(serializers.ModelSerializer):

    class Meta:
        model=Event_info
        fields=['club','event_name','incharge','start_date','end_date','venue','start_time','id','details','status','end_time','details']

class club_budgetserializer(serializers.ModelSerializer):

    class Meta:
        model=Club_budget
        fields=['club','budget_for','budget_amt','budget_file','status','id','description','remarks']

class Club_reportSerializers(serializers.ModelSerializer):
    class Meta:
        model = Club_report
        fields = ['club', 'incharge' , 'event_name' , 'date' , 'event_details' ]

class Fest_budgerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Fest_budget
        fields=['fest','budget_amt','budget_file','year','status']

class Registration_formSerializer(serializers.ModelSerializer):
    class Meta:
        model=Registration_form
        fields=['roll','user_name','branch','cpi','programme']

# class Voting_pollSerializer(serializers.ModelSerializer):

#     class Meta:
#         model=Voting_polls
#         fields=['title','pub_date','exp_date','created_by','groups','id','description']
class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ['id', 'club', 'budget_for', 'budget_requested', 'budget_allocated', 'budget_file', 'description', 'status', 'remarks', 'budget_comment']
class AchievementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievements
        fields = ['id', 'club_name', 'title', 'achievement']
class Budget_CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget_Comments
        fields = ['budget_id', 'commentator_designation', 'comment', 'comment_date', 'comment_time']
class Event_CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event_Comments
        fields = ['event_id', 'commentator_designation', 'comment', 'comment_date', 'comment_time']
class ClubPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubPosition
        fields = ['id', 'name', 'position', 'club']

class FestSerializer(serializers.ModelSerializer):
    class Meta:
        model=Fest
        fields= ['id', 'name', 'category', 'description', 'date', 'link']

class EventInputSerializer(serializers.ModelSerializer):
    # Use event name for dropdown-like functionality
    event = serializers.SlugRelatedField(
        queryset=Event_info.objects.all(), 
        slug_field='id')

    class Meta:
        model = EventInput
        fields = ['id', 'event', 'description','images']

class EventReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventReport
        fields = '__all__'
