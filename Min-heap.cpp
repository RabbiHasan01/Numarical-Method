
#include <bits/stdc++.h>
using namespace std;
int main() {
int n;
double x, a, b;
priority_queue <double, vector<double>, greater<double> > pq;
cin>>n;
for(int i=0; i<n; i++) {
cin>>x;
pq.push(x);
}
do {
a = pq.top();
pq.pop();
if(pq.empty()) {
break;
}
b = pq.top();
pq.pop();
pq.push(a+b);
} while(!pq.empty());
cout<<fixed << setprecision(10)<<a<<endl;
return 0;
}
