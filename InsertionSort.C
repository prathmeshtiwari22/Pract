// Online C compiler to run C program online
#include <stdio.h>
void Display(int *A,int n){
    for(int i=0;i<n;i++){
        printf(" %d  ",A[i]);
    }
    printf(" \n ");
}
void InsertionSort(int *A,int n){
    int key,j;
    for(int i=1;i<=n-1;i++){
        key=A[i];
        j=i-1;
        while(j>=0 && A[j]>key){
            A[j+1]=A[j];
            j--;
        }
        A[j+1]=key;
    }
}
int main(){
    int A[]={12,54,65,7,23,9};
    int n=sizeof(A)/sizeof(int);
    Display(A,n);
    InsertionSort(A,n);
    Display(A,n);
    return 0;
}
