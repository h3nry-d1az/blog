#include <cstdint>
#include <iostream>

template <typename T>
concept Monoid = requires(T a, T b) { a *b; };

template <Monoid A> A pow(A a, uint64_t n)
{
    A r{}; // starts being the monoid identity

    for (int i = 0; i < 64 - __builtin_clzll(n); i++)
    {
        if (n & (1ull << i))
            r = r * a;
        a = a * a;
    }

    return r;
}

struct M2x2
{
    uint64_t e11, e12, e21, e22;

    M2x2() : e11(1), e12(0), e21(0), e22(1)
    {
    }

    M2x2(uint64_t e11, uint64_t e12, uint64_t e21, uint64_t e22)
        : e11(e11), e12(e12), e21(e21), e22(e22)
    {
    }

    M2x2 operator*(const M2x2 &B) const
    {
        return (M2x2){
            (e11 * B.e11 + e12 * B.e21) % 46337,
            (e11 * B.e12 + e12 * B.e22) % 46337,
            (e21 * B.e11 + e22 * B.e21) % 46337,
            (e21 * B.e12 + e22 * B.e22) % 46337,
        };
    };
};

int main()
{
    uint64_t n;

    std::cin >> n;

    if (n == 0)
    {
        std::cout << 0 << std::endl;
        return 0;
    }

    std::cout << pow(M2x2{0, 1, 1, 1}, n - 1).e22 << std::endl;

    return 0;
}