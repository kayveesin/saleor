from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.views import serve
from django.views.i18n import javascript_catalog

from graphene_django.views import GraphQLView

from .cart.urls import urlpatterns as cart_urls
from .checkout.urls import urlpatterns as checkout_urls
from .core.sitemaps import sitemaps
from .core.urls import urlpatterns as core_urls
from .order.urls import urlpatterns as order_urls
from .product.urls import urlpatterns as product_urls
from .search.urls import urlpatterns as search_urls
from .userprofile.views import login as login_view
from .userprofile.urls import urlpatterns as userprofile_urls
from .data_feeds.urls import urlpatterns as feed_urls
from .dashboard.urls import urlpatterns as dashboard_urls
from .donation.urls import urlpatterns as donation_urls


urlpatterns = [
    url(r'^', include(core_urls)),
    url(r'^account/', include('allauth.urls')),
    url(r'^account/login', login_view, name="account_login"),
    url(r'^cart/', include(cart_urls, namespace='cart')),
    url(r'^checkout/', include(checkout_urls, namespace='checkout')),
    url(r'^dashboard/', include(dashboard_urls, namespace='dashboard')),
    url(r'^graphql', GraphQLView.as_view(graphiql=settings.DEBUG)),
    url(r'^jsi18n/$', javascript_catalog, name='javascript-catalog'),
    url(r'^order/', include(order_urls, namespace='order')),
    url(r'^products/', include(product_urls, namespace='product')),
    url(r'^profile/', include(userprofile_urls, namespace='profile')),
    url(r'^search/', include(search_urls, namespace='search')),
    url(r'^selectable/', include('selectable.urls')),
    url(r'^feeds/', include(feed_urls, namespace='data_feeds')),
    url(r'^donation/', include(donation_urls, namespace='donation')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
    url(r'', include('payments.urls'))
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += [
        url(r'^static/(?P<path>.*)$', serve)
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
