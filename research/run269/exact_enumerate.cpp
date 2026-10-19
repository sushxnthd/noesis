// Exact dyadic exhaustive neural-word verifier for NOESIS K001 Run269.
#include <boost/multiprecision/cpp_int.hpp>
#include <array>
#include <fstream>
#include <iostream>
#include <vector>
using boost::multiprecision::cpp_int;
using V=std::array<cpp_int,3>;
cpp_int D,A[3][3],E[3][3],b[3],v[3],c,scales[15],biases[14][3][3];
long long visited[15]={},errors[15]={};
std::vector<int> path,first_word;
int first_error=1000;
void walk(const V& h,int target,int depth){
  if(depth==14)return;
  for(int s=0;s<3;s++){
    int nexttarget=(s==1)?1:(s==2)?0:target;
    V nh;
    for(int i=0;i<3;i++){
      cpp_int x=biases[depth][s][i];
      for(int j=0;j<3;j++)x+=A[i][j]*h[j];
      nh[i]=(x>0)?x:cpp_int(0);
    }
    cpp_int logit=c*scales[depth+1];
    for(int j=0;j<3;j++)logit+=v[j]*nh[j];
    path.push_back(s);visited[depth+1]++;
    if(int(logit>0)!=nexttarget){
      errors[depth+1]++;
      if(depth+1<first_error){first_error=depth+1;first_word=path;}
    }
    walk(nh,nexttarget,depth+1);
    path.pop_back();
  }
}
int main(int argc,char**argv){
 if(argc!=2){std::cerr<<"Usage: exact_enumerate coefficients.txt\n";return 2;}
 std::ifstream f(argv[1]);if(!(f>>D))return 2;
 for(int i=0;i<3;i++)for(int j=0;j<3;j++)f>>A[i][j];
 for(int s=0;s<3;s++)for(int i=0;i<3;i++)f>>E[s][i];
 for(int i=0;i<3;i++)f>>b[i];
 for(int i=0;i<3;i++)f>>v[i];f>>c;
 if(!f)return 2;
 scales[0]=1;for(int i=1;i<=14;i++)scales[i]=scales[i-1]*D;
 for(int t=0;t<14;t++)for(int s=0;s<3;s++)for(int i=0;i<3;i++)
  biases[t][s][i]=(E[s][i]+b[i])*scales[t];
 V h={cpp_int(0),cpp_int(0),cpp_int(0)};walk(h,0,0);
 for(int t=1;t<=14;t++)std::cout<<"depth "<<t<<" visited "<<visited[t]<<" errors "<<errors[t]<<"\n";
 std::cout<<"first_error "<<first_error<<" word ";
 for(int s:first_word)std::cout<<s;std::cout<<"\n";
 return first_error==14?0:1;
}
