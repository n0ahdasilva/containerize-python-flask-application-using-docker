#
#   PROJECT : Containerize Python Flask Application Using Docker
# 
#   FILENAME : main.py
# 
#   DESCRIPTION :
#       Deploy a simple webserver application using the Flask library in Python. Then 
# 		containerize the application using Docker, with the use of Dockerfile and 
# 		docker-compose.yml
# 
#   FUNCTIONS :
#       main()
# 
#   NOTES :
#       - ...
# 
#   AUTHOR(S) : Noah Arcand Da Silva    START DATE : 2022.12.02 (YYYY.MM.DD)
#
#   CHANGES :
#       - ...
# 
#   VERSION     DATE        WHO             DETAILS
#   0.0.1a      2022.12.02  Noah            Creation of project.
#


from flask import Flask, request


app = Flask(__name__)

@app.route('/')
def get_remote_ip():
	remote_ip = request.remote_addr
	return f'<h1> You are connecting from {remote_ip}</h1>'

if __name__ == '__main__':
	app.run(host="0.0.0.0", debug=True)
