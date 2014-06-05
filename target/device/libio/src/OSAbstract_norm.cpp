#include "OSAbstract_norm.h"

void initWithTty(char *tty0, char *tty1, char *tty2) 
{
  char* ttys[] = {
     tty0,
     tty1,
     tty2
  };
  
  init(sizeof(ttys) / sizeof(char*), ttys); 
}
