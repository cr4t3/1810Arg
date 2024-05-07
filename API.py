from flask import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def read():
    return int(open("highscore.txt", "r").read())

def update(new: int):
    try:
        with open("highscore.txt", "w") as _:
            _.write(str(new))
            _.close()
            return
    except:
        print("An exception has ocurred")

spawn_vel = 500
percentage = 30
vel_per_100 = 0.5
score_add = 0.25

@app.route("/percentage/<int:percentage>", methods=["POST"])
def percentagepost(percentage_):
    global percentage
    percentage = percentage_
    return make_response(str(percentage), 200)

@app.route('/percentage', methods=['GET'])
def percentageget():
    return make_response(str(percentage), 200)

@app.route('/vel/<int:vel>', methods=['POST'])
def velpost(vel):
    global vel_per_100
    vel_per_100 = vel
    return make_response(str(vel_per_100), 200)

@app.route('/vel', methods=['GET'])
def velget():
    return make_response(str(vel_per_100), 200)

@app.route('/score/<float:score>', methods=['POST'])
def scorepost(score):
    global score_add
    score_add = score
    return make_response(str(score_add), 200)

@app.route('/score', methods=['GET'])
def scoreget():
    return make_response(str(score_add), 200)

@app.route('/spawn/<float:vel>', methods=['POST'])
def spawnpost(vel):
    global spawn_vel
    spawn_vel = vel
    return make_response(str(spawn_vel), 200)

@app.route('/spawn', methods=['GET'])
def spawnget():
    return make_response(str(spawn_vel), 200)

@app.route('/highscore/<int:highscore>', methods=['POST'])
def highpost(highscore):
    update(int(highscore))
    return make_response(int(highscore), 200)

@app.route("/highscore", methods=["GET", "POST"])
def highget():
    return make_response(str(read()), 200)

if __name__ == "__main__":
    app.run(debug=True)