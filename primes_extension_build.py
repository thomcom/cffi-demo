from cffi import FFI
ffibuilder = FFI()

ffibuilder.cdef("float primes(int* array, int length);")

ffibuilder.set_source("_primes",  # name of the output C extension
"""
    #include "primes.h"',
""",
    sources=['primes.c'],   # includes pi.c as additional sources
    libraries=['m'])    # on Unix, link with the math library

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
