
#include<bits/stdc++.h>
#define f(x) x*x*x - 2*x*x + x - 3
#define g(x) 3*x*x - 4*x + 1
using namespace std;
float newton_rapson(int n, float x0, float e){
float x1;
while(n--){
float fx = f(x0);
float gx = g(x0);
float d = fx/gx;
x0 = x0 - d;
if(d<e){
// return x0;
}
cout<<fx<<"\t"<<gx<<"\t"<<x0<<endl;
}
}
int main(){
newton_rapson(10, 3, 0.00001f);
}
