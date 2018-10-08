from _primes.lib import primes

from cffi import FFI
ffi = FFI()

num_primes = 10000

array = ffi.new(("int[%d]" % num_primes))

primes(array,num_primes)

for i in range(num_primes):
    print(array[i])

