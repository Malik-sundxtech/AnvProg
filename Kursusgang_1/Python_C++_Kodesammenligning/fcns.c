#include <stdio.h>
char* foo(){
    return "Hello from foo\n";
}

int main(){
    printf("%s", foo());
    return 0;
}


