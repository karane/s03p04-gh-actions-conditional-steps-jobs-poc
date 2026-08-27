from enum import Enum


class JobStatus(Enum):
    SUCCESS = "success"
    FAILURE = "failure"
    CANCELLED = "cancelled"


def should_run_on_success(status: JobStatus) -> bool:
    return status == JobStatus.SUCCESS


def should_run_on_failure(status: JobStatus) -> bool:
    return status == JobStatus.FAILURE


def should_run_always(status: JobStatus) -> bool:
    return True


def should_run_on_cancelled(status: JobStatus) -> bool:
    return status == JobStatus.CANCELLED


def is_push_to_main(event_name: str, ref: str) -> bool:
    return event_name == "push" and ref == "refs/heads/main"
