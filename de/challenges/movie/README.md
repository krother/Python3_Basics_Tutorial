
# Create a Movie

## Material:

 * Your favourite image(s)
 * Python + Pillow
 * `MEncoder` or another program to create movies from a set of images.
 * see the [Flower Assembly Movie](https://youtu.be/FE6_nx-MKc8) to get an idea how the result could look like.

## Task

Write a program using the PIL library that creates a set of `.png` images. Generate the images and generate a movie from that using a non-Python tool (e.g. MEncoder). Remember that a movie typically has 25 frames per second.

## Hints

* start with a very simple movie to make sure the assembly is working
* the [Flower Assembly Movie](https://youtu.be/FE6_nx-MKc8) was created by slowly disassembling the picture and playing the frames backwards

## Creating a movie from frames on Windows

MEncoder requires files with the frames to have names like frame_000123.png so that they have the right order in the final movie.

1. Collect all frame images in one directory
2. copy Mencoder into that directory.
3. open a console (`Start -> Execute -> cmd`)
4. switch with `cd <directory_name>` to that directory
5. type

    mencoder "mf://*.png" -mf fps=25 -o output.avi -ovc lavc -lavcopts vcodec=mpeg4
