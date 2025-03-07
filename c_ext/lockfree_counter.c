#include <stdatomic.h>
#include <stdlib.h>
//typedef _Atomic int atomic_int;

// Define structure for our counter
typedef struct {
  _Atomic int value;
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
