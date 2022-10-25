import request
import parse_html
import plot
import json


def main():
    # parse_html.parse_games_page(request.req_games_page())
    # with open('games.html', 'r') as f:
    #     text = f.read()
    #     links = parse_html.get_game_links(text)
    #     pages = request.req_game_pages(links)
    #     results = parse_html.get_game_results(pages)
    #     with open('results.json', 'w+') as res:
    #         json.dump(results, res)
    with open('results.json', 'r') as f:
        results = json.load(f)
        plot.make_plot(results)
        # print(results)


if __name__ == "__main__":
    main()
