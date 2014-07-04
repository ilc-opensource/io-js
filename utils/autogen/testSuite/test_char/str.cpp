#include <string.h>
char a[5];

char *p = a;

const char* pc = "Done";

const char *changeStr(char *str) {
  str[1] = str[1] + 1;
  return pc;
}

const char *copyCharArray(char str[]) {
  strcpy(a, str);
  return pc;
}
