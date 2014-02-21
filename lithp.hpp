#include <cstdio>
#include <cstdlib>
#include <vector>
#include <iostream>


using namespace std;

#define if(a,b,c) ((a)?(b):(c))
#define lt(a,b) ((a)<(b))
#define lte(a,b) ((a)<=(b))
#define gt(a,b) ((a)>(b))
#define gte(a,b) ((a)>=(b))
#define eq(a,b) ((a)==(b))
#define neq(a,b) ((a)!=(b))

//Underscores because not, and, or are keywords
#define not_(a) (!(a)) 
#define and_(a,b) ((a)&&(b))
#define or_(a,b) ((a)||(b))

#define add(a,b) ((a)+(b))
#define sub(a,b) ((a)-(b))
#define mult(a,b) ((a)*(b))
#define div(a,b) ((a)/(b))
#define mod(a,b) ((a)%(b))

#define index(v,i) (v[i])

template<class T>
void print(T a){
  cout << a << endl;
}

template<class T>
void print(vector<T> v){
  for(typename vector<T>::iterator it = v.begin(); it != v.end(); ++it){
    cout << (*it) << " ";
  }
  cout << endl;
}

vector<int> ints_nil;
vector<long long> longs_nil;
vector<float> floats_nil;
vector<double> doubles_nil;
vector<char> chars_nil;

template <class T1, class T2>
vector<T2> map(T2 (*func)(T1), vector<T1> v){
  vector<T2> v2;
  for (typename vector<T1>::iterator it = v.begin(); it != v.end(); ++it){
    v2.push_back(func(*it));
  }
  return v2;
}

template <class T>
vector<T> append(T item, vector<T> v){
  v.push_back(item);
  return v;
}

template <class T1, class T2>
T1 foldl(T1 (*func)(T1, T2), T1 start, vector<T2> v){
  for (typename vector<T2>::iterator it = v.begin(); it != v.end(); ++it){
    start = func(start, *it);
  }
  return start;
}

vector<int> range(int start, int stop, int step=1){
  vector<int> v;
  for(int i = start; i < stop; i += step){
    v.push_back(i);
  }
  return v;
}
