#include <iostream>
#include <vector>
#include <algorithm>
#include <chrono>
#include <random>

using namespace std;
using namespace std::chrono;

const int SIZE = 1000000;

int main() {
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<int> dist_int(0, 1000000);
    uniform_real_distribution<double> dist_float(0.0, 100000.0);

    cout << "Dang tao bo du lieu co kich thuoc " << SIZE << " phan tu" << endl;

    // 1. Int Sorted
    vector<int> arr1(SIZE);
    for(int &x : arr1) x = dist_int(gen);
    sort(arr1.begin(), arr1.end());

    auto start = high_resolution_clock::now();
    sort(arr1.begin(), arr1.end());
    cout << duration_cast<duration<double, milli>>(high_resolution_clock::now() - start).count() << endl;

    // 2. Int Reverse
    vector<int> arr2(SIZE);
    for(int &x : arr2) x = dist_int(gen);
    sort(arr2.begin(), arr2.end());
    reverse(arr2.begin(), arr2.end());

    start = high_resolution_clock::now();
    sort(arr2.begin(), arr2.end());
    cout << duration_cast<duration<double, milli>>(high_resolution_clock::now() - start).count() << endl;

    // 3, 4, 5. Int Random
    for(int i = 0; i < 3; ++i) {
        vector<int> arr(SIZE);
        for(int &x : arr) x = dist_int(gen);

        start = high_resolution_clock::now();
        sort(arr.begin(), arr.end());
        cout << duration_cast<duration<double, milli>>(high_resolution_clock::now() - start).count() << endl;
    }

    // 6, 7, 8, 9, 10. Float Random
    for(int i = 0; i < 5; ++i) {
        vector<double> arr(SIZE);
        for(double &x : arr) x = dist_float(gen);

        start = high_resolution_clock::now();
        sort(arr.begin(), arr.end());
        cout << duration_cast<duration<double, milli>>(high_resolution_clock::now() - start).count() << endl;
    }

    return 0;
}
