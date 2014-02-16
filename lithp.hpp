#include <cstdio>
#include <cstdlib>

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

#define int long long

int print(int d){
    return printf("%lld\\n", d);
}

int print(double f){
    return printf("%f\\n", f);
}

int print(float f){
    return printf("%f\\n", f);
}

int print(char c){
    return printf("%c\\n", c);
}

int print(){
    return printf("\\n");
}
