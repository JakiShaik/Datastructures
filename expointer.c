#include<stdio.h>
#include<stdlib.h>


int main() {

  int x=5;
  int *p = &x;
  printf("%d\n",x);
  printf("%u\n",&x);
  printf("%d\n",*(&x));
  printf("%u\n",p);
  printf("%d\n",*p);
  printf("%u\n",&p);
}
