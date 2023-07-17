# br - brightness utility

**created:** 7/17/23
<br>
**python version:** 3.11.3

## about
Simple brightness utility with Python. Takes cli arguments to
adjust the value in the /sys/ brightness file. The math is just kinda slapped together so there's sometimes an issue with rounding, but works just fine and does what I needed it to.

## usage 
I pop this this script in /usr/local/bin/br and use it as so:

- `br +10`  ->  increases brightness by 10%
- `br -10`  ->  decreases brightness by 10%
- `br 50`   ->  sets the brightness to 50%

User has to be added to the `video` group, or else only the root user can use this script. 