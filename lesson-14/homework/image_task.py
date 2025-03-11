import numpy as np
from PIL import Image
import random

# Flip the image horizontally and vertically
def flip_image(image_array):
    return np.flipud(np.fliplr(image_array))

# Add random noise to the image
def add_noise(image_array):
    noise = np.random.randint(0, 50, image_array.shape, dtype=np.uint8)
    noisy_image = np.clip(image_array + noise, 0, 255)
    return noisy_image

# Increase brightness of red and green channels
def brighten_channels(image_array, value=40):
    image_array[:, :, 0] = np.clip(image_array[:, :, 0] + value, 0, 255)  # Red channel
    image_array[:, :, 1] = np.clip(image_array[:, :, 1] + value, 0, 255)  # Green channel
    return image_array

# Apply a black mask to a 100x100 region in the center
def apply_mask(image_array):
    h, w, _ = image_array.shape
    x_start, y_start = w // 2 - 50, h // 2 - 50
    image_array[y_start:y_start + 100, x_start:x_start + 100] = [0, 0, 0]
    return image_array


def main(image_path, output_path):
    image = Image.open(image_path)
    image_array = np.array(image, dtype=np.uint8)

    # Apply transformations
    flipped = flip_image(image_array)
    noisy = add_noise(flipped)
    brightened = brighten_channels(noisy)
    masked = apply_mask(brightened)

    # Save output
    output_image = Image.fromarray(masked)
    output_image.save(output_path)
    print(f"Modified image saved to {output_path}")


if __name__ == "__main__":
    input_image_path = "/Users/a.fayzullayev/PycharmProjects/PythonProject1/birds.jpg"
    output_image_path = "/Users/a.fayzullayev/PycharmProjects/PythonProject1/birds_modified.jpg"
    main(input_image_path, output_image_path)
