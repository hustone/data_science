import pandas as pd


data = {"name": ["mohamed", "taha", "juju", "tapha"], "age": [24, 22, 23, 24],
        "job": ["pythoniste", "gamer", "politician", "doctor"]}

df = pd.DataFrame(data)


def main():
    if __name__ == "__main__":
        print(df)
        print(type(df))


main()
