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
  p=head->next->next;
  p->next->next->next = p;
  head->next=p->next;
  printf("%d\n",head->next->next->next->next->c);
  
}
