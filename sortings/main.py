from bubble_sorting import bubble_sort
from bubble_sorting_with_flag import bubble_sorting_with_flag
from shaker_sorting import shaker_sorting
from simple_insert_sorting import insertion_sorting_simple
from sentinel_insert_sorting import sentinel_insertion_sorting
from binary_search_insertion_sorting import binary_insertion_sorting
from shell_sorting import shell_sorting
from selection_sorting import selection_sorting
from bidirectional_selection_sorting import bidirectional_selection_sorting
from quick_sorting import quick_sorting
while True: 
    inp = input("")
    match inp:
        case "1":
            print(bubble_sort())
            break
        case "2":
            print(bubble_sorting_with_flag())
            break
        case "3":
            print(shaker_sorting())
            break
        case "4":
            print(insertion_sorting_simple())
            break 
        case "5":
            print(sentinel_insertion_sorting())
            break
        case "6":
            print(binary_insertion_sorting())
            break
        case "7":
            print(shell_sorting())
            break
        case "8":
            print(selection_sorting())
            break
        case "9":
            print(bidirectional_selection_sorting())
            break
        case "10":
            print(quick_sorting())
            break
        

