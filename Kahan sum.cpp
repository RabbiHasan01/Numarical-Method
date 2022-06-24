
#include <bits/stdc++.h>
using namespace std;
double kahanSum(vector<double> &v)
{
double sum = 0.0, error = 0.0;
for(double i : v)
{
double y = i - error;
double t = sum + y;
error = (t - sum) - y;
sum = t;
}
return sum;
}
double sum(vector<double> &v)
{
double sum = 0.0;
for(double i : v) {
sum = sum + i;
}
return sum;
}
int main()
{
int n;
cin>>n;
vector<double> v(n+1);
double x;
for(int i = 0; i < n; i++) {
        cin>>x;
v[i] = x;
}
cout << setprecision(16);
cout << "Normal sum: " << sum(v) <<endl;
cout << "Kahan sum: " << kahanSum(v);
}
