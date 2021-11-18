# Algorithms realizations by Categories

1. One Pass Algorithms
   - [x] count_nums
   - [x] simple_sum 
   - [x] simple_sum_short
   - [x] product
   - [x] maximum
   - [x] minimum
   - [x] finder

2. Brute Force Method
   - [x] is_simple_num
   - [x] factorize_num
   - [x] square_numbers
   - [x] array_search
   - [x] array_invert
   - [x] move_array_left
   - [x] move_array_right
   - [x] sieve_of_eratosthenes
   
3. Sorting Algorithms
   Quadratic
   - [x] insert sort
   - [x] select sort
   - [x] bubble sort
   Linear
   - [x] count sort !one pass algo
   - [x] check_sorted
   Linearithmic
   - [x] quick_sort tony hoar sorting
   - [x] merge_sort
     - [x] merge

4. Recursive Algorithms
   - [x] factorial
   - [x] gcd
   - [x] gcd_better
   - [x] gcd_one_liner
   - [x] power
   - [x] power_better
   - [x] hanoi [description](https://pythobyte.com/tower-of-hanoi-python-01725/)
   - [x] generate_permutations
     - [x] gen_bin_recursive
     - [x] gen_bin_iterative
     - [x] generate_numbers
     
5. Search Algorithms 
   - [x] binary_search

5. Dynamic Programming
   - [x] Fibonacci
     - [x] dynamic_fib
   - [x] cricket jumps problem
     - [x] trajectories_num
     - [x] count_trajectories
     - [x] count_min_cost
   - [x] Линеаризация массива Aij <-> A[i*M+j] N строк M элементов в строке
   - [x] 1 Список списков A = [[0]*M]*N так создавать нельзя двумерный массив
   - [x] 2 Список списков Best Practice A = [[0]*M for i in range(N)] 
   - [x] A[0] == A[1] в 1 и 2 случает true но есть оператор сравнения ссылок является ли одно другим A[0] is A[1] в 1 случае выведет да во 2 случае выведет нет так как по сути это разные объекты 1 вариант ошибочный
лекция 10