#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Sat Jul 16 15:59:02 2016
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


class qam256(gr.top_block):

    def __init__(self,EbN0db,semente):
        gr.top_block.__init__(self)
   

        ##################################################
        # Variables
        ##################################################
        self.h = h = 0.0816
        self.hj = hj = h*1j
        self.gj = gj = h*3j
        self.g = g = 3*h
        self.fj = fj = h*5j
        self.f = f = 5*h
        self.ej = ej = h*7j
        self.e = e = 7*h
        self.dj = dj = h*9j
        self.d = d = 9*h
        self.cj = cj = h*11j
        self.c = c = 11*h
        self.bj = bj = h*13j
        self.b = b = 13*h
        self.aj = aj = h*15j
        self.a = a = 15*h
        self.sym3 = sym3 = (-a+ej),(-b+ej),(-c+ej),(-d+ej),(-e+ej),(-f+ej),(-g+ej),(-h+ej),(+a+ej),(+b+ej),(+c+ej),(+d+ej),(+e+ej),(+f+ej),(+g+ej),(+h+ej),(-a+fj),(-b+fj),(-c+fj),(-d+fj),(-e+fj),(-f+fj),(-g+fj),(-h+fj),(+a+fj),(+b+fj),(+c+fj),(+d+fj),(+e+fj),(+f+fj),(+g+fj),(+h+fj),(-a+gj),(-b+gj),(-c+gj),(-d+gj),(-e+gj),(-f+gj),(-g+gj),(-h+gj),(+a+gj),(+b+gj),(+c+gj),(+d+gj),(+e+gj),(+f+gj),(+g+gj),(+h+gj),(-a+hj),(-b+hj),(-c+hj),(-d+hj),(-e+hj),(-f+hj),(-g+hj),(-h+hj),(+a+hj),(+b+hj),(+c+hj),(+d+hj),(+e+hj),(+f+hj),(+g+hj),(+h+hj)
        self.sym2 = sym2 = (-a+aj),(-b+aj),(-c+aj),(-d+aj),(-e+aj),(-f+aj),(-g+aj),(-h+aj),(+a+aj),(+b+aj),(+c+aj),(+d+aj),(+e+aj),(+f+aj),(+g+aj),(+h+aj),(-a+bj),(-b+bj),(-c+bj),(-d+bj),(-e+bj),(-f+bj),(-g+bj),(-h+bj),(+a+bj),(+b+bj),(+c+bj),(+d+bj),(+e+bj),(+f+bj),(+g+bj),(+h+bj),(-a+cj),(-b+cj),(-c+cj),(-d+cj),(-e+cj),(-f+cj),(-g+cj),(-h+cj),(+a+cj),(+b+cj),(+c+cj),(+d+cj),(+e+cj),(+f+cj),(+g+cj),(+h+cj),(-a+dj),(-b+dj),(-c+dj),(-d+dj),(-e+dj),(-f+dj),(-g+dj),(-h+dj),(+a+dj),(+b+dj),(+c+dj),(+d+dj),(+e+dj),(+f+dj),(+g+dj),(+h+dj)
        self.sym1 = sym1 = (-a-ej),(-b-ej),(-c-ej),(-d-ej),(-e-ej),(-f-ej),(-g-ej),(-h-ej),(+a-ej),(+b-ej),(+c-ej),(+d-ej),(+e-ej),(+f-ej),(+g-ej),(+h-ej),(-a-fj),(-b-fj),(-c-fj),(-d-fj),(-e-fj),(-f-fj),(-g-fj),(-h-fj),(+a-fj),(+b-fj),(+c-fj),(+d-fj),(+e-fj),(+f-fj),(+g-fj),(+h-fj),(-a-gj),(-b-gj),(-c-gj),(-d-gj),(-e-gj),(-f-gj),(-g-gj),(-h-gj),(+a-gj),(+b-gj),(+c-gj),(+d-gj),(+e-gj),(+f-gj),(+g-gj),(+h-gj),(-a-hj),(-b-hj),(-c-hj),(-d-hj),(-e-hj),(-f-hj),(-g-hj),(-h-hj),(+a-hj),(+b-hj),(+c-hj),(+d-hj),(+e-hj),(+f-hj),(+g-hj),(+h-hj)
        self.sym0 = sym0 = (-a-aj),(-b-aj),(-c-aj),(-d-aj),(-e-aj),(-f-aj),(-g-aj),(-h-aj),(+a-aj),(+b-aj),(+c-aj),(+d-aj),(+e-aj),(+f-aj),(+g-aj),(+h-aj),(-a-bj),(-b-bj),(-c-bj),(-d-bj),(-e-bj),(-f-bj),(-g-bj),(-h-bj),(+a-bj),(+b-bj),(+c-bj),(+d-bj),(+e-bj),(+f-bj),(+g-bj),(+h-bj),(-a-cj),(-b-cj),(-c-cj),(-d-cj),(-e-cj),(-f-cj),(-g-cj),(-h-cj),(+a-cj),(+b-cj),(+c-cj),(+d-cj),(+e-cj),(+f-cj),(+g-cj),(+h-cj),(-a-dj),(-b-dj),(-c-dj),(-d-dj),(-e-dj),(-f-dj),(-g-dj),(-h-dj),(+a-dj),(+b-dj),(+c-dj),(+d-dj),(+e-dj),(+f-dj),(+g-dj),(+h-dj)
        self.symbol1 = symbol1 = numpy.concatenate((sym2,sym3),0)
        self.symbol0 = symbol0 = numpy.concatenate((sym0,sym1),0)
        self.value = value = 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255
        self.symbol = symbol = numpy.concatenate((symbol0,symbol1),0)
        self.samp_rate = samp_rate = 200000
        self.constellation = constellation = digital.constellation_calcdist((symbol), (value), 0, 1).base()

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
        self.analog_random_source_x_0 = blocks.vector_source_b(map(int, numpy.random.randint(0, 256, 4000000)), False)
        self.analog_noise_source_x_0_0 = analog.noise_source_c(analog.GR_GAUSSIAN,self.EbN0_to_noise_voltage(EbN0db,int(8)),semente)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0_0, 0), (self.blocks_add_xx_0, 1))    
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.blks2_error_rate_0, 0), (self.vectorSink, 0))    
        self.connect((self.blocks_add_xx_0, 0), (self.digital_constellation_decoder_cb_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.blks2_error_rate_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))    
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.blocks_add_xx_0, 0))    
        self.connect((self.digital_constellation_decoder_cb_0, 0), (self.blks2_error_rate_0, 1))    


    def get_h(self):
        return self.h

    def set_h(self, h):
        self.h = h
        self.set_a(15*self.h)
        self.set_aj(self.h*15j)
        self.set_b(13*self.h)
        self.set_bj(self.h*13j)
        self.set_c(11*self.h)
        self.set_cj(self.h*11j)
        self.set_d(9*self.h)
        self.set_dj(self.h*9j)
        self.set_e(7*self.h)
        self.set_ej(self.h*7j)
        self.set_f(5*self.h)
        self.set_fj(self.h*5j)
        self.set_g(3*self.h)
        self.set_gj(self.h*3j)
        self.set_hj(self.h*1j)
        self.set_sym0((-self.a-self.aj),(-self.b-self.aj),(-self.c-self.aj),(-self.d-self.aj),(-self.e-self.aj),(-self.f-self.aj),(-self.g-self.aj),(-self.h-self.aj),(+self.a-self.aj),(+self.b-self.aj),(+self.c-self.aj),(+self.d-self.aj),(+self.e-self.aj),(+self.f-self.aj),(+self.g-self.aj),(+self.h-self.aj),(-self.a-self.bj),(-self.b-self.bj),(-self.c-self.bj),(-self.d-self.bj),(-self.e-self.bj),(-self.f-self.bj),(-self.g-self.bj),(-self.h-self.bj),(+self.a-self.bj),(+self.b-self.bj),(+self.c-self.bj),(+self.d-self.bj),(+self.e-self.bj),(+self.f-self.bj),(+self.g-self.bj),(+self.h-self.bj),(-self.a-self.cj),(-self.b-self.cj),(-self.c-self.cj),(-self.d-self.cj),(-self.e-self.cj),(-self.f-self.cj),(-self.g-self.cj),(-self.h-self.cj),(+self.a-self.cj),(+self.b-self.cj),(+self.c-self.cj),(+self.d-self.cj),(+self.e-self.cj),(+self.f-self.cj),(+self.g-self.cj),(+self.h-self.cj),(-self.a-self.dj),(-self.b-self.dj),(-self.c-self.dj),(-self.d-self.dj),(-self.e-self.dj),(-self.f-self.dj),(-self.g-self.dj),(-self.h-self.dj),(+self.a-self.dj),(+self.b-self.dj),(+self.c-self.dj),(+self.d-self.dj),(+self.e-self.dj),(+self.f-self.dj),(+self.g-self.dj),(+self.h-self.dj))
        self.set_sym1((-self.a-self.ej),(-self.b-self.ej),(-self.c-self.ej),(-self.d-self.ej),(-self.e-self.ej),(-self.f-self.ej),(-self.g-self.ej),(-self.h-self.ej),(+self.a-self.ej),(+self.b-self.ej),(+self.c-self.ej),(+self.d-self.ej),(+self.e-self.ej),(+self.f-self.ej),(+self.g-self.ej),(+self.h-self.ej),(-self.a-self.fj),(-self.b-self.fj),(-self.c-self.fj),(-self.d-self.fj),(-self.e-self.fj),(-self.f-self.fj),(-self.g-self.fj),(-self.h-self.fj),(+self.a-self.fj),(+self.b-self.fj),(+self.c-self.fj),(+self.d-self.fj),(+self.e-self.fj),(+self.f-self.fj),(+self.g-self.fj),(+self.h-self.fj),(-self.a-self.gj),(-self.b-self.gj),(-self.c-self.gj),(-self.d-self.gj),(-self.e-self.gj),(-self.f-self.gj),(-self.g-self.gj),(-self.h-self.gj),(+self.a-self.gj),(+self.b-self.gj),(+self.c-self.gj),(+self.d-self.gj),(+self.e-self.gj),(+self.f-self.gj),(+self.g-self.gj),(+self.h-self.gj),(-self.a-self.hj),(-self.b-self.hj),(-self.c-self.hj),(-self.d-self.hj),(-self.e-self.hj),(-self.f-self.hj),(-self.g-self.hj),(-self.h-self.hj),(+self.a-self.hj),(+self.b-self.hj),(+self.c-self.hj),(+self.d-self.hj),(+self.e-self.hj),(+self.f-self.hj),(+self.g-self.hj),(+self.h-self.hj))
        self.set_sym2((-self.a+self.aj),(-self.b+self.aj),(-self.c+self.aj),(-self.d+self.aj),(-self.e+self.aj),(-self.f+self.aj),(-self.g+self.aj),(-self.h+self.aj),(+self.a+self.aj),(+self.b+self.aj),(+self.c+self.aj),(+self.d+self.aj),(+self.e+self.aj),(+self.f+self.aj),(+self.g+self.aj),(+self.h+self.aj),(-self.a+self.bj),(-self.b+self.bj),(-self.c+self.bj),(-self.d+self.bj),(-self.e+self.bj),(-self.f+self.bj),(-self.g+self.bj),(-self.h+self.bj),(+self.a+self.bj),(+self.b+self.bj),(+self.c+self.bj),(+self.d+self.bj),(+self.e+self.bj),(+self.f+self.bj),(+self.g+self.bj),(+self.h+self.bj),(-self.a+self.cj),(-self.b+self.cj),(-self.c+self.cj),(-self.d+self.cj),(-self.e+self.cj),(-self.f+self.cj),(-self.g+self.cj),(-self.h+self.cj),(+self.a+self.cj),(+self.b+self.cj),(+self.c+self.cj),(+self.d+self.cj),(+self.e+self.cj),(+self.f+self.cj),(+self.g+self.cj),(+self.h+self.cj),(-self.a+self.dj),(-self.b+self.dj),(-self.c+self.dj),(-self.d+self.dj),(-self.e+self.dj),(-self.f+self.dj),(-self.g+self.dj),(-self.h+self.dj),(+self.a+self.dj),(+self.b+self.dj),(+self.c+self.dj),(+self.d+self.dj),(+self.e+self.dj),(+self.f+self.dj),(+self.g+self.dj),(+self.h+self.dj))
        self.set_sym3((-self.a+self.ej),(-self.b+self.ej),(-self.c+self.ej),(-self.d+self.ej),(-self.e+self.ej),(-self.f+self.ej),(-self.g+self.ej),(-self.h+self.ej),(+self.a+self.ej),(+self.b+self.ej),(+self.c+self.ej),(+self.d+self.ej),(+self.e+self.ej),(+self.f+self.ej),(+self.g+self.ej),(+self.h+self.ej),(-self.a+self.fj),(-self.b+self.fj),(-self.c+self.fj),(-self.d+self.fj),(-self.e+self.fj),(-self.f+self.fj),(-self.g+self.fj),(-self.h+self.fj),(+self.a+self.fj),(+self.b+self.fj),(+self.c+self.fj),(+self.d+self.fj),(+self.e+self.fj),(+self.f+self.fj),(+self.g+self.fj),(+self.h+self.fj),(-self.a+self.gj),(-self.b+self.gj),(-self.c+self.gj),(-self.d+self.gj),(-self.e+self.gj),(-self.f+self.gj),(-self.g+self.gj),(-self.h+self.gj),(+self.a+self.gj),(+self.b+self.gj),(+self.c+self.gj),(+self.d+self.gj),(+self.e+self.gj),(+self.f+self.gj),(+self.g+self.gj),(+self.h+self.gj),(-self.a+self.hj),(-self.b+self.hj),(-self.c+self.hj),(-self.d+self.hj),(-self.e+self.hj),(-self.f+self.hj),(-self.g+self.hj),(-self.h+self.hj),(+self.a+self.hj),(+self.b+self.hj),(+self.c+self.hj),(+self.d+self.hj),(+self.e+self.hj),(+self.f+self.hj),(+self.g+self.hj),(+self.h+self.hj))

    def get_hj(self):
        return self.hj

    def set_hj(self, hj):
        self.hj = hj
        self.set_sym1((-self.a-self.ej),(-self.b-self.ej),(-self.c-self.ej),(-self.d-self.ej),(-self.e-self.ej),(-self.f-self.ej),(-self.g-self.ej),(-self.h-self.ej),(+self.a-self.ej),(+self.b-self.ej),(+self.c-self.ej),(+self.d-self.ej),(+self.e-self.ej),(+self.f-self.ej),(+self.g-self.ej),(+self.h-self.ej),(-self.a-self.fj),(-self.b-self.fj),(-self.c-self.fj),(-self.d-self.fj),(-self.e-self.fj),(-self.f-self.fj),(-self.g-self.fj),(-self.h-self.fj),(+self.a-self.fj),(+self.b-self.fj),(+self.c-self.fj),(+self.d-self.fj),(+self.e-self.fj),(+self.f-self.fj),(+self.g-self.fj),(+self.h-self.fj),(-self.a-self.gj),(-self.b-self.gj),(-self.c-self.gj),(-self.d-self.gj),(-self.e-self.gj),(-self.f-self.gj),(-self.g-self.gj),(-self.h-self.gj),(+self.a-self.gj),(+self.b-self.gj),(+self.c-self.gj),(+self.d-self.gj),(+self.e-self.gj),(+self.f-self.gj),(+self.g-self.gj),(+self.h-self.gj),(-self.a-self.hj),(-self.b-self.hj),(-self.c-self.hj),(-self.d-self.hj),(-self.e-self.hj),(-self.f-self.hj),(-self.g-self.hj),(-self.h-self.hj),(+self.a-self.hj),(+self.b-self.hj),(+self.c-self.hj),(+self.d-self.hj),(+self.e-self.hj),(+self.f-self.hj),(+self.g-self.hj),(+self.h-self.hj))
        self.set_sym3((-self.a+self.ej),(-self.b+self.ej),(-self.c+self.ej),(-self.d+self.ej),(-self.e+self.ej),(-self.f+self.ej),(-self.g+self.ej),(-self.h+self.ej),(+self.a+self.ej),(+self.b+self.ej),(+self.c+self.ej),(+self.d+self.ej),(+self.e+self.ej),(+self.f+self.ej),(+self.g+self.ej),(+self.h+self.ej),(-self.a+self.fj),(-self.b+self.fj),(-self.c+self.fj),(-self.d+self.fj),(-self.e+self.fj),(-self.f+self.fj),(-self.g+self.fj),(-self.h+self.fj),(+self.a+self.fj),(+self.b+self.fj),(+self.c+self.fj),(+self.d+self.fj),(+self.e+self.fj),(+self.f+self.fj),(+self.g+self.fj),(+self.h+self.fj),(-self.a+self.gj),(-self.b+self.gj),(-self.c+self.gj),(-self.d+self.gj),(-self.e+self.gj),(-self.f+self.gj),(-self.g+self.gj),(-self.h+self.gj),(+self.a+self.gj),(+self.b+self.gj),(+self.c+self.gj),(+self.d+self.gj),(+self.e+self.gj),(+self.f+self.gj),(+self.g+self.gj),(+self.h+self.gj),(-self.a+self.hj),(-self.b+self.hj),(-self.c+self.hj),(-self.d+self.hj),(-self.e+self.hj),(-self.f+self.hj),(-self.g+self.hj),(-self.h+self.hj),(+self.a+self.hj),(+self.b+self.hj),(+self.c+self.hj),(+self.d+self.hj),(+self.e+self.hj),(+self.f+self.hj),(+self.g+self.hj),(+self.h+self.hj))

    def get_gj(self):
        return self.gj

    def set_gj(self, gj):
        self.gj = gj
        self.set_sym1((-self.a-self.ej),(-self.b-self.ej),(-self.c-self.ej),(-self.d-self.ej),(-self.e-self.ej),(-self.f-self.ej),(-self.g-self.ej),(-self.h-self.ej),(+self.a-self.ej),(+self.b-self.ej),(+self.c-self.ej),(+self.d-self.ej),(+self.e-self.ej),(+self.f-self.ej),(+self.g-self.ej),(+self.h-self.ej),(-self.a-self.fj),(-self.b-self.fj),(-self.c-self.fj),(-self.d-self.fj),(-self.e-self.fj),(-self.f-self.fj),(-self.g-self.fj),(-self.h-self.fj),(+self.a-self.fj),(+self.b-self.fj),(+self.c-self.fj),(+self.d-self.fj),(+self.e-self.fj),(+self.f-self.fj),(+self.g-self.fj),(+self.h-self.fj),(-self.a-self.gj),(-self.b-self.gj),(-self.c-self.gj),(-self.d-self.gj),(-self.e-self.gj),(-self.f-self.gj),(-self.g-self.gj),(-self.h-self.gj),(+self.a-self.gj),(+self.b-self.gj),(+self.c-self.gj),(+self.d-self.gj),(+self.e-self.gj),(+self.f-self.gj),(+self.g-self.gj),(+self.h-self.gj),(-self.a-self.hj),(-self.b-self.hj),(-self.c-self.hj),(-self.d-self.hj),(-self.e-self.hj),(-self.f-self.hj),(-self.g-self.hj),(-self.h-self.hj),(+self.a-self.hj),(+self.b-self.hj),(+self.c-self.hj),(+self.d-self.hj),(+self.e-self.hj),(+self.f-self.hj),(+self.g-self.hj),(+self.h-self.hj))
        self.set_sym3((-self.a+self.ej),(-self.b+self.ej),(-self.c+self.ej),(-self.d+self.ej),(-self.e+self.ej),(-self.f+self.ej),(-self.g+self.ej),(-self.h+self.ej),(+self.a+self.ej),(+self.b+self.ej),(+self.c+self.ej),(+self.d+self.ej),(+self.e+self.ej),(+self.f+self.ej),(+self.g+self.ej),(+self.h+self.ej),(-self.a+self.fj),(-self.b+self.fj),(-self.c+self.fj),(-self.d+self.fj),(-self.e+self.fj),(-self.f+self.fj),(-self.g+self.fj),(-self.h+self.fj),(+self.a+self.fj),(+self.b+self.fj),(+self.c+self.fj),(+self.d+self.fj),(+self.e+self.fj),(+self.f+self.fj),(+self.g+self.fj),(+self.h+self.fj),(-self.a+self.gj),(-self.b+self.gj),(-self.c+self.gj),(-self.d+self.gj),(-self.e+self.gj),(-self.f+self.gj),(-self.g+self.gj),(-self.h+self.gj),(+self.a+self.gj),(+self.b+self.gj),(+self.c+self.gj),(+self.d+self.gj),(+self.e+self.gj),(+self.f+self.gj),(+self.g+self.gj),(+self.h+self.gj),(-self.a+self.hj),(-self.b+self.hj),(-self.c+self.hj),(-self.d+self.hj),(-self.e+self.hj),(-self.f+self.hj),(-self.g+self.hj),(-self.h+self.hj),(+self.a+self.hj),(+self.b+self.hj),(+self.c+self.hj),(+self.d+self.hj),(+self.e+self.hj),(+self.f+self.hj),(+self.g+self.hj),(+self.h+self.hj))

    def get_g(self):
        return self.g

    def set_g(self, g):
        self.g = g
        self.set_sym0((-self.a-self.aj),(-self.b-self.aj),(-self.c-self.aj),(-self.d-self.aj),(-self.e-self.aj),(-self.f-self.aj),(-self.g-self.aj),(-self.h-self.aj),(+self.a-self.aj),(+self.b-self.aj),(+self.c-self.aj),(+self.d-self.aj),(+self.e-self.aj),(+self.f-self.aj),(+self.g-self.aj),(+self.h-self.aj),(-self.a-self.bj),(-self.b-self.bj),(-self.c-self.bj),(-self.d-self.bj),(-self.e-self.bj),(-self.f-self.bj),(-self.g-self.bj),(-self.h-self.bj),(+self.a-self.bj),(+self.b-self.bj),(+self.c-self.bj),(+self.d-self.bj),(+self.e-self.bj),(+self.f-self.bj),(+self.g-self.bj),(+self.h-self.bj),(-self.a-self.cj),(-self.b-self.cj),(-self.c-self.cj),(-self.d-self.cj),(-self.e-self.cj),(-self.f-self.cj),(-self.g-self.cj),(-self.h-self.cj),(+self.a-self.cj),(+self.b-self.cj),(+self.c-self.cj),(+self.d-self.cj),(+self.e-self.cj),(+self.f-self.cj),(+self.g-self.cj),(+self.h-self.cj),(-self.a-self.dj),(-self.b-self.dj),(-self.c-self.dj),(-self.d-self.dj),(-self.e-self.dj),(-self.f-self.dj),(-self.g-self.dj),(-self.h-self.dj),(+self.a-self.dj),(+self.b-self.dj),(+self.c-self.dj),(+self.d-self.dj),(+self.e-self.dj),(+self.f-self.dj),(+self.g-self.dj),(+self.h-self.dj))
        self.set_sym1((-self.a-self.ej),(-self.b-self.ej),(-self.c-self.ej),(-self.d-self.ej),(-self.e-self.ej),(-self.f-self.ej),(-self.g-self.ej),(-self.h-self.ej),(+self.a-self.ej),(+self.b-self.ej),(+self.c-self.ej),(+self.d-self.ej),(+self.e-self.ej),(+self.f-self.ej),(+self.g-self.ej),(+self.h-self.ej),(-self.a-self.fj),(-self.b-self.fj),(-self.c-self.fj),(-self.d-self.fj),(-self.e-self.fj),(-self.f-self.fj),(-self.g-self.fj),(-self.h-self.fj),(+self.a-self.fj),(+self.b-self.fj),(+self.c-self.fj),(+self.d-self.fj),(+self.e-self.fj),(+self.f-self.fj),(+self.g-self.fj),(+self.h-self.fj),(-self.a-self.gj),(-self.b-self.gj),(-self.c-self.gj),(-self.d-self.gj),(-self.e-self.gj),(-self.f-self.gj),(-self.g-self.gj),(-self.h-self.gj),(+self.a-self.gj),(+self.b-self.gj),(+self.c-self.gj),(+self.d-self.gj),(+self.e-self.gj),(+self.f-self.gj),(+self.g-self.gj),(+self.h-self.gj),(-self.a-self.hj),(-self.b-self.hj),(-self.c-self.hj),(-self.d-self.hj),(-self.e-self.hj),(-self.f-self.hj),(-self.g-self.hj),(-self.h-self.hj),(+self.a-self.hj),(+self.b-self.hj),(+self.c-self.hj),(+self.d-self.hj),(+self.e-self.hj),(+self.f-self.hj),(+self.g-self.hj),(+self.h-self.hj))
        self.set_sym2((-self.a+self.aj),(-self.b+self.aj),(-self.c+self.aj),(-self.d+self.aj),(-self.e+self.aj),(-self.f+self.aj),(-self.g+self.aj),(-self.h+self.aj),(+self.a+self.aj),(+self.b+self.aj),(+self.c+self.aj),(+self.d+self.aj),(+self.e+self.aj),(+self.f+self.aj),(+self.g+self.aj),(+self.h+self.aj),(-self.a+self.bj),(-self.b+self.bj),(-self.c+self.bj),(-self.d+self.bj),(-self.e+self.bj),(-self.f+self.bj),(-self.g+self.bj),(-self.h+self.bj),(+self.a+self.bj),(+self.b+self.bj),(+self.c+self.bj),(+self.d+self.bj),(+self.e+self.bj),(+self.f+self.bj),(+self.g+self.bj),(+self.h+self.bj),(-self.a+self.cj),(-self.b+self.cj),(-self.c+self.cj),(-self.d+self.cj),(-self.e+self.cj),(-self.f+self.cj),(-self.g+self.cj),(-self.h+self.cj),(+self.a+self.cj),(+self.b+self.cj),(+self.c+self.cj),(+self.d+self.cj),(+self.e+self.cj),(+self.f+self.cj),(+self.g+self.cj),(+self.h+self.cj),(-self.a+self.dj),(-self.b+self.dj),(-self.c+self.dj),(-self.d+self.dj),(-self.e+self.dj),(-self.f+self.dj),(-self.g+self.dj),(-self.h+self.dj),(+self.a+self.dj),(+self.b+self.dj),(+self.c+self.dj),(+self.d+self.dj),(+self.e+self.dj),(+self.f+self.dj),(+self.g+self.dj),(+self.h+self.dj))
        self.set_sym3((-self.a+self.ej),(-self.b+self.ej),(-self.c+self.ej),(-self.d+self.ej),(-self.e+self.ej),(-self.f+self.ej),(-self.g+self.ej),(-self.h+self.ej),(+self.a+self.ej),(+self.b+self.ej),(+self.c+self.ej),(+self.d+self.ej),(+self.e+self.ej),(+self.f+self.ej),(+self.g+self.ej),(+self.h+self.ej),(-self.a+self.fj),(-self.b+self.fj),(-self.c+self.fj),(-self.d+self.fj),(-self.e+self.fj),(-self.f+self.fj),(-self.g+self.fj),(-self.h+self.fj),(+self.a+self.fj),(+self.b+self.fj),(+self.c+self.fj),(+self.d+self.fj),(+self.e+self.fj),(+self.f+self.fj),(+self.g+self.fj),(+self.h+self.fj),(-self.a+self.gj),(-self.b+self.gj),(-self.c+self.gj),(-self.d+self.gj),(-self.e+self.gj),(-self.f+self.gj),(-self.g+self.gj),(-self.h+self.gj),(+self.a+self.gj),(+self.b+self.gj),(+self.c+self.gj),(+self.d+self.gj),(+self.e+self.gj),(+self.f+self.gj),(+self.g+self.gj),(+self.h+self.gj),(-self.a+self.hj),(-self.b+self.hj),(-self.c+self.hj),(-self.d+self.hj),(-self.e+self.hj),(-self.f+self.hj),(-self.g+self.hj),(-self.h+self.hj),(+self.a+self.hj),(+self.b+self.hj),(+self.c+self.hj),(+self.d+self.hj),(+self.e+self.hj),(+self.f+self.hj),(+self.g+self.hj),(+self.h+self.hj))

    def get_fj(self):
        return self.fj

    def set_fj(self, fj):
        self.fj = fj
        self.set_sym1((-self.a-self.ej),(-self.b-self.ej),(-self.c-self.ej),(-self.d-self.ej),(-self.e-self.ej),(-self.f-self.ej),(-self.g-self.ej),(-self.h-self.ej),(+self.a-self.ej),(+self.b-self.ej),(+self.c-self.ej),(+self.d-self.ej),(+self.e-self.ej),(+self.f-self.ej),(+self.g-self.ej),(+self.h-self.ej),(-self.a-self.fj),(-self.b-self.fj),(-self.c-self.fj),(-self.d-self.fj),(-self.e-self.fj),(-self.f-self.fj),(-self.g-self.fj),(-self.h-self.fj),(+self.a-self.fj),(+self.b-self.fj),(+self.c-self.fj),(+self.d-self.fj),(+self.e-self.fj),(+self.f-self.fj),(+self.g-self.fj),(+self.h-self.fj),(-self.a-self.gj),(-self.b-self.gj),(-self.c-self.gj),(-self.d-self.gj),(-self.e-self.gj),(-self.f-self.gj),(-self.g-self.gj),(-self.h-self.gj),(+self.a-self.gj),(+self.b-self.gj),(+self.c-self.gj),(+self.d-self.gj),(+self.e-self.gj),(+self.f-self.gj),(+self.g-self.gj),(+self.h-self.gj),(-self.a-self.hj),(-self.b-self.hj),(-self.c-self.hj),(-self.d-self.hj),(-self.e-self.hj),(-self.f-self.hj),(-self.g-self.hj),(-self.h-self.hj),(+self.a-self.hj),(+self.b-self.hj),(+self.c-self.hj),(+self.d-self.hj),(+self.e-self.hj),(+self.f-self.hj),(+self.g-self.hj),(+self.h-self.hj))
        self.set_sym3((-self.a+self.ej),(-self.b+self.ej),(-self.c+self.ej),(-self.d+self.ej),(-self.e+self.ej),(-self.f+self.ej),(-self.g+self.ej),(-self.h+self.ej),(+self.a+self.ej),(+self.b+self.ej),(+self.c+self.ej),(+self.d+self.ej),(+self.e+self.ej),(+self.f+self.ej),(+self.g+self.ej),(+self.h+self.ej),(-self.a+self.fj),(-self.b+self.fj),(-self.c+self.fj),(-self.d+self.fj),(-self.e+self.fj),(-self.f+self.fj),(-self.g+self.fj),(-self.h+self.fj),(+self.a+self.fj),(+self.b+self.fj),(+self.c+self.fj),(+self.d+self.fj),(+self.e+self.fj),(+self.f+self.fj),(+self.g+self.fj),(+self.h+self.fj),(-self.a+self.gj),(-self.b+self.gj),(-self.c+self.gj),(-self.d+self.gj),(-self.e+self.gj),(-self.f+self.gj),(-self.g+self.gj),(-self.h+self.gj),(+self.a+self.gj),(+self.b+self.gj),(+self.c+self.gj),(+self.d+self.gj),(+self.e+self.gj),(+self.f+self.gj),(+self.g+self.gj),(+self.h+self.gj),(-self.a+self.hj),(-self.b+self.hj),(-self.c+self.hj),(-self.d+self.hj),(-self.e+self.hj),(-self.f+self.hj),(-self.g+self.hj),(-self.h+self.hj),(+self.a+self.hj),(+self.b+self.hj),(+self.c+self.hj),(+self.d+self.hj),(+self.e+self.hj),(+self.f+self.hj),(+self.g+self.hj),(+self.h+self.hj))

    def get_f(self):
        return self.f

    def set_f(self, f):
        self.f = f
        self.set_sym0((-self.a-self.aj),(-self.b-self.aj),(-self.c-self.aj),(-self.d-self.aj),(-self.e-self.aj),(-self.f-self.aj),(-self.g-self.aj),(-self.h-self.aj),(+self.a-self.aj),(+self.b-self.aj),(+self.c-self.aj),(+self.d-self.aj),(+self.e-self.aj),(+self.f-self.aj),(+self.g-self.aj),(+self.h-self.aj),(-self.a-self.bj),(-self.b-self.bj),(-self.c-self.bj),(-self.d-self.bj),(-self.e-self.bj),(-self.f-self.bj),(-self.g-self.bj),(-self.h-self.bj),(+self.a-self.bj),(+self.b-self.bj),(+self.c-self.bj),(+self.d-self.bj),(+self.e-self.bj),(+self.f-self.bj),(+self.g-self.bj),(+self.h-self.bj),(-self.a-self.cj),(-self.b-self.cj),(-self.c-self.cj),(-self.d-self.cj),(-self.e-self.cj),(-self.f-self.cj),(-self.g-self.cj),(-self.h-self.cj),(+self.a-self.cj),(+self.b-self.cj),(+self.c-self.cj),(+self.d-self.cj),(+self.e-self.cj),(+self.f-self.cj),(+self.g-self.cj),(+self.h-self.cj),(-self.a-self.dj),(-self.b-self.dj),(-self.c-self.dj),(-self.d-self.dj),(-self.e-self.dj),(-self.f-self.dj),(-self.g-self.dj),(-self.h-self.dj),(+self.a-self.dj),(+self.b-self.dj),(+self.c-self.dj),(+self.d-self.dj),(+self.e-self.dj),(+self.f-self.dj),(+self.g-self.dj),(+self.h-self.dj))
        self.set_sym1((-self.a-self.ej),(-self.b-self.ej),(-self.c-self.ej),(-self.d-self.ej),(-self.e-self.ej),(-self.f-self.ej),(-self.g-self.ej),(-self.h-self.ej),(+self.a-self.ej),(+self.b-self.ej),(+self.c-self.ej),(+self.d-self.ej),(+self.e-self.ej),(+self.f-self.ej),(+self.g-self.ej),(+self.h-self.ej),(-self.a-self.fj),(-self.b-self.fj),(-self.c-self.fj),(-self.d-self.fj),(-self.e-self.fj),(-self.f-self.fj),(-self.g-self.fj),(-self.h-self.fj),(+self.a-self.fj),(+self.b-self.fj),(+self.c-self.fj),(+self.d-self.fj),(+self.e-self.fj),(+self.f-self.fj),(+self.g-self.fj),(+self.h-self.fj),(-self.a-self.gj),(-self.b-self.gj),(-self.c-self.gj),(-self.d-self.gj),(-self.e-self.gj),(-self.f-self.gj),(-self.g-self.gj),(-self.h-self.gj),(+self.a-self.gj),(+self.b-self.gj),(+self.c-self.gj),(+self.d-self.gj),(+self.e-self.gj),(+self.f-self.gj),(+self.g-self.gj),(+self.h-self.gj),(-self.a-self.hj),(-self.b-self.hj),(-self.c-self.hj),(-self.d-self.hj),(-self.e-self.hj),(-self.f-self.hj),(-self.g-self.hj),(-self.h-self.hj),(+self.a-self.hj),(+self.b-self.hj),(+self.c-self.hj),(+self.d-self.hj),(+self.e-self.hj),(+self.f-self.hj),(+self.g-self.hj),(+self.h-self.hj))
        self.set_sym2((-self.a+self.aj),(-self.b+self.aj),(-self.c+self.aj),(-self.d+self.aj),(-self.e+self.aj),(-self.f+self.aj),(-self.g+self.aj),(-self.h+self.aj),(+self.a+self.aj),(+self.b+self.aj),(+self.c+self.aj),(+self.d+self.aj),(+self.e+self.aj),(+self.f+self.aj),(+self.g+self.aj),(+self.h+self.aj),(-self.a+self.bj),(-self.b+self.bj),(-self.c+self.bj),(-self.d+self.bj),(-self.e+self.bj),(-self.f+self.bj),(-self.g+self.bj),(-self.h+self.bj),(+self.a+self.bj),(+self.b+self.bj),(+self.c+self.bj),(+self.d+self.bj),(+self.e+self.bj),(+self.f+self.bj),(+self.g+self.bj),(+self.h+self.bj),(-self.a+self.cj),(-self.b+self.cj),(-self.c+self.cj),(-self.d+self.cj),(-self.e+self.cj),(-self.f+self.cj),(-self.g+self.cj),(-self.h+self.cj),(+self.a+self.cj),(+self.b+self.cj),(+self.c+self.cj),(+self.d+self.cj),(+self.e+self.cj),(+self.f+self.cj),(+self.g+self.cj),(+self.h+self.cj),(-self.a+self.dj),(-self.b+self.dj),(-self.c+self.dj),(-self.d+self.dj),(-self.e+self.dj),(-self.f+self.dj),(-self.g+self.dj),(-self.h+self.dj),(+self.a+self.dj),(+self.b+self.dj),(+self.c+self.dj),(+self.d+self.dj),(+self.e+self.dj),(+self.f+self.dj),(+self.g+self.dj),(+self.h+self.dj))
        self.set_sym3((-self.a+self.ej),(-self.b+self.ej),(-self.c+self.ej),(-self.d+self.ej),(-self.e+self.ej),(-self.f+self.ej),(-self.g+self.ej),(-self.h+self.ej),(+self.a+self.ej),(+self.b+self.ej),(+self.c+self.ej),(+self.d+self.ej),(+self.e+self.ej),(+self.f+self.ej),(+self.g+self.ej),(+self.h+self.ej),(-self.a+self.fj),(-self.b+self.fj),(-self.c+self.fj),(-self.d+self.fj),(-self.e+self.fj),(-self.f+self.fj),(-self.g+self.fj),(-self.h+self.fj),(+self.a+self.fj),(+self.b+self.fj),(+self.c+self.fj),(+self.d+self.fj),(+self.e+self.fj),(+self.f+self.fj),(+self.g+self.fj),(+self.h+self.fj),(-self.a+self.gj),(-self.b+self.gj),(-self.c+self.gj),(-self.d+self.gj),(-self.e+self.gj),(-self.f+self.gj),(-self.g+self.gj),(-self.h+self.gj),(+self.a+self.gj),(+self.b+self.gj),(+self.c+self.gj),(+self.d+self.gj),(+self.e+self.gj),(+self.f+self.gj),(+self.g+self.gj),(+self.h+self.gj),(-self.a+self.hj),(-self.b+self.hj),(-self.c+self.hj),(-self.d+self.hj),(-self.e+self.hj),(-self.f+self.hj),(-self.g+self.hj),(-self.h+self.hj),(+self.a+self.hj),(+self.b+self.hj),(+self.c+self.hj),(+self.d+self.hj),(+self.e+self.hj),(+self.f+self.hj),(+self.g+self.hj),(+self.h+self.hj))

    def get_ej(self):
        return self.ej

    def set_ej(self, ej):
        self.ej = ej
        self.set_sym1((-self.a-self.ej),(-self.b-self.ej),(-self.c-self.ej),(-self.d-self.ej),(-self.e-self.ej),(-self.f-self.ej),(-self.g-self.ej),(-self.h-self.ej),(+self.a-self.ej),(+self.b-self.ej),(+self.c-self.ej),(+self.d-self.ej),(+self.e-self.ej),(+self.f-self.ej),(+self.g-self.ej),(+self.h-self.ej),(-self.a-self.fj),(-self.b-self.fj),(-self.c-self.fj),(-self.d-self.fj),(-self.e-self.fj),(-self.f-self.fj),(-self.g-self.fj),(-self.h-self.fj),(+self.a-self.fj),(+self.b-self.fj),(+self.c-self.fj),(+self.d-self.fj),(+self.e-self.fj),(+self.f-self.fj),(+self.g-self.fj),(+self.h-self.fj),(-self.a-self.gj),(-self.b-self.gj),(-self.c-self.gj),(-self.d-self.gj),(-self.e-self.gj),(-self.f-self.gj),(-self.g-self.gj),(-self.h-self.gj),(+self.a-self.gj),(+self.b-self.gj),(+self.c-self.gj),(+self.d-self.gj),(+self.e-self.gj),(+self.f-self.gj),(+self.g-self.gj),(+self.h-self.gj),(-self.a-self.hj),(-self.b-self.hj),(-self.c-self.hj),(-self.d-self.hj),(-self.e-self.hj),(-self.f-self.hj),(-self.g-self.hj),(-self.h-self.hj),(+self.a-self.hj),(+self.b-self.hj),(+self.c-self.hj),(+self.d-self.hj),(+self.e-self.hj),(+self.f-self.hj),(+self.g-self.hj),(+self.h-self.hj))
        self.set_sym3((-self.a+self.ej),(-self.b+self.ej),(-self.c+self.ej),(-self.d+self.ej),(-self.e+self.ej),(-self.f+self.ej),(-self.g+self.ej),(-self.h+self.ej),(+self.a+self.ej),(+self.b+self.ej),(+self.c+self.ej),(+self.d+self.ej),(+self.e+self.ej),(+self.f+self.ej),(+self.g+self.ej),(+self.h+self.ej),(-self.a+self.fj),(-self.b+self.fj),(-self.c+self.fj),(-self.d+self.fj),(-self.e+self.fj),(-self.f+self.fj),(-self.g+self.fj),(-self.h+self.fj),(+self.a+self.fj),(+self.b+self.fj),(+self.c+self.fj),(+self.d+self.fj),(+self.e+self.fj),(+self.f+self.fj),(+self.g+self.fj),(+self.h+self.fj),(-self.a+self.gj),(-self.b+self.gj),(-self.c+self.gj),(-self.d+self.gj),(-self.e+self.gj),(-self.f+self.gj),(-self.g+self.gj),(-self.h+self.gj),(+self.a+self.gj),(+self.b+self.gj),(+self.c+self.gj),(+self.d+self.gj),(+self.e+self.gj),(+self.f+self.gj),(+self.g+self.gj),(+self.h+self.gj),(-self.a+self.hj),(-self.b+self.hj),(-self.c+self.hj),(-self.d+self.hj),(-self.e+self.hj),(-self.f+self.hj),(-self.g+self.hj),(-self.h+self.hj),(+self.a+self.hj),(+self.b+self.hj),(+self.c+self.hj),(+self.d+self.hj),(+self.e+self.hj),(+self.f+self.hj),(+self.g+self.hj),(+self.h+self.hj))

    def get_e(self):
        return self.e

    def set_e(self, e):
        self.e = e
        self.set_sym0((-self.a-self.aj),(-self.b-self.aj),(-self.c-self.aj),(-self.d-self.aj),(-self.e-self.aj),(-self.f-self.aj),(-self.g-self.aj),(-self.h-self.aj),(+self.a-self.aj),(+self.b-self.aj),(+self.c-self.aj),(+self.d-self.aj),(+self.e-self.aj),(+self.f-self.aj),(+self.g-self.aj),(+self.h-self.aj),(-self.a-self.bj),(-self.b-self.bj),(-self.c-self.bj),(-self.d-self.bj),(-self.e-self.bj),(-self.f-self.bj),(-self.g-self.bj),(-self.h-self.bj),(+self.a-self.bj),(+self.b-self.bj),(+self.c-self.bj),(+self.d-self.bj),(+self.e-self.bj),(+self.f-self.bj),(+self.g-self.bj),(+self.h-self.bj),(-self.a-self.cj),(-self.b-self.cj),(-self.c-self.cj),(-self.d-self.cj),(-self.e-self.cj),(-self.f-self.cj),(-self.g-self.cj),(-self.h-self.cj),(+self.a-self.cj),(+self.b-self.cj),(+self.c-self.cj),(+self.d-self.cj),(+self.e-self.cj),(+self.f-self.cj),(+self.g-self.cj),(+self.h-self.cj),(-self.a-self.dj),(-self.b-self.dj),(-self.c-self.dj),(-self.d-self.dj),(-self.e-self.dj),(-self.f-self.dj),(-self.g-self.dj),(-self.h-self.dj),(+self.a-self.dj),(+self.b-self.dj),(+self.c-self.dj),(+self.d-self.dj),(+self.e-self.dj),(+self.f-self.dj),(+self.g-self.dj),(+self.h-self.dj))
        self.set_sym1((-self.a-self.ej),(-self.b-self.ej),(-self.c-self.ej),(-self.d-self.ej),(-self.e-self.ej),(-self.f-self.ej),(-self.g-self.ej),(-self.h-self.ej),(+self.a-self.ej),(+self.b-self.ej),(+self.c-self.ej),(+self.d-self.ej),(+self.e-self.ej),(+self.f-self.ej),(+self.g-self.ej),(+self.h-self.ej),(-self.a-self.fj),(-self.b-self.fj),(-self.c-self.fj),(-self.d-self.fj),(-self.e-self.fj),(-self.f-self.fj),(-self.g-self.fj),(-self.h-self.fj),(+self.a-self.fj),(+self.b-self.fj),(+self.c-self.fj),(+self.d-self.fj),(+self.e-self.fj),(+self.f-self.fj),(+self.g-self.fj),(+self.h-self.fj),(-self.a-self.gj),(-self.b-self.gj),(-self.c-self.gj),(-self.d-self.gj),(-self.e-self.gj),(-self.f-self.gj),(-self.g-self.gj),(-self.h-self.gj),(+self.a-self.gj),(+self.b-self.gj),(+self.c-self.gj),(+self.d-self.gj),(+self.e-self.gj),(+self.f-self.gj),(+self.g-self.gj),(+self.h-self.gj),(-self.a-self.hj),(-self.b-self.hj),(-self.c-self.hj),(-self.d-self.hj),(-self.e-self.hj),(-self.f-self.hj),(-self.g-self.hj),(-self.h-self.hj),(+self.a-self.hj),(+self.b-self.hj),(+self.c-self.hj),(+self.d-self.hj),(+self.e-self.hj),(+self.f-self.hj),(+self.g-self.hj),(+self.h-self.hj))
        self.set_sym2((-self.a+self.aj),(-self.b+self.aj),(-self.c+self.aj),(-self.d+self.aj),(-self.e+self.aj),(-self.f+self.aj),(-self.g+self.aj),(-self.h+self.aj),(+self.a+self.aj),(+self.b+self.aj),(+self.c+self.aj),(+self.d+self.aj),(+self.e+self.aj),(+self.f+self.aj),(+self.g+self.aj),(+self.h+self.aj),(-self.a+self.bj),(-self.b+self.bj),(-self.c+self.bj),(-self.d+self.bj),(-self.e+self.bj),(-self.f+self.bj),(-self.g+self.bj),(-self.h+self.bj),(+self.a+self.bj),(+self.b+self.bj),(+self.c+self.bj),(+self.d+self.bj),(+self.e+self.bj),(+self.f+self.bj),(+self.g+self.bj),(+self.h+self.bj),(-self.a+self.cj),(-self.b+self.cj),(-self.c+self.cj),(-self.d+self.cj),(-self.e+self.cj),(-self.f+self.cj),(-self.g+self.cj),(-self.h+self.cj),(+self.a+self.cj),(+self.b+self.cj),(+self.c+self.cj),(+self.d+self.cj),(+self.e+self.cj),(+self.f+self.cj),(+self.g+self.cj),(+self.h+self.cj),(-self.a+self.dj),(-self.b+self.dj),(-self.c+self.dj),(-self.d+self.dj),(-self.e+self.dj),(-self.f+self.dj),(-self.g+self.dj),(-self.h+self.dj),(+self.a+self.dj),(+self.b+self.dj),(+self.c+self.dj),(+self.d+self.dj),(+self.e+self.dj),(+self.f+self.dj),(+self.g+self.dj),(+self.h+self.dj))
        self.set_sym3((-self.a+self.ej),(-self.b+self.ej),(-self.c+self.ej),(-self.d+self.ej),(-self.e+self.ej),(-self.f+self.ej),(-self.g+self.ej),(-self.h+self.ej),(+self.a+self.ej),(+self.b+self.ej),(+self.c+self.ej),(+self.d+self.ej),(+self.e+self.ej),(+self.f+self.ej),(+self.g+self.ej),(+self.h+self.ej),(-self.a+self.fj),(-self.b+self.fj),(-self.c+self.fj),(-self.d+self.fj),(-self.e+self.fj),(-self.f+self.fj),(-self.g+self.fj),(-self.h+self.fj),(+self.a+self.fj),(+self.b+self.fj),(+self.c+self.fj),(+self.d+self.fj),(+self.e+self.fj),(+self.f+self.fj),(+self.g+self.fj),(+self.h+self.fj),(-self.a+self.gj),(-self.b+self.gj),(-self.c+self.gj),(-self.d+self.gj),(-self.e+self.gj),(-self.f+self.gj),(-self.g+self.gj),(-self.h+self.gj),(+self.a+self.gj),(+self.b+self.gj),(+self.c+self.gj),(+self.d+self.gj),(+self.e+self.gj),(+self.f+self.gj),(+self.g+self.gj),(+self.h+self.gj),(-self.a+self.hj),(-self.b+self.hj),(-self.c+self.hj),(-self.d+self.hj),(-self.e+self.hj),(-self.f+self.hj),(-self.g+self.hj),(-self.h+self.hj),(+self.a+self.hj),(+self.b+self.hj),(+self.c+self.hj),(+self.d+self.hj),(+self.e+self.hj),(+self.f+self.hj),(+self.g+self.hj),(+self.h+self.hj))

    def get_dj(self):
        return self.dj

    def set_dj(self, dj):
        self.dj = dj
        self.set_sym0((-self.a-self.aj),(-self.b-self.aj),(-self.c-self.aj),(-self.d-self.aj),(-self.e-self.aj),(-self.f-self.aj),(-self.g-self.aj),(-self.h-self.aj),(+self.a-self.aj),(+self.b-self.aj),(+self.c-self.aj),(+self.d-self.aj),(+self.e-self.aj),(+self.f-self.aj),(+self.g-self.aj),(+self.h-self.aj),(-self.a-self.bj),(-self.b-self.bj),(-self.c-self.bj),(-self.d-self.bj),(-self.e-self.bj),(-self.f-self.bj),(-self.g-self.bj),(-self.h-self.bj),(+self.a-self.bj),(+self.b-self.bj),(+self.c-self.bj),(+self.d-self.bj),(+self.e-self.bj),(+self.f-self.bj),(+self.g-self.bj),(+self.h-self.bj),(-self.a-self.cj),(-self.b-self.cj),(-self.c-self.cj),(-self.d-self.cj),(-self.e-self.cj),(-self.f-self.cj),(-self.g-self.cj),(-self.h-self.cj),(+self.a-self.cj),(+self.b-self.cj),(+self.c-self.cj),(+self.d-self.cj),(+self.e-self.cj),(+self.f-self.cj),(+self.g-self.cj),(+self.h-self.cj),(-self.a-self.dj),(-self.b-self.dj),(-self.c-self.dj),(-self.d-self.dj),(-self.e-self.dj),(-self.f-self.dj),(-self.g-self.dj),(-self.h-self.dj),(+self.a-self.dj),(+self.b-self.dj),(+self.c-self.dj),(+self.d-self.dj),(+self.e-self.dj),(+self.f-self.dj),(+self.g-self.dj),(+self.h-self.dj))
        self.set_sym2((-self.a+self.aj),(-self.b+self.aj),(-self.c+self.aj),(-self.d+self.aj),(-self.e+self.aj),(-self.f+self.aj),(-self.g+self.aj),(-self.h+self.aj),(+self.a+self.aj),(+self.b+self.aj),(+self.c+self.aj),(+self.d+self.aj),(+self.e+self.aj),(+self.f+self.aj),(+self.g+self.aj),(+self.h+self.aj),(-self.a+self.bj),(-self.b+self.bj),(-self.c+self.bj),(-self.d+self.bj),(-self.e+self.bj),(-self.f+self.bj),(-self.g+self.bj),(-self.h+self.bj),(+self.a+self.bj),(+self.b+self.bj),(+self.c+self.bj),(+self.d+self.bj),(+self.e+self.bj),(+self.f+self.bj),(+self.g+self.bj),(+self.h+self.bj),(-self.a+self.cj),(-self.b+self.cj),(-self.c+self.cj),(-self.d+self.cj),(-self.e+self.cj),(-self.f+self.cj),(-self.g+self.cj),(-self.h+self.cj),(+self.a+self.cj),(+self.b+self.cj),(+self.c+self.cj),(+self.d+self.cj),(+self.e+self.cj),(+self.f+self.cj),(+self.g+self.cj),(+self.h+self.cj),(-self.a+self.dj),(-self.b+self.dj),(-self.c+self.dj),(-self.d+self.dj),(-self.e+self.dj),(-self.f+self.dj),(-self.g+self.dj),(-self.h+self.dj),(+self.a+self.dj),(+self.b+self.dj),(+self.c+self.dj),(+self.d+self.dj),(+self.e+self.dj),(+self.f+self.dj),(+self.g+self.dj),(+self.h+self.dj))

    def get_d(self):
        return self.d

    def set_d(self, d):
        self.d = d
        self.set_sym0((-self.a-self.aj),(-self.b-self.aj),(-self.c-self.aj),(-self.d-self.aj),(-self.e-self.aj),(-self.f-self.aj),(-self.g-self.aj),(-self.h-self.aj),(+self.a-self.aj),(+self.b-self.aj),(+self.c-self.aj),(+self.d-self.aj),(+self.e-self.aj),(+self.f-self.aj),(+self.g-self.aj),(+self.h-self.aj),(-self.a-self.bj),(-self.b-self.bj),(-self.c-self.bj),(-self.d-self.bj),(-self.e-self.bj),(-self.f-self.bj),(-self.g-self.bj),(-self.h-self.bj),(+self.a-self.bj),(+self.b-self.bj),(+self.c-self.bj),(+self.d-self.bj),(+self.e-self.bj),(+self.f-self.bj),(+self.g-self.bj),(+self.h-self.bj),(-self.a-self.cj),(-self.b-self.cj),(-self.c-self.cj),(-self.d-self.cj),(-self.e-self.cj),(-self.f-self.cj),(-self.g-self.cj),(-self.h-self.cj),(+self.a-self.cj),(+self.b-self.cj),(+self.c-self.cj),(+self.d-self.cj),(+self.e-self.cj),(+self.f-self.cj),(+self.g-self.cj),(+self.h-self.cj),(-self.a-self.dj),(-self.b-self.dj),(-self.c-self.dj),(-self.d-self.dj),(-self.e-self.dj),(-self.f-self.dj),(-self.g-self.dj),(-self.h-self.dj),(+self.a-self.dj),(+self.b-self.dj),(+self.c-self.dj),(+self.d-self.dj),(+self.e-self.dj),(+self.f-self.dj),(+self.g-self.dj),(+self.h-self.dj))
        self.set_sym1((-self.a-self.ej),(-self.b-self.ej),(-self.c-self.ej),(-self.d-self.ej),(-self.e-self.ej),(-self.f-self.ej),(-self.g-self.ej),(-self.h-self.ej),(+self.a-self.ej),(+self.b-self.ej),(+self.c-self.ej),(+self.d-self.ej),(+self.e-self.ej),(+self.f-self.ej),(+self.g-self.ej),(+self.h-self.ej),(-self.a-self.fj),(-self.b-self.fj),(-self.c-self.fj),(-self.d-self.fj),(-self.e-self.fj),(-self.f-self.fj),(-self.g-self.fj),(-self.h-self.fj),(+self.a-self.fj),(+self.b-self.fj),(+self.c-self.fj),(+self.d-self.fj),(+self.e-self.fj),(+self.f-self.fj),(+self.g-self.fj),(+self.h-self.fj),(-self.a-self.gj),(-self.b-self.gj),(-self.c-self.gj),(-self.d-self.gj),(-self.e-self.gj),(-self.f-self.gj),(-self.g-self.gj),(-self.h-self.gj),(+self.a-self.gj),(+self.b-self.gj),(+self.c-self.gj),(+self.d-self.gj),(+self.e-self.gj),(+self.f-self.gj),(+self.g-self.gj),(+self.h-self.gj),(-self.a-self.hj),(-self.b-self.hj),(-self.c-self.hj),(-self.d-self.hj),(-self.e-self.hj),(-self.f-self.hj),(-self.g-self.hj),(-self.h-self.hj),(+self.a-self.hj),(+self.b-self.hj),(+self.c-self.hj),(+self.d-self.hj),(+self.e-self.hj),(+self.f-self.hj),(+self.g-self.hj),(+self.h-self.hj))
        self.set_sym2((-self.a+self.aj),(-self.b+self.aj),(-self.c+self.aj),(-self.d+self.aj),(-self.e+self.aj),(-self.f+self.aj),(-self.g+self.aj),(-self.h+self.aj),(+self.a+self.aj),(+self.b+self.aj),(+self.c+self.aj),(+self.d+self.aj),(+self.e+self.aj),(+self.f+self.aj),(+self.g+self.aj),(+self.h+self.aj),(-self.a+self.bj),(-self.b+self.bj),(-self.c+self.bj),(-self.d+self.bj),(-self.e+self.bj),(-self.f+self.bj),(-self.g+self.bj),(-self.h+self.bj),(+self.a+self.bj),(+self.b+self.bj),(+self.c+self.bj),(+self.d+self.bj),(+self.e+self.bj),(+self.f+self.bj),(+self.g+self.bj),(+self.h+self.bj),(-self.a+self.cj),(-self.b+self.cj),(-self.c+self.cj),(-self.d+self.cj),(-self.e+self.cj),(-self.f+self.cj),(-self.g+self.cj),(-self.h+self.cj),(+self.a+self.cj),(+self.b+self.cj),(+self.c+self.cj),(+self.d+self.cj),(+self.e+self.cj),(+self.f+self.cj),(+self.g+self.cj),(+self.h+self.cj),(-self.a+self.dj),(-self.b+self.dj),(-self.c+self.dj),(-self.d+self.dj),(-self.e+self.dj),(-self.f+self.dj),(-self.g+self.dj),(-self.h+self.dj),(+self.a+self.dj),(+self.b+self.dj),(+self.c+self.dj),(+self.d+self.dj),(+self.e+self.dj),(+self.f+self.dj),(+self.g+self.dj),(+self.h+self.dj))
        self.set_sym3((-self.a+self.ej),(-self.b+self.ej),(-self.c+self.ej),(-self.d+self.ej),(-self.e+self.ej),(-self.f+self.ej),(-self.g+self.ej),(-self.h+self.ej),(+self.a+self.ej),(+self.b+self.ej),(+self.c+self.ej),(+self.d+self.ej),(+self.e+self.ej),(+self.f+self.ej),(+self.g+self.ej),(+self.h+self.ej),(-self.a+self.fj),(-self.b+self.fj),(-self.c+self.fj),(-self.d+self.fj),(-self.e+self.fj),(-self.f+self.fj),(-self.g+self.fj),(-self.h+self.fj),(+self.a+self.fj),(+self.b+self.fj),(+self.c+self.fj),(+self.d+self.fj),(+self.e+self.fj),(+self.f+self.fj),(+self.g+self.fj),(+self.h+self.fj),(-self.a+self.gj),(-self.b+self.gj),(-self.c+self.gj),(-self.d+self.gj),(-self.e+self.gj),(-self.f+self.gj),(-self.g+self.gj),(-self.h+self.gj),(+self.a+self.gj),(+self.b+self.gj),(+self.c+self.gj),(+self.d+self.gj),(+self.e+self.gj),(+self.f+self.gj),(+self.g+self.gj),(+self.h+self.gj),(-self.a+self.hj),(-self.b+self.hj),(-self.c+self.hj),(-self.d+self.hj),(-self.e+self.hj),(-self.f+self.hj),(-self.g+self.hj),(-self.h+self.hj),(+self.a+self.hj),(+self.b+self.hj),(+self.c+self.hj),(+self.d+self.hj),(+self.e+self.hj),(+self.f+self.hj),(+self.g+self.hj),(+self.h+self.hj))

    def get_cj(self):
        return self.cj

    def set_cj(self, cj):
        self.cj = cj
        self.set_sym0((-self.a-self.aj),(-self.b-self.aj),(-self.c-self.aj),(-self.d-self.aj),(-self.e-self.aj),(-self.f-self.aj),(-self.g-self.aj),(-self.h-self.aj),(+self.a-self.aj),(+self.b-self.aj),(+self.c-self.aj),(+self.d-self.aj),(+self.e-self.aj),(+self.f-self.aj),(+self.g-self.aj),(+self.h-self.aj),(-self.a-self.bj),(-self.b-self.bj),(-self.c-self.bj),(-self.d-self.bj),(-self.e-self.bj),(-self.f-self.bj),(-self.g-self.bj),(-self.h-self.bj),(+self.a-self.bj),(+self.b-self.bj),(+self.c-self.bj),(+self.d-self.bj),(+self.e-self.bj),(+self.f-self.bj),(+self.g-self.bj),(+self.h-self.bj),(-self.a-self.cj),(-self.b-self.cj),(-self.c-self.cj),(-self.d-self.cj),(-self.e-self.cj),(-self.f-self.cj),(-self.g-self.cj),(-self.h-self.cj),(+self.a-self.cj),(+self.b-self.cj),(+self.c-self.cj),(+self.d-self.cj),(+self.e-self.cj),(+self.f-self.cj),(+self.g-self.cj),(+self.h-self.cj),(-self.a-self.dj),(-self.b-self.dj),(-self.c-self.dj),(-self.d-self.dj),(-self.e-self.dj),(-self.f-self.dj),(-self.g-self.dj),(-self.h-self.dj),(+self.a-self.dj),(+self.b-self.dj),(+self.c-self.dj),(+self.d-self.dj),(+self.e-self.dj),(+self.f-self.dj),(+self.g-self.dj),(+self.h-self.dj))
        self.set_sym2((-self.a+self.aj),(-self.b+self.aj),(-self.c+self.aj),(-self.d+self.aj),(-self.e+self.aj),(-self.f+self.aj),(-self.g+self.aj),(-self.h+self.aj),(+self.a+self.aj),(+self.b+self.aj),(+self.c+self.aj),(+self.d+self.aj),(+self.e+self.aj),(+self.f+self.aj),(+self.g+self.aj),(+self.h+self.aj),(-self.a+self.bj),(-self.b+self.bj),(-self.c+self.bj),(-self.d+self.bj),(-self.e+self.bj),(-self.f+self.bj),(-self.g+self.bj),(-self.h+self.bj),(+self.a+self.bj),(+self.b+self.bj),(+self.c+self.bj),(+self.d+self.bj),(+self.e+self.bj),(+self.f+self.bj),(+self.g+self.bj),(+self.h+self.bj),(-self.a+self.cj),(-self.b+self.cj),(-self.c+self.cj),(-self.d+self.cj),(-self.e+self.cj),(-self.f+self.cj),(-self.g+self.cj),(-self.h+self.cj),(+self.a+self.cj),(+self.b+self.cj),(+self.c+self.cj),(+self.d+self.cj),(+self.e+self.cj),(+self.f+self.cj),(+self.g+self.cj),(+self.h+self.cj),(-self.a+self.dj),(-self.b+self.dj),(-self.c+self.dj),(-self.d+self.dj),(-self.e+self.dj),(-self.f+self.dj),(-self.g+self.dj),(-self.h+self.dj),(+self.a+self.dj),(+self.b+self.dj),(+self.c+self.dj),(+self.d+self.dj),(+self.e+self.dj),(+self.f+self.dj),(+self.g+self.dj),(+self.h+self.dj))

    def get_c(self):
        return self.c

    def set_c(self, c):
        self.c = c
        self.set_sym0((-self.a-self.aj),(-self.b-self.aj),(-self.c-self.aj),(-self.d-self.aj),(-self.e-self.aj),(-self.f-self.aj),(-self.g-self.aj),(-self.h-self.aj),(+self.a-self.aj),(+self.b-self.aj),(+self.c-self.aj),(+self.d-self.aj),(+self.e-self.aj),(+self.f-self.aj),(+self.g-self.aj),(+self.h-self.aj),(-self.a-self.bj),(-self.b-self.bj),(-self.c-self.bj),(-self.d-self.bj),(-self.e-self.bj),(-self.f-self.bj),(-self.g-self.bj),(-self.h-self.bj),(+self.a-self.bj),(+self.b-self.bj),(+self.c-self.bj),(+self.d-self.bj),(+self.e-self.bj),(+self.f-self.bj),(+self.g-self.bj),(+self.h-self.bj),(-self.a-self.cj),(-self.b-self.cj),(-self.c-self.cj),(-self.d-self.cj),(-self.e-self.cj),(-self.f-self.cj),(-self.g-self.cj),(-self.h-self.cj),(+self.a-self.cj),(+self.b-self.cj),(+self.c-self.cj),(+self.d-self.cj),(+self.e-self.cj),(+self.f-self.cj),(+self.g-self.cj),(+self.h-self.cj),(-self.a-self.dj),(-self.b-self.dj),(-self.c-self.dj),(-self.d-self.dj),(-self.e-self.dj),(-self.f-self.dj),(-self.g-self.dj),(-self.h-self.dj),(+self.a-self.dj),(+self.b-self.dj),(+self.c-self.dj),(+self.d-self.dj),(+self.e-self.dj),(+self.f-self.dj),(+self.g-self.dj),(+self.h-self.dj))
        self.set_sym1((-self.a-self.ej),(-self.b-self.ej),(-self.c-self.ej),(-self.d-self.ej),(-self.e-self.ej),(-self.f-self.ej),(-self.g-self.ej),(-self.h-self.ej),(+self.a-self.ej),(+self.b-self.ej),(+self.c-self.ej),(+self.d-self.ej),(+self.e-self.ej),(+self.f-self.ej),(+self.g-self.ej),(+self.h-self.ej),(-self.a-self.fj),(-self.b-self.fj),(-self.c-self.fj),(-self.d-self.fj),(-self.e-self.fj),(-self.f-self.fj),(-self.g-self.fj),(-self.h-self.fj),(+self.a-self.fj),(+self.b-self.fj),(+self.c-self.fj),(+self.d-self.fj),(+self.e-self.fj),(+self.f-self.fj),(+self.g-self.fj),(+self.h-self.fj),(-self.a-self.gj),(-self.b-self.gj),(-self.c-self.gj),(-self.d-self.gj),(-self.e-self.gj),(-self.f-self.gj),(-self.g-self.gj),(-self.h-self.gj),(+self.a-self.gj),(+self.b-self.gj),(+self.c-self.gj),(+self.d-self.gj),(+self.e-self.gj),(+self.f-self.gj),(+self.g-self.gj),(+self.h-self.gj),(-self.a-self.hj),(-self.b-self.hj),(-self.c-self.hj),(-self.d-self.hj),(-self.e-self.hj),(-self.f-self.hj),(-self.g-self.hj),(-self.h-self.hj),(+self.a-self.hj),(+self.b-self.hj),(+self.c-self.hj),(+self.d-self.hj),(+self.e-self.hj),(+self.f-self.hj),(+self.g-self.hj),(+self.h-self.hj))
        self.set_sym2((-self.a+self.aj),(-self.b+self.aj),(-self.c+self.aj),(-self.d+self.aj),(-self.e+self.aj),(-self.f+self.aj),(-self.g+self.aj),(-self.h+self.aj),(+self.a+self.aj),(+self.b+self.aj),(+self.c+self.aj),(+self.d+self.aj),(+self.e+self.aj),(+self.f+self.aj),(+self.g+self.aj),(+self.h+self.aj),(-self.a+self.bj),(-self.b+self.bj),(-self.c+self.bj),(-self.d+self.bj),(-self.e+self.bj),(-self.f+self.bj),(-self.g+self.bj),(-self.h+self.bj),(+self.a+self.bj),(+self.b+self.bj),(+self.c+self.bj),(+self.d+self.bj),(+self.e+self.bj),(+self.f+self.bj),(+self.g+self.bj),(+self.h+self.bj),(-self.a+self.cj),(-self.b+self.cj),(-self.c+self.cj),(-self.d+self.cj),(-self.e+self.cj),(-self.f+self.cj),(-self.g+self.cj),(-self.h+self.cj),(+self.a+self.cj),(+self.b+self.cj),(+self.c+self.cj),(+self.d+self.cj),(+self.e+self.cj),(+self.f+self.cj),(+self.g+self.cj),(+self.h+self.cj),(-self.a+self.dj),(-self.b+self.dj),(-self.c+self.dj),(-self.d+self.dj),(-self.e+self.dj),(-self.f+self.dj),(-self.g+self.dj),(-self.h+self.dj),(+self.a+self.dj),(+self.b+self.dj),(+self.c+self.dj),(+self.d+self.dj),(+self.e+self.dj),(+self.f+self.dj),(+self.g+self.dj),(+self.h+self.dj))
        self.set_sym3((-self.a+self.ej),(-self.b+self.ej),(-self.c+self.ej),(-self.d+self.ej),(-self.e+self.ej),(-self.f+self.ej),(-self.g+self.ej),(-self.h+self.ej),(+self.a+self.ej),(+self.b+self.ej),(+self.c+self.ej),(+self.d+self.ej),(+self.e+self.ej),(+self.f+self.ej),(+self.g+self.ej),(+self.h+self.ej),(-self.a+self.fj),(-self.b+self.fj),(-self.c+self.fj),(-self.d+self.fj),(-self.e+self.fj),(-self.f+self.fj),(-self.g+self.fj),(-self.h+self.fj),(+self.a+self.fj),(+self.b+self.fj),(+self.c+self.fj),(+self.d+self.fj),(+self.e+self.fj),(+self.f+self.fj),(+self.g+self.fj),(+self.h+self.fj),(-self.a+self.gj),(-self.b+self.gj),(-self.c+self.gj),(-self.d+self.gj),(-self.e+self.gj),(-self.f+self.gj),(-self.g+self.gj),(-self.h+self.gj),(+self.a+self.gj),(+self.b+self.gj),(+self.c+self.gj),(+self.d+self.gj),(+self.e+self.gj),(+self.f+self.gj),(+self.g+self.gj),(+self.h+self.gj),(-self.a+self.hj),(-self.b+self.hj),(-self.c+self.hj),(-self.d+self.hj),(-self.e+self.hj),(-self.f+self.hj),(-self.g+self.hj),(-self.h+self.hj),(+self.a+self.hj),(+self.b+self.hj),(+self.c+self.hj),(+self.d+self.hj),(+self.e+self.hj),(+self.f+self.hj),(+self.g+self.hj),(+self.h+self.hj))

    def get_bj(self):
        return self.bj

    def set_bj(self, bj):
        self.bj = bj
        self.set_sym0((-self.a-self.aj),(-self.b-self.aj),(-self.c-self.aj),(-self.d-self.aj),(-self.e-self.aj),(-self.f-self.aj),(-self.g-self.aj),(-self.h-self.aj),(+self.a-self.aj),(+self.b-self.aj),(+self.c-self.aj),(+self.d-self.aj),(+self.e-self.aj),(+self.f-self.aj),(+self.g-self.aj),(+self.h-self.aj),(-self.a-self.bj),(-self.b-self.bj),(-self.c-self.bj),(-self.d-self.bj),(-self.e-self.bj),(-self.f-self.bj),(-self.g-self.bj),(-self.h-self.bj),(+self.a-self.bj),(+self.b-self.bj),(+self.c-self.bj),(+self.d-self.bj),(+self.e-self.bj),(+self.f-self.bj),(+self.g-self.bj),(+self.h-self.bj),(-self.a-self.cj),(-self.b-self.cj),(-self.c-self.cj),(-self.d-self.cj),(-self.e-self.cj),(-self.f-self.cj),(-self.g-self.cj),(-self.h-self.cj),(+self.a-self.cj),(+self.b-self.cj),(+self.c-self.cj),(+self.d-self.cj),(+self.e-self.cj),(+self.f-self.cj),(+self.g-self.cj),(+self.h-self.cj),(-self.a-self.dj),(-self.b-self.dj),(-self.c-self.dj),(-self.d-self.dj),(-self.e-self.dj),(-self.f-self.dj),(-self.g-self.dj),(-self.h-self.dj),(+self.a-self.dj),(+self.b-self.dj),(+self.c-self.dj),(+self.d-self.dj),(+self.e-self.dj),(+self.f-self.dj),(+self.g-self.dj),(+self.h-self.dj))
        self.set_sym2((-self.a+self.aj),(-self.b+self.aj),(-self.c+self.aj),(-self.d+self.aj),(-self.e+self.aj),(-self.f+self.aj),(-self.g+self.aj),(-self.h+self.aj),(+self.a+self.aj),(+self.b+self.aj),(+self.c+self.aj),(+self.d+self.aj),(+self.e+self.aj),(+self.f+self.aj),(+self.g+self.aj),(+self.h+self.aj),(-self.a+self.bj),(-self.b+self.bj),(-self.c+self.bj),(-self.d+self.bj),(-self.e+self.bj),(-self.f+self.bj),(-self.g+self.bj),(-self.h+self.bj),(+self.a+self.bj),(+self.b+self.bj),(+self.c+self.bj),(+self.d+self.bj),(+self.e+self.bj),(+self.f+self.bj),(+self.g+self.bj),(+self.h+self.bj),(-self.a+self.cj),(-self.b+self.cj),(-self.c+self.cj),(-self.d+self.cj),(-self.e+self.cj),(-self.f+self.cj),(-self.g+self.cj),(-self.h+self.cj),(+self.a+self.cj),(+self.b+self.cj),(+self.c+self.cj),(+self.d+self.cj),(+self.e+self.cj),(+self.f+self.cj),(+self.g+self.cj),(+self.h+self.cj),(-self.a+self.dj),(-self.b+self.dj),(-self.c+self.dj),(-self.d+self.dj),(-self.e+self.dj),(-self.f+self.dj),(-self.g+self.dj),(-self.h+self.dj),(+self.a+self.dj),(+self.b+self.dj),(+self.c+self.dj),(+self.d+self.dj),(+self.e+self.dj),(+self.f+self.dj),(+self.g+self.dj),(+self.h+self.dj))

    def get_b(self):
        return self.b

    def set_b(self, b):
        self.b = b
        self.set_sym0((-self.a-self.aj),(-self.b-self.aj),(-self.c-self.aj),(-self.d-self.aj),(-self.e-self.aj),(-self.f-self.aj),(-self.g-self.aj),(-self.h-self.aj),(+self.a-self.aj),(+self.b-self.aj),(+self.c-self.aj),(+self.d-self.aj),(+self.e-self.aj),(+self.f-self.aj),(+self.g-self.aj),(+self.h-self.aj),(-self.a-self.bj),(-self.b-self.bj),(-self.c-self.bj),(-self.d-self.bj),(-self.e-self.bj),(-self.f-self.bj),(-self.g-self.bj),(-self.h-self.bj),(+self.a-self.bj),(+self.b-self.bj),(+self.c-self.bj),(+self.d-self.bj),(+self.e-self.bj),(+self.f-self.bj),(+self.g-self.bj),(+self.h-self.bj),(-self.a-self.cj),(-self.b-self.cj),(-self.c-self.cj),(-self.d-self.cj),(-self.e-self.cj),(-self.f-self.cj),(-self.g-self.cj),(-self.h-self.cj),(+self.a-self.cj),(+self.b-self.cj),(+self.c-self.cj),(+self.d-self.cj),(+self.e-self.cj),(+self.f-self.cj),(+self.g-self.cj),(+self.h-self.cj),(-self.a-self.dj),(-self.b-self.dj),(-self.c-self.dj),(-self.d-self.dj),(-self.e-self.dj),(-self.f-self.dj),(-self.g-self.dj),(-self.h-self.dj),(+self.a-self.dj),(+self.b-self.dj),(+self.c-self.dj),(+self.d-self.dj),(+self.e-self.dj),(+self.f-self.dj),(+self.g-self.dj),(+self.h-self.dj))
        self.set_sym1((-self.a-self.ej),(-self.b-self.ej),(-self.c-self.ej),(-self.d-self.ej),(-self.e-self.ej),(-self.f-self.ej),(-self.g-self.ej),(-self.h-self.ej),(+self.a-self.ej),(+self.b-self.ej),(+self.c-self.ej),(+self.d-self.ej),(+self.e-self.ej),(+self.f-self.ej),(+self.g-self.ej),(+self.h-self.ej),(-self.a-self.fj),(-self.b-self.fj),(-self.c-self.fj),(-self.d-self.fj),(-self.e-self.fj),(-self.f-self.fj),(-self.g-self.fj),(-self.h-self.fj),(+self.a-self.fj),(+self.b-self.fj),(+self.c-self.fj),(+self.d-self.fj),(+self.e-self.fj),(+self.f-self.fj),(+self.g-self.fj),(+self.h-self.fj),(-self.a-self.gj),(-self.b-self.gj),(-self.c-self.gj),(-self.d-self.gj),(-self.e-self.gj),(-self.f-self.gj),(-self.g-self.gj),(-self.h-self.gj),(+self.a-self.gj),(+self.b-self.gj),(+self.c-self.gj),(+self.d-self.gj),(+self.e-self.gj),(+self.f-self.gj),(+self.g-self.gj),(+self.h-self.gj),(-self.a-self.hj),(-self.b-self.hj),(-self.c-self.hj),(-self.d-self.hj),(-self.e-self.hj),(-self.f-self.hj),(-self.g-self.hj),(-self.h-self.hj),(+self.a-self.hj),(+self.b-self.hj),(+self.c-self.hj),(+self.d-self.hj),(+self.e-self.hj),(+self.f-self.hj),(+self.g-self.hj),(+self.h-self.hj))
        self.set_sym2((-self.a+self.aj),(-self.b+self.aj),(-self.c+self.aj),(-self.d+self.aj),(-self.e+self.aj),(-self.f+self.aj),(-self.g+self.aj),(-self.h+self.aj),(+self.a+self.aj),(+self.b+self.aj),(+self.c+self.aj),(+self.d+self.aj),(+self.e+self.aj),(+self.f+self.aj),(+self.g+self.aj),(+self.h+self.aj),(-self.a+self.bj),(-self.b+self.bj),(-self.c+self.bj),(-self.d+self.bj),(-self.e+self.bj),(-self.f+self.bj),(-self.g+self.bj),(-self.h+self.bj),(+self.a+self.bj),(+self.b+self.bj),(+self.c+self.bj),(+self.d+self.bj),(+self.e+self.bj),(+self.f+self.bj),(+self.g+self.bj),(+self.h+self.bj),(-self.a+self.cj),(-self.b+self.cj),(-self.c+self.cj),(-self.d+self.cj),(-self.e+self.cj),(-self.f+self.cj),(-self.g+self.cj),(-self.h+self.cj),(+self.a+self.cj),(+self.b+self.cj),(+self.c+self.cj),(+self.d+self.cj),(+self.e+self.cj),(+self.f+self.cj),(+self.g+self.cj),(+self.h+self.cj),(-self.a+self.dj),(-self.b+self.dj),(-self.c+self.dj),(-self.d+self.dj),(-self.e+self.dj),(-self.f+self.dj),(-self.g+self.dj),(-self.h+self.dj),(+self.a+self.dj),(+self.b+self.dj),(+self.c+self.dj),(+self.d+self.dj),(+self.e+self.dj),(+self.f+self.dj),(+self.g+self.dj),(+self.h+self.dj))
        self.set_sym3((-self.a+self.ej),(-self.b+self.ej),(-self.c+self.ej),(-self.d+self.ej),(-self.e+self.ej),(-self.f+self.ej),(-self.g+self.ej),(-self.h+self.ej),(+self.a+self.ej),(+self.b+self.ej),(+self.c+self.ej),(+self.d+self.ej),(+self.e+self.ej),(+self.f+self.ej),(+self.g+self.ej),(+self.h+self.ej),(-self.a+self.fj),(-self.b+self.fj),(-self.c+self.fj),(-self.d+self.fj),(-self.e+self.fj),(-self.f+self.fj),(-self.g+self.fj),(-self.h+self.fj),(+self.a+self.fj),(+self.b+self.fj),(+self.c+self.fj),(+self.d+self.fj),(+self.e+self.fj),(+self.f+self.fj),(+self.g+self.fj),(+self.h+self.fj),(-self.a+self.gj),(-self.b+self.gj),(-self.c+self.gj),(-self.d+self.gj),(-self.e+self.gj),(-self.f+self.gj),(-self.g+self.gj),(-self.h+self.gj),(+self.a+self.gj),(+self.b+self.gj),(+self.c+self.gj),(+self.d+self.gj),(+self.e+self.gj),(+self.f+self.gj),(+self.g+self.gj),(+self.h+self.gj),(-self.a+self.hj),(-self.b+self.hj),(-self.c+self.hj),(-self.d+self.hj),(-self.e+self.hj),(-self.f+self.hj),(-self.g+self.hj),(-self.h+self.hj),(+self.a+self.hj),(+self.b+self.hj),(+self.c+self.hj),(+self.d+self.hj),(+self.e+self.hj),(+self.f+self.hj),(+self.g+self.hj),(+self.h+self.hj))

    def get_aj(self):
        return self.aj

    def set_aj(self, aj):
        self.aj = aj
        self.set_sym0((-self.a-self.aj),(-self.b-self.aj),(-self.c-self.aj),(-self.d-self.aj),(-self.e-self.aj),(-self.f-self.aj),(-self.g-self.aj),(-self.h-self.aj),(+self.a-self.aj),(+self.b-self.aj),(+self.c-self.aj),(+self.d-self.aj),(+self.e-self.aj),(+self.f-self.aj),(+self.g-self.aj),(+self.h-self.aj),(-self.a-self.bj),(-self.b-self.bj),(-self.c-self.bj),(-self.d-self.bj),(-self.e-self.bj),(-self.f-self.bj),(-self.g-self.bj),(-self.h-self.bj),(+self.a-self.bj),(+self.b-self.bj),(+self.c-self.bj),(+self.d-self.bj),(+self.e-self.bj),(+self.f-self.bj),(+self.g-self.bj),(+self.h-self.bj),(-self.a-self.cj),(-self.b-self.cj),(-self.c-self.cj),(-self.d-self.cj),(-self.e-self.cj),(-self.f-self.cj),(-self.g-self.cj),(-self.h-self.cj),(+self.a-self.cj),(+self.b-self.cj),(+self.c-self.cj),(+self.d-self.cj),(+self.e-self.cj),(+self.f-self.cj),(+self.g-self.cj),(+self.h-self.cj),(-self.a-self.dj),(-self.b-self.dj),(-self.c-self.dj),(-self.d-self.dj),(-self.e-self.dj),(-self.f-self.dj),(-self.g-self.dj),(-self.h-self.dj),(+self.a-self.dj),(+self.b-self.dj),(+self.c-self.dj),(+self.d-self.dj),(+self.e-self.dj),(+self.f-self.dj),(+self.g-self.dj),(+self.h-self.dj))
        self.set_sym2((-self.a+self.aj),(-self.b+self.aj),(-self.c+self.aj),(-self.d+self.aj),(-self.e+self.aj),(-self.f+self.aj),(-self.g+self.aj),(-self.h+self.aj),(+self.a+self.aj),(+self.b+self.aj),(+self.c+self.aj),(+self.d+self.aj),(+self.e+self.aj),(+self.f+self.aj),(+self.g+self.aj),(+self.h+self.aj),(-self.a+self.bj),(-self.b+self.bj),(-self.c+self.bj),(-self.d+self.bj),(-self.e+self.bj),(-self.f+self.bj),(-self.g+self.bj),(-self.h+self.bj),(+self.a+self.bj),(+self.b+self.bj),(+self.c+self.bj),(+self.d+self.bj),(+self.e+self.bj),(+self.f+self.bj),(+self.g+self.bj),(+self.h+self.bj),(-self.a+self.cj),(-self.b+self.cj),(-self.c+self.cj),(-self.d+self.cj),(-self.e+self.cj),(-self.f+self.cj),(-self.g+self.cj),(-self.h+self.cj),(+self.a+self.cj),(+self.b+self.cj),(+self.c+self.cj),(+self.d+self.cj),(+self.e+self.cj),(+self.f+self.cj),(+self.g+self.cj),(+self.h+self.cj),(-self.a+self.dj),(-self.b+self.dj),(-self.c+self.dj),(-self.d+self.dj),(-self.e+self.dj),(-self.f+self.dj),(-self.g+self.dj),(-self.h+self.dj),(+self.a+self.dj),(+self.b+self.dj),(+self.c+self.dj),(+self.d+self.dj),(+self.e+self.dj),(+self.f+self.dj),(+self.g+self.dj),(+self.h+self.dj))

    def get_a(self):
        return self.a

    def set_a(self, a):
        self.a = a
        self.set_sym0((-self.a-self.aj),(-self.b-self.aj),(-self.c-self.aj),(-self.d-self.aj),(-self.e-self.aj),(-self.f-self.aj),(-self.g-self.aj),(-self.h-self.aj),(+self.a-self.aj),(+self.b-self.aj),(+self.c-self.aj),(+self.d-self.aj),(+self.e-self.aj),(+self.f-self.aj),(+self.g-self.aj),(+self.h-self.aj),(-self.a-self.bj),(-self.b-self.bj),(-self.c-self.bj),(-self.d-self.bj),(-self.e-self.bj),(-self.f-self.bj),(-self.g-self.bj),(-self.h-self.bj),(+self.a-self.bj),(+self.b-self.bj),(+self.c-self.bj),(+self.d-self.bj),(+self.e-self.bj),(+self.f-self.bj),(+self.g-self.bj),(+self.h-self.bj),(-self.a-self.cj),(-self.b-self.cj),(-self.c-self.cj),(-self.d-self.cj),(-self.e-self.cj),(-self.f-self.cj),(-self.g-self.cj),(-self.h-self.cj),(+self.a-self.cj),(+self.b-self.cj),(+self.c-self.cj),(+self.d-self.cj),(+self.e-self.cj),(+self.f-self.cj),(+self.g-self.cj),(+self.h-self.cj),(-self.a-self.dj),(-self.b-self.dj),(-self.c-self.dj),(-self.d-self.dj),(-self.e-self.dj),(-self.f-self.dj),(-self.g-self.dj),(-self.h-self.dj),(+self.a-self.dj),(+self.b-self.dj),(+self.c-self.dj),(+self.d-self.dj),(+self.e-self.dj),(+self.f-self.dj),(+self.g-self.dj),(+self.h-self.dj))
        self.set_sym1((-self.a-self.ej),(-self.b-self.ej),(-self.c-self.ej),(-self.d-self.ej),(-self.e-self.ej),(-self.f-self.ej),(-self.g-self.ej),(-self.h-self.ej),(+self.a-self.ej),(+self.b-self.ej),(+self.c-self.ej),(+self.d-self.ej),(+self.e-self.ej),(+self.f-self.ej),(+self.g-self.ej),(+self.h-self.ej),(-self.a-self.fj),(-self.b-self.fj),(-self.c-self.fj),(-self.d-self.fj),(-self.e-self.fj),(-self.f-self.fj),(-self.g-self.fj),(-self.h-self.fj),(+self.a-self.fj),(+self.b-self.fj),(+self.c-self.fj),(+self.d-self.fj),(+self.e-self.fj),(+self.f-self.fj),(+self.g-self.fj),(+self.h-self.fj),(-self.a-self.gj),(-self.b-self.gj),(-self.c-self.gj),(-self.d-self.gj),(-self.e-self.gj),(-self.f-self.gj),(-self.g-self.gj),(-self.h-self.gj),(+self.a-self.gj),(+self.b-self.gj),(+self.c-self.gj),(+self.d-self.gj),(+self.e-self.gj),(+self.f-self.gj),(+self.g-self.gj),(+self.h-self.gj),(-self.a-self.hj),(-self.b-self.hj),(-self.c-self.hj),(-self.d-self.hj),(-self.e-self.hj),(-self.f-self.hj),(-self.g-self.hj),(-self.h-self.hj),(+self.a-self.hj),(+self.b-self.hj),(+self.c-self.hj),(+self.d-self.hj),(+self.e-self.hj),(+self.f-self.hj),(+self.g-self.hj),(+self.h-self.hj))
        self.set_sym2((-self.a+self.aj),(-self.b+self.aj),(-self.c+self.aj),(-self.d+self.aj),(-self.e+self.aj),(-self.f+self.aj),(-self.g+self.aj),(-self.h+self.aj),(+self.a+self.aj),(+self.b+self.aj),(+self.c+self.aj),(+self.d+self.aj),(+self.e+self.aj),(+self.f+self.aj),(+self.g+self.aj),(+self.h+self.aj),(-self.a+self.bj),(-self.b+self.bj),(-self.c+self.bj),(-self.d+self.bj),(-self.e+self.bj),(-self.f+self.bj),(-self.g+self.bj),(-self.h+self.bj),(+self.a+self.bj),(+self.b+self.bj),(+self.c+self.bj),(+self.d+self.bj),(+self.e+self.bj),(+self.f+self.bj),(+self.g+self.bj),(+self.h+self.bj),(-self.a+self.cj),(-self.b+self.cj),(-self.c+self.cj),(-self.d+self.cj),(-self.e+self.cj),(-self.f+self.cj),(-self.g+self.cj),(-self.h+self.cj),(+self.a+self.cj),(+self.b+self.cj),(+self.c+self.cj),(+self.d+self.cj),(+self.e+self.cj),(+self.f+self.cj),(+self.g+self.cj),(+self.h+self.cj),(-self.a+self.dj),(-self.b+self.dj),(-self.c+self.dj),(-self.d+self.dj),(-self.e+self.dj),(-self.f+self.dj),(-self.g+self.dj),(-self.h+self.dj),(+self.a+self.dj),(+self.b+self.dj),(+self.c+self.dj),(+self.d+self.dj),(+self.e+self.dj),(+self.f+self.dj),(+self.g+self.dj),(+self.h+self.dj))
        self.set_sym3((-self.a+self.ej),(-self.b+self.ej),(-self.c+self.ej),(-self.d+self.ej),(-self.e+self.ej),(-self.f+self.ej),(-self.g+self.ej),(-self.h+self.ej),(+self.a+self.ej),(+self.b+self.ej),(+self.c+self.ej),(+self.d+self.ej),(+self.e+self.ej),(+self.f+self.ej),(+self.g+self.ej),(+self.h+self.ej),(-self.a+self.fj),(-self.b+self.fj),(-self.c+self.fj),(-self.d+self.fj),(-self.e+self.fj),(-self.f+self.fj),(-self.g+self.fj),(-self.h+self.fj),(+self.a+self.fj),(+self.b+self.fj),(+self.c+self.fj),(+self.d+self.fj),(+self.e+self.fj),(+self.f+self.fj),(+self.g+self.fj),(+self.h+self.fj),(-self.a+self.gj),(-self.b+self.gj),(-self.c+self.gj),(-self.d+self.gj),(-self.e+self.gj),(-self.f+self.gj),(-self.g+self.gj),(-self.h+self.gj),(+self.a+self.gj),(+self.b+self.gj),(+self.c+self.gj),(+self.d+self.gj),(+self.e+self.gj),(+self.f+self.gj),(+self.g+self.gj),(+self.h+self.gj),(-self.a+self.hj),(-self.b+self.hj),(-self.c+self.hj),(-self.d+self.hj),(-self.e+self.hj),(-self.f+self.hj),(-self.g+self.hj),(-self.h+self.hj),(+self.a+self.hj),(+self.b+self.hj),(+self.c+self.hj),(+self.d+self.hj),(+self.e+self.hj),(+self.f+self.hj),(+self.g+self.hj),(+self.h+self.hj))

    def get_sym3(self):
        return self.sym3

    def set_sym3(self, sym3):
        self.sym3 = sym3
        self.set_symbol1(numpy.concatenate((self.sym2,self.sym3),0))

    def get_sym2(self):
        return self.sym2

    def set_sym2(self, sym2):
        self.sym2 = sym2
        self.set_symbol1(numpy.concatenate((self.sym2,self.sym3),0))

    def get_sym1(self):
        return self.sym1

    def set_sym1(self, sym1):
        self.sym1 = sym1
        self.set_symbol0(numpy.concatenate((self.sym0,self.sym1),0))

    def get_sym0(self):
        return self.sym0

    def set_sym0(self, sym0):
        self.sym0 = sym0
        self.set_symbol0(numpy.concatenate((self.sym0,self.sym1),0))

    def get_symbol1(self):
        return self.symbol1

    def set_symbol1(self, symbol1):
        self.symbol1 = symbol1
        self.set_symbol(numpy.concatenate((self.symbol0,self.symbol1),0))

    def get_symbol0(self):
        return self.symbol0

    def set_symbol0(self, symbol0):
        self.symbol0 = symbol0
        self.set_symbol(numpy.concatenate((self.symbol0,self.symbol1),0))

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

	

    def EbN0_to_noise_voltage(self, EbN0,bitspersymbol):
        """ Converts Eb/N0 to a complex noise voltage (assuming unit symbol power) """
        return 1.0 / math.sqrt(float(bitspersymbol)*10**(float(EbN0)/10))


