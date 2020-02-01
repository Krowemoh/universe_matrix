# universe_matrix

Wrapper for Multivalue Data

# Installation
    pip install universe-matrix
    
# What it does

Syntactically similar to how dynamic arrays are handled in BASIC. 

Indexing starts at 1 just like BASIC and -1 appends. 

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
