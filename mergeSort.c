#include <stdio.h>
#include <stdlib.h>

void printArr(int arr[], int len) {
    int i;
    for (i = 0; i < len; i++) {
        printf("%d ", arr[i]);
    }
}


void sortSides(int arr[], int l, int r) {
    if (l < r) {
        int m = (l + r) / 2;
        sortSides(arr, l, m);
        sortSides(arr, m + 1, r);
        mergeSort(arr, m, l, r);
    } else {
        return;
    }
}


void mergeSort(int arr[], int m, int l, int r) {
    int lLen = m - l + 1;
    int rLen = r - m;
    int leftArr[lLen], rightArr[rLen];
    int a, b, c;
    for (a = 0; a < lLen; a++) {
        leftArr[a] = arr[l + a];
    }
    for (a = 0; a < rLen; a++) {
        rightArr[a] = arr[m + a + 1];
    }
    a = 0;
    b = 0;
    c = l;
    while (a < lLen && b < rLen) {
        if (leftArr[a] < rightArr[b]) {
            arr[c] = leftArr[a];
            a++;
        } else {
            arr[c] = rightArr[b];
            b++;
        }
        c++;
    }
    while (a < lLen) {
        arr[c] = leftArr[a];
        a++;
        c++;
    }
    while (b < rLen) {
        arr[c] = rightArr[b];
        b++;
        c++;
    }
}


int main() {
    int valueLst[] = {15, 2, 7, 26, 35, 9, 4, 8, 52, 68};
    int i, sizeLst = sizeof(valueLst)/sizeof(valueLst[0]);
    printf("List: ");
    printArr(valueLst, sizeLst);
    sortSides(valueLst, 0, sizeLst-1);
    printf("\nSorted List: ");
    printArr(valueLst, sizeLst);
    printf("\n");
    system("PAUSE");
    return 0;
}
