;setList함수는 특정 리스트의 인덱스위치에 있는 요소의 값을 value매개변수값으로 변경합니다.
;변경된 리스트를 반환합니다.
(defun setList (list index value)
  (if (eq index 0)
      (cons value (cdr list))
      (cons (car list) (setList (cdr list) (- index 1) value))))

;삽입정렬 함수입니다
(defun insertion-sort (tar n)
    (progn
         (princ "정렬 시작")
         (terpri)
         (dotimes(i n) ;전달받은 tar리스트의 0부터 n-1까지의 요소를 순회합니다.
             (progn
                 (setq key (nth i tar)) ;삽입의 대상이될 요소를 key변수에 저장합니다.
                 (setq temp (- i 1))    ;삽입 위치를 저장하는 변수입니다.
                 (if (> i 0) ;0번 인덱스 요소는 비교할 대상이 없음으로 배제합니다
                     (progn
                         (princ "삽입될 요소: ")
                         (princ key)
                         (terpri)
                         (princ "삽입전: ")
                         (princ tar)
                         (terpri)
                         (setq check1 1) ;앞의 요소들중 key값도다 큰 요소를 발견한 경우 0으로 설정됩니다.
                         (setq check2 0) ;앞의 요소들중 key값보다 큰 요소가 하나라도 있을 경우 1로 설정됩니다.
                         (loop for j downfrom (- i 1) to 0 do ;자신보다 인덱스가 낮은 요소들을 순회하며 비교합니다.
                           (progn
                              ;key보다 작은요소를 발견한다면 요소들을 오른쪽으로 이동시키는 if문 입니다.
                              (if (and (> (nth j tar) key)(= 1 check1)) ;check1을 사용하여 key보다 큰 요소를 만난이후 요소이동을 금지합니다.
                                  (progn
                                      (setq temp j)
                                      (setq tar (setList tar (+ j 1) (nth j tar)))
                                  )
                              )
                              ;key보다 큰 요소를 만난 경우
                              (if (and (<= (nth j tar) key) (= 1 check1))
                                  (progn
                                      (setq check1 0)
                                      (setq check2 1)
                                      (setq temp j)
                                  )
                              )
                           )
                          )
                         ;check2값이 1일 경우는 자신보다 큰 요소의 인덱스가 temp에 저장됩니다.
                         ;따라서 temp값에 1을 더해 바로 뒤의 요소로 삽입 위치를 변경합니다.
                         (if (= check2 1) (setq temp (+ temp 1)))
                         (setq tar (setList tar temp key))
                         (princ "삽입후: ")
                         (princ tar)
                         (terpri)
                         (terpri)
                     )
                 )
              )
          )
          (princ "정렬완료: ")
          (princ tar)
          (terpri)
          (terpri)
     )
)

(setq list1 '(11 33 23 45 13 25 8 135))
(setq list2 '(83 72 65 54 47 33 29 11))

(insertion-sort list1 8)
(insertion-sort list2 8)
