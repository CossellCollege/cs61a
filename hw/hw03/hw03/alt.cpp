#include <iostream>
#include <optional>

// C++ 版本的 next_smaller_coin 函数
// int next_smaller_coin(int coin)
// {
//     if (coin == 25)
//         {
//                 return 10;
//                     }
//                         if (coin == 10)
//                             {
//                                     return 5;
//                                         }
//                                             if (coin == 5)
//                                                 {
//                                                         return 1;
//                                                             }
//                                                                 return -1; // C++ 中没有 None，使用 -1 表示没有更小的硬币
//                                                                 }
//
//                                                                 // C++ 版本的 constrained_count_small 函数
//                                                                 int constrained_count_small(int total, int largest_coin)
//                                                                 {
//                                                                     if (total == 0)
//                                                                         {
//                                                                                 return 1;
//                                                                                     }
//                                                                                         if (total < 0)
//                                                                                             {
//                                                                                                     return 0;
//                                                                                                         }
//                                                                                                             if (largest_coin == -1)
//                                                                                                                 {
//                                                                                                                         return 0;
//                                                                                                                             }
//                                                                                                                                 int without_coin = constrained_count_small(total, next_smaller_coin(largest_coin));
//                                                                                                                                     int with_coin = constrained_count_small(total - largest_coin, largest_coin);
//                                                                                                                                         return without_coin + with_coin;
//                                                                                                                                         }
//
//                                                                                                                                         // C++ 版本的 count_partitions 函数
//                                                                                                                                         int count_partitions(int total)
//                                                                                                                                         {
//                                                                                                                                             return constrained_count_small(total, 25);
//                                                                                                                                             }
//
//                                                                                                                                             // 主函数
//                                                                                                                                             int main()
//                                                                                                                                             {
//                                                                                                                                                 int total;
//                                                                                                                                                     std::cout << "Enter the total amount: ";
//                                                                                                                                                         std::cin >> total;
//
//                                                                                                                                                             int result = count_partitions(total);
//                                                                                                                                                                 std::cout << "Total partitions: " << result << std::endl;
//
//                                                                                                                                                                     return 0;
//                                                                                                                                                                     }
