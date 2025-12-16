import subprocess

IMAGE_NAME = "ramirez0000245/aurora_app_django:latest"

def main():
    docker_push()
    git_push()


def git_push():
    print('START: git_push')
    placeholder = input("Enter the comment for the commit: ")
    placeholder = '"' + placeholder + '"'

    PUSH = [
        ["git", "add", ".",],
        ["git", "commit", "-m", placeholder],
        ["git", "branch", "-M", "main"],
        ["git", "push", "-u", "origin", "main"]
    ]
    loop_actions(PUSH)

def docker_push():
    print("START: docker_push()")
    PUSH = [
        ["docker", "build", "-t", IMAGE_NAME, '.'],
        ["docker", "push", IMAGE_NAME]
    ]
    loop_actions(PUSH)


def loop_actions(command):
    for action in command:
        print("action: ", action)
        result = subprocess.run(action, shell=True, capture_output=True, text=True)
        print("result.stdout: ", result.stdout)

main()