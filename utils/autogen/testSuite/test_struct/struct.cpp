#include <stdio.h>
#include "struct.h"
struct ss sg;
struct_t st;
struct_t stp[2];

struct_t func(struct_t a, int *ib) {
  a.a[0] = 789;
  a.b = 23.45;
  a.e = EUC1;
  a.str[3] = 't';
  (a.st)->ss1 = 18;
  ((a.st)->ss2)[2] = 2;
  *ib = 10;
  return a;
}

struct_t *funcp(int *ib, struct_t *a) {
  a->a[0] = 789;
  a->b = 23.45;
  a->e = EUC1;
  a->str[3] = 't';
  (a->st)->ss1 = 18;
  ((a->st)->ss2)[2] = 2;
  *ib = 10;
  return a;
}

struct ss funcss(struct ss *a) {
  a->ss1 = 20;
  a->e = EUB;
  a->e1 = EUC1;
  a->ss2[2] = 3;
  return *a;
}
