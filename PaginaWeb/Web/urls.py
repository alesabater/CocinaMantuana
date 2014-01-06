from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PaginaWeb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'PaginaWeb.Web.views.index'),
    url(r'^productos/$', 'PaginaWeb.Web.views.productos'),
    url(r'^encuentranos/$', 'PaginaWeb.Web.views.encuentranos'),
    url(r'^contacto/$', 'PaginaWeb.Web.views.contacto'),
    url(r'^encuentranos-detalle/(?P<id>\w+)/$', 'PaginaWeb.Web.views.encuentranosdetalle'),
    url(r'^enviar-correo/$', 'PaginaWeb.Web.views.enviarMail'),
    url(r'^eventos/$', 'PaginaWeb.Web.views.eventos'),
)
