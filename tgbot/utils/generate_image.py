import io
import matplotlib.pyplot as plt
import numpy as np


def generate_dashboard(avg_prices, avg_sales):
    max_price = max(avg_prices)
    max_sales = max(avg_sales)

    # Use a custom color palette
    colors = plt.cm.Set2(np.linspace(0, 1, 8))

    # Create the subplots
    fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(8, 8))

    # Plot the sales data
    ax[0].plot(avg_sales, marker='o', markersize=7, color=colors[0])
    ax[0].set_title('Средние продажи по месяцам', fontsize=16, fontweight='bold')
    ax[0].set_xlabel('Месяц', fontsize=14)
    ax[0].set_ylabel('Продажи', fontsize=14)
    ax[0].set_ylim([0, max_sales])

    # Plot the price data
    ax[1].plot(avg_prices, marker='o', markersize=7, color=colors[1])
    ax[1].set_title('Средняя цена по месяцам', fontsize=16, fontweight='bold')
    ax[1].set_xlabel('Месяц', fontsize=14)
    ax[1].set_ylabel('Цена ', fontsize=14)
    ax[1].set_ylim([0, max_price])

    # Customize the tick labels and grid lines
    for ax in fig.axes:
        ax.tick_params(labelsize=12)
        ax.grid(linestyle=':', linewidth=0.5, color='gray')

    # Set the layout and generate a PNG image
    fig.tight_layout()
    image_data = io.BytesIO()
    fig.savefig(image_data, format='png')
    image_data.seek(0)
    plt.close(fig)
    return image_data
