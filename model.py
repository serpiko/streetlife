import operator
import random
import json
import requests

class Station(object):
    self.conn = set()

    def __init__(self,id,name):
        self.id = id
        self.name = name
        self.lcats = set()
        self.lowners = set()
        self.enabled = True

    def add_owner(self, idowner):
        #self.lowners.append(idowner)
        self.dcats.add(idowner)

    def add_cat(self, idcat):
        #self.lowners.append(idcat)
        self.lowners.add(idowner)

    def add_conn(self,con):
        self.conn.add(con)

    def rm_conn(self, con):
        try:
            self.conn.remove(c)
        except KeyError:
            pass

    def __str__(self):
        return "id {}, name {}, has {} owners and {} cats".format(self.id, self.name,len(self.lowners),len(self.lcats))

    """
    we asume that when an owner finds his cat we can remove it
    from the station, ergo the set
    """
    def has_cat(self,idcat):
        try:
            pos = self.lcats.remove(idcat)
        except ValueError:
            return -1
        #close station, Cat Found!!
        self.enabled = False
        return pos

class Cat(object):
    __init__(self,id,st):
        self.id = id
        self.st = st


class Owner(object):
    self.seen = set()

    __init__(self,id,st,pos,map):
        self.id = id
        self.st = st
        self.pos = pos
        self.map = map

    def visit(station):
        self.seen.add(station)

    def move(self, stations):
        station = stations.diff(self.seen)
        self.__init__(station)


def create_map(stations,cons):
    cons2 = {}
    for i in cons:

        k = int(i[0])
        if cons2.has_key(k):
            cons2[k].append(i[1])
        else:
            cons2.update({ k : list(i[1])})
    return cons2




# Test
# optparse input 
N = 20
uri_conn = """https://gist.githubusercontent.com/jorgebastida/f90adff6bf83736b2a23/raw/a218d0387ac9c8c74882d67f8b242e251d70f6c1/tfl_connections.json"""
uri_stations = """https://gist.githubusercontent.com/jorgebastida/f90adff6bf83736b2a23/raw/a218d0387ac9c8c74882d67f8b242e251d70f6c1/tfl_stations.json"""
res_cons = requests.get(uri_conn)
cons = res_cons.json()
res_stations = requests.get(uri_stations)
stations = res_stations.json()
#initialise stations
stationList = []
for i in range(len(stations)):
    #Create Station
    st = Station(int(stations[i][0]),stations[i][1])
    stationList.append(st)

# iterate the game
for i in range(N):
    # get random init station
    uniq = False
    while not unique:
        init_cat_st = int(random.choice(stations)[0]) #[u'239', u'South Ruislip'] -> 239
        init_own_st = int(random.choice(stations)[0]) #[u'239', u'South Ruislip'] -> 239
        if init_cat_st != init_own_st:
            unique = True
    # first create owner value then the cat's and repeat if equals
    o = Owner(i,init_own_st)
    #move onwer to station
    move_owner_station(o

    c = Cat(i,init_cat_st)
    # move cat to station



#stationList.sort(key=operator.attrgetter('id'))

for station in stationList:
    print(station)
