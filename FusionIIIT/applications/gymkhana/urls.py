from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from applications.gymkhana.api.views import (
    AddClub_BudgetAPIView,
    AddMemberToClub,
    ApproveEvent,
    ChangeHeadAPIView,
    ClubMemberAPIView,
    ClubMemberApproveView,
    ClubMemberDeleteAPIView,
    CreateClubAPIView,
    DeanReviewBudgetAPIView,
    DeleteClubAPIView,
    DeleteClubBudgetAPIView,
    EventDeleteAPIView,
    EventUpdateAPIView,
    FreeMembersForClubAPIView,
    SessionUpdateAPIView,
    UpdateClubBudgetAPIView,
    UpdateClubNameAPIView,
    UpdateClubStatusAPIView,
    UploadActivityCalendarAPIView,
    ModifyEventAPIView,
    ModifyBudgetAPIView,
    RejectEventAPIView,
    RejectBudgetAPIView,
    UpdateEventAPIView,
    FestListView,
    EventReportListAPIView,
    EventReportAPIView,
    EventReportPDFView
)
from applications.gymkhana.api.views import (
    clubname,
    Club_Details,
    club_events,
    club_budgetinfo,
    Fest_Budget,
    club_report,
    Registraion_form,
)
from applications.gymkhana.api.views import session_details, UpdateBudgetAPIView
from applications.gymkhana.api.views import (
    DeleteSessionsView,
    NewEventAPIView,
    NewSessionAPIView,
    Club_Detail,
    UpcomingEventsAPIView,
    PastEventsAPIView,
    Budgetinfo,
    AddClubAPI,
    NewBudgetAPIView,
    FICApproveBudgetAPIView,
    CounsellorApproveBudgetAPIView,
    DeanApproveBudgetAPIView,
    FICApproveEventAPIView,
    CounsellorApproveEventAPIView,
    DeanApproveEventAPIView,
    AddAchievementAPIView,
    AchievementsAPIView,
    CreateBudgetCommentAPIView,
    CreateEventCommentAPIView,
    ListBudgetCommentsAPIView,
    ListEventCommentsAPIView,
    AddClubPositionAPIView,
    ListClubPositionAPIView,
    NewFestAPIView,
    CoordinatorEventsAPIView, 
    EventInputAPIView, 
    NewsletterPDFAPIView
)
from . import views
from rest_framework.authtoken.views import obtain_auth_token

app_name = "gymkhana"

