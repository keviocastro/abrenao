from openalpr import Alpr

alpr = Alpr("br", "openalpr.conf", "runtime_data")
if not alpr.is_loaded():
    print("Error loading OpenALPR")
else:
    print("Using OpenALPR version %s" % alpr.get_version())

results = alpr.recognize_file("car_image.jpg")
for plate in results['results']:
    print("Plate Number: %s" % plate['plate'])
    print("Confidence: %f" % plate['confidence'])

alpr.unload()
