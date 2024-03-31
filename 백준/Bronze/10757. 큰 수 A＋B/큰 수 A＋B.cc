#include <iostream>
#include <string>
using namespace std;

int main() {
    string A, B, result = "";
    cin >> A >> B;

    int maxLength = max(A.length(), B.length());
    bool carry = false;

    while (A.length() < maxLength)
        A = '0' + A;

    while (B.length() < maxLength)
        B = '0' + B;

    for (int i = maxLength - 1; i >= 0; i--) {
        int num = (A[i] - '0') + (B[i] - '0') + carry;
        carry = (num >= 10);
        result = to_string(num % 10) + result;
    }

    if (carry) result = '1' + result;

    cout << result << endl;
    return 0;
}