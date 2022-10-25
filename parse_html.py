from bs4 import BeautifulSoup


def get_game_links(content: str):
    soup = BeautifulSoup(content, 'html.parser')
    boxes = soup.find_all(class_='-col')
    links = []
    for box in boxes:
        links.append(box.a['href'])
    return links


def get_game_results(content_list: list):
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
