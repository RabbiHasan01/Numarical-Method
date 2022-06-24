

#include<bits/stdc++.h>
using namespace std;

void printBits(unsigned int a){

    static int flag=0;
    if(flag!=32){
       ++flag;
       printBits(a/2);
       printf("%d",a%2);
       --flag;
       if(flag==31 || flag == 23){
            putchar(' ');
       }
    }
}

void pFloatbits(float x){

    unsigned int *ip =(unsigned *) &x;
    printBits(*ip);


}
void test(double x,int n,double sum){
    double avg=sum/n;
    cout << "std deviation ";
    cout <<fabs(x-avg)/n << "\n";

}

int main(){

int n;
cin>>n;
int c=1;
double v[n+1];
double x,sum=0.0;
for(int i = 1; i <= n; i++) {
        //cout<<setprecision(6);
        srand(time(0));
        double d = rand()/double(RAND_MAX)*i;///0 - 1

v[i] = d;
}

for(int i = 1; i <= n; i++) {
    cout << v[i] << " ";
}
cout << endl;
for(int i = 1; i <=5; i++) {
    //cout << v[i] << " ";
    printf("bit representation " );
    pFloatbits(v[i]);
    cout << endl;
}
for(int i = 1; i <= n; i++) {
    //test(v[i],n,sum);
}
cout <<"k-th num average \n";
for(int i = 1; i <= n; i++) {
    sum+=v[i];
}
}
