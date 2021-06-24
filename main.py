import functions
from icecream import ic

if __name__ == '__main__':
    df = functions.make_data()
    ic(df)
    functions.show_map(df)
