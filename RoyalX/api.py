from royalapp.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'sabab', Reason_view, basename='sabab')
router.register(r'student', Student_view, basename='student')
router.register(r'aboutus', Teacher_view, basename='aboutus')
router.register(r'contact', Contact_view, basename='contact')