#include "struct.h"
void func(struct_t a, int ib) {
  a.b = 23.45;
  a.st->ss1 = 18;
}
void funcp(struct_t *a, int ib) {
  a->b = 23.45;
  a->st->ss1 = 18;
}
