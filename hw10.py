import pickle
filepath = 'score.bin'

def save_data (score,avg):
    with open(filepath, 'wb') as file:
        pickle.dump(score, file)
        pickle.dump(avg, file)

def load_data ():
    with open(filepath, 'rb') as file :
        score = pickle.load(file)
        avg = pickle.load(file)

    return score, avg

def input_scores():
    s=[]
    i=1
    while True:
        n = int(input(f'#{i}?'))
        if n < 0 :
            break
        s.append(n)
        i += 1
    return s

def get_average(s):
    total = 0
    for n in s:
        total += n
    return total / len(s)

def show_scores(s):
    for n in s:
        print(n, end=' ')
    print()

print('[점수 입력]')
scores=input_scores()
print('개인 점수 : ',end='')
show_scores(scores)
avg = get_average(scores)
print(f'평균 : {avg:.1f}')
save_data(scores,avg)

r_scores,r_avg = load_data()

print(r_scores)
print(r_avg)