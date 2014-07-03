#include <stdio.h>
class A {
  public:
    A(int a=9){ a_ = a;};
    int a_;
    int getValue() {
      return a_;
    }
};

class B {
  private:
    A *ap;
  public:
    B (A *a) {
      ap = a;
    }

    A* getA() {
      return ap;
    }

    void setA(A * a) {
      ap = a;
    }

    int getValue() {
      return ap->getValue();
    }
};
extern A Ainstance;
extern B Binstance;
