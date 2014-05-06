typedef struct {
  int ss1;
  int ss2;
} ss;
typedef struct {
  int a;
  float b;
  char * str;
  ss *st;
} struct_t;

void func(struct_t a, int ib);
void funcp(struct_t *a, int ib);
