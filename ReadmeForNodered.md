# node-red branch
Generated nodes for node-red framework from .h file

## How to use
* followed `Readme.md` to setup enviroments
* Set env `NODERED_PATH` in util/autogen/config.py
* run the script for test
```shell
npm test
```
* find what are generated in your own NODERED_PATH 
 
## Supported function types
* function overwrite
* function with basic-type args
* function with one-level-pointer-type args
* function with one-divison-array args
* function with stucture args
* function with enum args

## Not supported function types
* function which is defined in class
* function with two or more level pointer args
* function with two or more level array args
* function with union args 

## How to pass msg for generated nodes
* `inject node` as the input
  - msg.payload format is comform with json style as
    ``` shell
    {"0": ..., "1": ..., ... }
    ```
* args 
  - integer type
    * `Dec`: 123 or "123"
    * `Hex`: "0x123"
    * `Oct`: "0123"
  - float type
    * 123.56
    * 12.2e20
  - char
    * `character`: "c"
    * `integer`:   98
  - char array
    * `string`: "hello"
    * `int array`: [, , , ,]
  - array
    * [,,,,]
  - struct
    * {"a": ..., "b": ..., "c",...}
  - enum
    * integer: 2

  - function pointer
    * string: "var args0 = function() {}"

* for example 1
  ``` shell
  extern struct_t func(struct_t a, int *ib);
  struct ss {
    int ss1;
    enum eub e;
    eua e1; 
    int ss2[10];
  };

  typedef struct {
    int a[5];
    float b;
    eua e;
    char str[10];
    struct ss st[2];
  } struct_t;
  ```
  args shoule be
  ``` shell
  {"0":{"a":[10,20,30,40], "b": 21.2e2, "e":0, "str":"nihao", "st" : [ {"ss1": "10" ,"e": 0, "e1": 0, "ss2": [10,"0x20","030"]}]},"1":[20,"0x10"]}
  ```

* for example 2
  ``` shell
  typedef int (*fp_int_r_floatp)(float *);
  extern int func_int_r_fp1(fp_int_r_floatp fp1);
  ```
  args should be
  ``` shell
  {"0":" var arg0 = function(a) {     return io.func_int_r_floatp(a);   }"}
  ```

# How to check the output
  - user `debug node` to check output
  - the `first debug node` is the return value
  - the `other debug nodes` show the arg changes of pointer or array types.
  - for example
    ``` shell
    * const char *changeStr(char *str,  int i1, char *str2)
    * the output 
      - 1st debug node: return value "char *"
      - 2nd debug node: arg "str" after call
      - 3rd debug node: arg "str2" after call
    ```

