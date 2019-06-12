''' Graph2D/Sorts.py
    Author: Ryan Stenmark <ryanpstenmark@gmail.com> (rstenmark.github.io)
    Date: May 16, 2019
'''

from random import randint
from sys import maxsize
import BarGraph as bg


def swap(array, i, j):
    # Swaps the elements at self.array[i] and self.array[j]
    k = array[i]
    array[i] = array[j]
    array[j] = k

def is_sorted(array, mintomax=True):
    arraysz = len(array)
    if mintomax is True:
        for i in range(1, arraysz):
            if array[i] >= array[i-1]:
                continue
            else:
                return False
    else:
        for i in range(1, arraysz):
            if array[i] <= array[i-1]:
                continue
            else:
                return False

    return True

def bogosort(bargraph, mintomax=True):
    # Get array and array size
    array = bargraph.array
    arraysz = len(bargraph.array)-1

    # Check if array is sorted before doing anything
    if is_sorted(array, mintomax):
        bargraph.reset_cursors()
        return True

    # Get cursor position before operation
    cursor = bargraph.get_cursor(0)

    # Reset all bar colors to white
    bargraph.reset_colors()

    # Increment cursor position & wrap around
    if cursor < arraysz:
        bargraph.set_cursor(0, cursor+1)
    else:
        bargraph.set_cursor(0, 0)

    # Determine random element to swap with cursor element
    j = randint(0, arraysz)

    # Perform swap operation
    if not cursor == j:
        bargraph.swapWithCursor(0, j)

    # Set element at j to green
    bargraph.set_cursor(1, j, bg.green)

def bubblesort(bargraph, mintomax=True):
    # Get array and array size
    array = bargraph.array
    arraysz = len(bargraph.array)-1

    # Check if array is sorted before doing anything
    if is_sorted(array, mintomax):
        bargraph.reset_cursors()
        return True

    # Reset all bar colors to white
    bargraph.reset_colors()

    # Increment cursor position & wrap around
    i = bargraph.get_cursor(0)
    if i < arraysz-1:
        bargraph.set_cursor(0, i+1)
    else:
        bargraph.set_cursor(0, 0)

    # Set element at j to green
    i = bargraph.get_cursor(0)
    j = i + 1
    bargraph.set_color(j, bg.green)

    if mintomax is True:
        if array[i] > array[j]:
            swap(array, i, j)
    else:
        if array[i] < array[j]:
            swap(array, i, j)

def _sort(bargraph, mintomax=True):
    # Get array and array size
    array = bargraph.array
    arraysz = len(bargraph.array)-1

    # Check if array is sorted before doing anything
    if is_sorted(array, mintomax):
        bargraph.reset_cursors()
        return True

    bargraph.reset_colors()

    i = bargraph.get_cursor(0)
    j = bargraph.get_cursor(1)

    # If the parent cursor is at the end of array
    # Reset both cursors to index 0
    if i+1 > arraysz:
        i = 0
        bargraph.set_cursor(0, i)
        bargraph.set_cursor(1, i)

    # If search cursor is at the end of array
    # Move parent cursor forward and move search cursor to parent
    if j+1 > arraysz:
        bargraph.set_cursor(0, i+1)
        bargraph.set_cursor(1, i+1, bg.green)
        j = i+1
        # Otherwise move search cursor forward
    else:
        # Keep parent cursor highlighted
        bargraph.set_cursor(0, i)
        bargraph.set_cursor(1, j+1, bg.green)
        j +=1

    if mintomax is True:
        if array[i] >= array[j]:
            swap(array, i, j)
            bargraph.set_cursor(0, i+1)
            bargraph.set_cursor(1, i+1)
    else:
        if array[i] <= array[j]:
            swap(array, i, j)
            bargraph.set_cursor(0, i+1)
            bargraph.set_cursor(1, i+1)

    bargraph.update_cursors(2)

def selectionsort(bargraph, mintomax=True):
    # Get array and array size
    array = bargraph.array
    arraysz = len(bargraph.array)-1

    # Check if array is sorted before doing anything
    if is_sorted(array, mintomax):
        bargraph.reset_cursors()
        return True

    bargraph.reset_colors()

    i = bargraph.get_cursor(0)
    j = bargraph.get_cursor(1)

    if j+1 <= arraysz:
        # Haven't searched entire space
        # Move search cursor forward
        bargraph.set_cursor(1, j+1, bg.green)
        j = bargraph.get_cursor(1)

        if array[j] <= array[bargraph.get_cursor(2)] and array[j] <= array[i]:
            # If array[j] is less than the parent cursor value
            # and less than the previous found minimum value
            # make it the new minimum value
            bargraph.set_cursor(2, j, bg.blue)

    else:
        # Searched entire space
        # Swap the found new minimum with parent cursor
        min = bargraph.get_cursor(2)
        swap(array, i, min)
        bargraph.set_cursor(2, i+1, bg.blue)
        bargraph.set_cursor(1, i+1, bg.green)
        bargraph.set_cursor(0, i+1)

    bargraph.update_cursors(3)