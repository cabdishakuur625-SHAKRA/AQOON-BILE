from generate_arabic_subject import (
    create_ch1_questions,
    create_ch2_questions,
    create_ch3_questions,
    create_ch4_questions,
    create_ch5_questions,
    create_ch6_questions,
)

chaps = [
    create_ch1_questions,
    create_ch2_questions,
    create_ch3_questions,
    create_ch4_questions,
    create_ch5_questions,
    create_ch6_questions,
]

for i, fn in enumerate(chaps, 1):
    e, m, h = fn()
    print(f"Chapter {i}: Easy={len(e)}, Medium={len(m)}, Hard={len(h)}")
