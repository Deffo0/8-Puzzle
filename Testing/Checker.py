
def is_solvable(board: list):
    my_board = board.copy()
    my_board.remove("0")
    return count_inversions(my_board, 0, len(my_board) - 1) % 2 == 0


def count_inversions(board: list, start, end):
    if start == end:
        return 0
    else:
        mid = start + int((end - start) / 2)
        inversions = count_inversions(board, start, mid)
        inversions += count_inversions(board, mid + 1, end)
        inversions += merge(board, start, mid, end)
        return inversions


def merge(board: list, start, mid, end):
    i, j, inversions = start, mid + 1, 0
    new_board = []
    while i <= mid and j <= end:
        if int(board[i]) <= int(board[j]):
            new_board.append(board[i])
            i += 1
        else:
            inversions += (mid - i + 1)
            new_board.append(board[j])
            j += 1
    while i <= mid:
        new_board.append(board[i])
        i += 1
    while j <= end:
        new_board.append(board[j])
        j += 1
    for k in range(start, end + 1):
        board[k] = new_board[k - start]
    return inversions
