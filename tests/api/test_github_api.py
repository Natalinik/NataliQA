import pytest


@pytest.mark.api
def test_user_exists(github_api):
    user_defunkt = github_api.get_user("defunkt")
    assert user_defunkt["login"] == "defunkt"


@pytest.mark.api
def test_user_not_exists(github_api):
    user_butenkosergii = github_api.get_user("butenkosergii")
    assert user_butenkosergii["message"] == "Not Found"


@pytest.mark.api
def test_repo_can_be_found(github_api):
    result_of_search = github_api.search_repo("become-qa-auto")
    assert result_of_search["total_count"] == 58


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    result_of_search = github_api.search_repo("sergiibutenko_repo_non_exist")
    assert result_of_search["total_count"] == 0


@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    result_of_search_s = github_api.search_repo("s")
    assert result_of_search_s["total_count"] != 0


@pytest.mark.api
def test_list_releases_found(github_api):
    releases = github_api.list_releases("Natalinik", "NataliQA")
    assert len(releases) >= 1
    # Check the oldest release
    assert releases[-1]["tag_name"] == "1.0.0"
    assert releases[-1]["author"]["login"] == "Natalinik"


@pytest.mark.api
def test_list_releases_not_found(github_api):
    releases = github_api.list_releases("Natalinik", "QA")
    assert releases["status"] == "404"


@pytest.mark.api
def test_list_commits_on_pr(github_api):
    commits = github_api.list_commits_on_pull_request("Natalinik", "NataliQA", 1)
    assert commits[0]["sha"] == "31ba51d3cbc2416bff865262d53b1580c725cf17"
    assert commits[0]["commit"]["author"]["name"] == "Nataliia Platonova"
 
    
@pytest.mark.api
def test_list_commits_on_pr_not_found(github_api):
    commits = github_api.list_commits_on_pull_request("Natalinik", "NataliQA", "Bad_pr_number")
    assert commits["message"] == "Not Found"
    assert commits["status"] == "404"
