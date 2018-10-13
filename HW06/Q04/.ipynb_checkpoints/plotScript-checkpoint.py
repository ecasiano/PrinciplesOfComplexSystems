#Plot

import numpy as np
import matplotlib.pyplot as plt

#Import data
data1 = np.loadtxt("forestDistributionsL32N3000000p0.30.dat")
data2 = np.loadtxt("forestDistributionsL32N3000000p0.60.dat")
data3 = np.loadtxt("forestDistributionsL32N3000000p0.80.dat")
data4 = np.loadtxt("forestDistributionsL32N3000000p0.90.dat")

#Forest sizes for each run
l1 = data1[:,0]
l2 = data2[:,0]
l3 = data3[:,0]
l4 = data3[:,0]

#Groups of l-sized forests for each run
Nl1 = data1[:,1]
Nl2 = data2[:,1]
Nl3 = data3[:,1]
Nl4 = data3[:,1]

fig, ax1 = plt.subplots()
ax1.plot(l1,Nl1,'o')
ax1.set_xlabel(r"$\ell$")
ax1.set_ylabel(r"$N_{\ell}$")
ax1.text(0.50,0.7,r"p: %.2f"%(0.3),transform=ax1.transAxes)
ax1.loglog()
#ax1.text(0.50,0.8,"%.d X %.d lattice"%(L,L),transform=ax1.transAxes)
#ax1.text(0.50,0.9,r"MC Time Steps per point: %d"%mcSteps,transform=ax1.transAxes)
#ax1.axvline(x=0.6,color='#888888',linestyle='--',zorder=0)
#plt.legend(loc="best")
plt.savefig("forests1_zipf.jpg")

fig, ax2 = plt.subplots()
ax2.plot(l2,Nl2,'o')
ax2.set_xlabel(r"$\ell$")
ax2.set_ylabel(r"$N_{\ell}$")
ax2.text(0.50,0.7,r"p: %.2f"%(0.6),transform=ax2.transAxes)
ax2.loglog()
#ax1.text(0.50,0.8,"%.d X %.d lattice"%(L,L),transform=ax1.transAxes)
#ax1.text(0.50,0.9,r"MC Time Steps per point: %d"%mcSteps,transform=ax1.transAxes)
#ax1.axvline(x=0.6,color='#888888',linestyle='--',zorder=0)
#plt.legend(loc="best")
plt.savefig("forests2_zipf.jpg")

fig, ax3 = plt.subplots()
ax3.plot(l3,Nl3,'o')
ax3.set_xlabel(r"$\ell$")
ax3.set_ylabel(r"$N_{\ell}$")
ax3.text(0.50,0.7,r"p: %.2f"%(0.8),transform=ax3.transAxes)
ax3.loglog()
#ax1.text(0.50,0.8,"%.d X %.d lattice"%(L,L),transform=ax1.transAxes)
#ax1.text(0.50,0.9,r"MC Time Steps per point: %d"%mcSteps,transform=ax1.transAxes)
#ax1.axvline(x=0.6,color='#888888',linestyle='--',zorder=0)
#plt.legend(loc="best")
plt.savefig("forests3_zipf.jpg")

fig, ax4 = plt.subplots()
ax4.plot(l3,Nl3,'o')
ax4.set_xlabel(r"$\ell$")
ax4.set_ylabel(r"$N_{\ell}$")
ax4.text(0.50,0.7,r"p: %.2f"%(0.9),transform=ax4.transAxes)
ax4.loglog()
#ax1.text(0.50,0.8,"%.d X %.d lattice"%(L,L),transform=ax1.transAxes)
#ax1.text(0.50,0.9,r"MC Time Steps per point: %d"%mcSteps,transform=ax1.transAxes)
#ax1.axvline(x=0.6,color='#888888',linestyle='--',zorder=0)
#plt.legend(loc="best")
plt.savefig("forests4_zipf.jpg")



