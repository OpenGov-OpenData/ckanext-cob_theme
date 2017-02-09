import ckan.lib.helpers as h
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


def recent_datasets(num=5):
    """Return a list of recent datasets."""
    sorted_datasets = []
    datasets = toolkit.get_action('current_package_list_with_resources')({},{'limit': num})
    if datasets:
        sorted_datasets = sorted(datasets, key=lambda k: k['metadata_modified'], reverse=True)
    return sorted_datasets[:num]


def popular_datasets(num=5):
    """Return a list of popular datasets."""
    datasets = []
    search = toolkit.get_action('package_search')({},{'rows': num, 'sort': 'views_recent desc'})
    if search.get('results'):
        datasets = search.get('results')
    return datasets[:num]


def dataset_count():
    """Return a count of all datasets"""
    count = 0
    result = toolkit.get_action('package_search')({}, {'rows': 1})
    if result.get('count'):
        count = result.get('count')
    return count


def groups(num=12):
    """Return a list of groups"""
    groups = toolkit.get_action('group_list')({}, {'all_fields': True, 'sort': 'packages'})
    return groups[:num]


def showcases(num=24):
    """Return a list of showcases"""
    sorted_showcases = []
    try:
        showcases = toolkit.get_action('ckanext_showcase_list')({},{})
        sorted_showcases = sorted(showcases, key=lambda k: k.get('metadata_modified'), reverse=True)
    except:
        print "[cob_theme] Error in retrieving list of showcases"
    return sorted_showcases[:num]


def get_package_metadata(package):
    """Return the metadata of a dataset"""
    result = toolkit.get_action('package_show')(None, {'id': package.get('name'), 'include_tracking': True})
    return result


def is_facet_active(name):
    """Returns if a facet is active or not"""
    facet_items = h.get_facet_items_dict(name)
    for item in facet_items:
        if item.get('active'):
            return True
    return False


def abbr_name(name):
    """Returns an abbreviation"""
    name_snippets = name.split()
    res = ""
    for s in name_snippets:
        res += s[0].upper()
    return res


def is_resource_data_format_downloadable(resourceDataFormat):
    """Return if a resource is downloadable or not"""
    if isinstance(resourceDataFormat, basestring):
        if resourceDataFormat.upper() in ["ESRI REST", "HTML", ""]:
            return False
    return True


class Cob_ThemePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)
    plugins.implements(plugins.IFacets)
    
    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'cob_theme')
    
    def get_helpers(self):
        """Register cob_theme_* helper functions"""
        
        return {'cob_theme_recent_datasets': recent_datasets,
                'cob_theme_popular_datasets': popular_datasets,
                'cob_theme_dataset_count': dataset_count,
                'cob_theme_get_groups': groups,
                'cob_theme_get_showcases': showcases,
                'cob_theme_get_package_metadata': get_package_metadata,
                'cob_theme_is_facet_active':is_facet_active,
                'cob_theme_abbr_name': abbr_name,
                'cob_theme_is_resource_data_format_downloadable': is_resource_data_format_downloadable,
               }

    def dataset_facets(self, facets_dict, package_type):
        self._update_facets(facets_dict)
        return facets_dict

    def group_facets(self, facets_dict, group_type, package_type):
        self._update_facets(facets_dict)
        return facets_dict

    def organization_facets(self, facets_dict, organization_type, package_type):
        self._update_facets(facets_dict)
        return facets_dict

    def _update_facets(self, facets_dict):
        #facets_dict.update({
        #    'provider': plugins.toolkit._('Provider'),
        #})
        pass
