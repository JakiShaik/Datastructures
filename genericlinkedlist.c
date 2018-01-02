#include<stdio.h>
#include<stdlib.h>


struct node {

  void * data;
  struct node * next;
} node;



void push(struct node** head_ref,void* new_data,size_t data_size) {

  //creating new node
  struct node* new_node = (struct node *) malloc(sizeof(struct node));


  new_node->data = malloc(data_size);
  new_node->next = (*head_ref);
  
  int i;
  
  //sending data byte by byte and char is one byte size
  for(i=0;i<data_size;i++) {
    *(char *) (new_node->data+i) = *(char *) (new_data + i);
  }
  
  
  *(head_ref) = new_node;

}

//function to print the linked list, have one function pointer of void type.
void printList(struct node * node, void (*fnptr) (void *)) {
  printf("********\n");
  while(node != NULL) {
    
    (*fnptr) (node->data); //sending arguments to function pointer
    node = node->next;
  }
  
}

void printInt(void *n) {
  printf("%d\t",*(int *)n);
}

void printFloat(void *n) {

  printf("%.2f\t",*(float *)n);
}

int main() {

  int i;
  struct node * start=NULL;

  int arr[]={10,20,30,40,50};
  unsigned int_size = sizeof(int);

  for(i=4;i>=0;i--)
    push(&start,&arr[i],int_size);
  printf("created one integer linked list\n");
  printList(start,printInt);
  printf("\n");

  unsigned float_size = sizeof(float);
  //making start to the null again
  start = NULL;

  float arr2[]={10.1,10.2,20.1,20.2,30.3};
  
  for(i=4;i>=0;i--){
    push(&start,&arr2[i],float_size);
  }
  printf("created one Float linked list\n");
  printList(start,printFloat);
  printf("\n");
  return 0;
}
