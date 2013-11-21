from fabric.api import env, run, put, sudo, local, cd

def server():
  local('python app.py')

def build():
  local('python app.py build')
  
def deploy():
  build()
  local('rsync --verbose -r -p ./build/ marc@notwandering.com:/home/marc/public_html/smallredtile.com/public/')
  