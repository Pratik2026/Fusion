from django.conf.urls import url

from . import views
from applications.scholarships.api.views import GetWinnersView
from applications.scholarships.api.views import create_award,McmUpdateView, McmRetrieveView, DirectorSilverRetrieveView,DirectorSilverUpdateView,DirectorGoldRetrieveView,DirectorGoldUpdateView,ProficiencyDmRetrieveView,ProficiencyDmUpdateView,AwardAndScholarshipCreateView,DirectorSilverMarksheetView,DirectorGoldMarksheetView
from applications.scholarships.api.views import ScholarshipDetailView,StudentDetailView,DirectorSilverDetailView,DirectorGoldDetailView,DirectorGoldListView,ReleaseCreateView,McmStatusUpdateView,DirectorSilverDecisionView,DirectorGoldAcceptRejectView,DirectorSilverListView,GetReleaseByAwardView,McmDocumentsRetrieveView
app_name = 'spacs'

urlpatterns = [

    # url(r'^$', views.spacs, name='spacs'),
    # url(r'^student_view/$', views.student_view, name='student_view'),
    # url(r'^convener_view/$', views.convener_view, name='convener_view'),
    # url(r'^staff_view/$', views.staff_view, name='staff_view'),
    # url(r'^stats/$', views.stats, name='stats'),
    # url(r'^convenerCatalogue/$', views.convenerCatalogue, name='convenerCatalogue'),
    # url(r'^getWinners/$', views.getWinners, name='getWinners'),
    # url(r'^get_MCM_Flag/$', views.get_MCM_Flag, name='get_MCM_Flag'),
    # url(r'^getConvocationFlag/$', views.getConvocationFlag, name='getConvocationFlag'),
    # url(r'^getContent/$', views.getContent, name='getContent'),
    # url(r'^updateEndDate/$', views.updateEndDate, name='updateEndDate'),
    url('get-winners/', GetWinnersView.as_view(), name='get-winners')
    
]