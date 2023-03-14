#include <stdio.h>
#include <stdint.h>
#define int uint32_t

int a, b;
int next(){
    a = a^(14*a);
    a^=b;
    b = 62555385*b+17;
    return a;
}

void menu(){
    char feedback[0x20];
    int choice = 0;
    while(1){
        printf("THE MARK MACHINE\n");
        printf("1. Guesstimate your mark\n2. Get your student number\n3. Enter Feedback\n4. Exit\nEnter here: ");
        scanf("%i", &choice);
        if(choice == 1){
            printf("Your mark is: %i\n", next()%49);
        }
        if(choice == 2){
            printf("Your student number is: %08x\n", next());
        }
        if(choice == 3){
            printf("We totally value your feedback!\nPlease enter it here for our great team of shredders to attend to it!\n");
            getchar();
            gets(feedback);
        }
        if(choice == 4){
            break;
        }
    }
}

int main(){
    setvbuf(stdin, NULL, 2, 0);
    setvbuf(stdout, NULL, 2, 0);
    a = (int)((long long)menu>>32);
    b = (int)((long long)menu&(0xffffffff));
    menu();
}
