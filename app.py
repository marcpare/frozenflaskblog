from flask import Flask, render_template
from flask_flatpages import FlatPages

app = Flask(__name__)
app.config.from_pyfile('sitesettings.cfg')
pages = FlatPages(app)

@app.route('/')
def index():
  return "Hello World"

@app.route('/<path:path>/')
def page(path):
  page = pages.get_or_404(path)
  return render_template('page.html', page=page)
  
if __name__ == "__main__":
  app.run(debug=True)