#include "stdio.h"
#include "funcPoint_failed.h"
int fail_gafp;

void fail_func_v_r_intp(int *f) {
  printf("Before: fail_gafp = %d\n", fail_gafp);
  *f = 26;
  printf("After: fail_gafp = %d\n", fail_gafp);
  if (fail_gafp != 26)
    printf("\n[C]: Global Variable Value Error!!!!\n\n");
}

int fail_func_int_r_int_fp1(int arg0, fail_fp_v_r_intp fp1) {
  fp1(&fail_gafp);
  return arg0;
}
