typedef void (*fail_fp_v_r_intp)(int *);

extern void fail_func_v_r_intp(int *);

extern int fail_func_int_r_int_fp1(int arg0, fail_fp_v_r_intp fp1);

extern int fail_gafp;
