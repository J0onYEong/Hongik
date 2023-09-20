#include <bits/stdc++.h>
#define ll long long
#define endl "\n"

using namespace std;

void possibleCase(int n) {
    // n개의 메트릭스 곱셈 경우의수
    // 노드수에 따른 트리경우의 수를 의미한다.
    int *memo = new int[n];
    memo[0] = 1;
    memo[1] = 1;
    for(int i=2; i<n; i++) {
        for(int j=0; j<i; j++) {
            int left = j;
            int right = (i-1)-j;
            memo[i] += memo[left] * memo[right];
        }
    }
    cout << memo[n-1] << endl;
}
void solution() {
    int n;
    cin >> n;
    possibleCase(n);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    solution();
    return 0;
}
