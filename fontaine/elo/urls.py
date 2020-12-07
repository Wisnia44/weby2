from django.urls import path
from .views import (
	SendEmailView,
	CheckCompanyInfoView,
	CompareCompanyInfoView,
	TagView,
	TaxCalView,
	DaneKupView,
	OcrView,
	DownloadView,
	UploadView,
	HomeView
	)

urlpatterns = [
    path('sendemail/', SendEmailView.as_view(), name='sendemail'),
    path('checkinfo/', CheckCompanyInfoView.as_view(), name='checkinfo'),
    path('compare/', CompareCompanyInfoView.as_view(), name='compare'),
    path('tag/', TagView.as_view(), name='tag'),
    path('tax/', TaxCalView.as_view(), name='tax'),
    path('danekup/', DaneKupView.as_view(), name='danekup'),
    path('ocr/', OcrView.as_view(), name='ocr'),
    path('download/', DownloadView.as_view(), name='download'),
    path('upload/', UploadView.as_view(), name='upload'),
    path('', OcrView.as_view(), name='home'),
]