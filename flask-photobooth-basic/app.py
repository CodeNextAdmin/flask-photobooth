from flask import Flask, render_template
import picamera
import datetime
import time
import glob
 
app = Flask(__name__)

@app.route('/')
def home():
    
    return render_template('index.html')       

@app.route('/capture', methods=["POST"])
def capture():
    camera = picamera.PiCamera()
    #use a timestamp to save pics with unique names based on seconds since 1970.
    picName=str(int(time.time())) 
    #picName="captured" 

    #build the file path to store the image
    photo="static/images/"+picName +".jpg"
    
    try:
        #comment out these 3 lines if no preview is desired.
        camera.start_preview()
        time.sleep(2)
        camera.stop_preview()
        #capture the photo to the specified path
        camera.capture(photo)
    finally:
        camera.close()
    
    print(photo)
    
    return render_template('index.html', photo=photo)      

@app.route("/all")
def show_all():
    
    #Use glob to return an array of paths to all pics. 
    #the * wildcard will pattern match any .jpg in our images folder.
    photos=glob.glob("static/images/*.jpg")

    return render_template('all.html', photos=photos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

    

