#include <bits/stdc++.h>

using namespace std;
const int N = 100010;
int n, C, dp[N];
int w[N], c[N], m[N];  // 价值；体积；数量；

int new_n = 0;
int new_w[N], new_c[N], new_m[N];

int main() {

    cin >> n >> C;

    for (int i = 1; i <= n; ++i) {
        cin >> w[i] >> c[i] >> m[i];
    }

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m[i]; j <<= 1) {  // 二进制拆分
            m[i] -= j;
            ++new_n;
            new_c[new_n] = j * c[i];
            new_w[new_n] = j * w[i];
        }

        if (m[i] > 0) {  // 找到余数：25 - (1 + 2 + 4 + 8) = 10
            ++new_n;
            new_c[new_n] = m[i] * c[i];
            new_w[new_n] = m[i] * w[i];
        }
    }
    
    // 滚动数组
    for (int i = 1; i <= new_n; ++i) {
        for (int j = C; j >= new_c[i]; --j) {
            dp[j] = max(dp[j], dp[j - new_c[i]] + new_w[i]);
        }
    }

    cout << dp[C] << endl;

    return 0;
}
