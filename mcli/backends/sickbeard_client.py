import requests
import logging


logger = logging.getLogger('media-cli')


def create_req(sb_config, api_cmd):
    request_url = "{}/api/{}/{}".format(sb_config['server_url'], sb_config['api_key'], api_cmd)
    return request_url


def format_data(data, type):
    output = []
    if type == 'upcoming':
        for i in data:
            line = '{} - {} - {} - S{}E{} - {}'.format(
                i['airdate'],
                i['airs'],
                i['show_name'],
                i['season'],
                i['episode'],
                i['ep_name'])
            output.append(line)
    elif type == 'history':
        for i in data:
            line = '{} - {} - S{}E{} - {}'.format(
                i['date'],
                i['show_name'],
                i['season'],
                i['episode'],
                i['status']
            )
            output.append(line)
    return output


def fetch_data(sb_config, api_cmd):
    try:
        response = requests.get(create_req(sb_config, api_cmd), timeout=(5, 120))
    except (requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout):
        logger.exception("Timeout querying Sickbeard for data")
        return []
    if response.status_code != requests.codes.ok:
        logger.error("Error querying Sickbeard for  data: %s", response.text)
        return []
    else:
        return response.json()['data']


def upcoming(sb_config):
    api_cmd = 'future?type=soon&sort=date'
    logger.info("Fetching Upcoming(Soon)...")
    data = fetch_data(sb_config, api_cmd)
    output = format_data(data['soon'], 'upcoming')
    for i in output:
        print(i)


def history(sb_config):
    api_cmd = 'history?limit=25&sort=date'
    logger.info("Fetching History...")
    data = fetch_data(sb_config, api_cmd)
    output = format_data(data, 'history')
    for i in output:
        print(i)
