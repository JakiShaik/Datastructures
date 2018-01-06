#include<stdio.h>
#include<stdlib.h>

struct node {
  int c;
  struct node * next;
}Node;

int main() {
  
  struct node * head = NULL;
  struct node * p= NULL;
  int i;
  struct node * current;
  //linked list creation
  for(i=0;i<6;i++) {
    struct node * new = (struct node *) malloc(sizeof(struct node));
    new->c=i;
    if(i==0) {
      head = new;
      current = new;
    }
    else {
      current->next= new;
      current = new;
    }
  }
  current->next=NULL; //if we dont add this line we will get segmentation fault
  //printf("head->c is %d\n",head->c);
  //printing linkedlist
  p = (struct node *) malloc(sizeof(struct node));
  p = head;
  //printf("p->c is %d\n",p->c);
  while(p != NULL) {
    //printf("inside while\n");
    printf("%d\t",p->c);
    p = p->next;
  }
  printf("\n");
  return 0;
}
