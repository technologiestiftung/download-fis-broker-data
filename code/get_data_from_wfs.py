import geopandas as gpd
from owslib.wfs import WebFeatureService
from requests import Request
import warnings
import os, ssl
import argparse
import logging


###   Parameters   ###

argParser = argparse.ArgumentParser()

argParser.add_argument("-l",   "--layer",              help="The name of the layer. Use '-' instead of ':'")
argParser.add_argument("-v",   "--verbose",            help="Show more info", action="store_true"                          )
argParser.add_argument("-fp",  "--file_path",          help="Base path to store files with trailing slash",       default="./data/"   )
argParser.add_argument("-fn",  "--file_name",          help="Optional, by default it will be named like the layer.", required=False )
argParser.add_argument("-url", "--base_url",           help="Optional, by default FIS broker URL.",  default="https://fbinter.stadt-berlin.de/fb/wfs/data/senstadt/" )
argParser.add_argument("-of",  "--output_format",      help="Optional, by default 'text/xml; subtype=gml/3.2.1'",  default="text/xml; subtype=gml/3.2.1" )
# argParser.add_argument("-gp", "--gdal_path",         help="Path to gdal executable",              default="./includes/gdal/"   )
# argParser.add_argument("-box",  "--box",             help="Use bounding boxes", action="store_true"                      )

args = argParser.parse_args()

if (args.verbose):
    logger=logging.getLogger()
    logger.setLevel(logging.INFO)

if args.layer:
    layer_name = args.layer
else:
    logging.error("Please provide a layer name")
    quit()

if args.file_name:
    file_name = args.file_name
else:
    file_name = args.layer

file_path     = args.file_path
base_url      = args.base_url
output_format = args.output_format

layer_url     = base_url + layer_name
output_file   = file_path + file_name + ".geojson"


logging.info("Parameters:")
logging.info("layer: "         + layer_name)
logging.info("Base URL: "      + base_url)
logging.info("Layer url: "     + layer_url)
logging.info("File name: "     + file_name)
logging.info("File path "      + file_path)
logging.info("Output file: "   + output_file)
logging.info("Output Format: " + output_format)

###   Set up    ###

if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

###   Functions    ###

def get_wfs(wfs_layer_url, output_format, output_file):

    wfs = WebFeatureService(url=wfs_layer_url)
    wfs_layer = list(wfs.contents)[-1]
    logging.info('Layer from wfs ' + wfs_layer)
    params = dict(service='WFS', version="1.0.0", request='GetFeature',
        typeName=wfs_layer, outputFormat=output_format)

    # Parse the URL with parameters
    q = Request('GET', wfs_layer_url, params=params).prepare().url
    logging.info('Request WFS from ' + q)
    # Read data from URL
    data = gpd.read_file(q)

    logging.info('Writting to file' + output_file)
    data.to_file(output_file, driver="GeoJSON")

    logging.info('All done')

    #ogr2ogr -f gpkg s_wfs_baumbestand_an.gpkg WFS:"https://fbinter.stadt-berlin.de/fb/wfs/data/senstadt/s_wfs_baumbestand_an" s_wfs_baumbestand_an
    #ogr2ogr -f gpkg s_wfs_baumbestand_an.gpkg WFS:"https://fbinter.stadt-berlin.de/fb/wfs/data/senstadt/s_bparkplatz" s_wfs_baumbestand_an


get_wfs(layer_url, output_format, output_file)
exit()
