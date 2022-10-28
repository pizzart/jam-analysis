import request
import parse_html
import gui
import plot
from PySimpleGUI import easy_print, easy_print_close
# import json


def main():
    params = gui.gui_main()

    if params == None:
        return

    username: str = params['username'].strip()
    scale: float = params['scale']

    if 'ldjam.com' in username:
        username = username.split('/')[4]
    elif len(username) == 0:
        return

    # request.init()
    easy_print(
        f'requesting user\'s games page: {"https://ldjam.com/users/"+username+"/games"}')
    main_page = request.req_main_page(username)
    easy_print('parsing links and full username')
    links, proper_username = parse_html.get_links_and_name(main_page)
    easy_print(f'full username: {proper_username}')
    easy_print('requesting game pages')
    pages, nums = request.req_game_pages(links)
    # stat_pages = request.req_stat_pages(nums)
    # lowest_submission_amount = parse_html.get_lowest_submission_amount(stat_pages)
    easy_print('parsing results')
    results = parse_html.get_results(pages)
    # with open(f'{username}.json', 'w+') as res:
    #     json.dump(results, res)

    # with open(f'{username}.json', 'r') as f:
    # results = json.load(f)
    easy_print_close()
    plot.make_plot(results, nums, proper_username, scale)


if __name__ == "__main__":
    main()
