from django.conf.urls import url
from lab6.apps.db_app import views
from lab6.apps.db_app.views import FilmsList, ActorsList, FilmmakersList, Film_writersList, ProducersList, CameramenList, CountriesList


urlpatterns = [
    url(r'^main/', views.main, name='main_url'),
    url(r'^films/', FilmsList.as_view(), name='films_url'),
    url(r'^actors/', ActorsList.as_view(), name='actors_url'),
    url(r'^filmmakers/', FilmmakersList.as_view(), name='filmmakers_url'),
    url(r'^film_writers/', Film_writersList.as_view(), name='film_writers_url'),
    url(r'^producers/', ProducersList.as_view(), name='producers_url'),
    url(r'^cameramen/', CameramenList.as_view(), name='cameramen_url'),
    url(r'^countries/', CountriesList.as_view(), name='countries_url'),
    url(r'^registration/', views.registration, name='reg_url'),
    url(r'^registration2/', views.registration2, name='reg2_url'),
    url(r'^login/', views.login, name='login_url'),
    url(r'^account/', views.account, name='account_url'),
    url(r'^logout/', views.logout, name='logout_url'),
]
