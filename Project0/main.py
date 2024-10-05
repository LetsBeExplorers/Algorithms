import matplotlib.pyplot as plt
import numpy as np


# functions for Deliverable 1
def f1(n):
  return 0.5 * n * (n - 1) + 10


def g1(n):
  return n**2


# functions for Deliverable 3
def f2(n):
  return np.sqrt(n**5 + 3 * n + 1)


def g2(n):
  return 5 * n**2


# functions for Deliverable 4
def f3(n):
  return np.log(n)


def g3(n):
  return np.sqrt(n)


# functions for Deliverable 5
def f4(n):
  return np.log2(n)


def g4(n):
  return np.log10(n)


# Generate n ranges
n1 = np.arange(1, 11, 0.25)
n2 = np.arange(1, 10**6 + 1, 0.5)
n3 = np.arange(2, 11, 0.25)
n4 = np.arange(2, 10**6 + 1, 0.5)


# Function to save plots
def save_plot(x,
              y1,
              y2,
              filename,
              xlabel='n',
              ylabel='Function values',
              title='',
              labels=('f(n)', 'g(n)')):
  plt.figure(figsize=(10, 6))
  plt.plot(x, y1, label=labels[0])
  plt.plot(x, y2, label=labels[1])
  plt.title(title)
  plt.xlabel(xlabel)
  plt.ylabel(ylabel)
  plt.legend()
  plt.grid(True)
  plt.savefig(filename)
  plt.close()


def save_ratio_plot(x, y1, y2, filename, xlabel='n', ylabel='Ratio', title=''):
  plt.figure(figsize=(10, 6))
  plt.plot(x, y1 / y2, label='f(n) / g(n)')
  plt.title(title)
  plt.xlabel(xlabel)
  plt.ylabel(ylabel)
  plt.legend()
  plt.grid(True)
  plt.savefig(filename)
  plt.close()


# Deliverable 1
save_plot(n1,
          f1(n1),
          g1(n1),
          'plot_deliverable1_smalln.png',
          title='Deliverable 1: Small n',
          labels=('f(n) = 0.5n(n - 1) + 10', 'g(n) = n^2'))
save_plot(n2,
          f1(n2),
          g1(n2),
          'plot_deliverable1_largen.png',
          title='Deliverable 1: Large n',
          labels=('f(n) = 0.5n(n - 1) + 10', 'g(n) = n^2'))

# Deliverable 2
save_ratio_plot(n1,
                f1(n1),
                f2(n1),
                'plot_deliverable2_ratio_smalln.png',
                title='Deliverable 2: Ratio f(n)/g(n) - Small n')
save_ratio_plot(n2,
                f1(n2),
                g1(n2),
                'plot_deliverable2_ratio_largen.png',
                title='Deliverable 2: Ratio f(n)/g(n) - Large n')

# Deliverable 3
save_plot(n1,
          f2(n1),
          g2(n1),
          'plot_deliverable3_smalln.png',
          title='Deliverable 3: Small n',
          labels=('f(n) = sqrt(n^5 + 3n + 1)', 'g(n) = 5n^2'))
save_plot(n2,
          f2(n2),
          g2(n2),
          'plot_deliverable3_largen.png',
          title='Deliverable 3: Large n',
          labels=('f(n) = sqrt(n^5 + 3n + 1)', 'g(n) = 5n^2'))
save_ratio_plot(n1,
                f2(n1),
                g2(n1),
                'plot_deliverable3_ratio_smalln.png',
                title='Deliverable 3: Ratio f(n)/g(n) - Small n')
save_ratio_plot(n2,
                f2(n2),
                g2(n2),
                'plot_deliverable3_ratio_largen.png',
                title='Deliverable 3: Ratio f(n)/g(n) - Large n')

# Deliverable 4
save_plot(n1,
          f3(n1),
          g3(n1),
          'plot_deliverable4_smalln.png',
          title='Deliverable 4: Small n',
          labels=('f(n) = log(n)', 'g(n) = sqrt(n)'))
save_plot(n2,
          f3(n2),
          g3(n2),
          'plot_deliverable4_largen.png',
          title='Deliverable 4: Large n',
          labels=('f(n) = log(n)', 'g(n) = sqrt(n)'))
save_ratio_plot(n1,
                f3(n1),
                g3(n1),
                'plot_deliverable4_ratio_smalln.png',
                title='Deliverable 4: Ratio f(n)/g(n) - Small n')
save_ratio_plot(n2,
                f3(n2),
                g3(n2),
                'plot_deliverable4_ratio_largen.png',
                title='Deliverable 4: Ratio f(n)/g(n) - Large n')

# Deliverable 5
save_plot(n1,
          f4(n1),
          g4(n1),
          'plot_deliverable5_smalln.png',
          title='Deliverable 5: Small n',
          labels=('f(n) = log2(n)', 'g(n) = log10(n)'))
save_plot(n2,
          f4(n2),
          g4(n2),
          'plot_deliverable5_largen.png',
          title='Deliverable 5: Large n',
          labels=('f(n) = log2(n)', 'g(n) = log10(n)'))
save_ratio_plot(n3,
                f4(n3),
                g4(n3),
                'plot_deliverable5_ratio_smalln.png',
                title='Deliverable 5: Ratio f(n)/g(n) - Small n')
save_ratio_plot(n4,
                f4(n4),
                g4(n4),
                'plot_deliverable5_ratio_largen.png',
                title='Deliverable 5: Ratio f(n)/g(n) - Large n')
