#include "enum.h"
enum ea ga = A2;
enum_b gb = B2;
enum_b testEnum(enum ea a)
{
  return (enum_b)((int)a + 1);
}

enum ea testEnumT(enum_b b)
{
  return (enum ea)((int)b + 2);
}
