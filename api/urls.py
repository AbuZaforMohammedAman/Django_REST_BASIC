from django.urls import path
#from status.views import StatusViewer, StatusUpdateView
#from status.views import StatusListView, StatusDeleteView
#from status.views import StatusCreateView, StatusDetailView
from status.views import StatusListCreateApiView, StatusDetailDeleteUpdateView

urlpatterns = [
    #path('status/<int:id>/', StatusViewer.as_view(), name='status_view'),
    #path('statuses/', StatusListView.as_view(), name='status_list_view'),
    path('status/', StatusListCreateApiView.as_view(), name='status_list_view'),
    #path('status/create/', StatusCreateView.as_view()),
    path('status/<pk>/', StatusDetailDeleteUpdateView.as_view()),
    #path('status/<pk>/', StatusDetailView.as_view()),
    #path('status/update/<pk>/', StatusUpdateView.as_view()),
    #path('status/delete/<pk>/', StatusDeleteView.as_view())
]
