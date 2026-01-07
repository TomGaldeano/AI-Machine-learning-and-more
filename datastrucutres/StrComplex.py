import time
import matplotlib.pyplot as plt
"""
Devise an experiment to discover the complexity of comparing strings in Python.
Does the size of the string affect the efficiency of the string comparison and if so,
what is the complexity of the comparison? In this experiment you might want to
consider a best case, worst case, and average case complexity plot the average times
"""
short = "hello world " * 3
medium = "hello world " * 300
long = "hello world " * 3000

def compare_strings(repeats=1000):
    sizes = []
    avg_times = []
    for s in (short, medium, long):
        run_times = []
        for _ in range(repeats):
            start = time.perf_counter()
            _ = (s == s)
            end = time.perf_counter()
            time.sleep(.01)  # Allow system to settle
            run_times.append((end - start) * 1e6)
        sizes.append(len(s))
        avg_times.append(sum(run_times) / len(run_times))
    return sizes, avg_times

def plot_string_comparison():
    sizes, times = compare_strings()
    plt.plot(sizes, times, marker='o')
    plt.xlabel("String Length (characters)")
    plt.ylabel("Average Comparison Time (microseconds)")
    plt.title("String Comparison Time vs String Length")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    plot_string_comparison()