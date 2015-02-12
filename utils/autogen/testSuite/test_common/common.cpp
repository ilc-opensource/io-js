#include <stdio.h>
char gc;
unsigned char guc;
int gi;
unsigned int gui;
unsigned gu;
short gs;
unsigned short gus;
long gl;
unsigned long gul;
long long gll;
unsigned long long gull;
float gf;
double gd;

double funcd(float f, double d) {
  return f + d;
}

float funcf(double d) {
  return d;
}

unsigned long long funcull(unsigned long ul , long long l) {
  return ul + l;
}

long long funcll(unsigned long long ull, long long ll) {
  return ull - ll;
}

unsigned long funcul(unsigned long long ull, long l) {
  return ull - l;
}

long funcl(unsigned long long ull, long l) {
  return ull + l;
}

unsigned int funcui(unsigned int ui, unsigned short us) {
  return ui + us;
}

unsigned funcu(unsigned u, unsigned short us) {
  return u + us;
}

int funci(int i, unsigned int ui) {
  return i - ui;
}

unsigned short funcus(short s) {
  return s * 2;
}

short funcs(unsigned short us) {
  return us - 0x78;
}

unsigned char funcuc(unsigned int ui, unsigned char uc) {
  return ui - uc;
}

char funcc(int i, char c) {
  return i - c;
}

void funcvn() {
  printf("\nhere is void funcvn()\n");
}

void funcvv(void) {
  printf("\nhere is void funcvv(void)\n");
}
