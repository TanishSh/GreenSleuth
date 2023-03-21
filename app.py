from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
import AItalk
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map, icons
#lib>[your python version]>site-packages>flask_googlemaps>templates>googlemaps>gmapjs.html and around line 46 -- fullscreenControl: blablabla , add a comma at the endf that line, save and test it.

text =  AItalk.report()
addressco, addressUrl = AItalk.address(text)



googleApp = Flask(__name__,template_folder='templates')
app = Flask(__name__,template_folder='report')
googleApp.config['GOOGLEMAPS_KEY'] = "AIzaSyD_ils9W_xYR9QAd5ZORGl8aF4pU0N4jTA"
GoogleMaps(googleApp,key="AIzaSyD_ils9W_xYR9QAd5ZORGl8aF4pU0N4jTA")

@googleApp.route('/')
def map_created_in_view():

    gmap = Map(
        identifier="gmap",
        varname="gmap",
        lat=37.4419,
        lng=-122.1419,
        center_on_user_location=[(float(addressco[0]), float(addressco[1]))],
        markers={
            icons.dots.red: [(float(addressco[0]), float(addressco[1]), text)],
        },
        styles="height:400pixels;width:600pixels;margin:0;",
    )

    return render_template("simple.html", gmap=gmap)





    # Get files with wav suffix
    #files = [os.path.join("../Downloads",f) for f in os.listdir('../Downloads') if f.endswith('.wav')]
    # filepath
    #files = "output.wav"
    
    # audioPath = files[-1]
    
    #return flask.jsonify({"coordinate": addressco, "report": text}),render_template('map.html', mymap=mymap)




if __name__ == '__main__':
   
    googleApp.run(port=5050)
    #app.run(port=5010)


    