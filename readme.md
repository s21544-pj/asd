|   |sort  |random  |reversesort|
|---|------|--------|-----------|
|QS |0.3227|1004.741|580.62     |
|Kop|0.8269|0.8361  |0.7841     |
|Bub|837.64|406.834 |1144.58    |

Pierwotne pomiary wymagały modyfikacji w postaci zmienay algorytmu Quick Sort na wersję iteracyjną, przy 100 tysiącach elementów tablicy rekurencja była zbyt głęboka. Zdecydowanie kopcowanie poradziło sobie najlepiej na tle pozostałych, właściwie w każdym przypadku skalując się odpowiednio do zadanego rozmiaru. Przy takiej ilości elementów bubble sort jest zbyt powolnym algorytmem, podobnie iteracyjna wersja quick sorta z racji płynnego przejścia tylko przez już posortowaną tablicę, oba algorytmy niezbyt skutecznie skalują się wraz z wielkością, w przypadku quick sorta raczej z powodu zastosowania iteracji niż samego algorytmu.