import matplotlib.pyplot as plt
import io


def generate_dashboard(avg_prices, avg_sales):
    max_price = max(avg_prices)
    max_sales = max(avg_sales)

    plt.subplot(2, 1, 1)
    plt.plot(avg_sales, 'r-o')
    plt.title('Средняя цена по месяцам')
    plt.xlabel('Месяц')
    plt.ylabel('Продажи')
    plt.ylim([0, max_price])

    plt.subplot(2, 1, 2)
    plt.plot(avg_prices, 'b-o')
    plt.title('Средние продажи по месяцам')
    plt.xlabel('Месяц')
    plt.ylabel('Цена')
    plt.ylim([0, max_sales])

    plt.tight_layout()
    fig = plt.gcf()
    fig.canvas.draw()
    image_data = io.BytesIO()
    fig.savefig(image_data, format='png')
    image_data.seek(0)
    plt.clf()
    plt.close(fig)
    return image_data
