import requests


class HTTP:
    @staticmethod
    def get(url, return_json=True):
        """
        get the content from http
        :param url:
        :param return_json:
        :return:
        """
        r = requests.get(url)
        # if searched book not found
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text

