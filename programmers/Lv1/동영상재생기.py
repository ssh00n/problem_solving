def handle_prev(curr: int):
    return max(curr - 10, 0)

def handle_next(curr: int, video_len: int):
    return min(curr + 10, video_len)

def solution(video_len, pos, op_start, op_end, commands):
    def time_to_seconds(time_str):
        minutes, seconds = map(int, time_str.split(":"))
        return minutes * 60 + seconds

    video_len_seconds = time_to_seconds(video_len)
    curr = time_to_seconds(pos)
    op_start_seconds = time_to_seconds(op_start)
    op_end_seconds = time_to_seconds(op_end)

    # 오프닝 구간이면 바로 op_end로 이동
    if op_start_seconds <= curr <= op_end_seconds:
        curr = op_end_seconds

    for command in commands:
        if command == "next":
            curr = handle_next(curr, video_len_seconds)
        elif command == "prev":
            curr = handle_prev(curr)

        # 명령어 실행 후 오프닝 구간이면 op_end로 이동
        if op_start_seconds <= curr <= op_end_seconds:
            curr = op_end_seconds

    # 초 단위를 "mm:ss" 형식으로 변환
    res_minute = curr // 60
    res_second = curr % 60
    return f"{res_minute:02}:{res_second:02}"