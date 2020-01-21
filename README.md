# Interpolate

Given a line based input of either (X) or (X,Y) values (can be mixed) calculate
the cubic interpolation of the points in between each two consecutive values.
It is required that the input is sorted by X value, ascending.

In and output can either be files or pipes.

## Usage

```
usage: interpolate.py [-h] (--resolution RESOLUTION | --steps STEPS) [--plot]
                      [--dx DX]
                      [infile] [outfile]

positional arguments:
  infile                stdin if omitted or '-'.
  outfile               stdout if omitted or '-'.

optional arguments:
  -h, --help            show this help message and exit
  --resolution RESOLUTION
                        Resolution of interpolated points.
  --steps STEPS         Desired number of steps between to given points.
  --plot                Show plot when done.
  --dx DX               When no X given use DX as offset to the previous X.
```

## Example

```bash
for i in {1..10}; do echo $RANDOM; done | python3 interpolate.py --resolution=0.01 --plot - out
```

![plot](https://raw.githubusercontent.com/yschaeff/interpolate/master/plot.png)
