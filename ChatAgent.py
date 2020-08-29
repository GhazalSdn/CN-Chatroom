from BroadcastListener import BroadcastListener
from Broadcaster import Broadcaster
print "Select your agent type(Broadcaster OR BroadcastListener) :  \n"
input = raw_input()
if input=="Broadcaster":
    agent = Broadcaster()
    agent.execute()
if input=="BroadcastListener":
    agent = BroadcastListener()
    agent.execute()