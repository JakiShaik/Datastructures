#include<stdio.h>
#include<stdlib.h>

void strngcpy(char *t,char *s) {
  printf("t is %s\n",t);
  while(*s++ = *t++)
    ; 
  //printf("s is %s\n",*s);
}

int main()
{
  char *t = "jaki";
  char *s;
  s = (char *) malloc(sizeof(char)*6);
  printf("t is %s\n",t);
  //strngcpy(t,s);
  int i=0;
  //We can not use *s++ or *t++ here, because t should not move from starting address. Hence we are incrementing i and getting the value in that location
  while(*(s+i) = *(t+i))
    i++;
  printf("s is %s\n",s);
  return 0;
}
