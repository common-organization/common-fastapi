from enum import Enum


class ErrorCode(Enum):
    """
    요약:
        예측 가능한 에러를 상수로 명시해둔 ErrorCode 클래스

    설명:
        각 반환 코드는 음수로 표시된다.
        첫번째 값은 에러들의 항목을 의미한다.

    Attributes:
        code(int): 에러코드
        message(str): 에러 메세지
    """
    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message

    # 일반 에러
    FAILURE_JSON_PARSING = (-901, "JSON 변환이 실패되었습니다.")
    API_FAILURE = (-902, "API 호출에 실패했습니다.")
    # 음성&채팅 메세지
    USER_NOT_FOUND = (-401, "해당 사용자 정보가 없습니다.")


class ControlledException(RuntimeError):
    """
    예측 가능한 에러를 관리하기 위한 Exception Class
    """
    def __init__(self, error_code: ErrorCode):
        self.error_code = error_code