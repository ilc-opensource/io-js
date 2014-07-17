typedef int (*fp_int_r_int) (int);
typedef int (*fp_int_r_floatp)(float *);
typedef int* (*fp_intp_r_intp)(int *);
typedef void (*fp_v_r_intp)(int *);
typedef float (*fp_float_r_int_charp)(int, char *);

typedef void (*fp_v_r_v)(void);
extern void func_v_r_v(void);

extern int func_int_r_int(int);
extern int func_int_r_floatp(float *);
extern int* func_intp_r_intp(int *);
extern float func_float_r_int_charp(int a, char* b);
extern void func_v_r_intp(int *);
extern void func_v_r_intp_t(int *);

extern int func_int_r_fp2(fp_int_r_int fp1, fp_int_r_int fp2);
extern int func_int_r_fp1(fp_int_r_floatp fp1);
// extern int *func_intp_r_fp1(fp_intp_r_intp fp1);
extern float func_float_r_fp1(fp_float_r_int_charp fp1);
extern int func_int_r_fpd(int (*f2p)(int));
extern void func_v_r_fp(fp_v_r_v fp1);

extern int func_int_r_int_fp1(int arg0, void(*f)(int*));
extern int func_int_r_int_fp1_t(int arg0, fp_v_r_intp fp1);

extern int gafp;
extern int gbfp;
