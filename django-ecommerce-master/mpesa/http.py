import requests


def post(url, headers, data):
    """
    Post a request to a given url
    :param url:
    :param headers:
    :param data:
    :return:
    """
    request = requests.post(url=url, headers=headers, json=data)

    return request


def get(url, auth):
    """
    Send a GET Request
    :param url:
    :param headers:
    :return:
    """
    request = requests.get(url=url,auth=auth)

    return request
