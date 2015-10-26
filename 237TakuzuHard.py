import copy

class TazukuSolver(object):
    def solve_tazuku_brute(self, board):
        next_empty = self.get_next_empty_slot(board)
        if not next_empty:
            print 'FINISHED'
            return board

        for pos_val in ['0','1']:
            y, x = next_empty
            board[y][x] = pos_val
            if (self.cond_two_adjacent(board) and self.cond_equal_numbers(board)
                and self.cond_equal_rows_cols(board)):

                new_board = self.solve_tazuku_brute(copy.deepcopy(board))
                if new_board:
                    return new_board
        return None

    def get_next_empty_slot(self, board):
        for y in xrange(len(board)):
            for x in xrange(len(board)):
                if board[y][x] == '.':
                    print y,x
                    return y, x
        return None

    def cond_two_adjacent(self, board):
        for y in xrange(len(board)):
            for x in xrange(len(board)):
                piece = board[y][x]
                if piece == '.':
                    continue
                if x+2 <= len(board)-1:
                    if ((piece == board[y][x+1]) and (piece == board[y][x+2])):
                        return False
                if y+2 <= len(board)-1:
                    if ((piece == board[y+1][x]) and (piece == board[y+2][x])):
                        return False
        return True

    def cond_equal_numbers(self, board):
        for x in xrange(len(board)):
            if '.' not in board[x]:
                if not (board[x].count('0') == board[x].count('1')):
                    return False
            col_vals = [row[x] for row in board]
            if '.' not in col_vals:
                if not (col_vals.count('0') == col_vals.count('1')):
                    return False
        return True

    def cond_equal_rows_cols(self, board):
        rows = [tuple(row) for row in board if '.' not in row]
        if len(rows) > len(set(rows)):
            return False
        cols = [col for col in map(tuple, zip(*board)) if '.' not in col]
        if len(cols) > len(set(cols)):
            return False
        return True

if __name__ == '__main__':
    #board = []
    #board.append(list(raw_input()))
    #for x in xrange(len(board[0])-1):
    #    board.append(list(raw_input()))
    #print board
    #board = [['.', '.', '.', '.'], ['0', '.', '0', '.'], ['.', '.', '0', '.'], ['.', '.', '.', '1']]
    #board = [['1', '1', '0', '.', '.', '.'], ['1', '.', '.', '.', '0', '.'], ['.', '.', '0', '.', '.', '.'], ['1', '1', '.', '.', '1', '0'], ['.', '.', '.', '.', '0', '.'], ['.', '.', '.', '.', '.', '.']]
    board = [['0', '.', '.', '.', '.', '1', '1', '.', '.', '0', '.', '.'], ['.', '.', '.', '1', '.', '.', '.', '0', '.', '.', '.', '.'], ['.', '0', '.', '.', '.', '.', '1', '.', '.', '.', '0', '0'], ['1', '.', '.', '1', '.', '.', '1', '1', '.', '.', '.', '1'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '1', '.', '.'], ['0', '.', '0', '.', '.', '.', '1', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '0', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '0', '1', '.', '0', '.', '.', '.', '.'], ['.', '.', '0', '0', '.', '.', '0', '.', '0', '.', '.', '0'], ['.', '.', '.', '.', '.', '1', '.', '.', '.', '.', '1', '.'], ['1', '0', '.', '0', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '1', '.', '.', '.', '.', '1', '.', '.', '0', '0']]

    print 'Solving'
    print TazukuSolver().solve_tazuku_brute(board)


