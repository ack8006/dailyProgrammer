def run_game(score_line):
    score_line = list(''.join(score_line.split()))
    total_score = 0
    for throw_ind in xrange(len(score_line)):
        throw = score_line[throw_ind]
        if throw in ['X', '/']:
            if throw == '/':
                total_score += get_value(throw) - get_value(score_line[throw_ind-1])
            elif throw == 'X':
                total_score += get_value(throw)
                total_score += get_value(score_line[throw_ind+2])
            total_score += get_value(score_line[throw_ind+1])
            if len(score_line) - throw_ind <= 3:
                return total_score
        else:
            total_score += get_value(throw)
    return total_score

def get_value(value):
    if value in ['X','/']:
        return 10
    elif value == '-':
        return 0
    else:
        return int(value)

if __name__ == '__main__':
    print run_game(raw_input())
    #score_lines = ['62 71  X 9- 8/  X  X 35 72 5/8',
    #               'X X X X X X X X X XXX',
    #               'X -/ X 5- 8/ 9- X 81 1- 4/X']
    #for score_line in score_lines:
    #    print run_game(score_line)
