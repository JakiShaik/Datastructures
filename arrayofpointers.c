#include<stdio.h>
#include<stdlib.h>


int main() {

  char *name[] = {"Jaki","Sharief","Shaik"};

  printf("%s\n",*(name));
  printf("%s\n",*(name + 1));
  printf("%s\n",*(name +2));
  printf("%c\n",**name);
  printf("%c\n",*(*name+1));
  printf("%c\n",*(*name+2));
  printf("%c\n",*(*name+3));
  printf("%c\t%c\t%c\t%c\t%c\t%c\t%c\n",**(name+1),*(*(name+1)+1),*(*(name+1)+2),*(*(name+1)+3),*(*(name+1)+4),*(*(name+1)+5),*(*(name+1)+6));
  return 0;
}
