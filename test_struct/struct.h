typedef struct {
  int ss1;
  int* ss2;
} ss;
typedef struct {
  int *a;
  float b;
  char * str;
  ss *st;
} struct_t;

struct_t func(struct_t a, int *ib);
struct_t* funcp(struct_t *a, int *ib);
