#include <stdio.h>
#include "struct.h"
struct_t func(struct_t a, int *ib) {
  a.a[0] = 789;
  a.b = 23.45;
  a.str[3] = 't';
  a.st->ss1 = 18;
  a.st->ss2[2] = 2;
  *ib = 10;
  return a;
}
struct_t *funcp(struct_t *a, int *ib) {
  a->a[0] = 789;
  a->b = 23.45;
  a->str[3] = 't';
  a->st->ss1 = 18;
  a->st->ss2[2] = 2;
  *ib = 10;
  return a;
}
