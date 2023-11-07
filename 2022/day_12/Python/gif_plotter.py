from PIL import Image
import numpy as np

class GifPlotter:

    def __init__(self) -> None:
        self.frames:list[Image.Image] = []

    def old_snap(self, array:np.ndarray) -> None:
        array = array / array.size
        array = (array * 255).astype(np.uint8)
        self.frames.append(Image.fromarray(array.T))

    def snapshot(self, distances:np.ndarray, heights:np.ndarray):
        pathed_to = distances < distances.size
        pathed_filter = np.array((pathed_to, pathed_to))
        height_pixels = (heights / np.max(heights) * 200 + 55).astype(np.uint8)
        rgb = np.array((height_pixels, height_pixels, height_pixels))
        rgb[1:,:,:][pathed_filter] = 0 # colour pathed in red
        rgb = np.repeat(rgb, 6, axis=1)
        rgb = np.repeat(rgb, 6, axis=2)
        self.frames.append(Image.fromarray(rgb.T))

    def save(self, name):
        durations = np.ones(len(self.frames), dtype=int) * 50
        durations[-1] = 1000
        self.frames[0].save(f"../{name}.gif", save_all=True, append_images=self.frames[1:], loop=0, duration=list(durations))