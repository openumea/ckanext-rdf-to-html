# CKAN Extension RDF to HTML

This repository contains code for integrating the [RDF to HTML converter](https://github.com/openumea/RDFtoHTML) with
CKAN.

## Plugin
The plugin is responsible for converting the fields from extras into separate fields before sending the data to the templates (or to the API).
It also overrides templates to display the DCAT fields correctly.

## Upload script
An upload script for inserting data into CKAN can be found in the [RDF to HTML converter](https://github.com/openumea/RDFtoHTML).


## CKAN extension
The extension can be installed the same way other CKAN extensions are installed. Refer to the [official documentation](http://docs.ckan.org/en/latest/extensions/tutorial.html) if you don't know how
 to do this.

The only setup needed outside CKAN is to add the following line to the SOLR schema (if you use SOLR). It should be place inside the `<field>` tag. 
`<dynamicField name= "dcat_fields*" type="text" indexed="true" stored="true" multiValued="true"/>`

## Using the extension
The extension works by storing rdf metadata in the extras field for each dataset. To connect a dataset to a RDF resource you should visit the edit page for your dataset. There you will have an 
option to set a value for the `rdf:about` field. This should be set to the corresponding `rdf:about` tag in your RDF file.

The extension does not automatically fetch data from the RDF file as this would be to slow to do each time the page is loaded. You will have to use the upload script mentioned a couple of 
paragraphs above.

When run, this script will connect to a given CKAN instance and look at the `rdf:about` tag for each dataset and update them with data from given RDF file.
