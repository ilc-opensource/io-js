#include "stdio.h"
#include "funcPoint.h" 
int f3 (int a) {
  printf ("f3: %d\n", a);
}
int fint (int a) {
  printf ("fint: %d\n", a);
  return a;
}

float fintfloat(int a, float b) {
  float t = a + b;
  printf("In fintfloat: %f\n", t);
  return t;
}

int fp7(int (*f3)(int)) {
  printf ("fp 3: func_intp_r_int\n");
  f3(4);
}

int fp4(func_int_r_int fp1, func_int_r_int fp2) {
  printf ("fp4(func_int_r_int fp1, func_int_r_int fp2)");
  return fp1(6) +  fp2(7);
}

float fp5(func_float_r_int_float fp1) {
  printf ("fp5(func_int_r_int_float fp1)\n");
  float f = fp1(6, 3.5);
  return f;
}
