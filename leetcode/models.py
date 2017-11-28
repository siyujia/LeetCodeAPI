from typing import Dict


class Problem:
    def __init__(self, dic: Dict[str, object]):
        self.level: int = dic.get("difficulty", {}).get("level", 0)
        self.frequency: float = dic.get("frequency", 0.0)
        self.paid_only: bool = dic.get("paid_only", False)
        self.status: str = dic.get("status", None)
        stat: Dict[str, object] = dic.get("stat", {})
        self.is_new: bool = stat.get("is_new_question", False)
        self.title: str = stat.get("question__title", None)
        self.title_slug: str = stat.get("question__title_slug", None)
        self.article_slug: str = stat.get("question__article_slug", None)
        self.id: int = stat.get("question_id", 0)
        self.total_acs: int = stat.get("total_acs", 0)
        self.total_submitted: int = stat.get("total_submitted", 0)