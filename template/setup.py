#!/usr/bin/env python3

import argparse
import base64
import errno
import getpass
import os
import requests
import subprocess
import sys

ARTIFACTORY_URL = "https://artifactory.my-org.com/artifactory/api/security/apiKey"
ARTIFACTORY_DOCKER_REPO_URL = "docker.artifactory.my-org.com"
ARTIFACTORY_NPM_REGISTRY="artifactory.my-org.com/artifactory/api/npm"


def get_auth():
    # check if those variables exist
    user = os.getenv("ARTIFACTORY_USER", None)
    password = os.getenv("ARTIFACTORY_PASS", None)

    if user is None or password is None:
        user = input("UserName: ")
        password = getpass.getpass()
    return (user, password)


def check_response_result(response):
    resp_value = response.json()

    if response.status_code not in [200, 201]:
        resp_value = response.json()
        print("Error: {} {}".format(response.status_code,
              resp_value['errors'][0]['message']), file=sys.stderr)
        sys.exit(1)

    return resp_value.get("apiKey", None)


def write_api_key(filename, apikey):
    with open(filename, "w+") as fid:
        fid.write("{}\n".format(apikey))


def check_file_exists(filename):
    return (os.path.isfile(filename))


def request_api_key(url, auth):
    response = requests.get(url, auth=auth)
    return check_response_result(response)


def write_api_key_npmrc(path, user, api_key):
    # encode username and api-key with base 64
    input_string = "{username}:{api_key}".format(
        username=user, api_key=api_key)
    input_bytes = input_string.encode("ascii")
    base64_bytes = base64.b64encode(input_bytes)
    base64_string = base64_bytes.decode("ascii")

    file_path = "{path}/.env".format(path=path)

    with open(file_path, "a+") as fid:
      fid.write("export NPM_AUTH_TOKEN={auth}\n".format(auth=base64_string))


def docker_login(repo_url, user, api_key):
    cmd = "echo {api_key} | docker login -u {user} --password-stdin {url}".format(
        user=user, api_key=api_key, url=repo_url)
    subprocess.run(cmd, shell=True)

parser = argparse.ArgumentParser()
parser.add_argument("-r", "--refresh", help="refresh the login",
                    default=False, required=False, action="store_true")
args = parser.parse_args()

base_path = os.path.expanduser("~")

if (args.refresh is True):
    try:
        os.remove("{path}/.api_key".format(path=base_path))
    except OSError as e:
        if e.errno != errno.ENOENT:  # only ignore the error if file does not exist
            raise

if (check_file_exists("{path}/.api_key".format(path=base_path))):
    print("API-Key File found. Doing nothing.")
    sys.exit(0)

auth = get_auth()
api_key = request_api_key(ARTIFACTORY_URL, auth)

write_api_key_npmrc(base_path, auth[0], api_key)
docker_login(ARTIFACTORY_DOCKER_REPO_URL, auth[0], api_key)
write_api_key("{path}/.api_key".format(path=base_path), api_key)
