enum ea {
  A0,
  A1,
  A2,
  A3,
  A4,
  A5
};

typedef enum {
//  B0,
  B1,
  B2 = -1,
  B3,
  B4,
  B5
} enum_b;

extern enum_b testEnum(enum ea a);
extern enum ea testEnumT(enum_b a);

extern enum ea ga;
extern enum_b gb;
