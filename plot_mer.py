#!/usr/bin/env python
import matplotlib
matplotlib.rcParams['font.family'] = 'sans-serif'
matplotlib.rcParams['font.sans-serif'] = 'Arial'
matplotlib.rcParams['font.size'] = 9
matplotlib.rcParams['axes.linewidth'] = 0.5
matplotlib.rcParams['axes.titlesize'] = 13
matplotlib.rcParams['axes.labelsize'] = 11
matplotlib.rcParams['xtick.direction'] = 'out'
matplotlib.rcParams['ytick.direction'] = 'out'
matplotlib.rcParams['xtick.top'] = True
matplotlib.rcParams['ytick.right'] = True
matplotlib.rcParams['xtick.labelsize'] = 9
matplotlib.rcParams['ytick.labelsize'] = 9
matplotlib.rcParams['xtick.major.size'] = 5
matplotlib.rcParams['xtick.minor.size'] = 2
matplotlib.rcParams['ytick.major.size'] = 5
matplotlib.rcParams['ytick.minor.size'] = 2
matplotlib.rcParams['mathtext.fontset']='custom'
matplotlib.rcParams['mathtext.rm']='Arial'
matplotlib.rcParams['mathtext.it']='Arial:italic'
matplotlib.rcParams['mathtext.bf']='Arial:bold'
matplotlib.rcParams['hatch.linewidth'] = 0.1
matplotlib.use('Agg')
from matplotlib.dates import date2num, num2date
import matplotlib.gridspec as gridspec
from matplotlib.ticker import NullFormatter, LogLocator
import numpy as np
import matplotlib.pyplot as plt

###
## equation (4) in Barth et al., 2019
###
a = np.array([1.,2.5,5.,10.,15.])
Q = 10 ** np.arange(1,9,0.02)
rho = 2500.0
c = 1500.0
dP = [None,None,None,None,None,None,None,None,None,None]
eta = 1000.0
for i in range(len(a)):
	ai = a[i]
	ui = Q / (np.pi * ai ** 2.) / rho
	#M = ui**2./c**.0
	M = 0.01
	Re = 2 * ui * rho * ai / eta
	#f = 16 / Re + 0.01
	f = 0.0
	#dP[i] = - ui * (rho*9.8+rho*ui**2.*f/ai)
	dP[i] = - ui / (1-M**2.) * (rho*9.8+rho*ui**2.*f/ai)
	

fig = plt.figure(figsize=(8,6))
axgrid = gridspec.GridSpec(1,1,bottom=0.1,left=0.1,right=0.92,top=0.95,hspace=0.8,wspace=0.3) 
ax = plt.subplot(axgrid[0,0])
for i in range(len(a)):
	flag = dP[i] < 0 
	ax.plot(-dP[i][flag]/1E6, Q[flag], '-', color='0.5', linewidth=0.5)
	iarg = np.argmin(np.abs(dP[i]/1E6+10))
	ax.text(13,Q[iarg]/1.25,'%g m' % (a[i])) 
	
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel('Decompression rate [MPa/s]')
ax.set_ylabel('Mass flow rate (mass discharge rate) [kg/s]')
ax.set_xlim([1E-5,1E1])
ax.set_ylim([1E2,1E9])
ax.xaxis.set_minor_locator(LogLocator(base=10.0,subs=(0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9),numticks=40))
ax.xaxis.set_minor_formatter(NullFormatter())
ax.tick_params(which='both',axis='both',left=True,right=True,top=True,bottom=True)

plt.savefig('mer_all.pdf')
plt.close()

