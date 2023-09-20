#include <bits/stdc++.h>
#define ll long long
#define endl "\n"
#define MAXINTEGER 2147483647

using namespace std;

void solution() {
    int n;
    // 메트릭스 개수
    cin >> n;
    int *d = new int[n+2]; // 1...n+1
    for(int i=1; i<=n+1; i++)
        cin >> d[i];

    int **opt = new *int[n];
    for(int i=0; i<n;i++) {
        opt[i] = new int[n];
        for(int j=0; j<n; j++)
            opt[i][j] = MAXINTEGER;
    }   
    
    for(int j=1;j<=n;j++) {
        for(int i=j; i>=1; i--) {
            if(i == j) {
                opt[i][j] = 0;
                continue;
            }
            int temp = 0;
            for(int k=i; k<j; k++) 
                opt[i][j] = min(opt[i][j], opt[i][k] + opt[k+1][j] + d[i]*d[k+1]*d[j+1]);
        }
    }

    
    for(int i=1; i<=n; i++) {
        for(int j=1; j<=n; j++) {
            printf("%10d ", opt[i][j]);
        }
        cout << endl;
    }

}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    solution();
    return 0;
}
