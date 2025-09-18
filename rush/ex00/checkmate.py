def checkmate(board):
    """
    Check if the King is in check by analyzing the board state.
    Returns True if King is in check, False otherwise.
    """
    try:
        # Find the King position
        king_pos = None
        board_size = len(board)
        
        if board_size == 0:
            return False
        
        # Validate board is square
        for row in board:
            if len(row) != board_size:
                return False
                
        # Find King position
        for i in range(board_size):
            for j in range(board_size):
                if board[i][j] == 'K':
                    if king_pos is not None:  # Multiple kings
                        return False
                    king_pos = (i, j)
        
        if king_pos is None:  # No king found
            return False
            
        # Check if any enemy piece can capture the King
        king_row, king_col = king_pos
        
        for i in range(board_size):
            for j in range(board_size):
                piece = board[i][j]
                if piece in ['P', 'B', 'R', 'Q']:  # Enemy pieces
                    if can_capture(board, i, j, king_row, king_col, piece):
                        return True
        
        return False
        
    except Exception:
        return False

def can_capture(board, piece_row, piece_col, target_row, target_col, piece_type):
    """
    Check if a piece can capture the target position.
    """
    try:
        if piece_type == 'P':  # Pawn
            return can_pawn_capture(piece_row, piece_col, target_row, target_col)
        elif piece_type == 'B':  # Bishop
            return can_bishop_capture(board, piece_row, piece_col, target_row, target_col)
        elif piece_type == 'R':  # Rook
            return can_rook_capture(board, piece_row, piece_col, target_row, target_col)
        elif piece_type == 'Q':  # Queen
            return (can_bishop_capture(board, piece_row, piece_col, target_row, target_col) or
                    can_rook_capture(board, piece_row, piece_col, target_row, target_col))
        
        return False
    except Exception:
        return False

def can_pawn_capture(piece_row, piece_col, target_row, target_col):
    """
    Check if pawn can capture target. Pawns capture diagonally forward.
    """
    # Pawn captures diagonally (one square diagonally forward)
    row_diff = target_row - piece_row
    col_diff = abs(target_col - piece_col)
    
    return row_diff == 1 and col_diff == 1

def can_bishop_capture(board, piece_row, piece_col, target_row, target_col):
    """
    Check if bishop can capture target along diagonal lines.
    """
    row_diff = abs(target_row - piece_row)
    col_diff = abs(target_col - piece_col)
    
    # Must be diagonal move
    if row_diff != col_diff or row_diff == 0:
        return False
    
    # Check path is clear
    row_step = 1 if target_row > piece_row else -1
    col_step = 1 if target_col > piece_col else -1
    
    current_row = piece_row + row_step
    current_col = piece_col + col_step
    
    while current_row != target_row:
        if board[current_row][current_col] != '.':
            return False
        current_row += row_step
        current_col += col_step
    
    return True

def can_rook_capture(board, piece_row, piece_col, target_row, target_col):
    """
    Check if rook can capture target along horizontal or vertical lines.
    """
    # Must be horizontal or vertical move
    if piece_row != target_row and piece_col != target_col:
        return False
    
    if piece_row == target_row and piece_col == target_col:
        return False
    
    # Check horizontal movement
    if piece_row == target_row:
        start_col = min(piece_col, target_col) + 1
        end_col = max(piece_col, target_col)
        for col in range(start_col, end_col):
            if board[piece_row][col] != '.':
                return False
    
    # Check vertical movement
    if piece_col == target_col:
        start_row = min(piece_row, target_row) + 1
        end_row = max(piece_row, target_row)
        for row in range(start_row, end_row):
            if board[row][piece_col] != '.':
                return False
    
    return True
