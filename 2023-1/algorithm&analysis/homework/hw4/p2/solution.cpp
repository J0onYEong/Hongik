#include<bits/stdc++.h>

using namespace std;

int main() {
    int count[128];
    for(int i=0; i<128; i++) 
        count[i] = 0;

    FILE *fs;
    fs = fopen("anna-karerina.txt", "r");

    while(feof(fs) == 0) {
        int c = fgetc(fs);
        count[c]++;
    }
    fclose(fs);

    for(int i=0; i<128; i++) 
        printf("count[%d]=%d\n", i, count[i]);

    vector<int> temp;
   
   for(int i=0; i<128; i++) 
        if(count[i] > 0)
            temp.push_back(count[i]);
    
    sort(temp.begin(), temp.end());

    queue<int> A, B;
    for(auto d : temp)
        A.push(d);
    int sum = 0;
    queue<int> con;
    while(!A.empty() || !B.empty()) {
        if(A.empty()) {
            con.push(B.front());
            B.pop();
        } else if (B.empty()) {
            con.push(A.front());
            A.pop();
        } else {
            int c1 = A.front();
            int c2 = B.front();
            if(c1 < c2) {
                con.push(c1);
                A.pop();
            } else {
                con.push(c2);
                B.pop();
            }
        }

        if(con.size() == 2) {
            int temp = 0;
            temp += con.front();
            con.pop();
            temp += con.front();
            con.pop();
            sum += temp;
            B.push(temp);
        }
    }
    cout << "compressed: " << sum << endl;    
    cout << sum/8 << " bytes" << endl;

    return 0;
}
