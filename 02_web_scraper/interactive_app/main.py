import random
import requests
from bs4 import BeautifulSoup

URL = "https://www.imdb.com/chart/top"
HTML_PARSER = "html.parser"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                  " AppleWebKit/537.36 (KHTML, like Gecko)"
                  " Chrome/114.0.0.0 Safari/537.36"
}

DIV_CLI_TITLE = "div.cli-title"
SPAN_CLI_TITLE_META_DATA_ITEM = "div.cli-title-metadata span.cli-title-metadata-item"
SPAN_IPC_RATING = "span.ipc-rating-star--rating"
H3_IPC_TITLE_TEXT = "h3.ipc-title__text"
NA_STR = "N/A"


def get_title(div):
    title_tag = div.select_one(H3_IPC_TITLE_TEXT)
    title = title_tag.text.strip() if title_tag else NA_STR
    return title


def get_year(i: int, metadata_spans) -> str:
    year = metadata_spans[i * 3].text.strip() if i * 3 < len(metadata_spans) else NA_STR
    return year


def get_rating(i, rating_spans):
    rating = rating_spans[i].text.strip() if i < len(rating_spans) else NA_STR
    return rating


def main():
    """Main function."""
    response = requests.get(url=URL, headers=HEADERS)
    soup = BeautifulSoup(response.text, HTML_PARSER)
    # print(soup.prettify())

    movie_divs = soup.select(DIV_CLI_TITLE)
    metadata_spans = soup.select(SPAN_CLI_TITLE_META_DATA_ITEM)
    rating_spans = soup.select(SPAN_IPC_RATING)

    titles = []
    years = []
    ratings = []

    for i, div in enumerate(movie_divs):
        title = get_title(div)
        titles.append(title)

        year = get_year(i, metadata_spans)
        years.append(year)

        rating = get_rating(i, rating_spans)
        ratings.append(rating)

    # Example output
    # for title, year, rating in zip(titles, years, ratings):
    #     print(f"{title} ({year}) - Rating: {rating}")

    n_movies = len(titles)

    while True:
        idx = random.randrange(0, n_movies)

        print("{} ({}), Rating: {}".format(
            titles[idx], years[idx], ratings[idx],
        ))

        user_input = input("Would you like to select another movie (y/[n])?")
        if user_input.lower() != "y":
            break


if __name__ == "__main__":
    main()
