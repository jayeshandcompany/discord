from threading import Thread
from flask import Flask # Import Flask Class
app = Flask('') # Create an Instance

@app.route('/') # Route the Function
def main(): # Run the function
	return 'Hello World'
def run():
  app.run(host='0.0.0.0', port=5000) 
def keep():
  t=Thread(target=run)
  t.start()  
# Run the Application (in debug mode)