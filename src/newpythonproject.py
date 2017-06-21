# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import gedcom
import image
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np



if __name__ == "__main__":


    gedcomFile = gedcom.parse("Wainwright_Wroblewski.ged")

    me = gedcomFile.pointers['@P1@']
    mom = gedcomFile.pointers['@P3@']
    # print(me['BIRT'].place)
    # print(family)
    # print(mom)
    names = []
    birthYear = []
    birthPlace = []
    i = 0
    for person in gedcomFile.individuals:
        i = i + 1
        birthPlaces = person['BIRT']
        firstName, lastName = person.name
        personName = firstName + " " + lastName
        names.append(personName)
        birthYear.append(birthPlaces.date)
        birthPlace.append(birthPlaces.place)
        # print(firstName, lastName)
        print(birthPlace)
        #    except IndexError:  # catch the error
        #    i = i +1
        #    names.append(personName)
        #    birthYear.append("Index Error")
        #    birthYear.append("Unknown Place")
        #    pass
        # except AttributeError:
        #     i = i + 1
        #    names.append(personName)
        #   birthYear.append("Attribute error")
        #  birthYear.append("Unknown Dt?")
        # pass
    print(i)
    print(len(names))
    print(len(birthYear))
    print(len(birthPlace))
    print(names)
    print(birthYear)

    myMap = Basemap(projection="mill", llcrnrlat=0, llcrnrlon=-120, urcrnrlat=75, urcrnrlon=45, resolution='l')
    myMap.drawcoastlines()
    myMap.drawcountries(linewidth=1)
    myMap.drawstates(color='b')
    myMap.fillcontinents()

    # myMap.etopo()
    myMap.bluemarble()
    xs = []
    ys = []

    x = []
    y = []

    locations = ((-74.4057, 40.0853), (31.1656, 49.3794), (-74.0059, 42.0), (-61.2225, 10.6918), (-64.7505, 32.3078),
                 (-1.4101, 53.5598))

    xpt, ypt = myMap(x, y)

    xs.append(x)
    ys.append(y)

    myMap.plot(xpt, ypt, 'r.', markersize=35)
    plt.title("Birth Locations of Matt's Ancestors")

    point = myMap.plot(x, y, 'ro', markersize=20)[0]


    def init():
        point.set_data([], [])
        return point,

    # NJ[0] -74.4057, 40.0853  --- Ukraine[1] 31.1656, 49.3794 --- New York [2] -74.0059, 42.0, Trinidad [3] -61.2225, 10.6918 --- Bermuda [4] -64.7505, 32.3078 -- England[5] -1.4101,53.5598  ----
    #
    # animation function.  This is called sequentially
    def animate(i):
        plt.text(-1.4101,53.5598,"hisafdlksajfdkl")
        if birthPlace[i] == "England":
            lons, lats = (-1.4101,53.5598)
        elif birthPlace[i] == "New Jersey":
            lons, lats = (-74.4057, 40.0853)
        elif birthPlace[i] == "Ukraine":
            lons, lats = (31.1656, 49.3794)
        elif birthPlace[i] == "Trinidad":
            lons, lats = (-61.2225, 10.6918)
        elif birthPlace[i] == "Bermuda":
            lons, lats = (-64.7505, 32.3078)
        else:
            lons, lats = (0,0)#locations[i]
        x, y = myMap(lons, lats)
        point.set_data(x, y)
        return point,


    # call the animator.  blit=True means only re-draw the parts that have changed.
    anim = animation.FuncAnimation(plt.gcf(), animate, init_func=init,
                                   frames=10, interval=1000, blit=True)
    plt.show()
    fig=plt.figure()
    ax = fig.add_subplot(111)

    print(locations[0])