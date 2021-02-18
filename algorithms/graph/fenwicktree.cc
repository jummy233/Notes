#include <array>
#include <iostream>

// fenwick tree (binary index tree) BIT.
//
// Motivation:
// For an array, we normally can do two things:
//  1. modify one element
//  2. query range sum (by taking the difference between two prefix sums)
// We have O(1) for 1, but O(n) for 2.
//
// --------------------------------------------------------------------------------
// arr:   1 2 3 4 5
//  for get prefix sum of 3, we need to calculate 1 + 2 + 3.
// --------------------------------------------------------------------------------
//
// To speed up the range query, we can try to store the parital sum of elements
// instead of elements themselves in an array. This way we can have O(1) range
// query. But to modify an element, the change will propagate to all rest
// elements, so update will be O(n)
//
// --------------------------------------------------------------------------------
// arr:   1 3 6 10 15
//  for updating 3 to 4, we need to modify 6->7, 10->11, 15->16.
// --------------------------------------------------------------------------------
//
// Bit allows you good balance of the two operations. We can have O(logn) for
// both! This is particularly useful when you need frequent range query and
// array updates.
//
// For an given array, we can make another array to store it's prefix sum:
// psum: 1  3  6 10 15
//       |  |  |  |  |
// arr:  1  2  3  4  5
// This structure has both problem we had above, because whenever we do an O(1)
// operation we need to trgger the O(n) on the other array to keep everything
// update to date.
//
//              a
//

#define lowbit(x) ((x) & (-x))

constexpr int MAXN = 100000;

std::array<int, MAXN> tree;

// modify one element.
inline void update(int i, int x) {
  for (int pos = i; pos < MAXN; pos += lowbit(pos)) {
    tree[pos] += x;
  }
}

// accumulate sum
inline int query(int n) {
  int ans = 0;
  for (int pos = n; pos; pos -= lowbit(pos))
    ans += tree[pos];
  return ans;
}

inline int query(int a, int b) { return query(b) - query(a - 1); }
