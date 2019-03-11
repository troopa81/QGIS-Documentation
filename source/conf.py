# -*- coding: utf-8 -*-
#
# QGIS Website documentation build configuration file, created by
# sphinx-quickstart on Fri Aug 23 10:59:00 2013.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('.'))

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.imgmath', 'sphinx.ext.intersphinx']


# Add any paths that contain templates here, relative to this directory.
templates_path = ['../themes/qgis-theme']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'docs/index'

# General information about the project.
project = u'QGIS Documentation Project'
copyright = u'2014, QGIS project'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = 'testing'
# The full version, including alpha/beta/rc tags.
release = 'testing'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['../output', "../i18n", "../resources", "../scripts"]
# for faster builds, you can exclude certain parts from the build
# uncomment one or more lines below, or construct such line yourself
# uncomment to exclude the processing algs from build
# exclude_patterns += ['docs/user_manual/processing_algs/*']
# uncomment to exclude the user manual from build
# exclude_patterns += ['docs/user_manual/*']
# uncomment to exclude training manual from build
# exclude_patterns += ['docs/training_manual/*']
# uncomment to exclude developer guides from build
# exclude_patterns += ['docs/developers_guide/*']
# uncomment to exclude doc guides from build
# exclude_patterns += ['docs/documentation_guidelines/*']
# uncomment to exclude gentle intro  from build
# exclude_patterns += ['docs/gentle_gis_introduction/*']
# uncomment to exclude pyqgis dev book from build
# exclude_patterns += ['docs/pyqgis_developer_cookbook/*']

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False

intersphinx_mapping = {'pyqgis_api': ('https://qgis.org/pyqgis/master/', None)}

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'basic'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = ""

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = '../static/common/logo.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['../themes/qgis-theme/static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%H:%M %b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
html_sidebars = {
    #'site/index': [],
    #'site/about/**': ['myglobaltoc.html'],
    #'site/about/index': [],
    #'site/forusers/**': ['myglobaltoc.html'],
    #'site/forusers/index': [],
    #'site/forusers/download': [],
    ##'site/getinvolved/**': ['myglobaltoc.html'],
    #'site/getinvolved/index': [],
    #'site/getinvolved/donations': [],
#    'docs/index': ['myglobaltoc.html'],
#    'docs/**': ['mylocaltoc.html'],
    'index': ['myglobaltoc.html'],
    'search': [],
    '**': ['myglobaltoc.html'],
}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False # default to True
html_copy_source = False # NOT copying source, meaning we have search results without context

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = False

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'QGISWebsitedoc'

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
 'papersize': 'a4paper',

  # The font size ('10pt', '11pt' or '12pt').
  #'pointsize': '10pt',

  # Additional stuff for the LaTeX preamble.
  'preamble': u'''\\usepackage{combelow}
    \\usepackage{newunicodechar}
    \\newunicodechar{Ș}{\\cb{S}}
    \\newunicodechar{ș}{\\cb{s}}
    \\newunicodechar{Ț}{\\cb{T}}
    \\newunicodechar{ț}{\\cb{t}}
    '''
}

rst_prolog = """
.. role:: disclaimer
"""
#.. |updatedisclaimer| replace:: :disclaimer:`Docs for 'QGIS testing'. Visit https://docs.qgis.org/2.18 for QGIS 2.18 docs and translations.`
#"""

# Substitutions below are sorted and should be in lowerCamelCase
# NOTE that for inline images (like button and menu icons inline in text) you HAVE TO make a substitution
# so ONLY use common for this kind of images

# rst_epilog = ""

# -- Options for LaTeX output --------------------------------------------------

