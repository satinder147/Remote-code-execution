#include<bits/stdc++.h>
using namespace std;
int randomize()
{
    return rand()%100000;
}
int main()
{
    srand(time(NULL));
    cout<<"enter number of test files"<<endl;
    int n;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        string test_name="test/test"+to_string(i)+".txt";
        string ans_name="test/ans"+to_string(i)+".txt";
        ofstream test(test_name,ios::out);
        ofstream ans(ans_name,ios::out);
        //int num=randomize();
        int num=5;
        test<<num<<'\n';
        for(int j=0;j<num;j++)
        {
            int a=randomize();
            int b=randomize();
            //cout<<a<<" "<<b;
            int solution=a+b;
            test<<to_string(a)<<" "<<to_string(b)<<'\n';
            ans<<solution<<'\n';

        }
    test.close();
    ans.close();
        
    }


}