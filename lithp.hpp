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

vector<long long> ints_nil;
vector<double> doubles_nil;
vector<char> chars_nil;

template <class T>
vector<T> map(T (*func)(T), vector<T> v){
  for (typename vector<T>::iterator it = v.begin(); it != v.end(); ++it){
    *it = func(*it);
  }
  return v;
}

template <class T>
vector<T> append(T item, vector<T> v){
  v.push_back(item);
  return v;
}
