typedef int (*func_int_r_int) (int);
typedef float (*func_float_r_int_float)(int, float);
typedef int* (*func_intp_r_int)(int);
typedef long long int64 ;
typedef long  int34 ;

int f3(int);
int fint(int);
float fintfloat(int a, float b);
int fp3(func_intp_r_int fp3);
int fp4(func_int_r_int fp1, func_int_r_int fp2);
float fp5(func_float_r_int_float fp3);
//int fp6(int34 fp);
int fp7(int (*f2p)(int));
//void attachInterrupt(char, void (*)(void), int mode);
