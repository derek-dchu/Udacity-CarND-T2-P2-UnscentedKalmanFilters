"""
A helper script to generate simple analysis on NIS log
"""

import matplotlib.pyplot as plt
import matplotlib.transforms as transforms


def main():
    nis = []
    with open('NIS.log') as nis_log:
        nis = [float(l) for l in nis_log.readlines()][1:]

    c = 0
    for n in nis:
        if 0.35 <= n <= 7.81:
            c += 1
    res = c / len(nis) * 100

    _, ax = plt.subplots()
    ax.plot(range(1, len(nis)+1), nis)
    ax.set_title("{0:.2f}% NIS are between 0.35 and 7.81".format(res))
    ax.set_xlabel('Step')
    ax.set_ylabel('NIS')
    ax.axhline(0.35, color='r')
    ax.axhline(7.81, color='r')

    trans = transforms.blended_transform_factory(ax.get_yticklabels()[0].get_transform(), ax.transData)
    ax.text(0, 0.35, "{:.2f}".format(0.35), color='r', transform=trans, ha="right", va="center")
    ax.text(0, 7.81, "{:.2f}".format(7.81), color='r', transform=trans, ha="right", va="center")

    plt.show()


if __name__ == '__main__':
    main()
