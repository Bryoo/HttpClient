import requests

main_api = ""


def _url(path):
    return 'https://jsonplaceholder.typicode.com' + path


def get_posts():
    resp = requests.get(_url('/posts/'))
    if resp.status_code != 200:
        # This means something went wrong.
        raise ApiError('GET /posts/ {}'.format(resp.status_code))

    for post in resp.json():
        print('{} {}'.format(post['id'], post['title']))


def describe_post(post_id):
    return requests.get(_url('/posts/{:d}'.format(post_id)))


def add_post(title, body, user_id=10):
    return requests.post(_url('/posts/'), json={
        'user_id': user_id,
        'title': title,
        'body': body,
        })


def update_post(title, body, post_id, user_id=10):
    return requests.put(_url('/posts/:id'), json={
        'user_id': user_id,
        'id': post_id,
        'title': title,
        'body': body,
    })


def main():
    print("This is a simple http client to view or update posts")

    input()

    get_r = describe_post(2)
    print(get_r.text)

    added = add_post("le jore denarera", "This is the body", )
    if added.status_code != 201:
        raise ApiError('Cannot create post: {}'.format(added.status_code))
    print('Created task. ID: {}'.format(added.json()["id"]))


# print('{} {}' .format(added['post_id'], added['title']))
