from gpiozero import MCP3008
import time
import os

station_dial = MCP3008(0)

Magic = "http://tx.whatson.com/icecast.php?i=magic1054.mp3.m3u"
Radio1 = "http://www.listenlive.eu/bbcradio1.m3u"

def change_station(station):
    os.system("killall mplayer")
    os.system("mplayer -playlist " + station + " &")

while True:
    if station_dial.value >= 0.5 and station != Magic:
        station = Magic
        change_station(station)
    elif station_dial.value < 0.5 and station != Radio1:
        station = Radio1
        change_station(station)
    time.sleep(0.1)
