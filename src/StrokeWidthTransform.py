"""
File Name: StrokeWidthTransform.py

Authors: Kyle Seidenthal

Date: 10-06-2019

Description: Implementation of the stroke width transform

"""
import numpy as np
import matplotlib.pyplot as plt

from skimage import feature
from skimage.data import page, astronaut
from skimage import color

def _compute_image_properties(img):
    """
    Compute the canny edges and gradient direction for the image
    
    :param img: The image to process, as a numpy array
    :returns: The canny edges, and the gradient directions for each pixel in the image
    """
    
    # TODO: This is not finding the edges in the text image
    edges = feature.canny(img)
    
    plt.imshow(edges)
    plt.show()
    # TODO: Get canny edges and gradient directions of all pixels

    return edges, None


def SWT(img):
    """
    Compute the stroke width transform of the given image
    
    :param img: The image to process
    :returns: The SWT of the image
    """
    
    # Create a new SWT image and set all elements to infinity
    SWT_image = np.full(img.shape, np.inf) 
    edges, directions = _compute_image_properties(img)

    # TODO: Get the image properties
    
    # TODO: For each edge pixel p follow the ray r = p + n * d_p until another edge pixel q is found
        
        # TODO: If the gradient direction at q is roughly opposite to the direction at p, set each element of the SWT
        # image along the ray from p to q to the width ||p - q||, unless it already has a lower value

        # TODO: If q is not found, or the direction of q is not opposite of p, discard the ray


    # TODO: For each ray that we kept above, compute the median SWT calue of all pixels in the ray, then set all pixels
    # of the ray with SWT values above that median to be equal to the median


            
    pass

def main():
    img = page()
    img = color.rgb2gray(img)
    plt.imshow(img)
    plt.show()

    SWT(img)

if __name__ == "__main__":

    main()
