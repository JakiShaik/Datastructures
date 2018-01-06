#include<stdio.h>
#include<stdlib.h>


struct node {
  int data;
  struct node * next;
};

struct node * addnode(int dat) {
  
  struct node * new = (struct node *) malloc(sizeof(struct node));
  new->data = dat;
  new->next = NULL;
  return new;
}

int main() {
  char c;
  int d,i;
  struct node * head = (struct node *) malloc(sizeof(struct node));
  struct node * temp = (struct node *) malloc(sizeof(struct node));
  struct node * new = (struct node *) malloc(sizeof(struct node));
  head = NULL, temp = NULL;
  while(1) {
    //printf("\n");
    printf("Please enter your choice: s:Insert a node at start i: after an index e: at the end of the list; CTRL+C to stop\n");
    //scanf("%c",&c);
    fflush(stdin);
    c = getchar();
    //printf("c is %c\n",c);
    if(c=='s') {
      printf("Please enter the data in the node\n");
      scanf("%d",&d);
      if(head == NULL) {
	new = addnode(d);
	head = new;
      }
      else {
	new = addnode(d);
	new->next = head;
	head = new;
      }
      temp = head;
      printf("Your list is:\n");
      while(temp) {
	printf("%d\n",temp->data);
	temp = temp->next;
      }
    }
    else if(c =='i') {
      printf("Please enter the index of the node\n");
      scanf("%d",&i);
      printf("Please enter the value of the node\n");
      scanf("%d",&d);
      int count = 1;
      printf("inserting after index %d\n",i);
      temp = head;
      for(;count<i;count++){
	printf("count is %d\n",count);
	printf("temp->next is %d\n",temp->data);
	temp = temp->next;
	printf("temp->next os %d\n",temp->data);
      }
      new = addnode(d);
      new->next = temp->next;
      temp->next = new;
      temp = head;
      printf("Your list is:\n");
      while(temp) {
	printf("%d\n",temp->data);
	temp = temp->next;
      }
    }
    else if(c == 'e') {
      
      printf("Please enter value of the node\n");
      scanf("%d",&d);
      temp = head;
      while(temp->next)
	temp = temp->next;
      new = addnode(d);
      temp->next = new;
      temp = head;
      printf("Your list is:\n");
      while(temp) {
	printf("%d\n",temp->data);
	temp = temp->next;  
      }
    }
    else printf("Please enter a valid option\n");
    //printf("\n");
    fflush(stdin);
  }
}
