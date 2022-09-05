import imageio
import matplotlib.pyplot as plt
import os

class Gif:
    """A list of images that can be turned into a gif   

    Methods:
    - add_frame()
    - add_frame_from_file(filename)
    - add_frame_from_figure(figure)
    - clear()
    - export(filename, fps)

    """
    def __init__(self):
        self.frames = []

    def add_frame(self):
        """Append a frame from the current figure"""
        filename = "temp_gif_frame_image.png"
        plt.savefig(filename, bbox_inches='tight')
        image = imageio.imread(filename)
        os.remove(filename)
        self.frames.append(image)
    
    def add_frame_from_file(self, filename):
        """Append a frame from an image file"""
        image = imageio.imread(filename)
        self.frames.append(image)

    def add_frame_from_figure(self, figure):
        """Append a frame from a given figure/figure number"""
        plt.figure(figure)
        self.add_frame()
    
    def clear(self):
        """Clear all frames within a gif"""
        self.frames.clear()
    
    def export(self, filename, fps=10):
        """Export a gif to a file (at a specified fps)"""
        imageio.mimsave(filename, self.frames, fps=fps)
