import geopandas as gpd
from owslib.wfs import WebFeatureService
from requests import Request
import warnings
import os, ssl
import argparse
import logging

###   Parameters   ###

argParser = argparse.ArgumentParser()

argParser.add_argument("-l",  "--layer",             help="The name of the layer. Use '-' instead of ':'")
argParser.add_argument("-f",  "--output_file",       help="The name of the output file.", default="output" )
argParser.add_argument("-v",  "--verbose",           help="Show more info", action="store_true"                          )
argParser.add_argument("-fp", "--file_path",         help="Path to store files",       default="./data/"   )
# argParser.add_argument("-p",  "--prefix",            help="Prefix for the database.",             default=""   )
# argParser.add_argument("-dn", "--database_name",     help="Database name",                        default="Vienna_OGD"   )
# argParser.add_argument("-dh", "--database_host",     help="Database host, default localhost.",    default="localhost"    )
# argParser.add_argument("-dp", "--database_pass",     help="Database password.",                   default="postgres"     )
# argParser.add_argument("-do", "--database_port",     help="Database port.",                       default="5432"     )
# argParser.add_argument("-du", "--database_user",     help="Database user.",                       default="postgres"     )
# argParser.add_argument("-id", "--id",                help="Id for clean up",                      default="objectid"     )
# argParser.add_argument("-gp", "--gdal_path",         help="Path to gdal executable",              default="./includes/gdal/"   )
# argParser.add_argument("-box",  "--box",             help="Use bounding boxes", action="store_true"                      )

args = argParser.parse_args()

if (args.verbose):
    logger=logging.getLogger()
    logger.setLevel(logging.INFO)


if args.layer:
    layerName = args.layer
else:
    logging.error("Please provide a layer name")
    quit()

output_file        = args.output_file
file_path          = args.file_path

# prefix        = args.prefix
# database_name = args.database_name
# database_host = args.database_host
# database_pass = args.database_pass
# database_port = args.database_port
# database_user = args.database_user
# gdal_path     = args.gdal_path
# objectid      = args.id

logging.info("Parameters:")
logging.info("layer: "        + layerName)
logging.info("Output file: "  + output_file)
logging.info("File path "     + file_path)
# logging.info("database name: " + database_name)
# logging.info("database host: " + database_host)
# logging.info("database pass: " + database_pass)
# logging.info("database port: " + database_port)
# logging.info("database user: " + database_user)

###   Set up    ###


if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context


###   Functions    ###


def get_wfs(wfs_url, wfs_output_format, outfile_name):

    wfs = WebFeatureService(url=wfs_url)
    layer = list(wfs.contents)[-1]
    params = dict(service='WFS', version="1.0.0", request='GetFeature',
        typeName=layer, outputFormat=wfs_output_format)

    # Parse the URL with parameters
    q = Request('GET', wfs_url, params=params).prepare().url
    print('Request WFS from ' + q)
    # Read data from URL
    data = gpd.read_file(q)

    data.to_file(outfile_name + ".geojson", driver="GeoJSON")
    print('WFS was written to file' + outfile_name + ".geojson")


    #ogr2ogr -f gpkg s_wfs_baumbestand_an.gpkg WFS:"https://fbinter.stadt-berlin.de/fb/wfs/data/senstadt/s_wfs_baumbestand_an" s_wfs_baumbestand_an

    #ogr2ogr -f gpkg s_wfs_baumbestand_an.gpkg WFS:"https://fbinter.stadt-berlin.de/fb/wfs/data/senstadt/s_bparkplatz" s_wfs_baumbestand_an



# set urls to wfs services
wfs_trees_streets =   'https://fbinter.stadt-berlin.de/fb/wfs/data/senstadt/s_wfs_baumbestand'
wfs_trees_parks =     'https://fbinter.stadt-berlin.de/fb/wfs/data/senstadt/s_wfs_baumbestand_an'
k_alkis_gebaeude =    'https://fbinter.stadt-berlin.de/fb/wfs/data/senstadt/s_wfs_alkis_gebaeudeflaechen'
#'https://fbinter.stadt-berlin.de/fb/wfs/data/senstadt/s_bparkplatz'
# Specify the output Format of the WFS for fetching the data
wfs_output_format = 'text/xml; subtype=gml/3.2.1'
new_trees_streets_filename = "tree_data/data_files/s_wfs_baumbestand_apr22"
new_trees_parks_filename = "tree_data/data_files/s_wfs_baumbestand_an_apr22"
k_alkis_gebaeude_filename = "tree_data/data_files/k_alkis_gebaeude"


get_wfs(layerName, wfs_output_format, output_file)
exit()


# get_wfs(wfs_trees_streets, wfs_output_format, new_trees_streets_filename)
# get_wfs(wfs_trees_parks, wfs_output_format, new_trees_parks_filename)

#new_trees.to_file(new_trees_filename + ".json", driver="GeoJSON")
