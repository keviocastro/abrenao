import sys
from openalpr import Alpr

alpr = Alpr("br", "/srv/openalpr/config/openalpr.conf.defaults", "/srv/openalpr/config/runtime_data")
if not alpr.is_loaded():
    print("Error loading OpenALPR")
    sys.exit(1)
else:
    print("Using OpenALPR version %s" % alpr.get_version())

def get_plate_number(image_path):
    results = alpr.recognize_file(image_path)
    
    print("Plate Number: %s" % plate['plate'])
    print("Confidence: %f" % plate['confidence'])

    for plate in results['results']:
        return plate['plate']

def unload_model():
    alpr.unload()
