from django.conf.urls import patterns, url

from oscar.core.loading import get_class
from oscar.core.application import Application

MultiFacetedSearchView = get_class('search.views', 'MultiFacetedSearchView')
MultiFacetedSearchForm = get_class('search.forms', 'MultiFacetedSearchForm')


class SearchApplication(Application):
    name = 'search'
    search_view = MultiFacetedSearchView

    def get_urls(self):
        urlpatterns = patterns('',
            url(r'^$', self.search_view(form_class=MultiFacetedSearchForm), name='search'),
        )
        return self.post_process_urls(urlpatterns)


application = SearchApplication()