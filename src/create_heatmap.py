import matplotlib.pyplot as pl
import matplotlib.image as mpimg
import numpy as np
import scipy
import scipy.ndimage


def heatmap_from_overlay(fpath):

    img = mpimg.imread(fpath)

    img_gauss = scipy.ndimage.filters.gaussian_filter(img, 100)
    fig = pl.figure()
    fig.set_size_inches(5,5)
    ax = pl.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    # pl.set_cmap('RdPu')
    ax.imshow(np.negative(img_gauss[:,:,0]), aspect = 'equal')

    
    pl.savefig("heatmap_{:s}".format(fpath), dpi=300)
    


if __name__ == "__main__":

    heatmap_from_overlay("overlay_axon_1-5_noalpha.png")
    heatmap_from_overlay("overlay_dendrite_1-5_noalpha.png")
    
