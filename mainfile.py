import httpclient

def user_get_post():
    print('='*20)
    print("View Post")
    print('=' * 20)
    num = input("Which post number do you want to see : ")

    if num.isdigit():
        num = int(num)
    get_post = httpclient.describe_post(num)

    if get_post.status_code != 200:
        raise ApiError('Cannot get the post: {}'.format(get_post.status_code))

    print("Post requested. \n ID: {}\n Title: {}\n Body: {}".format(get_post.json()["id"],
                                                                    get_post.json()["title"],
                                                                    get_post.json()["body"]
                                                                    )
          )


def user_add_post():
    print("Now lets add a post: ")
    print('='*10)
    print("Add Post")
    print('=' * 10)

    title = input("Give your post a title ")
    body = input("Give your post a body")

    add = httpclient.add_post(title, body)
    if add.status_code != 201:
        raise ApiError('Cannot create post: {}'.format(add.status_code))
    print("Post added. \n ID: {}\n Title: {}\n Body: {}".format(add.json()["id"],
                                                                add.json()["title"],
                                                                add.json()["body"]
                                                                )
          )


def user_update_post():
    print("Now lets update a post: ")
    print('='*10)
    print("Update Post")
    print('=' * 10)
    title = input("update title ")
    body = input("update body")

    update = httpclient.update_post(title, body)

    print(update.status_code)

    if update.status_code != 200:
        if update.status_code == 404:
            raise Exception('Cannot find post: {}'.format(update.status_code))
        else:
            raise Exception('No permissions to update post: '.format(update.status_code))

    print("Post updated. \n ID: {}\n Title: {}\n Body: {}".format(update.json()["id"],
                                                                  update.json()["title"],
                                                                  update.json()["body"]
                                                                 )
          )


def main():
    print("This is a simple http client to view or update posts")


    user_get_post()

    user_add_post()

    user_update_post()

if __name__ == '__main__':
    main()
