from dataclasses import dataclass

@dataclass(frozen=False)
class Comment:
    pk: str =  None
    user_id: str =  None
    user: dict =  None
    type: int =  None
    text: str =  None
    did_report_as_spam: bool =  None
    created_at: int =  None
    created_at_utc: int =  None
    content_type: str =  None
    status: str =  None
    bit_flags: str =  None
    share_enabled: int =  None
    is_ranked_comment: bool =  None
    is_covered: bool =  None
    media_id: str =  None
    is_created_by_media_owner: bool =  None
    reply_to_comment_id: str =  None
    inline_composer_display_condition: str =  None
    has_liked_comment: bool =  None
    comment_like_count: int =  None
    preview_child_comments: list =  None
    over_preview_users: list =  None
    private_reply_status: int =  None
    has_translation: bool =  None