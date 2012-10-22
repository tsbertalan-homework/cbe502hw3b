def dxdt((x,y,z)):
    return -1*(y+z)
    
def dydt((x,y,z)):
    a=.2
    return x + a*y

def dzdt((x,y,z)):
    b=.2
    c=5.7
    return b+z*(x-c)
    
if __name__=='__main__':
    import matplotlib.pyplot as plt
    import numpy as np
    dt=.01
    state0 = [0,0,0]
    state = list(state0)
    stateb0 = [0.01,0.01,0.01]
    stateb = list(stateb0)
    xs = []
    ys = []
    zs = []
    xsb = []
    ysb = []
    zsb = []
    tmax=256
    ts = np.arange(0,tmax,dt)
    for t in ts:
        xs.append(state[0])
        ys.append(state[1])
        zs.append(state[2])
        state[0] += dxdt(state)*dt
        state[1] += dydt(state)*dt
        state[2] += dzdt(state)*dt
        
        xsb.append(stateb[0])
        ysb.append(stateb[1])
        zsb.append(stateb[2])
        stateb[0] += dxdt(stateb)*dt
        stateb[1] += dydt(stateb)*dt
        stateb[2] += dzdt(stateb)*dt
    fig = plt.figure(figsize=(24,12))
        #figsize=(12,6), dpi=120
    ax1 = fig.add_subplot(3,1,1)
    ax1.set_xlim([0,tmax])
    ax1.plot(ts,xs)
    ax1.plot(ts,xsb, linestyle='dotted')
    ax1.set_xlabel('time')
    ax1.set_ylabel('x')
    state_format = '(%.2f, %.2f, %.2f)'
    initial_state_a = state_format % tuple(state0)
    initial_state_b = state_format % tuple(stateb0)
    ax1.legend(['from initial state'+initial_state_a, 'from initial state'+initial_state_b])
    ax1.set_title(r'Chaotic for parameters $a=b=0.2$ and $c=5.7$ $-$ Small changes in initial conditions lead to completely different eventual behavior.')
    
    #axb = fig.add_subplot(3,1,2)
    #axb.plot(ts,xsb)
    
    ax2 = fig.add_subplot(2,2,3)
    ax2.plot(xs,ys)
    #ax2.plot(xsb,ysb)
    ax2.set_xlabel('x')
    ax2.set_ylabel('y')
    ax2.legend(['from initial state'+initial_state_a,])
    #ax2.legend(['from initial state'+initial_state_a, 'from initial state'+initial_state_b])
    
    ax3 = fig.add_subplot(2,2,4)
    ax3.plot(xs,zs)
    #ax3.plot(xsb,zsb)
    ax3.set_xlabel('x')
    ax3.set_ylabel('z')
    ax3.legend(['from initial state'+initial_state_a,])
    #ax3.legend(['from initial state'+initial_state_a, 'from initial state'+initial_state_b])
    plt.savefig('hw3_2.37.png')
    #plt.show()
    