class myThread (threading.Thread):
    def __init__(self, EbN0,semente):
        threading.Thread.__init__(self)
        self.EbN0 = EbN0
        self.semente = semente
        self.tb = qam256(self.EbN0,self.semente)
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
    EbN0_max = 25
    EbN0_range = range(EbN0_min, EbN0_max+1)
    wb = xlwt.Workbook()
    ws = wb.add_sheet('qam256') 
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

    for x in range(0,3):
        
	print "Eb/N0 = %d dB" % x
	ber_theory[x] = berawgn(x,4)
        ber_theory1[x] = berawgn(x,6)
        ber_theory2[x] = berawgn(x,8)
	

	for v in range(19,25):
		gc.enable()
		ber_simu[x]   = simulate_ber(x,v)
		print "seed",v,"\tqam 256", ber_simu[x]
		ws.write(v+1,x+1, ber_simu[x])
		wb.save('qam256.xls')
		gc.collect()

        print "\nqam 256 teorico", ber_theory2[x]     


    wb.save('qam256.xls')



    f = pylab.figure()
    s = f.add_subplot(1,1,1)
    #s.semilogy(EbN0_range, ber_theory, 'k-.', label="Theoretical qam16")
    #s.semilogy(EbN0_range, ber_theory1, 'b-.', label="Theoretical qam64")
    s.semilogy(EbN0_range, ber_theory2, 'g-.', label="Theoretical qam256")
    s.semilogy(EbN0_range, ber_simu, 'b-o', label="qam256")
    s.set_title('BER Simulation')
    s.set_xlabel('Eb/N0 (dB)')
    s.set_ylabel('BER')
    s.legend()
    s.grid()
    pylab.show()


