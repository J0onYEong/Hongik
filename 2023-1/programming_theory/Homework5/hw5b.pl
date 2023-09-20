% 특정 퀸에 대해 리스트의 다른 퀸들과 비교하여 해당 위치에 배치가 가능한지 확인하는 규칙
checkconflict(_, []).                      % 비교대상이 없을 경우, 해당 조합이 성공적이라는 의미이다.
checkconflict(Queen, [Row|OtherQueens]) :- % 최초로 유효성 검사를 시작한다.
    Queen =\= Row,
    DiagonalDistance is 1,               % 다음퀸과의 대각선 거리를 의미한다.
    Queen + DiagonalDistance =\= Row,    % 대각선거리에 비교하는 퀸의 위치할 경우 두 퀸이 대각선상에 위치함으로 false
    Queen - DiagonalDistance =\= Row,
    NewDistance is DiagonalDistance + 1, % 다음퀸은 비교대상 퀸가의 거리가 1만큼 떨어짐으로 대각거리를 1만큼 증가시킨다.
    checkconflict(Queen, OtherQueens, NewDistance). % 유효성 검증 성공후 다음 퀸으로 이동

checkconflict(_, [], _). % 더이상 비교할 퀸이 없는 경우, 즉 모든 퀸에 대해 해당 위치에 배치가 가능
checkconflict(Queen, [Row|OtherQueens], DiagonalDistance) :-
    Queen =\= Row,
    Queen + DiagonalDistance =\= Row,
    Queen - DiagonalDistance =\= Row,
    NewDistance is DiagonalDistance + 1,
    checkconflict(Queen, OtherQueens, NewDistance). % 다음퀸으로 이동

checkcombination([]).
checkcombination([Queen|OtherQueens]) :-
    checkconflict(Queen, OtherQueens),      % 전달받은 리스트이 가장 앞쪽 퀸을 다른 퀸들과 비교하며 유효성 확인
    checkcombination(OtherQueens).          % 제귀적 호츌을 통해 다른 퀸들도 유효성을 검사

n_queen(N, Queens) :-
    numlist(1, N, Rows),        % 1...N범위의 요소를 가진 리스트를 생성합니다.
    permutation(Rows, Queens),  % 전달한 리스트를 가능한 경우의 수만큼 랜덤하게 정렬합니다.
    checkcombination(Queens).   % 랜덤하게 정렬된 리스트가 유효한지 확인합니다.
