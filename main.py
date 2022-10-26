import request
import parse_html
# import gui
import plot
import json


def main():
    username = input('username (as shown in the url): ')

    # request.init()
    main_page = request.req_main_page(username)
    links, proper_username = parse_html.get_links_and_name(main_page)
    pages, nums = request.req_game_pages(links)
    stat_pages = request.req_stat_pages(nums)
    lowest_submission_amount = parse_html.get_lowest_submission_amount(
        stat_pages)
    results = parse_html.get_results(pages)
    # with open(f'{username}.json', 'w+') as res:
    #     json.dump(results, res)

    # with open(f'{username}.json', 'r') as f:
    # results = json.load(f)
    plot.make_plot(results, nums, lowest_submission_amount, proper_username)


if __name__ == "__main__":
    main()
