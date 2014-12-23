#include <string.h>
char a[5];

char *p = a;

const char* pc = "Done";

const char *changeStr(char *str) {
  str[1] = str[1] + 1;
  return pc;
}

const char *changeStr(char *str, char *str2) {
  str[1] = str[1] + 1;
  str2[0] = str2[0] - 32;
  return pc;
}

const char *changeStr(char *str, char *str2, char *str3) {
  str[1] = str[1] + 1;
  str2[0] = str2[0] + 32;
  str3[0] = str3[0] - 32;
  return pc;
}

const char *copyCharArray(char str[]) {
  strcpy(a, str);
  return pc;
}
