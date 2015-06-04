"""

Python BioSemi ActiveTwo: an example how to read and visualize raw signal
Copyright 2015, Ilya Kuzovkin
Licensed under MIT

"""

from pyactivetwo import ActiveTwo

if __name__ == '__main__':

    # initialize the device
    device = ActiveTwo(host='127.0.0.1', sfreq=512, port=778, nchannels=32, tcpsamples=4)

    # read 30 seconds of signal and print out the data
    for run in range(30):
        rawdata = device.read(duration=1.0)
        print rawdata
