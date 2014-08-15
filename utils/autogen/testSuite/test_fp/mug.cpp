#include "mug.h"
#include <stdio.h>

motion_data_t msa = {1, 2};

void mug_func(motion_data_t *m) {
  printf("Before:\n");
  printf("ax = %d\n", msa.ax);
  printf("ay = %d\n", msa.ay);
  m->ax = 10;
  m->ay = 20;
  printf("After:\n");
  printf("msa.ax = %d\n", msa.ax);
  printf("msa.ay = %d\n", msa.ay);
  if (msa.ax != 10 || msa.ay != 20)
    printf("\n[C]: Error!!!\n\n");
}

void mug_read_motion_sensor_async(motion_cb_t cb) {
  cb(&msa);
}

int main()
{
  mug_read_motion_sensor_async(mug_func);
  printf("ax4 = %d\n", msa.ax);
  printf("ay4 = %d\n", msa.ay);
}
