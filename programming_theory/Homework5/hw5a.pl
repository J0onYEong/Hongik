% 삽입하려는 리스트가 빈 경우 요소를 빈 리스트에 삽입
insert(Element, [], [Element]).

% 삽입하려는 리스트의 헤드보다 값이 작다면 리스트의 헤드에 해당요소를 삽입
insert(Element, [Head|Tail], [Element, Head|Tail]) :-
    Element =< Head.
insert(Element, [Head|Tail], [Head|Result]) :- 
    % 헤드보다 값이 크다면 Head를 제외한 리스트를 사용하여 insert을 제귀적으로 호출
    Element > Head,
    insert(Element, Tail, Result).

% 리스트의 끝 요소부터 빈 리스트에 삽입되는 과정으로 정렬이 진행된다.
sorting([], []).
sorting([Head|Tail], Result) :-
    sorting(Tail, Rest),
    write('target: '), 
    write(Head), nl,    % 삽입의 대상이 되는 요소를 출력
    insert(Head, Rest, Result),
    write('inserted list: '),
    write(Result), nl.  % 삽입과정이후 변경된 리스트 출력
