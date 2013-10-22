import sys
from flask import Flask, render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer

app = Flask(__name__)
app.config.from_pyfile('sitesettings.cfg')
pages = FlatPages(app)
freezer = Freezer(app)

@app.route('/')
def index():
  return page('index')

@app.route('/blog')
def blog():
  posts = [post for post in pages if 'published' in post.meta]
  posts = sorted(posts, reverse=True, 
    key=lambda post: post.meta['published'])
  page = pages.get_or_404('blog')
  return render_template('blog_listing.html', posts=posts, page=page)

@app.route('/<path:path>/')
def page(path):
  page = pages.get_or_404(path)
  return render_template('page.html', page=page)
  
@freezer.register_generator
def page_generator():
  for post in pages:
    print post.path
    if post.meta.get('visible', True):
      yield 'page', {'path': post.path} 
    
if __name__ == "__main__":
  if len(sys.argv) > 1 and sys.argv[1] == "build":
    freezer.freeze()
  else:
    app.run(debug=True)