#include <stdio.h>
typedef struct  
{
   void (*fnctn1)(void *self);
   void (*fnctn2)(void *self);
   void (*fnctn3)(void *self);
}vtable;
typedef struct
{
   vtable*vtable;
}base;

