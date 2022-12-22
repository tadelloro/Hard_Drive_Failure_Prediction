import matplotlib.pyplot as plt

def nboxplot(df, cols, title):
    """
    Boxplot of features.
    
    Parameters:
        df: Dataframe.
        cols: Columns within dataframe containing data to be plotted.

    Returns: 
        Boxplot figure.
    """
    
    plt.figure(figsize=(15, 3))
    boxplot = plt.boxplot(df[cols], 
                vert=True, 
                notch=False, 
                labels=cols,
                patch_artist=True, 
                showfliers=False, 
                  )

    cm = plt.cm.get_cmap('rainbow')
    colors = [cm(val/len(cols)) for val in range(len(cols))]
    for patch, color in zip(boxplot['boxes'], colors):
        patch.set_facecolor(color)

    plt.xticks(rotation=60)
    #plt.xlabel('Feature')
    plt.ylabel('Distribution')
    plt.title(title)
    plt.show()



def catbar(height, title):
    x = [0, 1, 2, 3]
    # categories
    plt.figure(figsize=(5, 4.3))
    plt.bar(x=x, height=height, edgecolor='k', alpha=0.7, color=['tab:red', 'tab:blue', 'tab:green', 'tab:orange'], label=x)
    plt.xticks(x)
    plt.xlabel('Category')
    plt.ylabel('Count')
    plt.legend()
    plt.title(title)
    plt.show()
    
    
    
def sctrmtrx(df, pairs, m, n):
    """
    Creates an m x n grid of scatter plots of selected columns. The number of column pairs must be equal to m x n.
    
    Parameters:
        df: Dataframe containing the columns to plot.
        pairs: Names of pairs of columns to plot.
        m: number of rows of scatter plots
        n: number of columns of scatter plots.

    Returns: 
        m x n Scatter plot figure.
    """
    colormap = {0:'tab:red', 1:'tab:blue', 2:'tab:green', 3:'tab:orange'}
    fig, ax = plt.subplots(m, n, figsize=(15, 18))
    d = dict(zip([(x, y) for x in range(0,m) for y in range(0,n)], pairs))
    for k, p in d.items():
        ax[k[0]][k[1]].scatter(df[p[0]], df[p[1]], c=df['category'].map(colormap) , s=25, alpha=0.5, edgecolor='k', linewidth=0.5)
        ax[k[0]][k[1]].set_xlabel(p[0])
        ax[k[0]][k[1]].set_ylabel(p[1])
        # ax[k[0]][k[1]].set_xlim(-3, 3)
        # ax[k[0]][k[1]].set_ylim(-3, 3)
            
    #plt.suptitle('Feature Scatter Plots', size=12)
    plt.tight_layout()
    plt.show()