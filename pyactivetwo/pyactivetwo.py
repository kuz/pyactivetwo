"""

Python BioSemi ActiveTwo: main class
Copyright 2015, Ilya Kuzovkin
Licensed under MIT

Builds on example code by Jack Keegan
https://batchloaf.wordpress.com/2014/01/17/real-time-analysis-of-data-from-biosemi-activetwo-via-tcpip-using-python/

"""

import socket
import numpy as np


class ActiveTwo():
    """
    Main class which implements major functions needed for communication with BioSemi ActiveTwo device
    """

    #: Host where ActiView acquisition software is running
    host = None

    #: This is the port ActiView listens on
    port = None

    #: Number of channles
    nchannels = None

    #: Data packet size (default: 32 channels @ 512Hz)
    buffer_size = None

    def __init__(self, host='127.0.0.1', sfreq=512, port=778, nchannels=32, tcpsamples=4):
        """
        Initialize connection and parameters of the signal
        :param host: IP address where ActiView is running
        :param port: Port ActiView is listening on
        :param nchannels: Number of EEG channels
        """

        # store parameters
        self.host = host
        self.port = port
        self.nchannels = nchannels
        self.sfreq = sfreq
        self.tcpsamples = tcpsamples
        self.buffer_size = self.nchannels * self.tcpsamples * 3

        # open connection
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.host, self.port))

    def read(self, duration):
        """
        Read signal from the EEG device
        :param duration: How long to read in seconds
        :return: Signal in the matrix form: samples x channels
        """

        # initialize final data array
        rawdata = np.empty((0,32))

        # The reader process will run until requested amount of data is collected
        samples = 0
        while samples < duration * self.sfreq:

            # Create a 16-sample signal_buffer
            signal_buffer = np.zeros((self.nchannels, self.tcpsamples))

            # Read the next packet from the network
            # sometimes there is an error and packet is smaller than needed, read until get a good one
            data = []
            while len(data) != self.buffer_size:
                data = self.s.recv(self.buffer_size)

            # Extract 16 samples from the packet (ActiView sends them in 16-sample chunks)
            for m in range(self.tcpsamples):

                # extract samples for each channel
                for ch in range(self.nchannels):
                    offset = m * 3 * self.nchannels + (ch * 3)

                    # The 3 bytes of each sample arrive in reverse order
                    sample = (ord(data[offset+2]) << 16)
                    sample += (ord(data[offset+1]) << 8)
                    sample += ord(data[offset])

                    # Store sample to signal buffer
                    signal_buffer[ch, m] = sample

            # update sample counter
            samples += self.tcpsamples

            # transpose matrix so that rows are samples
            signal_buffer = np.transpose(signal_buffer)

            # add to the final dataset
            rawdata = np.concatenate((rawdata, signal_buffer), axis=0)

        return rawdata