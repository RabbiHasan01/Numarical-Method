#include<bits/stdc++.h>
using namespace std;
int main(){
// without srand(time(0)). rand() function always generate specific sequence.
// for my laptop: it generate 41 18467 6334 26500 19169 15724 11478 29358 26962
//24464
srand(time(0));
// if you divide a number by its maximum possible value.
// then result is between 0 and 1
// cout<<fixed<<setprecision(10)<<rand()/double(RAND_MAX)<<endl;
double d = rand()/double(RAND_MAX); // output: d = 0.968993
// now multiply the number by the range.
// let range is 1000
double range_nmbr = d*1000;
printf("%.12lf\n", range_nmbr); // now you will get any number from 0 to 1000
}
