# universe_matrix

This package lets developers use BASIC style dynamic arrays within python. This is useful when you're sending data back to universe and are trying to structure it to how it will be used natively.   

Key points here are that indexing starts from 1 and -1 as a position means append, similar to how BASIC handles arrays. 

# Requirements

This package requires the Rocket supplied module u2py as this is just a wrapper around it. 

# Installation
    pip install universe-matrix
    
# Examples

	>>> from universe_matrix import UniverseMatrix
  
	>>> a = UniverseMatrix()
	>>> a[1] = 'Hello'
	>>> a[2] = 'World'
	>>> print(a.u2())
	HelloþWorld

	>>> a = UniverseMatrix()
	>>> a[-1] = 'Hello'
	>>> a[-1] = 'World'
	>>> print(a.u2())
	HelloþWorld

	>>> a = UniverseMatrix()
	>>> a[1] = 1
	>>> a[2] = 2
	>>> a[2,1] = 3
	>>> a[2,2] = 4
	>>> a[2,3] = 5
	>>> a[2,3,1] = 6
	>>> a[2,3,2] = 7
	>>> a[2,3,2,2] = 8
	>>> print(a.u2())
	1þ3ý4ý6ü7û8

	>>> print(a[2,3,1])
	6
