# import fabrics API functions - self-explanatory once you see 
from fabric.api import *
# env.hosts = ['vimm@ghost']
# def pushpull():
#     local('git push') # runs the command on the local environment
#     run('cd /code/spring_exercise/web_sikhshalaya/src; git pull') # runs the command on the remote environment 
result=run('ls ~')
print(result)