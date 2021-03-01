#include <stdio.h>

int main(void) 
{
    char name[200];
    printf("What is your name? ");
    fgets(name,200,stdin);
    printf("hello %s", name);
    return 0;
}