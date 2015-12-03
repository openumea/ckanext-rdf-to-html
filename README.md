# CKAN Extension RDF to HTML

This repository contains code for integrating the [RDF to HTML converter](https://github.com/openumea/RDFtoHTML) with
CKAN.

This application consists of two parts, the CKAN plugin and a script for uploading RDF data to CKAN.

## Upload script
The script is located in the ckan-loader package. When run it will check in CKAN for datasets that have a
rdf_about field (which can be set when editing a dataset if you have installed the plugin) and upload this data
to the given CKAN instance.

The data is saved using the "extras" field in CKAN. To distinguish these fields from regular extras they will have the prefix `_dcat_value_`.

## Plugin
The plugin is responsible for converting the fields from extras into separate fields before sending the data to the templates (or to the API).
It also overrides templates to display the DCAT fields correctly.

## Setup

### Plugin

The plugin also requires the solr schema to be changed so the fields tag includes this entry 
`<dynamicField name= "dcat_fields*" type="text" indexed="true" stored="true" multiValued="true"/>`

### Upload Script