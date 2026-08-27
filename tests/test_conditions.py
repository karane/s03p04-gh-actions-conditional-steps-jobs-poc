from src.conditions import (
    JobStatus,
    should_run_on_success,
    should_run_on_failure,
    should_run_always,
    should_run_on_cancelled,
    is_push_to_main,
)


def test_should_run_on_success_only_for_success():
    assert should_run_on_success(JobStatus.SUCCESS) is True
    assert should_run_on_success(JobStatus.FAILURE) is False


def test_should_run_on_failure_only_for_failure():
    assert should_run_on_failure(JobStatus.FAILURE) is True
    assert should_run_on_failure(JobStatus.SUCCESS) is False


def test_should_run_always_regardless_of_status():
    assert should_run_always(JobStatus.SUCCESS) is True
    assert should_run_always(JobStatus.FAILURE) is True
    assert should_run_always(JobStatus.CANCELLED) is True


def test_should_run_on_cancelled_only_for_cancelled():
    assert should_run_on_cancelled(JobStatus.CANCELLED) is True
    assert should_run_on_cancelled(JobStatus.SUCCESS) is False


def test_is_push_to_main_true_for_push_on_main():
    assert is_push_to_main("push", "refs/heads/main") is True


def test_is_push_to_main_false_for_pull_request():
    assert is_push_to_main("pull_request", "refs/heads/main") is False


def test_is_push_to_main_false_for_other_branch():
    assert is_push_to_main("push", "refs/heads/feature-x") is False
