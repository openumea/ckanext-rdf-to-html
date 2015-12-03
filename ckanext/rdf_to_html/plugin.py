import ckan.plugins as p
import ckan.plugins.toolkit as tk
import ckan.plugins.interfaces as interfaces


class RDFToHTMLPlugin(p.SingletonPlugin):
    """
    This plugin allows for showing RDF data on the dataset overview page.
    The data must be loaded with the ckan-uploader present in this repository.

    More information on how this works can be found in the readme.
    """
    p.implements(interfaces.IPackageController)
    p.implements(p.IConfigurer)

    def update_config(self, config):
        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        tk.add_template_directory(config, 'templates')

    def read(self, entity):
        pass

    def create(self, entity):
        pass

    def edit(self, entity):
        pass

    def authz_add_role(self, object_role):
        pass

    def authz_remove_role(self, object_role):
        pass

    def delete(self, entity):
        pass

    def after_create(self, context, pkg_dict):
        pass

    def after_update(self, context, pkg_dict):
        pass

    def after_delete(self, context, pkg_dict):
        pass

    def after_show(self, context, pkg_dict):
        # Convert all dcat extras to separate list
        dcat = []
        to_remove = []
        for extra in pkg_dict['extras']:
            # Skip non dcat fields
            if not extra['key'].startswith('_dcat_field_'):
                continue

            to_remove.append(extra)
            # Remove the prefix: _dcat_field_
            extra['key'] = extra['key'][12:]

            # Convert from the internal CKAN storage format
            split1 = extra['key'].split(';')
            split2 = extra['value'].split(';')
            objs = []
            for i in range(0, len(split2), 2):
                objs.append({
                    'link': split2[i],
                    'title': split2[i+1],
                })

            dcat.append({
                'pred_link': split1[0],
                'pred_title': split1[1],
                'objs': objs,
            })

        # Add them as a separate entry in the dict
        # and remove them from the extras
        pkg_dict['dcat_fields'] = sorted(dcat, key=lambda k: k['pred_title'])
        for item in to_remove:
            pkg_dict['extras'].remove(item)

        # Convert the dcat_about field
        dcat_about = None
        for extra in pkg_dict['extras']:
            if extra['key'] == '_dcat_about_':
                dcat_about = extra
                break

        if dcat_about:
            pkg_dict['dcat_about'] = dcat_about['value']
            pkg_dict['extras'].remove(dcat_about)
        return pkg_dict

    def before_search(self, search_params):
        return search_params

    def after_search(self, search_results, search_params):
        return search_results

    def before_index(self, pkg_dict):
        return pkg_dict

    def before_view(self, pkg_dict):
        return pkg_dict



