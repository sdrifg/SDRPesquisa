#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Fri Jul 22 16:18:17 2016
##################################################

from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import gr
from grc_gnuradio import blks2 as grc_blks2
import math
import numpy
import sys
import threading
import time
import xlwt
import gc

try:
    from scipy.special import erfc
except ImportError:
    print "Error: could not import scipy (http://www.scipy.org/)"
    sys.exit(1)

try:
    import pylab
except ImportError:
    print "Error: could not import pylab (http://matplotlib.sourceforge.net/)"
    sys.exit(1)
help=0

class bpsk(gr.top_block):

    def __init__(self,EbN0db,semente):
        gr.top_block.__init__(self)

        ##################################################
        # Variables
        ##################################################
        self.value = value = 0, 1
        self.symbol = symbol = -1,1
        self.samp_rate = samp_rate = 200000
        self.constellation = constellation = digital.constellation_calcdist((symbol), (value), 4, 1).base()

        ##################################################
        # Blocks
        ##################################################
        self.digital_constellation_decoder_cb_0 = digital.constellation_decoder_cb(constellation)
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bc((symbol), 1)
        self.vectorSink = blocks.vector_sink_f(1)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.blks2_error_rate_0 = grc_blks2.error_rate(
        	type='BER',
        	win_size=10000000,
        	bits_per_symbol=int(math.log(len(symbol))/math.log(2)),
        )
        self.analog_random_source_x_0 = blocks.vector_source_b(map(int, numpy.random.randint(0, 2, 4000000)), False)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN,self.EbN0_to_noise_voltage(EbN0db,int(1)),semente)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 1))    
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.blks2_error_rate_0, 0), (self.vectorSink, 0))    
        self.connect((self.blocks_add_xx_0, 0), (self.digital_constellation_decoder_cb_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.blks2_error_rate_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))    
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.blocks_add_xx_0, 0))    
        self.connect((self.digital_constellation_decoder_cb_0, 0), (self.blks2_error_rate_0, 1))    

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_symbol(self):
        return self.symbol

    def set_symbol(self, symbol):
        self.symbol = symbol
        self.digital_chunks_to_symbols_xx_0.set_symbol_table((self.symbol))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_constellation(self):
        return self.constellation

    def set_constellation(self, constellation):
        self.constellation = constellation



    def nome(self):
	a=numpy.sum(self.vectorSink.data())/(len(self.vectorSink.data()))
	self.vectorSink.reset()
	return a

    def limpa(self):
	self.vectorSink.reset()
	#self.vectorSink.clear_finished()

	

    def EbN0_to_noise_voltage(self, EbN0,bitspersymbol):
        """ Converts Eb/N0 to a complex noise voltage (assuming unit symbol power) """
        return 1.0 / math.sqrt(float(bitspersymbol)*10**(float(EbN0)/10))


class myThread (threading.Thread):
    def __init__(self, EbN0,semente):
        threading.Thread.__init__(self)
        self.EbN0 = EbN0
        self.semente = semente
        self.tb = bpsk(self.EbN0,self.semente)
	self._stop = threading.Event()

    def run(self):
	try:
	        print "Starting "
		self.tb.start()
		print "running "
	        self.tb.wait()
		print "Exiting "
	except:
		print "Erro de memoria estamos tentando consertar "
	

    def stop(self):
	self.tb.limpa()
	self.tb.stop()
	self.tb.limpa()
	gc.collect()
	self._stop.set()
	
	

    def getValue(self):
	return self.tb.nome()

  
def berawgn(EbN0,k):
    return (float(4)/k)*(float(1)-float(1)/math.sqrt(2**k))*0.5*erfc(math.sqrt((3*k*10**(float(EbN0)/10))/((2**k)-1))/math.sqrt(2))
def berawgn1(EbN0,k):
    return (float(1)/float(k))*erfc(math.sqrt((float(k)*10**(float(EbN0)/10)))*math.sin(math.pi/(2**k)))


def simulate_ber(EbN0,semente):
    try:
    	thread1 = myThread(EbN0,semente)
    	thread1.start()
    	time.sleep(12)
    	help=thread1.getValue()
   
    	thread1.stop()
    	time.sleep(3)
    	print "thread stop "  
    	return help
    except:
	print "Erro de memoria estamos tentando consertar "
	return 1000
    



if __name__ == "__main__":
    #main()
    EbN0_min = 0
    EbN0_max = 10
    EbN0_range = range(EbN0_min, EbN0_max+1)
    wb = xlwt.Workbook()
    ws = wb.add_sheet('bpsk') 
    ws.write(0, 0, "seed")
    for i in range(len(EbN0_range)):
    	ws.write(0, i+1, str(i)+"dB")


    print "Simulating..."
    ber_theory =numpy.zeros((EbN0_max+1,), dtype=numpy.float)
    ber_theory1 =numpy.zeros((EbN0_max+1,), dtype=numpy.float)
    ber_theory2 =numpy.zeros((EbN0_max+1,), dtype=numpy.float)
    ber_simu =numpy.zeros((EbN0_max+1,), dtype=numpy.float)  

    for v in range(50):
	ws.write(v+1,0, v)

    for x in range(3,11):
        
	print "Eb/N0 = %d dB" % x
	ber_theory[x] = berawgn(x,1)
        ber_theory1[x] = berawgn1(x,1)
	

	for v in range(30):
		gc.enable()
		ber_simu[x]   = simulate_ber(x,v)
		print "seed",v,"\tbpsk", ber_simu[x]
		ws.write(v+1,x+1, ber_simu[x])
		wb.save('bpsk.xls')
		gc.collect()

        print "\nbpsk teorico2", ber_theory1[x] 
	print "\nbpsk teorico1", ber_theory[x]    


    wb.save('bpsk.xls')



    f = pylab.figure()
    s = f.add_subplot(1,1,1)
    s.semilogy(EbN0_range, ber_theory, 'k-.', label="Theoretical bpsk1")
    s.semilogy(EbN0_range, ber_theory1, 'r-.', label="Theoretical bpsk2")
    #s.semilogy(EbN0_range, ber_theory2, 'g-.', label="Theoretical qam256")
    s.semilogy(EbN0_range, ber_simu, 'b-o', label="bpsk")
    s.set_title('BER Simulation')
    s.set_xlabel('Eb/N0 (dB)')
    s.set_ylabel('BER')
    s.legend()
    s.grid()
    pylab.show()


