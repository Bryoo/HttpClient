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
        'userId': user_id,
        'id': post_id,
        'title': title,
        'body': body,
    })


def main():
    print("This is a simple http client to view or update posts")
    print('='*10)
    print("View Post")
    print('=' * 10)
    num = input("Which post number do you want to see : ")

    if num.isdigit():
        num = int(num)
    get_post = describe_post(num)

    if get_post.status_code != 200:
        raise ApiError('Cannot get the post: {}'.format(get_post.status_code))

    print("Post requested. \n ID: {}\n Title: {}\n Body: {}".format(get_post.json()["id"],
                                                                    get_post.json()["title"],
                                                                    get_post.json()["body"]
                                                                    )
          )

    print("Now lets add a post: ")
    print('='*10)
    print("Add Post")
    print('=' * 10)

    title = input("Give your post a title ")
    body = input("Give your post a body")

    add = add_post(title, body)
    if add.status_code != 201:
        raise ApiError('Cannot create post: {}'.format(add.status_code))
    print("Post added. \n ID: {}\n Title: {}\n Body: {}".format(add.json()["id"],
                                                                add.json()["title"],
                                                                add.json()["body"]
                                                                )
          )

if __name__ == '__main__':
    main()
