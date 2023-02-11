import time
import threading
import pygame as pg
import sys
import random
pg.init()

class Graph:

    def __init__(self, max_value, width, height):
        self.max_value = max_value
        self.width, self.height = width, height
        self.list1 = []

        for x in range(self.max_value, 0, -1):
            n = random.randint(0, self.max_value)
            while n in self.list1:
                n = random.randint(0, self.max_value)
            
            self.list1.append(n)

        self.bg_color = (0, 0, 0)
        self.running = True

        sys.setrecursionlimit(self.max_value + 10)

    def show(self):
        clock = pg.time.Clock()
        window = pg.display.set_mode((self.width, self.height))
        window.fill(self.bg_color)

        while self.running:
            window.fill(self.bg_color)

            for e in pg.event.get():
                if e.type == pg.QUIT:
                    self.running = False
            
            l = len(self.list1)
            w = self.width / max(1, l)
            h = self.height / self.max_value
            x = 0

            for line in self.list1:
                
                rect1 = pg.Rect(self.width - x, 0, max(1, w), h * line)
                pg.draw.rect(window, (255, 0, 0), rect1)
                x += w

            pg.display.flip()

        #end main loop
        pg.quit()

    def display_values(self):
        print(self.list1)
        time.sleep(0.01)

    def bubble_sort(self, list1):
        
        copyList = []

        for x in list1:
            copyList.append(x)

        for i in range(len(list1) - 1):
            pole = list1[i]
            pole2 = list1[i + 1]
            if pole2 < pole:
                list1[i] = pole2
                list1[i + 1] = pole

        self.display_values()

        return list1 == copyList, list1

    def bubble_sort_main(self):
        while self.running:
            ready, list1 = self.bubble_sort(self.list1)

            if ready:
                break

    def partition(self, arr, low, high):
        i = (low-1)         # index of smaller element
        pivot = arr[high]     # pivot
     
        for j in range(low, high):
     
            # If current element is smaller than or
            # equal to pivot
            if arr[j] <= pivot:
     
                # increment index of smaller element
                i = i+1
                arr[i], arr[j] = arr[j], arr[i]
     
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return (i+1)
     
    def quickSort(self, arr, low, high):
        self.display_values()

        if len(arr) == 1:
            return arr

        if low < high:
            pi = self.partition(self.list1, low, high)
     
            self.quickSort(self.list1, low, pi-1)
            self.quickSort(self.list1, pi+1, high)
     
    def start_sort(self):
        ## quick sort
        self.t = threading.Thread(target=self.quickSort, args=[self.list1, 0, len(self.list1)-1])
        
        ## bubble sort
        #self.t = threading.Thread(target=self.bubble_sort_main)
        self.t.start()

if __name__ == "__main__":
    # pygame
    graph = Graph(1_000, 1000, 600)
    graph.start_sort()
    graph.show()
