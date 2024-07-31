import requests
import datetime as dt

# Find your Token at following Url
# and set it as environment variable.
pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "XXXX"
TOKEN = "YYYY"
GRAPH_ID = "graph1"


def create_user_account():
    user_params = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }

    # POST
    response = requests.post(url=pixela_endpoint, json=user_params)
    print(response.text)


def create_graph_definition():
    graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

    graph_config = {
        "id": GRAPH_ID,
        "name": "Swimming",
        "unit": "hour",
        "type": "float",
        "color": "ajisai"
    }

    headers = {
        "X-USER-TOKEN": TOKEN
    }

    response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
    print(response.text)


def post_pixel_to_graph(date):
    post_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

    pixel_data = {
        "date": date.strftime("%Y%m%d"),
        "quantity": input(f"How many hours did you swim on {date.strftime("%Y-%m-%d")}? "),
    }

    headers = {
        "X-USER-TOKEN": TOKEN
    }

    response = requests.post(url=post_graph_endpoint, json=pixel_data, headers=headers)
    print(response.text)


def update_pixel_in_graph(date):
    update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date.strftime('%Y%m%d')}"

    new_pixel_data = {
        "quantity": input(f"Enter your new hours you've swam on {date.strftime("%Y-%m-%d")}? ")
    }

    headers = {
        "X-USER-TOKEN": TOKEN
    }

    # PUT
    response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
    print(response.text)


def delete_pixel_from_graph(date):
    delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date.strftime('%Y%m%d')}"

    headers = {
        "X-USER-TOKEN": TOKEN
    }

    # DELETE
    response = requests.delete(url=delete_endpoint, headers=headers)
    print(response.text)


# create_user_account()
# create_graph_definition()

# Now, you can see your graph via: https://pixe.la/v1/users/[USERNAME]/graphs/[GRAPH_ID].html
#  https://pixe.la/v1/users/mnsoureh76/graphs/graph1.html

today = dt.datetime.now()
yesterday = dt.datetime.now() - dt.timedelta(days=1)
before_yesterday = dt.datetime.now() - dt.timedelta(days=2)

# post_pixel_to_graph(date=today)
# post_pixel_to_graph(date=yesterday)
# post_pixel_to_graph(date=before_yesterday)

# update_pixel_in_graph(yesterday)

# delete_pixel_from_graph(yesterday)
