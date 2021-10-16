from flask import Flask, render_template
import picamera
#TODO: add glob, time libraries

 
app = Flask(__name__)

@app.route('/')
def home():
    
    return render_template('index.html')       

@app.route('/capture', methods=["POST"])
def capture():
    camera = picamera.PiCamera()
    #Todo: use a timestamp to save pics with unique names.
   

    #Todo: build the file path to store the image
  
    
    try:
        
        camera.start_preview()
        time.sleep(2)
        camera.stop_preview()
        #TODO: capture the photo to the specified path
        
    finally:
        camera.close()
    
     
    #TODO: pass the data (path for image) to the template
    return render_template('index.html')      

@app.route("/all")
def show_all():
    
    #Use glob to return an array of paths to all pics. 
    #the * wildcard will pattern match any .jpg in our images folder.
     

    return render_template('all.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

    

