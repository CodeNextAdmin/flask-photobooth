# flask-photobooth - teaching version
 ** This version has the main code removed for instructional purposes. ** 
 
 A basic Flask-based Photobooth for demonstrating interaction between Raspberry Pi Camera and a Flask app. For use in Google's Code Next Team Edge program. 
 Use this project to highlight how to:
 - display dynamic content using Jinja2 (comes with Flask).
 - use a button to submit a POST request to Flask.
 - handle a POST request in Flask and return data.
 - run the picamera library inside a Flask project.
 - use timestamps to generate unique file names.
 - (optional) add CSS to the photobooth to make it pretty!
 
 
 ### Usage:
 
1. Clone the project.
2. Connect the Raspberry Pi camera to an arleady set up and updated Rpi.
3. Run `$ python app.py` and open on browser witht he given link from the Terminal, shold be: http://0.0.0.0:5000/
4. Take pics! Each pic will save in the static/images folder
5. http://0.0.0.0:5000/all will show all the captured images.

### Notes:
- This project uses [glob](https://docs.python.org/3/library/glob.html) to pattern-match all paths for the image files.

### Extend me!
This project is meant to be bare-bones and ugly. Coaches and instructors should use it to expand to other uses, or more advanced photobooths. Some examples 
could include:
- Adding a loop to multiple pictures with a loop and the sleep command, like a real photo booth.
- Adding more UI to navigate between pages.
- Adding option to send image(s) via email with another form wrapper and flask route.
- Connect Twilio API to send SMS with images.
- Add image effects (see [picamera library](https://picamera.readthedocs.io/en/release-1.13/recipes1.html))
- Add CSS to give it a nicer feel. 


