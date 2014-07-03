#include <string.h>
char a[5];

char *p = a;

char *changeStr(char *str) {
  str[1] = str[1] + 1;
  return "Done";
}

char *copyCharArray(char str[]) {
  strcpy(a, str);
  return "Done";
}
