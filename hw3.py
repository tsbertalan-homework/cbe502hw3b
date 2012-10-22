def n232nondiscriminant(a,b):
    return(b-a**2-1)

def n232discriminant(a,b):
    return((a**2-b+1)**2 - 4*a**2)

if __name__ == "__main__":
    stable_real_a = []
    stable_real_b = []
    unstable_real_a = []
    unstable_real_b = []
    
    stable_imaginary_a = []
    stable_imaginary_b = []
    unstable_imaginary_a = []
    unstable_imaginary_b = []
    a_range=[-1,4]
    b_range=[-1,4]
    resolution=10
    for x in range(a_range[0]*resolution, a_range[1]*resolution):
        a=x/float(resolution)
        for y in range(b_range[0]*resolution, b_range[1]*resolution):
            b=y/float(resolution)
            disc = n232discriminant(a,b)
            nondisc = n232nondiscriminant(a,b)
            if disc >= 0: # all real
                from_disc = disc**0.5 # the +/- part
                if nondisc < 0 and abs(from_disc) <= abs(nondisc):
                    case = 'real, all positive'
                    stable_real_a.append(a)
                    stable_real_b.append(b)
                else:
                    case = 'one or both negative real eigenvalues'
                    unstable_real_a.append(a)
                    unstable_real_b.append(b)
            else: # imaginary part (discriminant is negative)
                if nondisc < 0:
                    case = 'imaginary with positive real part'
                    stable_imaginary_a.append(a)
                    stable_imaginary_b.append(b)
                else:
                    case = 'imaginary with negative real part'
                    unstable_imaginary_a.append(a)
                    unstable_imaginary_b.append(b)
    import matplotlib.pyplot as plt
    ax = plt.figure(figsize=(12,6), dpi=120).add_subplot(1,1,1)
    ax.scatter(stable_real_a,stable_real_b, color='b')
    ax.scatter(unstable_real_a,unstable_real_b, color='r', marker='d')
    ax.scatter(stable_imaginary_a,stable_imaginary_b, color='g', marker='+')
    ax.scatter(unstable_imaginary_a, unstable_imaginary_b, color='y', marker='s')
    plt.legend(['stable_real (nonoscillatory)', 'unstable_real (nonoscillatory)', 'stable_imaginary (oscillatory)', 'unstable_imaginary (oscillatory)'])
    plt.xlim(a_range)
    plt.ylim(b_range)
    plt.xlabel('a')
    plt.ylabel('b')
    plt.title('hw3, 2.32')
    plt.savefig('hw3_regions.png')
    plt.show()
    