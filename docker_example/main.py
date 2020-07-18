from flask import Flask 
app = Flask(__name__) 
  
@app.route('/') 
def hello(): 
    return "This is Docker Example"
  
  
if __name__ == "__main__": 
    app.run(port = 5001, debug = True)
    #app.run(host ='0.0.0.0', port = 5001, debug = True)  


# docker commands 

 #docker build --tag flask-docker-demo-app .

 #docker run --name flask-docker-demo-app -p 5001:5001 flask-docker-demo-app

 # docker images

 # docker ps 

 # docker stop container_id