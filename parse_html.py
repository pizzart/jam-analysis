from bs4 import BeautifulSoup


def get_links_and_name(content: str):
    soup = BeautifulSoup(content, 'html.parser')
    boxes = soup.find_all(class_='-col')
    links = []
    for box in boxes:
        links.append(box.a['href'])
    username = soup.find('span', class_='-main').get_text()
    return (links, username)


def get_results(content_list: list):
    results_list = {}

    for content in content_list:
        soup = BeautifulSoup(content, 'html.parser')
        grades = soup.find_all(class_='-grade')

        results = {
            # 'Overall': {
            #     'place': 0,
            #     'rating': 0,
            #     'amount': 0,
            # }
        }

        for grade in grades:
            title = grade.span.get_text()[:-1].lower()
            try:
                place = int(grade.strong.get_text())
            except:
                pass
            stats = grade.get_text().split('(')[1].split(' ')
            rating = float(stats[0])
            amount = int(stats[3])
            results[title] = {'place': place,
                              'rating': rating, 'amount': amount}

        game_name = soup.find('a', class_='-text').get_text()
        results_list[game_name] = results

    return results_list


def get_lowest_submission_amount(stat_pages: list):
    submission_amounts = []

    for content in stat_pages:
        soup = BeautifulSoup(content, 'html.parser')
        amount = soup.find('span', class_='-value -title').get_text()
        submission_amounts.append(int(amount))

    return max(submission_amounts)
