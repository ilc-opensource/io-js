#include "stdio.h"
#include "funcPoint.h"
int gafp;

int func_int_r_int(int a) {
  return a;
}

int func_int_r_floatp(float *a) {
  return *a;
}

int *func_intp_r_intp(int *a) {
  *a = 10;
  return a;
}

float func_float_r_int_charp(int a, char* b) {
  float t = a + b[0];
  return t;
}

void func_v_r_v(void) {
  gafp = 16;
}

int func_int_r_fp2(fp_int_r_int fp1, fp_int_r_int fp2) {
  return fp1(5) + fp2(6);
}

int func_int_r_fp1(fp_int_r_floatp fp1) {
  float f[5] = {1.0, 2.1, 3.2};
  return fp1(f);
}

int *func_intp_r_fp1(fp_intp_r_intp fp1) {
  int a[4] = { 2, 3, 4};
  return fp1(a);
}

float func_float_r_fp1(fp_float_r_int_charp fp1) {
  return fp1(6, "hello");
}

int func_int_r_fpd(int (*fp1)(int)) {
  return fp1(123);
}

void func_v_r_fp(fp_v_r_v fp1) {
  fp1();
}
