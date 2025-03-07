from cffi import FFI

ffibuilder = FFI()

# Define the interface to expose.
ffibuilder.cdef(
    """
typedef struct Counter Counter;

Counter* create_counter(int initial);
void free_counter(Counter* c);
int increment_counter(Counter* c);
int get_counter(Counter* c);
"""
)

# Pass the C source code.
ffibuilder.set_source(
    "lockfree_counter",
    """
#include <stdlib.h>
#include <stdatomic.h>
typedef _Atomic int atomic_int; 

// Define structure for our counter
typedef struct {
  atomic_int value;
} Counter;

// Create a new counter
Counter * create_counter(int initial) {
  Counter * c = (Counter *)malloc(sizeof(Counter));
  if (c != NULL) {
    atomic_init(&c->value, initial);
  }
  return c;
}

// Free counter
void free_counter(Counter * c) {
  free(c);
}

// Atomically increment counter and return the new value
int increment_counter(Counter * c) {
  return atomic_fetch_add(&c->value, 1) + 1;
}

// Atomically get the current counter value 
int get_counter(Counter * c) {
  return atomic_load(&c->value);
}
""",
    libraries=[],
    extra_compile_args=["-std=c11"]
)

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
