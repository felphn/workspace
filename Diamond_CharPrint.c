#include <stdio.h>
#include <stdlib.h>

void printSpace(int len) {
    int k;
    for (k = 0; k < len; k++) {
        printf(" ");
    }
}


int main() {
    char letList[] = {"ABCDE"};
    int i, j = 0;
    for (i = 0; i < 5; i++) {
        printSpace(7-i);
        printf("%c", letList[i]);
        if (i > 0) {
            printSpace(i+j);
            printf("%c", letList[i]);
            j++;
        }
        printf("\n");
    }
    for (i = 0; i < 4; i++) {
        printSpace(4+i);
        printf("%c", letList[3-i]);
        if (i >= 0 && i != 3) {
            printSpace((j+1)-i);
            printf("%c", letList[3-i]);
            j--;
        }
        printf("\n");
    }
    system("PAUSE");
    return 0;
}
