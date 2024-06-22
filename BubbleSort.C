#include<stdio.h>
void Display(int* A,int n){
    for(int i=0;i<n;i++){
     printf("%d  ",A[i]);   
    }
    printf("\n");
}
void BubbleSort(int* A,int n){
    int temp,isSorted;
    for(int i=0;i<n-1;i++){
        printf("Pass %d on the Array \n",i);
        isSorted=1;
        for(int j=0;j<n-1-i;j++){
            if(A[j]>A[j+1]){
               temp=A[j];
               A[j]=A[j+1];
               A[j+1]=temp;
               isSorted=0;
            }
        }
        if(isSorted){
            return;
        }
    }
}
int main(){
    int A[]={232,223,334,21,22,11,21,31};
    int n=sizeof(A)/sizeof(int);
    Display(A,n);
    BubbleSort(A,n);
    Display(A,n);
}

// 232  223  334  21  22  11  21  31  
//Pass 0 on the Array 
//Pass 1 on the Array 
//Pass 2 on the Array 
//Pass 3 on the Array 
//Pass 4 on the Array 
//Pass 5 on the Array 
// 11  21  21  22  31  223  232  334  
