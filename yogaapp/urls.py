from django.urls import path
from . import views
app_name="yogaapp"

urlpatterns = [
    path('', views.index, name='index'),
    path('200HoursYogaTeachersTrainingCourse', views.twohundred, name='200HoursYogaTeachersTrainingCourse'),
    path('300HoursYogaTeachersTrainingCourse', views.threehundred, name='300HoursYogaTeachersTrainingCourse'),
    path('YogaPhilosophyTeachersTraining', views.philosophy, name='YogaPhilosophyTeachersTraining'),
    path('ChakraHealerCourse', views.chakra, name='ChakraHealerCourse'),
    path('AncientCosmicEnergyHealingProcess', views.cosmic, name='AncientCosmicEnergyHealingProcess'),
    path('PrenatalandPostnatalYogaTTC', views.natal, name='PrenatalandPostnatalYogaTTC'),
    path('whatsapp', views.whatsapp, name='whatsapp'),
    path('test', views.test, name='test'),
    path('instructor', views.instructor, name='instructor'),
    path('Become_A_Healer', views.Become_A_Healer, name='Become_A_Healer'),
    path('Spiritual_Retreat', views.Spiritual_Retreat, name='Spiritual_Retreat'),
    path('Contact', views.Contact, name='Contact'),
    path('sitemap', views.sitemap, name='sitemap'),
    path('robot', views.robot, name='robot'),

]

