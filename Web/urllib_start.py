# Using urllib to request data
# TODO: import urllib request class
import urllib.request

def main():
    # URL to retrieve sample data from
    url = "http://httpbin.org/xml"
    # Issue request with data params as part of the url
    result = urllib.request.urlopen(url)

    print("Result code: {0}".format(result.status))

    print("Headers: ----------------------")
    print(result.getheaders())

    print("Returned data: ----------------")
    print(result.read().decode('utf-8'))


if __name__ == "__main__":
    main()