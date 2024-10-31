import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk


def f1(x):
    return 1 / np.sqrt(2 * x ** 2 + 1)


def f2(x):
    return np.log10(x + 2) / x


def f3(x):
    return 1 / np.sqrt(x ** 2 + 2.3)


def rectangle_method(f, lower_bound, upper_bound, num_intervals, method='middle'):
    h = (upper_bound - lower_bound) / num_intervals
    sum_ = 0.0
    match method:
        case 'left':
            for i in range(num_intervals):
                x = lower_bound + i * h
                sum_ += f(x)
        case 'right':
            for i in range(1, num_intervals + 1):
                x = lower_bound + i * h
                sum_ += f(x)
        case 'middle':
            for i in range(num_intervals):
                x = lower_bound + h * (i + 0.5)
                sum_ += f(x)
        case default:
            return "There is no such method"
    return sum_ * h


def simpsons_rule(f, lower_bound, upper_bound, num_intervals):
    if num_intervals % 2 != 0:
        raise ValueError("num_intervals must be even for Simpson's rule")
    dx = (upper_bound - lower_bound) / num_intervals
    result = f(lower_bound) + f(upper_bound)
    for i in range(1, num_intervals, 2):
        result += 4 * f(lower_bound + i * dx)
    for i in range(2, num_intervals - 1, 2):
        result += 2 * f(lower_bound + i * dx)
    result *= dx / 3
    return result


def trapezoidal_rule(f, lower_bound, upper_bound, num_intervals):
    dx = (upper_bound - lower_bound) / num_intervals
    result = 0.5 * (f(lower_bound) + f(upper_bound))
    result += sum(f(lower_bound + i * dx) for i in range(1, num_intervals))
    result *= dx
    return result


def plot_function(f, lower_bound, upper_bound, title):
    x = np.linspace(lower_bound, upper_bound, 400)
    y = f(x)

    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label=title)
    plt.title(f"Plot of {title}")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.legend()
    plt.show()


def calculate_integral_1():
    try:
        lower_bound = float(lower_bound1_entry.get())
        upper_bound = float(upper_bound1_entry.get())
        num_intervals = int(num_intervals1_entry.get())

        result_middle = rectangle_method(f1, lower_bound, upper_bound, num_intervals, method='middle')
        result_left = rectangle_method(f1, lower_bound, upper_bound, num_intervals, method='left')
        result_right = rectangle_method(f1, lower_bound, upper_bound, num_intervals, method='right')

        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END,
                            f"1st Integral Results:\n"
                            f"Midpoint Method: {result_middle:.4f}\n"
                            f"Left Method: {result_left:.4f}\n"
                            f"Right Method: {result_right:.4f}\n\n"
                            )
        plot_function(f1, lower_bound, upper_bound, "f1(x) = 1 / sqrt(2 * x^2 + 1)")
    except ValueError:
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END,
                            "Input error: Please enter valid numbers for lower_bound, upper_bound, and num_intervals.")


def calculate_integral_2():
    try:
        lower_bound = float(lower_bound2_entry.get())
        upper_bound = float(upper_bound2_entry.get())
        num_intervals = int(num_intervals2_entry.get())

        if num_intervals % 2 != 0:
            results_text.delete(1.0, tk.END)
            results_text.insert(tk.END, "Input error: num_intervals must be even for Simpson's rule.")
            return

        result = simpsons_rule(f2, lower_bound, upper_bound, num_intervals)
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, f"2nd Integral Result:\nSimpson's Rule: {result:.5f}\n\n")
        plot_function(f2, lower_bound, upper_bound, "f2(x) = log10(x + 2) / x")
    except ValueError:
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END,
                            "Input error: Please enter valid numbers for lower_bound, upper_bound, and num_intervals.")


def calculate_integral_3():
    try:
        lower_bound = float(lower_bound3_entry.get())
        upper_bound = float(upper_bound3_entry.get())
        num_intervals = int(num_intervals3_entry.get())

        result = trapezoidal_rule(f3, lower_bound, upper_bound, num_intervals)
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, f"3rd Integral Result:\nTrapezoidal Rule: {result:.5f}\n\n")
        plot_function(f3, lower_bound, upper_bound, "f3(x) = 1 / sqrt(x^2 + 2.3)")
    except ValueError:
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END,
                            "Input error: Please enter valid numbers for lower_bound, upper_bound, and num_intervals.")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Numerical Integration")

    frame1 = tk.Frame(root)
    frame1.pack(pady=10)

    tk.Label(frame1, text="1st Integral (Rectangle Method)").grid(row=0, columnspan=3)

    tk.Label(frame1, text="Lower Bound:").grid(row=1, column=0)
    lower_bound1_entry = tk.Entry(frame1)
    lower_bound1_entry.grid(row=1, column=1)

    tk.Label(frame1, text="Upper Bound:").grid(row=2, column=0)
    upper_bound1_entry = tk.Entry(frame1)
    upper_bound1_entry.grid(row=2, column=1)

    tk.Label(frame1, text="Number of Intervals:").grid(row=3, column=0)
    num_intervals1_entry = tk.Entry(frame1)
    num_intervals1_entry.grid(row=3, column=1)

    tk.Button(frame1, text="Calculate", command=calculate_integral_1).grid(row=4, columnspan=2)

    frame2 = tk.Frame(root)
    frame2.pack(pady=10)

    tk.Label(frame2, text="2nd Integral (Simpson's Rule)").grid(row=0, columnspan=3)

    tk.Label(frame2, text="Lower Bound:").grid(row=1, column=0)
    lower_bound2_entry = tk.Entry(frame2)
    lower_bound2_entry.grid(row=1, column=1)

    tk.Label(frame2, text="Upper Bound:").grid(row=2, column=0)
    upper_bound2_entry = tk.Entry(frame2)
    upper_bound2_entry.grid(row=2, column=1)

    tk.Label(frame2, text="Number of Intervals:").grid(row=3, column=0)
    num_intervals2_entry = tk.Entry(frame2)
    num_intervals2_entry.grid(row=3, column=1)

    tk.Button(frame2, text="Calculate", command=calculate_integral_2).grid(row=4, columnspan=2)

    frame3 = tk.Frame(root)
    frame3.pack(pady=10)

    tk.Label(frame3, text="3rd Integral (Trapezoidal Rule)").grid(row=0, columnspan=3)

    tk.Label(frame3, text="Lower Bound:").grid(row=1, column=0)
    lower_bound3_entry = tk.Entry(frame3)
    lower_bound3_entry.grid(row=1, column=1)

    tk.Label(frame3, text="Upper Bound:").grid(row=2, column=0)
    upper_bound3_entry = tk.Entry(frame3)
    upper_bound3_entry.grid(row=2, column=1)

    tk.Label(frame3, text="Number of Intervals:").grid(row=3, column=0)
    num_intervals3_entry = tk.Entry(frame3)
    num_intervals3_entry.grid(row=3, column=1)

    tk.Button(frame3, text="Calculate", command=calculate_integral_3).grid(row=4, columnspan=2)

    results_text = tk.Text(root, height=10, width=50)
    results_text.pack(pady=10)

    root.mainloop()
