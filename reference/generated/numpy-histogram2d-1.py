from matplotlib.image import NonUniformImage
import matplotlib.pyplot as plt

# Construct a 2-D histogram with variable bin width. First define the bin
# edges:

xedges = [0, 1, 3, 5]
yedges = [0, 2, 3, 4, 6]

# Next we create a histogram H with random bin content:

x = np.random.normal(2, 1, 100)
y = np.random.normal(1, 1, 100)
H, xedges, yedges = np.histogram2d(x, y, bins=(xedges, yedges))
# Histogram does not follow Cartesian convention (see Notes),
# therefore transpose H for visualization purposes.
H = H.T

# :func:`imshow <matplotlib.pyplot.imshow>` can only display square bins:

fig = plt.figure(figsize=(7, 3))
ax = fig.add_subplot(131, title='imshow: square bins')
plt.imshow(H, interpolation='nearest', origin='lower',
        extent=[xedges[0], xedges[-1], yedges[0], yedges[-1]])
# <matplotlib.image.AxesImage object at 0x...>

# :func:`pcolormesh <matplotlib.pyplot.pcolormesh>` can display actual edges:

ax = fig.add_subplot(132, title='pcolormesh: actual edges',
        aspect='equal')
X, Y = np.meshgrid(xedges, yedges)
ax.pcolormesh(X, Y, H)
# <matplotlib.collections.QuadMesh object at 0x...>

# :class:`NonUniformImage <matplotlib.image.NonUniformImage>` can be used to
# display actual bin edges with interpolation:

ax = fig.add_subplot(133, title='NonUniformImage: interpolated',
        aspect='equal', xlim=xedges[[0, -1]], ylim=yedges[[0, -1]])
im = NonUniformImage(ax, interpolation='bilinear')
xcenters = (xedges[:-1] + xedges[1:]) / 2
ycenters = (yedges[:-1] + yedges[1:]) / 2
im.set_data(xcenters, ycenters, H)
ax.images.append(im)
plt.show()

# It is also possible to construct a 2-D histogram without specifying bin
# edges:

# Generate non-symmetric test data
n = 10000
x = np.linspace(1, 100, n)
y = 2*np.log(x) + np.random.rand(n) - 0.5
# Compute 2d histogram. Note the order of x/y and xedges/yedges
H, yedges, xedges = np.histogram2d(y, x, bins=20)

# Now we can plot the histogram using
# :func:`pcolormesh <matplotlib.pyplot.pcolormesh>`, and a
# :func:`hexbin <matplotlib.pyplot.hexbin>` for comparison.

# Plot histogram using pcolormesh
fig, (ax1, ax2) = plt.subplots(ncols=2, sharey=True)
ax1.pcolormesh(xedges, yedges, H, cmap='rainbow')
ax1.plot(x, 2*np.log(x), 'k-')
ax1.set_xlim(x.min(), x.max())
ax1.set_ylim(y.min(), y.max())
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('histogram2d')
ax1.grid()

# Create hexbin plot for comparison
ax2.hexbin(x, y, gridsize=20, cmap='rainbow')
ax2.plot(x, 2*np.log(x), 'k-')
ax2.set_title('hexbin')
ax2.set_xlim(x.min(), x.max())
ax2.set_xlabel('x')
ax2.grid()

plt.show()
