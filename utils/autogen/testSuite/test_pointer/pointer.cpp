#include "stdio.h"
short psa[5];
short *ppsa = psa;

long la[10];
long long lla[10];
long long *plla = lla;

float fa[3];
double lfa[3];
double *plfa = lfa;

int* funcP(int a[], int *b, short *si){
  *a = 5;
  *b = 10;
  *si = 15;
  return a;
}

long long* funcLP(long l[], long long ll[], long long *llp){
  l[1] = 0x5a5a5a;
  ll[2] = 0x5a5a5a5a5a;
  *llp = 0x1a1a1a1a1a;
  return llp;
}

double* funcFP(float f[], double lf[], double *lfp){
  f[1] = 1238.789;
  lf[1] = 123456.0e+50;
  *lfp = 15896.0E+78;
  return lfp;
}
