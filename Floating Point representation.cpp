

#include<bits/stdc++.h>
using namespace std;
int main(){
float x;
cin>>x;
unsigned u = *(unsigned*)&x;
for(int i = 31; i>=0; i--){
printf("%d", u>>i & 0x1);
}
}
