;temp배열은 특정 열에 배치될 퀸의 행번호를 저장하는 배열입니다. temp[1]=2 이라면 2행 2(1+1)열에 퀸이 배치된 상태입니다.
(setq temp '(0 0 0 0))
(setq N 4)
;setList함수는 특정 리스트의 인덱스위치에 있는 요소의 값을 value매개변수값으로 변경합니다.
;변경된 리스트를 반환합니다.
(defun setList (list index value)
  (if (eq index 0)
      (cons value (cdr list))
      (cons (car list) (setList (cdr list) (- index 1) value))))

;특정 열에 위치될 수 있는 퀸의 자리를 탐색하는 함수입니다.
(defun nQueen (col)
    (cond ((= col N)(print temp)) ;탐색하는 자리가 N인 경우는 이미 모든 퀸이 배치된 이후 임으로 결과를 출력합니다.
        (t (dotimes(i N)( ;0부터 N-1까지의 행을 순회하며 퀸이 배치될 자리를 찾습니다.
           progn
               (setq temp (setList temp col (+ i 1))) ;해당 열의 모든 행에 임시로 퀸을 배치시킵니다.
               (setq check 1)
               (dotimes(j col) ;현재 열의 앞의 열에서 배치한 퀸들을 순회합니다.
                   (progn
                       (setq con1 (= (nth j temp) (nth col temp))) ;같은 행에 있지 않을 조건
                       (setq con2 (= (- col j) (abs (- (nth j temp) (nth col temp))))) ;대각선에 위치하지 않을 조건
                       (if (or con1 con2) (setq check 0)) ;두조건중 하나라도 참이라면 현재 행에는 퀸을 배치할 수 없습니다.
                    )
               )
               (if (= check 1)(nQueen (+ col 1))) ;특정 행에 퀸배치를 성공한 경우 재귀함수를 통해 다음 열로 이동합니다.
            )
         )
      )
   )
)

(nQueen 0) ;0번 열부터 배치를 시작합니다.
