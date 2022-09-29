import pandas

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_column = squirrel_data["Primary Fur Color"]


gray_squirrels = len(fur_column[fur_column == "Gray"])
red_squirrels = len(fur_column[fur_column == "Cinnamon"])
black_squirrels = len(fur_column[fur_column == "Black"])

squirrel_count = {"Fur Color": ["Gray", "Cinnamon", "Black"],
                  "Count": [gray_squirrels, red_squirrels, black_squirrels]
                  }
squirrel_count_dataframe = pandas.DataFrame(squirrel_count)
squirrel_count_dataframe.to_csv("squirrel_count.csv")



