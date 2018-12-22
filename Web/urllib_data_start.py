# Send data to a server using urllib
# TODO: import urllib request and parse modules
import urllib.request
import urllib.parse

def main():
    # URL to retrieve sample data from
    url = "http://httpbin.org/get"

    # TODO: create some data to pass to the GET request

    args = {
        "name": "David Liceaga",
        "is_author": True
    }

    # TODO: data needs to be url-encoded before passing as arguments

    data = urllib.parse.urlencode(args)

    # TODO: issue request with data params as part of the url

    #result = urllib.request.urlopen(url + "?" + data)

    # TODO: issue request with a data parameter to use POST
    url = "http://httpbin.org/post"
    data = data.encode()
    result = urllib.request.urlopen(url, data=data)

    print("Result code: {0}".format(result.status))
    print("Returned data: ----------------")
    print(result.read().decode('utf-8'))


if __name__ == "__main__":
    main()