urlpatterns = [
    # for club_detail,upcomingevents and past events
    url(r"^club_detail/$", Club_Detail.as_view()),
    url(r"^upcoming_events/$", UpcomingEventsAPIView.as_view()),
    url(r"^past_events/$", PastEventsAPIView.as_view()),
    url(r"^budget/$", Budgetinfo.as_view()),
    url(r"^session_details/$", session_details.as_view()),
    url(r"^event_info/$", club_events.as_view()),
    url(r"^club_budgetinfo/$", club_budgetinfo.as_view()),
    # academic administration
    url(r"^club_approve/$", views.club_approve, name="club_approve"),
    url(r"^del_mem/$", views.del_mem, name="del_mem"),
    url(r"^club_reject/$", views.club_reject, name="club_reject"),
    url(r"^budget_approve/$", views.budget_approve, name="budget_approve"),
    url(r"^budget_reject/$", views.budget_reject, name="budget_reject"),
    # This is post method which takes username and password to generates/return Token
    url(r"^login/$", obtain_auth_token, name="login"),
    # api for "clubdetails" method="get" with TokenAuthentication
    url(r"^clubdetails/$", Club_Details.as_view()),
    # api for "clubname" method="get" with TokenAuthentication
    url(r"^Fest_budget/$", Fest_Budget.as_view(), name="Fest_budget"),
    # api for "festbudget" method="get" with TokenAuthentication
    url(r"^club_report/$", club_report.as_view()),
    # api for "club_report" method="get" with TokenAuthentication
    url(r"^registration_form/$", Registraion_form.as_view()),
    # api for "registration_form" method="get" with TokenAuthentication
    # url(r'^voting_polls/$',Voting_Polls.as_view()),
    # api for "voting_polls" method="get" with TokenAuthentication
    # url(r"^api/new_event/$", NewEventAPIView.as_view(), name="new_event_api"),
    # url(r"^api/club_membership/$", AddMemberToClub.as_view(), name="new_club_member"),
    # url(r"^api/delete_event/$", DeleteEventsView.as_view(), name="delete_events_api"),
    # url(
    #     r"^api/delete_sessions/$",
    #     DeleteSessionsView.as_view(),
    #     name="delete_sessions_api",
    # ),
    # url(r"^api/new_session/$", NewSessionAPIView.as_view(), name="new_session_api"),
    url(r"^clubname/$", clubname.as_view()),
    url(r"^$", views.gymkhana, name="gymkhana"),
    url(r"^delete_requests/$", views.delete_requests, name="delete_requests"),
    url(r"^form_avail/$", views.form_avail, name="form_avail"),
    url(r"^registration_form/$", views.registration_form, name="registration_form"),
    url(r"^new_club/$", views.new_club, name="new_club"),
    # url(r"^api/members_records/$", ClubMemberAPIView.as_view(), name="club_members"),
    # club_head
    url(r"^approve/$", views.approve, name="approve"),
    url(r"^reject/$", views.reject, name="reject"),
    url(r"^cancel/$", views.cancel, name="cancel"),
    url(r"^new_event/$", views.new_event, name="new_event"),
    url(r"^new_session/$", views.new_session, name="new_session"),
    url(r"^event_report/$", views.event_report, name="event_report"),
    url(r"^club_event_report/$", views.club_report, name="club_report"),
    url(r"^change_head/$", views.change_head, name="change_head"),
    url(r"^club_budget/$", views.club_budget, name="club_budget"),
    url(r"^act_calender/$", views.act_calender, name="act_calender"),
    url(r"^date_sessions/$", views.date_sessions, name="date_sessions"),
    url(r"^date_events/$", views.date_events, name="date_events"),
    url(r"^delete_sessions/$", views.delete_sessions, name="delete_sessions"),
    url(r"^delete_events/$", views.delete_events, name="delete_events"),
    url(r"^(?P<event_id>\d+)/edit_event/$", views.edit_event, name="edit_event"),
    url(r"^(?P<session_id>\d+)/editsession/$", views.editsession, name="editsession"),
    url(r"^delete_memberform/$", views.delete_memberform, name="delete_memberform"),
    # url(r'^voting_poll/$', views.voting_poll, name='voting_poll'),
    # url(r'^delete_poll/(?P<poll_id>\d+)/$', views.delete_poll, name='delete_poll'),
    # student
    url(r"^registration_form/$", views.registration_form, name="registration_form"),
    url(r"^delete_requests/$", views.delete_requests, name="delete_requests"),
    url(r"^club_membership/$", views.club_membership, name="membership"),
    # url(r'^(?P<poll_id>\d+)/$', views.vote, name='vote'),
    url(r"^$", views.gymkhana, name="gymkhana"),
    # data recieving
    url(r"^form_avail/$", views.form_avail, name="form_avail"),
    url(r"^faculty_data/$", views.facultyData, name="faculty_data"),
    url(r"^students_data/$", views.studentsData, name="students_data"),
    url(r"^students_club_members/$", views.studentsClubMembers, name="students_data"),
    url(r"^get_venue/$", views.getVenue, name="get_venue"),
    # core_team
    # url(r"^core_team/$", views.core_team, name="core_team"),
    url(r"^festbudget/$", views.fest_budget, name="fest_budget"),
    # fic
    # url(r"^Inventory_update/$", views.core_team, name="Inventory_update"),
    url(r"^del_club/$", views.del_club, name="del_club"),
    url(r"^approve_events/$", views.approve_events, name="approve_events"),
    url(r"^update-club-name/$", views.update_club_name, name="update-club-name"),
    url(
        r"^update-budget-amount/$",
        views.update_budget_amount,
        name="update_budget_amount",
    ),
    # url(r"^update-spent-amount/$", views.update_spent_amount, name='update_spent_amount'),
    
    
    
    #app
    
    url(r'^api/update_clubBudget/$', UpdateClubBudgetAPIView.as_view(), name='update budget'),
    url(r'^api/add_clubBudget/$', AddClub_BudgetAPIView.as_view(), name='edit event'),
    url(r'^api/update_coordinator/$', ChangeHeadAPIView.as_view(), name = 'update coordinator'),
    url(r'^api/activity_calender/$', UploadActivityCalendarAPIView.as_view(), name='update activity calendder'),
    url(r'^api/delete_event/$', EventDeleteAPIView.as_view(), name='delete_events_api'),
    url(r'^api/delete_sessions/$', DeleteSessionsView.as_view(), name='delete_sessions_api'),
    url(r'^api/new_session/$',NewSessionAPIView.as_view(), name='new_session_api'),
    url(r'^api/new_event/$',NewEventAPIView.as_view(), name='new_event_api'),
    url(r'^api/delete_club/$',DeleteClubAPIView.as_view(), name='delete_club'),
    url(r'^api/members_records/$', ClubMemberAPIView.as_view(), name='club_members'),
    url(r'^api/member_approve/$', ClubMemberApproveView.as_view(), name='approval'),
    url(r'^api/member_reject/$', ClubMemberDeleteAPIView.as_view(), name='reject'),
    url(r'^api/club_membership/$', AddMemberToClub.as_view(), name='new_club_member'),
    # url(r'^api/show_voting_choices/$', ShowVotingChoicesAPIView.as_view(), name='voting_choices'),
    # url(r'^api/delete_poll/$', VotingPollsDeleteAPIView.as_view(), name='delete poll'),
    # url(r'^api/vote/$', VoteIncrementAPIView.as_view(), name='give vote'),
    url(r"^api/edit_session/$", SessionUpdateAPIView.as_view(), name="edit session"),
    url(r"^api/edit_event/$", EventUpdateAPIView.as_view(), name="edit event"),
    url(
        r"^api/delete_budget/$", DeleteClubBudgetAPIView.as_view(), name="delete budget"
    ),
    url(
        r"^api/upload_activitycalender/$",
        UploadActivityCalendarAPIView.as_view(),
        name="calender",
    ),
    url(r"^api/create_club/$", CreateClubAPIView.as_view(), name="new club"),
    url(
        r"^api/update_clubStatus/$",
        UpdateClubStatusAPIView.as_view(),
        name="update club status",
    ),
    url(
        r"^api/updateClubName/$",
        UpdateClubNameAPIView.as_view(),
        name="update club name",
    ),
    url(r"^api/approve_event/$", ApproveEvent.as_view(), name="approve event"),
    # add club api
    url(r"^api/add_club/$", AddClubAPI.as_view(), name="add club"),
    # new budget api
    url(r"^api/new_budget/$", NewBudgetAPIView.as_view(), name="new budget"),
    # fic approve budget api
    url(
        r"^api/fic_approve_budget/$",
        FICApproveBudgetAPIView.as_view(),
        name="fic approve budget",
    ),
    # counsellor approve budget api
    url(
        r"^api/counsellor_approve_budget/$",
        CounsellorApproveBudgetAPIView.as_view(),
        name="counsellor approve budget",
    ),
    # dean approve budget api
    url(
        r"^api/dean_approve_budget/$",
        DeanApproveBudgetAPIView.as_view(),
        name="dean approve budget",
    ),
    url(r'^api/dean_review_budget/$', DeanReviewBudgetAPIView.as_view(), name = 'review budget'),
    # new event api
    url(r"^api/new_events/$", NewEventAPIView.as_view(), name="new events"),
    # fic approve event api
    url(
        r"^api/fic_approve_event/$",
        FICApproveEventAPIView.as_view(),
        name="fic approve event",
    ),
    # counsellor approve event api
    url(
        r"^api/counsellor_approve_event/$",
        CounsellorApproveEventAPIView.as_view(),
        name="counsellor approve event",
    ),
    # dean approve event api
    url(
        r"^api/dean_approve_event/$",
        DeanApproveEventAPIView.as_view(),
        name="dean approve event",
    ),
    url(
        r"^api/add_achievement/$", AddAchievementAPIView.as_view(), name="approve event"
    ),
    url(
        r"^api/show_achievement/$", AchievementsAPIView.as_view(), name="approve event"
    ),
    url(
        r"^api/create_budget_comment/$",
        CreateBudgetCommentAPIView.as_view(),
        name="create budget comment",
    ),
    url(
        r"^api/create_event_comment/$",
        CreateEventCommentAPIView.as_view(),
        name="create event comment",
    ),
    url(
        r"^api/list_budget_comments/$",
        ListBudgetCommentsAPIView.as_view(),
        name="list budget comments",
    ),
    url(
        r"^api/list_event_comments/$",
        ListEventCommentsAPIView.as_view(),
        name="list event comments",
    ),
    url(r"^api/modify_event/$", ModifyEventAPIView.as_view(), name="modify event"),
    url(r"^api/modify_budget/$", ModifyBudgetAPIView.as_view(), name="modify budget"),
    url(r"^api/reject_event/$", RejectEventAPIView.as_view(), name="reject event"),
    url(r"^api/reject_budget/$", RejectBudgetAPIView.as_view(), name="reject budget"),
    url(
        r"^api/add_club_position/$",
        AddClubPositionAPIView.as_view(),
        name="add club position",
    ),
    url(
        r"^api/list_club_position/$",
        ListClubPositionAPIView.as_view(),
        name="list club position",
    ),
    url(r"^api/new_event/$", UpdateEventAPIView.as_view(), name="update event"),
    url(r"^api/update_event/$", UpdateEventAPIView.as_view(), name="update event"),
    url(r"^api/update_budget/$", UpdateBudgetAPIView.as_view(), name="update budget"),
    url(r"^fest/$" , FestListView.as_view(), name="fest"),
    url(r'^api/new_fest/$', NewFestAPIView.as_view(), name='new_fest'),
    url(r'^api/event_allocation/$',  FreeMembersForClubAPIView.as_view(), name='event allocation'),
    url(r'^api/coordinator_events/$', CoordinatorEventsAPIView.as_view(), name='coordinator_events'),
    url(r'^api/coordinator_eventsinput/$', EventInputAPIView.as_view(), name='coordinator_eventsinput'),
    url(r'^api/newsletter_pdf/$', NewsletterPDFAPIView.as_view(), name='newsletter_pdf'),
    url(r'^api/event_report_list/$', EventReportListAPIView.as_view(), name='event_report_list'),
    url(r'^api/add_event_report/$', EventReportAPIView.as_view(), name='add_event_report'),
    url(r'^api/event_report_pdf/(?P<report_id>\d+)/$', EventReportPDFView.as_view(), name='event_report_pdf'),
    url(r'^api/update_budget/$',  UpdateBudgetAPIView.as_view(), name='update event'),
]
