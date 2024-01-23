import pytest

def test_init(my_issues):
    assert my_issues.repo_owner == "topq-practice"
    assert my_issues.repo_name == "api-practice"
    assert my_issues.access_token == "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"

def test_open_issues(my_issues):
    # There are 3 open Issues in the beggining
    assert my_issues.get_open_issues_count() == 3

def test_by_label(my_issues):
    assert my_issues.get_issues_by_label()==1

def test_create(my_issues):
    res = my_issues.create_new_issue("Limor's issue",
                                    "This issue was created via REST API from <Python",
                                    ["practice1"],["topq-practice"])
    # If the return status is 201 the problem has created
    assert res == 201 



