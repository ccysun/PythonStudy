import pandas as pd

data = {
    "calories": [420,380,390],
    "duration": [50,40,45]
}
# DataFrame 개체 데이터 로드:
df = pd.DataFrame(data)
print(df)
print("")

#행 index 참조:
print(df.loc[0])
print("")

# 인덱스 리스트 사용:
print(df.loc[[0,1]])
print("")

print(df.loc[0])
print(df.loc[1])
print("")


data1 = {
    "calories": [420,380,390],
    "duration": [50,40,45]
}
# Named Indexes
df1 = pd.DataFrame(data1, index= ["day1","day2","day3"])
print(df1)
print("")
# 행 index 참조
print(df1.loc["day2"])
print("")



