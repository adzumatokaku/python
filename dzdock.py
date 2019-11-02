# task 4
import docker
#1
base_url = input('URL to the Docker server in form "http://ip:port" : \n')
client = docker.DockerClient(base_url)
if not client:
    
    client = docker.from_env()
if client.containers.list('status=exited'):
    print ('Warning! There are dead or stoped containers: \n')
    cont = list(client.containers.list('status=exited'))
    for con in cont:
        print (con)
#2
print('All containers: \n')
allcont = list((client.containers.list(all=True)))
for allcon in allcont:
    print (allcon)
#3
print('Docker images: \n')
images = list(client.images.list())
for im in images:
    print (im)
#4
def inspect_func(): 
    cont_id = input('Container id: \n')
    if not cont_id:
        cont_id = 'a9488b0f59' #just for test on my machine
    print('Docker inspect: \n')
    print(client.api.inspect_container(cont_id))
inspect_func()


