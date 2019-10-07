import pandas as pd 
import matplotlib.pyplot as plt
from math import ceil

def plot(dataframes):

#~~~~~~~~~~~~~~~~~~~~~~~~~~~ PLOT 1 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    labels = ['2-Coev', '2-Coev-RS', '1-Coev-RS', '1-Coev', '1-Evol-RS']
    colors = ['b', 'g', 'r', 'c', 'm']
    markers = ['o', 'v', 'D', 's', 'd']
    
    ax1 = plt.subplot(1, 2, 1)
    ax2 = ax1.twiny()
    legend = []
    for idx, df in enumerate(dataframes):
        df['effort'] = df['effort'] / 1000
        l = ax1.plot(df['effort'], df['avg'], color=colors[idx],
                    label=labels[idx], marker=markers[idx], markevery=32,
                    linewidth=0.8, markeredgecolor='black')
        legend += l

    ax1.set_xlabel('Rozegranych gier (×1000)')
    ax1.set_ylabel('Odsetek wygranych gier [%]')
    ax2.set_xlabel('Pokolenie')

    ax1.set_xlim([0, 500])
    ax1.set_ylim([60, 100])

    x_ticks = [x for x in range(0, ceil(dataframes[0]['effort'].max() + 1), 100)]
    ax1.set_xticks(x_ticks)
    ax1.tick_params(direction='in')

    ax2.set_xlim(ax1.get_xlim())
    ax2.set_xticks(x_ticks)
    ax2.set_xticklabels([x * 40 for x in range(6)])
    ax2.tick_params(direction='in')    

    ax1.grid(True, linestyle='--')

    legend_labels = [l.get_label() for l in legend]

    ax1.legend(legend, legend_labels, loc='lower right', numpoints=2,
                fancybox=False, edgecolor='black')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~ PLOT 2 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    ax3 = plt.subplot(1, 2, 2)
    data = list()
    for df in dataframes:
        data.append(df['avg'])

    flierprops = dict(marker="+", markeredgecolor='blue')
    bp = ax3.boxplot(data, notch=True, flierprops=flierprops, showmeans=True)
    plt.setp(bp['boxes'], color='blue')
    plt.setp(bp['whiskers'], color='blue', linestyle='--')
    plt.setp(bp['caps'], color='black')
    plt.setp(bp['medians'], color='red')
    plt.setp(bp['means'], markeredgecolor='black', marker='o', markerfacecolor='blue')

    ax3.yaxis.tick_right()

    ax3.set_xticklabels(labels, rotation=22)
    ax3.tick_params(
        direction='in'
    )
    ax3.grid(True, linestyle='--')

    
    plt.savefig('wykres.png')


def clean_data(df):
    df['avg'] = df.mean(axis=1) * 100
    return df

def main():
    pd_2cel = pd.read_csv('2cel.csv')
    pd_2cel_rs = pd.read_csv('2cel-rs.csv')
    pd_cel_rs = pd.read_csv('cel-rs.csv')
    pd_cel = pd.read_csv('cel.csv')
    pd_rsel = pd.read_csv('rsel.csv')

    dataframes = [pd_2cel, pd_2cel_rs, pd_cel_rs, pd_cel, pd_rsel]
    for idx, df in enumerate(dataframes):
        generation, effort = df['generation'], df['effort']
        df = df.drop(['generation', 'effort'], axis=1)
        df = clean_data(df)
        df = pd.concat([generation, effort, df['avg']], axis=1)
        dataframes[idx] = df

    plot(dataframes)


if __name__ == '__main__':
    main()
