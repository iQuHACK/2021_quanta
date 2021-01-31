import matplotlib.pyplot as plt
import numpy as np

def game_result(result):
    wins1 = 0
    wins2 = 0
    for kk in result:
        lst = [int(i) for i in kk]
        if test_win(lst):
            wins1 += result[kk]
        elif not test_win(lst):
            wins2 += result[kk]
        elif test_win(lst) == 2:
            pass
    return (wins1, wins2)

def plot_result(result):
    labels = ['player1', 'player2']
    result = game_result(result)

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    ax.bar(x, result, width)

    ax.set_ylabel('Scores', fontsize = 15)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize = 15)
    ax.tick_params(labelsize = 15)

def test_win(lst): #return 0 for player 0 win, 1 for player 1 win, 2 for tie or neither wins
    win1=0
    win0=0
    if lst[0]==lst[1]==lst[2]:
        if lst[1]==1:
            win1+=1
        else:
            win0+=1
    if lst[3]==lst[4]==lst[5]:
        if lst[3]==1:
            win1+=1
        else:
            win0=1
    if lst[6]==lst[7]==lst[8]:
        if lst[6]==1:
            win1+=1
        else:
            win0+=1
    if lst[0]==lst[4]==lst[8]:
        if lst[0]==1:
            win1+=1
        else:
            win0+=1
    if lst[2]==lst[4]==lst[6]:
        if lst[2]==1:
            win1+=1
        else:
            win0=1
    if lst[0]==lst[3]==lst[6]:
        if lst[0]==1:
            win1+=1
        else:
            win0+=1
    if lst[1]==lst[4]==lst[7]:
        if lst[1]==1:
            win1+=1
        else:
            win0+=1
    if lst[2]==lst[5]==lst[8]:
        if lst[2]==1:
            win1+=1
        else:
            win0+=1
    if win1>win0:
        return 1
    elif win0>win1:
        return 0
    else:
        return 2
