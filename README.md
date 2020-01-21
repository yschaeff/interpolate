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

the file out will contain:

```
 2.0,  4609.0
 2.01,  4614.9
 2.02,  4618.53
 2.03,  4619.98
 2.04,  4619.3
 2.05,  4616.58
 2.06,  4611.88
 2.07,  4605.29
 2.08,  4596.87
 2.09,  4586.69
 2.1,  4574.84
 2.11,  4561.37
 2.12,  4546.37
 2.13,  4529.91
 2.14,  4512.05
...
```
