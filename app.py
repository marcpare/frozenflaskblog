from flask import Flask, render_template
app = Flask(__name__)

def render_content(filename):
  # grab the YAML header stuff
  

@app.route("/")
def render_page():
  return render_template('index.html')

if __name__ == "__main__":
  app.run(debug=True)