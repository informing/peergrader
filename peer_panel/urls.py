from django.conf.urls import url

from .views import PanelViews

urlpatterns = [
	url(r'^$', PanelViews.homepage),
	#url(r'^$', views.PanelViews.doo),
	# url(r'^articles/2003/$', views.special_case_2003),
	# url(r'^articles/([0-9]{4})/$', views.year_archive),
	# url(r'^articles/([0-9]{4})/([0-9]{2})/$', views.month_archive),
	# url(r'^articles/([0-9]{4})/([0-9]{2})/([0-9]+)/$', views.article_detail),
]
