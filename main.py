import flask 
main = flask.Flask(__name__)
@main.route("/")

def index (): 
    tvlist = ["Flash", "Our Beloved Summer", "All of us are dead", " Ghosts", " Modern Family"]
    favorite = ["Flash"]
    pictures = ["flash.jpg", "our beloved summer.jpg", "all of us are dead.jpg", "ghosts.jpg", "modern family.jpg"]
  
    return flask.render_template("index.html", len = len(tvlist),tvlist = tvlist, favorite = favorite, pictures=pictures)
    
main.run(debug=True)
