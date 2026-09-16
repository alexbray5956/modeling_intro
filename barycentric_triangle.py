###Added edits after initial commit to "actually" complete the expected task
###Initial commit had 3 sections that did literally nothing

# Setup the Library
import matplotlib.pyplot as plt
import numpy as np


# Exercise 2: Reorganization
def point_in_triangle(p, a, b, c):
    """
    Return True if point p is inside triangle abc.
    Uses barycentric coordinates.
    """
    v0 = c - a
    v1 = b - a
    v2 = p - a

    dot00 = np.dot(v0, v0)
    dot01 = np.dot(v0, v1)
    dot02 = np.dot(v0, v2)
    dot11 = np.dot(v1, v1)
    dot12 = np.dot(v1, v2)

    denom = dot00 * dot11 - dot01 * dot01

    u = (dot11 * dot02 - dot01 * dot12) / denom
    v = (dot00 * dot12 - dot01 * dot02) / denom

    return (u >= 0) and (v >= 0) and (u + v <= 1)


# Exercise 2: Reorganization
def generate_triangle(width=800, height=700, border=150):

    # Create empty RGB image initialized to white
    image = np.ones((height, width, 3), dtype=float)

    # Triangle description
    red_point = np.array([width / 2, border])
    green_point = np.array([border, height - border])
    blue_point = np.array([width - border, height - border])

    max_dist = max(
        np.linalg.norm(red_point - green_point),
        np.linalg.norm(red_point - blue_point),
        np.linalg.norm(green_point - blue_point),
    )

    # Loop through every pixel
    for y in range(height):
        for x in range(width):
            p = np.array([x, y])

            if point_in_triangle(p, red_point, green_point, blue_point):
                d_red = np.linalg.norm(p - red_point)
                d_green = np.linalg.norm(p - green_point)
                d_blue = np.linalg.norm(p - blue_point)

                # Convert distances into "closeness"
                r = 1.0 - d_red / max_dist
                g = 1.0 - d_green / max_dist
                b = 1.0 - d_blue / max_dist

                color = np.array([r, g, b])

                # Normalize so colors remain vivid
                color /= color.max()

                image[y, x] = color

    return image


# Exercise 3: Add Project Point
def plot_point(red, green, blue):

    total = red + green + blue

    x = (red * 400 + green * 150 + blue * 650) / total

    y = (red * 150 + green * 550 + blue * 550) / total

    plt.plot(x, y, marker="o", markersize=15, color="black")


# Exercise 4: Display and optionally save the figure
def display_triangle(
    red=0.25, green=0.1, blue=0.9, save=False, filename="triangle1.png"
):

    image = generate_triangle()

    # Display result
    plt.figure(figsize=(8, 7))
    plt.imshow(image)

    # Add project point
    plot_point(red, green, blue)

    plt.axis("off")

    # Save figure if requested
    if save:
        plt.savefig(filename)

    plt.show()


if __name__ == "__main__":
    display_triangle()
