from flask import *

app = Flask(__name__)

@app.route('/')

def index():
	return "Soyez les bienvenus...!<br> Foyer LORD.."

if __name__ == "__main__":
	app.run()
