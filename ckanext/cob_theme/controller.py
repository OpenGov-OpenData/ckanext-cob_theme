# encoding: utf-8

import os.path
import ckan.lib.base as base
from ckan.common import c
import ckan.lib.helpers as h

render = base.render

class CobThemeController(base.BaseController):
  
    def render_docs(self,path):
        '''the controller for the docs page'''

        c.docTitle = path
        if not(os.path.isfile(os.path.dirname(__file__) + "/templates/docs/snippets/api/index.html")):
            return h.redirect_to('http://docs.ckan.org/en/latest/')     
        elif not(os.path.isfile(os.path.dirname(__file__) + "/templates/docs/snippets/" + path)):
            return h.redirect_to('/docs/api/index.html')
        else:
            return render("docs/doc_template.html")
            