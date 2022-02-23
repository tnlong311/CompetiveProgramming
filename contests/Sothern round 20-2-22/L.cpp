#include <bits/stdc++.h>

using namespace std;
#define int long long
const int MAX = (int) 1e4 + 3;

signed main() { 
    int n; cin >> n;
    int maxValue = INT_MIN;
    map<int, int> counting;

    // Count the frequency
    for(int i = 0; i < n; i++) {
        int value; cin >> value;
        maxValue = max(value, maxValue);
        counting[value]++;
    }

    int total = 0;
    for(int i = 2; i <= maxValue; i++) {
        int cnt = 0;
        int j = 1;
        while(pow(i, j) <= maxValue) {
            if(counting.find(pow(i, j)) != counting.end()) {
                cnt += counting[pow(i, j)];
                counting.erase(pow(i, j));
            }
            j++;
        }

        total = total + (cnt * (cnt - 1)) / 2;
    }

    if(counting.find(1) != counting.end())
        total = total + (counting[1] * (counting[1] - 1)) / 2;

    cout << total;
    return 0;
}