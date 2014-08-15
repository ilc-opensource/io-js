#ifndef __MUG__
#define __MUG__ 1
typedef struct {
  int ax;
  int ay;
} motion_data_t;

typedef void (*motion_cb_t)(motion_data_t *);

void mug_func(motion_data_t *);

void mug_read_motion_sensor_async(motion_cb_t cb);

extern motion_data_t msa;
#endif
