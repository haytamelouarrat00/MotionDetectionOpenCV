# Motion Detection Using OpenCV

This project demonstrates a simple motion detection system built with Python and OpenCV. It utilizes frame differencing, thresholding, contour detection, and drawing to identify and highlight movement in video streams.

## Features

- **Frame Differencing**: Compares two consecutive frames to find areas of change which indicate motion.
- **Dynamic Thresholding**: Isolates regions of motion using a binary threshold method.
- **Contour Detection**: Identifies the outlines of moving objects.
- **Bounding Boxes and Labels**: Draws rectangles around moving objects and labels them as "Movement".

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed
- OpenCV-Python package installed
- NumPy package installed
- Matplotlib package installed (optional, for further data visualization needs)

You can install the required packages using pip:

```bash
pip install numpy opencv-python matplotlib
