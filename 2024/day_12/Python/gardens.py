import numpy as np

# Load in as an image
# Split into 26 images for each letter in image
# For each:
    # Use scipy image label for each to find each feature:
        # https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.label.html#scipy.ndimage.label
    # Extract each feature
    # Count area
    # Count perimeter https://stackoverflow.com/a/13444457


def load_image(img: [[str]]):

    np.ndarray()