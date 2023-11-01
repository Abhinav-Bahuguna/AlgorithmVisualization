from manim import *

def binarySearch(arr, target):
    
    steps = []

    left , right, mid = 0, len(arr) -1, -1

    while( left < right ):

        mid = (left + right) // 2
        steps.append((left, right, mid))

        if arr[mid] < target :
            left = mid + 1
        elif  arr[mid] > target :
            right = right - 1
        else:
            return (steps, mid)

    steps.append((left, right, mid))
    return (steps, -1)

def linearSearch(arr, target):
    
    steps = []

    for idx, value in enumerate(arr):
        if value == target:
            return (steps, idx)
        steps.append(idx)

    return (steps, -1)


class BinarySearchViz(Scene):
    def construct(self):

        arr = [ 2, 5, 10, 12, 15, 30, 40, 50, 55, 56, 57, 90, 100 ]
        max_value = max(arr)
        steps, idx = binarySearch(arr, 48)

        rects = [ Rectangle(height=(value/max_value) * 4, width=0.1, color=PINK, fill_color=PINK, fill_opacity=1) for value in arr ]
        v_group = Group(*rects).arrange(buff=0.15, aligned_edge=DOWN)

        self.add(v_group)

        for (left, right, mid) in steps:
            # highlight left, right, and mid
            self.play(rects[left].animate.set_color(GREEN), rects[right].animate.set_color(GREEN), rects[mid].animate.set_color(RED), runtime=10)
            # revert highlight
            self.play(rects[left].animate.set_color(PINK), rects[right].animate.set_color(PINK), rects[mid].animate.set_color(PINK), runtime=0.5)

        if idx != -1 :
            self.play(Indicate(rects[idx], run_time=5))

        self.wait(4)


class LinearSearchViz(Scene):
    def construct(self):

        arr = [ 2, 5, 10, 12, 15, 30, 40, 50, 55, 56, 57, 90, 100 ]
        max_value = max(arr)
        steps, idx = linearSearch(arr, 55)

        print(steps)

        rects = [ Rectangle(height=(value/max_value) * 4, width=0.1, color=PINK, fill_color=PINK, fill_opacity=1) for value in arr ]
        v_group = Group(*rects).arrange(buff=0.15, aligned_edge=DOWN)

        self.add(v_group)

        for step in steps:
            self.play(rects[step].animate.set_color(GREEN))
            self.play(rects[step].animate.set_color(PINK))

        if idx != -1 :
            self.play(Indicate(rects[idx]))

        self.wait(4)

if __name__ == "__main__":

    steps, idx = binarySearch([ x for x in range(10, 50) ], 48)


