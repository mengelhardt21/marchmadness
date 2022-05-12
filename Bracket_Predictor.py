import numpy as np
import pandas as pd
import random as r

#df.at[index, "SOS"] * sos_value * sos_value)  

def randomizeO(adjustment, df, index):
    return (df.at[index, "3P"] * r.uniform(.5, 1.5) / ((df.at[index, "Seed"]) * adjustment)) + (df.at[index, "FTA"] * r.uniform(.5, 1.5) / ((df.at[index, "Seed"]) * adjustment)) + (df.at[index, "ORB"] * r.uniform(.5, 1.5) / ((df.at[index, "Seed"]) * adjustment)) - (df.at[index, "TOV"] * r.uniform(.5, 1.5) * ((df.at[index, "Seed"]) * adjustment))

def randomizeD(adjustment, df, index):
    return 1 / ((df.at[index, "O3P"] * r.uniform(.5, 1.5) * (df.at[index, "Seed"])  * adjustment) + (df.at[index, "OFTA"] * r.uniform(.5, 1.5) * (df.at[index, "Seed"]) * adjustment) + (df.at[index, "OORB"] * r.uniform(.5, 1.5) * (df.at[index, "Seed"]) * adjustment) - (df.at[index, "OTOV"] * r.uniform(.5, 1.5) / (df.at[index, "Seed"]) * adjustment))

def pickWinner(df, index1, index2, roundO, roundD):
    if (df.at[index1, roundO] + df.at[index2, roundD]) > (df.at[index2, roundO] + df.at[index1, roundD]):
        loser = index2
        winner = index1
    else:
        loser = index1
        winner = index2
    print(df.at[winner, "School"])
    """
    print(df.at[winner, roundO])
    print(df.at[winner, roundD])
    print(df.at[loser, "School"])
    print(df.at[loser, roundO])
    print(df.at[loser, roundD])
    """
    return loser

def printRound (round_text, roundO, roundD, games, df):
    odd = 0
    even = 1

    print(round_text)

    for i in range(games):
        loser = pickWinner(df, odd, even,roundO, roundD)
        df = df.drop(loser)
        odd = odd + 2
        even = even + 2
    
    df = df.reset_index(drop=True)

    return df


df = pd.read_csv("Data.csv")


df["Round_64O"] = pd.NaT
df["Round_64D"] = pd.NaT
df["Round_32O"] = pd.NaT
df["Round_32D"] = pd.NaT
df["Round_16O"] = pd.NaT
df["Round_16D"] = pd.NaT
df["Round_8O"] = pd.NaT
df["Round_8D"] = pd.NaT
df["Round_4O"] = pd.NaT
df["Round_4D"] = pd.NaT
df["Round_FinalO"] = pd.NaT
df["Round_FinalD"] = pd.NaT

for i in range(64):
    df.at[i, 'Round_64O'] = randomizeO(10, df, i)
    df.at[i, 'Round_64D'] = randomizeD(10, df, i)
    df.at[i, 'Round_32O'] = randomizeO(.001, df, i)
    df.at[i, 'Round_32D'] = randomizeD(.001, df, i)
    df.at[i, 'Round_16O'] = randomizeO(.001, df, i)
    df.at[i, 'Round_16D'] = randomizeD(.001, df, i)
    df.at[i, 'Round_16O'] = randomizeO(.001, df, i)
    df.at[i, 'Round_16D'] = randomizeD(.001, df, i)
    df.at[i, 'Round_8O'] = randomizeO(.0001, df, i)
    df.at[i, 'Round_8D'] = randomizeD(.0001, df, i)
    df.at[i, 'Round_4O'] = randomizeO(.0001, df, i)
    df.at[i, 'Round_4D'] = randomizeD(.0001, df, i)
    df.at[i, 'Round_FinalO'] = randomizeO(.0001, df, i)
    df.at[i, 'Round_FinalD'] = randomizeD(.0001, df, i)

#pickWinner(df, 0, 1, 'Round_64O', 'Round_64D')

df = printRound("Round 1", "Round_64O", "Round_64D", 32, df)
df = printRound("Round 2", "Round_32O", "Round_32D", 16, df)
df = printRound("Sweet Sixteen", "Round_16O", "Round_16D", 8, df)
df = printRound("Elite Eight", "Round_8O", "Round_8D", 4, df)
df = printRound("Final Four", "Round_4O", "Round_4D", 2, df)
df = printRound("Championship", "Round_FinalO", "Round_FinalD", 1, df)


"""
odd = 0
even = 1


print("Round 1")

for i in range(32):
    loser = pickWinner(df, odd, even, "Round_64O", "Round_64D")
    df = df.drop(loser)
    odd = odd + 2
    even = even + 2
    
df = df.reset_index(drop=True)

odd = 0
even = 1

print("Round 2")

for i in range(16):
    loser = pickWinner(df, odd, even, "Round_32O", "Round_32D")
    df = df.drop(loser)
    odd = odd + 2
    even = even + 2
    
df = df.reset_index(drop=True)

odd = 0
even = 1

print("Sweet 16")

for i in range(8):
    loser = pickWinner(df, odd, even, "Round_16O", "Round_16D")
    df = df.drop(loser)
    odd = odd + 2
    even = even + 2
    
df = df.reset_index(drop=True)

odd = 0
even = 1

print("Elite 8")

for i in range(4):
    loser = pickWinner(df, odd, even, "Round_8O", "Round_8D")
    df = df.drop(loser)
    odd = odd + 2
    even = even + 2
    
df = df.reset_index(drop=True)

odd = 0
even = 1

print("Final Four")

for i in range(2):
    loser = pickWinner(df, odd, even, "Round_4O", "Round_4D")
    df = df.drop(loser)
    odd = odd + 2
    even = even + 2
    
df = df.reset_index(drop=True)

odd = 0
even = 1

print("Championship")

loser = pickWinner(df, odd, even, "Round_FinalO", "Round_FinalD")

"""

