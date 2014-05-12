#include <stdio.h>
int funcP(int *a, int *b, char *str){
  *a = 5;
  *b = 10;
  printf("C:str: %s\n", str);
  *str = 'h';
  return *a + *b;
}