# The paper size ('letter' or 'a4').
# latex_paper_size = 'a4'  # deprecated, now in latex_elements

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('docs/user_manual/index', 'QGISUserGuide.tex', u'QGIS User Guide', u'QGIS Project', 'manual'),
  ('docs/pyqgis_developer_cookbook/index', 'PyQGISDeveloperCookbook.tex', u'PyQGIS developer cookbook', u'QGIS Project', 'manual'),
  ('docs/training_manual/index', 'QGISTrainingManual.tex', u'QGIS Training Manual', u'QGIS Project', 'manual'),
  ('docs/developers_guide/index', 'QGISDevelopersGuide.tex', u'QGIS Developers Guide', u'QGIS Project', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
latex_use_parts = False

# Additional stuff for the LaTeX preamble.
#latex_preamble = ''

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_use_modindex = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'qgiswebsite', u'QGIS Website Documentation',
     [u'QGIS Contributors'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'QGISWebsite', u'QGIS Website Documentation',
   u'QGIS Contributors', 'QGISWebsite', 'One line description of project.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False

locale_dirs = ['../i18n/']
gettext_compact = False

figure_language_filename = '{path}{language}/{basename}{ext}'

# adding this because in pycookbook a lot of text is referencing classes, which cannot be found by sphinx
# eg: Map canvas is implemented as :class:`QgsMapCanvas` ...
# I hope somebody will create the real references for these so they can be removed here...
nitpick_ignore = [('py:class', 'QAction'),
                  ('py:class', 'QDomElement'),
                  ('py:class', 'QFileInfo'),
                  ('py:class', 'QGraphicsScene'),
                  ('py:class', 'QgsAccessControlFilter'),
                  ('py:class', 'QgsCategorizedSymbolRenderer'),
                  ('py:class', 'QgsComposerItem'),
                  ('py:class', 'QgsComposition'),
                  ('py:class', 'QgsCoordinateReferenceSystem'),
                  ('py:class', 'QgsCoordinateTransform'),
                  ('py:class', 'QgsDataSourceUri'),
                  ('py:class', 'QgsDistanceArea'),
                  ('py:class', 'QgsEditError'),
                  ('py:class', 'QgsExpression'),
                  ('py:class', 'QgsFeature'),
                  ('py:class', 'QgsFeatureRendererV2'),
                  ('py:class', 'QgsFields'),
                  ('py:class', 'QgsFillSymbol'),
                  ('py:class', 'QgsFillSymbolV2'),
                  ('py:class', 'QgsGeometry'),
                  ('py:class', 'QgsGraduatedSymbolRenderer'),
                  ('py:class', 'QgsGraphAnalyzer'),
                  ('py:class', 'QgsInterface'),
                  ('py:class', 'QgisInterface'),
                  ('py:class', 'QgsLayerTreeMapCanvasBridge'),
                  ('py:class', 'QgsLineSymbol'),
                  ('py:class', 'QgsLogger'),
                  ('py:class', 'QgsMapCanvasItem'),
                  ('py:class', 'QgsMapCanvasItem'),
                  ('py:class', 'QgsMapCanvasMap'),
                  ('py:class', 'QgsMapRenderer'),
                  ('py:class', 'QgsMapRendererJob'),
                  ('py:class', 'QgsMapServiceException'),
                  ('py:class', 'QgsMapTool'),
                  ('py:class', 'QgsMapToolPan'),
                  ('py:class', 'QgsMapToolZoom'),
                  ('py:class', 'QgsMarkerSymbol'),
                  ('py:class', 'QgsMessageBar'),
                  ('py:class', 'QgsMessageLog'),
                  ('py:class', 'QgsPoint'),
                  ('py:class', 'QgsPointXY'),
                  ('py:class', 'QgsProject'),
                  ('py:class', 'QgsRasterLayer'),
                  ('py:class', 'QgsRasterDataProvider'),
                  ('py:class', 'QgsRasterIdentifyResult'),
                  ('py:class', 'QgsRasterRenderer'),
                  ('py:class', 'QgsRendererV2AbstractMetadata'),
                  ('py:class', 'QgsRendererRegistry'),
                  ('py:class', 'QgsRendererV2Widget'),
                  ('py:class', 'QgsRequestHandler'),
                  ('py:class', 'QgsRubberBand'),
                  ('py:class', 'QgsServerFilter'),
                  ('py:class', 'QgsServerInterface'),
                  ('py:class', 'QgsSingleSymbolRenderer'),
                  ('py:class', 'QgsStyleV2'),
                  ('py:class', 'QgsSymbolLayer'),
                  ('py:class', 'QgsSymbolLayerV2Registry'),
                  ('py:class', 'QgsSymbol'),
                  ('py:class', 'QgsSymbolV2'),
                  ('py:class', 'QgsTask'),
                  ('py:class', 'QgsTaskManager'),
                  ('py:class', 'QgsVectorColorRampV2'),
                  ('py:class', 'QgsVectorFileWriter'),
                  ('py:class', 'QgsVectorLayer'),
                  ('py:class', 'QgsVectorLayerEditUtils'),
                  ('py:class', 'QgsVertexMarker'),
                  ('py:class', 'QMenu'),
                  ('py:class', 'QSettings'),
                  ('py:class', 'QgsSymbolLayerRegistry'),
                  ('py:class', 'QgsFeatureRenderer'),
                  ('py:class', 'QgsRendererWidget'),
                  ('py:class', 'QgsStyle'),
                  ('py:class', 'QgsRendererAbstractMetadata'),

                  ('py:data', 'iface'),
                  ('py:data', 'qgis.utils.iface'),

                  ('py:func', 'addFeatures'),
                  ('py:func', 'addPluginToDatabaseMenu'),
                  ('py:func', 'addPluginToMenu'),
                  ('py:func', 'addPluginToRasterMenu'),
                  ('py:func', 'addPluginToVectorMenu'),
                  ('py:func', 'addPluginToWebMenu'),
                  ('py:func', 'angle'),
                  ('py:func', 'asMultiPoint'),
                  ('py:func', 'asMultiPolygon'),
                  ('py:func', 'asMultiPolyline'),
                  ('py:func', 'beginEditCommand'),
                  ('py:func', 'capabilities'),
                  ('py:func', 'capabilitiesString'),
                  ('py:func', 'changed'),
                  ('py:func', 'classAttribute'),
                  ('py:func', 'classFactory'),
                  ('py:func', 'clone'),
                  ('py:func', 'color'),
                  ('py:func', 'commitChanges'),
                  ('py:func', 'contains'),
                  ('py:func', 'create*'),
                  ('py:func', 'createRenderer'),
                  ('py:func', 'createRendererWidget'),
                  ('py:func', 'createSimple'),
                  ('py:func', 'createSpatialIndex'),
                  ('py:func', 'createSymbolLayer'),
                  ('py:func', 'createSymbolLayerWidget'),
                  ('py:func', 'destroyEditCommand'),
                  ('py:func', 'difference'),
                  ('py:func', 'dijkstra'),
                  ('py:func', 'dump'),
                  ('py:func', 'endEditCommand'),
                  ('py:func', 'executeRequest'),
                  ('py:func', 'exitQgis'),
                  ('py:func', 'features'),
                  ('py:func', 'fields'),
                  ('py:func', 'getFeatures'),
                  ('py:func', 'hide'),
                  ('py:func', '__init__'),
                  ('py:func', 'identify'),
                  ('py:func', 'initAttributes'),
                  ('py:func', 'initGui'),
                  ('py:func', 'initGui()'),
                  ('py:func', 'initQgis'),
                  ('py:func', 'instance'),
                  ('py:func', 'intersects'),
                  ('py:func', 'isEditable'),
                  ('py:func', 'isMultipart'),
                  ('py:func', 'isValid'),
                  ('py:func', 'label'),
                  ('py:func', 'layerType'),
                  ('py:func', 'mode'),
                  ('py:func', 'nextFeature'),
                  ('py:func', 'pendingFields'),
                  ('py:func', 'properties'),
                  ('py:func', 'QgsApplication.setPrefixPath'),
                  ('py:func', 'QgsCoordinateReferenceSystem.createFromString'),
                  ('py:func', 'QgsExpression.prepare'),
                  ('py:func', 'read()'),
                  ('py:func', 'read'),
                  ('py:func', 'registerFilter'),
                  ('py:func', 'renderer'),
                  ('py:func', 'renderPoint'),
                  ('py:func', 'renderPolygon'),
                  ('py:func', 'renderPolyline'),
                  ('py:func', 'requestReady'),
                  ('py:func', 'requestReady()'),
                  ('py:func', 'responseComplete'),
                  ('py:func', 'rollBack'),
                  ('py:func', 'sample'),
                  ('py:func', 'selectedFeatures'),
                  ('py:func', 'sendResponse'),
                  ('py:func', 'sendResponse()'),
                  ('py:func', 'serverClassFactory'),
                  ('py:func', 'setClassAttribute'),
                  ('py:func', 'setColor'),
                  ('py:func', 'setDataSource'),
                  ('py:func', 'setIcon'),
                  ('py:func', 'setLimit'),
                  ('py:func', 'setMapTool'),
                  ('py:func', 'setRenderer'),
                  ('py:func', 'select'),
                  ('py:func', 'setSelectionColor'),
                  ('py:func', 'setSymbol'),
                  ('py:func', 'setSymbolLayer'),
                  ('py:func', 'shortestTree'),
                  ('py:func', 'show'),
                  ('py:func', 'size'),
                  ('py:func', 'showPluginHelp'),
                  ('py:func', 'sourceColorRamp'),
                  ('py:func', 'sourceSymbol'),
                  ('py:func', 'startEditing'),
                  ('py:func', 'startRender'),
                  ('py:func', 'stopRender'),
                  ('py:func', 'symbol'),
                  ('py:func', 'symbolForFeature'),
                  ('py:func', 'symbolLayer'),
                  ('py:func', 'transform'),
                  ('py:func', 'type'),
                  ('py:func', 'union'),
                  ('py:func', 'unload'),
                  ('py:func', 'unload()'),
                  ('py:func', 'usedAttributes'),
                  ('py:func', 'value'),
                  ('py:func', 'value()'),
                  ('py:func', 'width'),
                  ('py:func', 'wkbType'),
                  ('py:func', 'write'),
                  ('py:func', 'writeEntry'),
                  ('py:func', 'x'),
                  ('py:func', 'y'),

                  ('py:obj', 'QgsFeatureRequest'),
                  ('py:obj', 'QgsExpression'),

                  ('py:const', 'EpsgCrsId'),
                  ('py:const', 'InternalCrsId'),
                  ('py:const', 'PostgisCrsId'),
                  ('py:const', 'True'),

                  ('py:mod', 'qgis.core'),
                  ('py:mod', 'qgis.gui'),
                  ('py:mod', 'qgis.utils'),
                  ('py:meth', 'qgis.core.QgsVectorDataProvider.nextFeature'),
                  ('py:meth', 'qgis.core.QgsSymbol.angle'),
                  ('py:meth', 'qgis.core.QgsSymbol.width'),
                  ('py:meth', 'qgis.core.QgsSymbol.size'),
                  ('py:meth', 'qgis.core.QgsMarkerSymbolLayer.layerType'),
                  ('py:meth', 'qgis.core.QgsMarkerSymbolLayer.clone'),
                  ('py:meth', 'qgis.core.QgsMarkerSymbolLayer.stopRender'),
                  ('py:meth', 'qgis.core.QgsMarkerSymbolLayer.renderPolygon'),
                  ('py:meth', 'qgis.core.QgsMarkerSymbolLayer.renderPolyline'),
                  ]
