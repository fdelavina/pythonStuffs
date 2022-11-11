import random
import time
import threading
from flask import Flask
from flask_json import FlaskJSON, JsonError, json_response, as_json

class NavigationData:
    lat = 0.0
    lon = 0.0
    heading = 0.0
    pitch = 0.0
    roll = 0.0
    speed = 0.0

    def createRandValue(self):
        self.lat     = random.uniform( 0.0  , 90.0)
        self.lon     = random.uniform( 0.0  , 180.0)
        self.heading = random.uniform(-180.0, 180.0)
        self.pitch   = random.uniform(-5.0  , 5.0)
        self.roll    = random.uniform(-5.0  , 5.0)
        self.speed   = random.uniform( 0.0  , 20.0) 
    
    def showData(self):
        
        print("latitud: ", (self.lat), "longitud: ", self.lon, "heading: ", self.heading, "pitch: ", self.pitch, "roll: ", self.roll, "speed: ", self.speed)


def runSimulation(navData):
    while(True):
        time.sleep(2.5)
        navData.createRandValue()
        #navData.showData()


def runServer(navData):
    app = Flask(__name__)
    FlaskJSON(app)
    @app.route('/getNavData')
    def getNavData():
        return json_response(latitud  = navData.lat, 
                             longitud = navData.lon,
                             heading  = navData.heading,
                             pitch    = navData.pitch,
                             roll     = navData.roll,
                             speed    = navData.speed)
        #return "hola"

    app.run(port=9500)

if __name__ == '__main__':
    navData = NavigationData()
    #runSimulation(navData)
    #runServer(navData)

    x = threading.Thread( target = runSimulation, args = (navData, ) )
    y = threading.Thread( target = runServer,     args = (navData, ) )
    x.start()
    y.start()

    x.join()
    y.join()
